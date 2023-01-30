---
bookCollapseSection: false
weight: 1
title: EngineApi
---

The `EngineApi` module provides access to the Entity-Component-System framework shared between the World Explorer (which runs the game loop) and individual scenes (which manage their own entities), plus related utilities.

```ts
const engine = require("~system/EngineApi")
```

This module is the most complex and rich in functionality, and the likeliest to receive updates and extensions. It's where most of the power of Decentraland resides, since it determines the kind of experiences people can create.

The API is designed around synchronizing the state of the world between the Explorer and the scene, routing updates and events in both directions. It implements an extensible message protocol that allows scenes to:

* Create and destroy entities.
* Attach, update, and remove components.
* Cast rays in the 3D environment and detect hits.
* Receive input from the player.

{{< info >}}
The `EngineApi` module is undergoing renovations. If you go to the source definitions, you will find legacy methods that are no longer used or can be implemented as no-ops in the latest version (more [[on this later nono put link]]).
{{< /info >}}

`EngineApi` contains the following methods:

* [`function crdtSendToRenderer`](#crdtSendToRenderer)
* [`function crdtGetState`](#crdtGetState)

And the following types:

* [`interface CrdtSendToRendererRequest`](#CrdtSendToRendererRequest)
* [`interface CrdtSendToResponse`](#CrdtSendToResponse)
* [`interface CrdtGetStateRequest`](#CrdtGetStateRequest)
* [`interface CrdtGetStateResponse`](#CrdtGetStateResponse)


## ECS Framework

With the `EngineApi` module comes a generic and extensible implementation of a shared ECS framework, which allows both scenes and the Explorer itself to create entities, attach components and update their states.

Changes made from either side are reflected in the other by exchanging messages, [[serialized]] to a compact binary representation. The mechanism used ([[see below]]) ensures that both parties agree on the order of any updates and reach eventual consistency about the state of the world.

{{< info >}}
Most scenes use the [[Decentraland SDK]], which encapsulates the `EngineApi` module and offers a much nicer, higher-level interface for content developers. Scenes that directly access the messaging protocol in this module are extremely rare.
{{< /info >}}

The World Explorer implements a well-known set of basic components (positions, shapes, textures, multimedia and more), and knows how to deserialize and apply changes to their state when it receives an update. Scenes using the [[SDK]] also have utilities to create custom components, but those are entirely managed by the scene (not synchronized) and thus outside the scope of the protocol.

### Synchronization

Both the World Explorer and the scene must manage a set of shared entities and components, where updates come from both sides in an asynchronous fashion. Without additional measures, their versions of the state of the world can (and will) end up being different.

To prevent this, a CRDT ([conflict-free replicated data type](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type)) is used to reach an agreement between both parties by exchanging messages with updates. This offers a number of advantages:

* Both parties can update the state independently and concurrently.
* Conflicts are managed by a shared resolution strategy applied identically by both parties.
* Both parties are guaranteed to converge to a shared, identical state.
* Besides a small overhead in message size, no additional coordination or messaging round-trips are required.

```goat
.------------------------------------------------------.
| World Explorer                                       |
| .-------------.                       .------------. |
| | Game Engine |                       |  Runtime   | |
| |  .-------.  |                       |  .------.  | |
| |  |       +--+-----------------------+->|      |  | |
| |  | CRDT  |  |   Messsage Protocol   |  | CRDT |  | |
| |  |       |<-+-----------------------+--+      |  | |
| |  '-------'  |                       |  '------'  | |
| |             |                       |            | |
| '-------------'                       '------------' |
'------------------------------------------------------'
```

{{< info >}}
As a World Explorer developer, you are under no obligation to use the same synchronization strategy employed by the Foundation's implementation as long as you preserve API compatibility -- but the design described here is the product of accumulated insights and lessons, and we recommend it.
{{< /info >}}

The implementation of the CRDT synchronization mechanism consists of three parts:

1. An internal representation of the state of all entities and components.
2. A conflict resolution strategy to choose between competing states.
3. A messaging protocol to communicate and process updates to the state.

#### CRDT State {#crdtState}

The CRDT holds the state of all components for all their attached entities, and can be stored in a mapping of components to timestamped states for each entity. In pseudocode:

```ts
// The (completely generic) state of a component for a specific entity, at a point in time:
type EntityComponentState = { timestamp: number, state: byte[] }

// The state of a component for all attached entities:
type ComponentState = Map<EntityId, EntityComponentState>

// The entire state of the CRDT:
type CRDTState = Map<ComponentId, ComponentState>
```

Timestamps aren't actually Unix-style timestamps, and don't refer to a point in real time. They are a type of shared incremental counter to sequence updates, with no relation to clock time. More on this [[below]].

<div id="crdtStateAutoCreate"><!-- just an invisible anchor to link --></div>

Since the CRDT layer doesn't know (or need to know) all available components, the initial state is an empty map. Entries are created on-the-fly when operations involve a `ComponentId` or `EntityId` that was not already mapped. When an entity is removed, the associated state is deleted from all components.

Let's illustrate this with some more pseudocode.

```ts
const crdtState = new Map()
```

```ts
function putEntityComponentState(componentId, entityId, entityComponentState) {
  // If this component is not known yet, add it:
  if (!crdtState[componentId]) {
    crdtState[componentId] = new Map()
  }

  // If this entity has no state for this component, set it and be done:
  if (!crdtState[componentId][entityId]) {
    crdtState[componentId][entityId] = entityComponentState
    return
  }

  // At this point, we have two competing states. The one we received is not necessarily the one
  // that should be kept. We need to decide.
  const existingEntityComponentState = crdtState[componentId][entityId]

  // Only if the rules of conflict resolution say so (more on this later), replace the state:
  if (shouldReplace(entityComponentState, existingEntityComponentState)) {
    crdtState[componentId][entityId] = entityComponentState
  }
}
```

```ts
function deleteEntity(entityId) {
  // Delete the state for this entity in every component:
  for (componentState of crdtState) {
    delete componentState[entityId]
  }
}
```

!! This example code has a glaring problem with deleted entities unless care is taken when calling put. In current code, the handling of deleted entities is this layer. Adding that here may not be the best way to explain it. Address this in either code or text.

The pseudocode above (if translated to actual code) is obviously incomplete and sub-optimal. In particular, it's missing the definition of `shouldReplace`, the function that encapsulates a conflict resolution strategy.

!!ask about the memory usage of the deletedEntities grow-only set (curiosity)
!!ask about the reconstruction of state

#### Timestamps

As mentioned above, when talking about CRDT timestamps we're not referring to actual Unix timestamps for a point in time. Instead, a [Lamport timestamp](https://en.wikipedia.org/wiki/Lamport_timestamp) (a special type of shared incremental counter) is used to keep track of the sequence of events by both parties.

The value of this counter is updated according to these rules:

1. Initialize the local counter to `0`.
2. Before sending a message to remote parties, increment the local counter.
3. After receiving a message from a remote party, set the local counter to the maximum between its value and the received value, plus `1`.

In pseudocode:

```ts
const localTimestamp = 0

function sendState(state) {
  send({ state, timestamp: localTimestamp++ })
}

function receiveState() {
  const { state, timestamp } = receive()
  localTimestamp = max(localTimestamp, remoteTimestamp) + 1
}
```

#### Conflict Resolution {#crdtConflicts}

When the CRDT encounters two competing states, it needs a shared resolution strategy that all parties apply identically, ensuring the same decision is reached by everyone. The Decentraland protocol uses very simple rules:

1. If there was no prior state, keep the new state.
2. If the new state has a greater timestamp, keep the new state.
3. If the new state has a lesser timestamp, keep the old state.
4. If both timestamps are equal, compare the states byte-by-byte and keep the lower value.

Most cases will be resolved by rules `1` and `2`. Rule `3` applies when both parties perform an update before they can exchange messages about it !!ugh. Rule `4` should rarely be used, but it may happen !!detail pl0x.


#### Messaging Protocol

Messages between the World Explorer and the scene runtime are structures in a serialized binary representation. Every message carries a header indicating the type and length, followed by a particular payload for each type of message.

```goat
.----------------.--------------.---------------------------------.                                 
| length: uint32 | type: uint32 |     payload: byte[length]       |
'----------------'--------------'---------------------------------'
╵         common fields         ╵         type-dependent          ╵
```

There are three message types in the CRDT protocol:

* [`PutComponent`](#PutComponent)
* [`DeleteComponent`](#DeleteComponent)
* [`DeleteEntity`](#DeleteEntity)

Note that there are no `CreateComponent` or `CreateEntity` messages. The CRDT rules auto-create entities and components that weren't previously known, as [explained above](#crdtStateAutoCreate).

###### `PutComponent` {#PutComponent}

Update the `state` of a `component` for a particular `entity`, creating unknown components and entities in the CRDT if necessary. [Resolve conflicts](#crdtConflicts) according to `timestamp`.

!! document entity IDs and the compound representation via EntityUtils

```goat
.----------------.-------------------.-------------------------------------------.                  
| entity: uint32 | component: uint32 | timestamp: uint32 |     state: byte[]     |
'----------------'-------------------'-------------------------------------------'
╵                       common fields                    ╵  component-dependent  ╵
```

The `state` field is a component-defined binary serialization. Most components use [[protocol buffers]] to encode messages as specified in the `.proto` files of [[the protocol package]]. The notable exception to this rule is the `Transform` component, which (being the most common by far) has an optimized serialization format.

This additional layer of serialization has an important advantage: the CRDT protocol is agnostic to any present or future component implementations.

If the update contained in this message is applied to the CRDT, the `state` field is copied as-is into the structure.


###### `DeleteComponent` {#DeleteComponent}

Remove the state of `component` for an `entity`. [Resolve conflicts](#crdtConflicts) according to `timestamp`.

```goat
.----------------.-------------------.-------------------.                                          
| entity: uint32 | component: uint32 | timestamp: uint32 |                
'----------------'-------------------'-------------------'                
```

###### `DeleteEntity` {#DeleteEntity}

Delete `entity` (i.e. all associated component state), expecting the identifier to never be reused for a different entity.

```goat
.----------------.                                                                                  
| entity: uint32 |
'----------------'              
```

Note that there is no `timestamp` field. Since the lifespan of `entity` is over, the conflict resolution strategy for any out-of-order updates is to simply ignore them.


## Methods and Types

!!
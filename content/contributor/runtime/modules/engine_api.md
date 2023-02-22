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

This module contains the following methods:

* [`function crdtSendToRenderer`](#crdtSendToRenderer)
* [`function crdtGetState`](#crdtGetState)


## Introduction

The `EngineApi` module is designed to synchronize the state of the world between the Explorer and the scene by exchanging updates, events and commands. It implements an extensible message protocol that allows scenes to, among other things:

* Create and destroy entities.
* Attach, update, and remove components.
* Cast rays in the 3D environment and detect hits.
* Receive events such as input from the player.

```goat
.------------------------------------------------------.
| World Explorer                                       |       
|                                                      |
|                   [Engine API]                       |
|                        |                             |
|  .--------.            |              .------------. |
|  |        |<-----------+<-------------+  Runtime   | |
|  |  Game  |            |   Commands   |  .------.  | |
|  |        |   Events   |              |  | Scene | | |
|  | Engine +----------->+------------->|  |       | | |
|  |        |            |              |  '-------' | |
|  '--------'            |              '------------' |
|                                                      |
'------------------------------------------------------'
```

{{< info >}}
The `EngineApi` module is undergoing renovations. If you go to the source definitions, you will find legacy methods that are no longer used or can be implemented as no-ops in the latest version (more on this below).
{{< /info >}}

## ECS Framework

With the `EngineApi` module comes a generic and extensible implementation of a shared ECS framework, which allows both scenes and the game engine itself to create entities, attach components and update their states.

Changes made from either side are reflected in the other by exchanging messages. The mechanism used ([see below](#synchronization)) ensures that both parties agree on the order of any updates and reach eventual consistency about the state of the world.

The World Explorer implements a well-known set of basic components (positions, shapes, textures, media and more), and knows how to deserialize and apply changes to their state when it receives an update. Scenes using the [SDK](https://docs.decentraland.org/creator) also have utilities to create custom components, but those are entirely managed by the scene (not synchronized) and thus outside the scope of the protocol.

{{< info >}}
Most scenes use the Decentraland SDK, which encapsulates the `EngineApi` module and offers a much nicer, higher-level interface for content developers. Scenes that directly access the messaging protocol in this module are extremely rare.
{{< /info >}}


### Identifying Entities {#identifying}

Entity IDs are plain integers starting with `0`. 

By protocol, IDs below `512` are reserved for the World Explorer, and thus invalid for scene-created entities. Numbers `0`, `1` and `2` are actually in use (see [basic entities]({{< relref "../entities" >}})), with the rest of the range available for future extensions.

Each scene has its own private range of IDs, which the Explorer can transparently map to a global identifier among all entities in the game engine.

Over time, as entities are created and deleted, it's perfectly valid to reuse IDs that were previously freed -- indeed, this may be required for perfomance reasons ([see below](crdtStateDeleteEntities)).


### Synchronization {#synchronization}

Both the World Explorer and the scene must manage a set of shared entities and components, where updates come from both sides in an asynchronous fashion. Without additional measures, their versions of the state of the world can (and will) end up being different.

To prevent this, a CRDT ([conflict-free replicated data type](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type)) is used to reach an agreement between both parties by exchanging messages with updates. This offers a number of advantages:

* Both parties can update the state independently and concurrently.
* Conflicts are managed by a shared resolution strategy applied locally by both parties.
* Both parties are guaranteed to converge to a shared, identical state.
* Besides a small overhead in message size, no additional coordination or messaging round-trips are required.

{{< info >}}
This page explains the use of the CRDT to synchronize state between a locally running scene and the game engine, but the real potential of this mechanism lies in multiplayer scenarios. Using this protocol, players can coordinate their game state and share the same experience.
{{< /info >}}

For this to work, all messages must be commutative and idempotent. Out-of-order messages can be applied even if a supposedly intermediate update was not received yet, and equal messages can be re-processed without breaking consistency.

Let's revisit the architectural diagram above, now focusing on the CRDT:

```goat
.-------------------------------------------------------.
| World Explorer                                        |
|                                                       |
| .-------------.                       .------------.  |
| | Game Engine |                       |   Scene     | |      
| |  .-------.  |                       |  .-------.  | |
| |  |       +--+-----------------------+->|       |  | |
| |  | CRDT  |  |     Sync Protocol     |  | CRDT  |  | |
| |  |       |<-+-----------------------+--+       |  | |
| |  '-------'  |                       |  '-------'  | |
| |             |                       |             | |
| '-------------'                       '-------------' |
'-------------------------------------------------------'
```

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

Timestamps aren't actually Unix-style timestamps. They are a type of incremental counter to sequence updates, with no relation to clock time. More on this [below](#timestamps).

<div id="crdtStateAutoCreate"><!-- just an invisible anchor to link --></div>

Since the CRDT layer doesn't know (or need to know) all available components, the initial state is an empty map. Entries are created on-the-fly when operations involve a `ComponentId` or `EntityId` that was not already mapped. When an entity is removed, the associated state is deleted from all components.

Let's illustrate this with some more pseudocode.

```ts
const crdtState = new Map() // empty, we'll automatically make room for new components and entities
```

```ts
function putEntityComponentState(componentId, entityId, entityComponentState) {
  // If this component is not known yet, add it:
  if (!crdtState[componentId]) {
    crdtState[componentId] = new Map()
  }

  // If this entity has no state for this component, add it and be done:
  if (!crdtState[componentId][entityId] && shouldCreate(entityId)) {
    crdtState[componentId][entityId] = entityComponentState
    return
  }

  // At this point, we have two competing states. The one we just received is not necessarily the
  // one that should be kept. We need to decide.
  const existingEntityComponentState = crdtState[componentId][entityId]

  // Only if the rules of conflict resolution say so (more on this later), replace the state:
  if (shouldReplace(entityComponentState, existingEntityComponentState)) {
    crdtState[componentId][entityId] = entityComponentState
  }
}
```

The pseudocode above (if translated to actual code) is obviously incomplete and sub-optimal. In particular, it's missing the definition of `shouldCreate` and `shouldReplace`, which encapsulate the conflict resolution strategy. These have requirements:

* `shouldCreate` must add new entities, but refuse to re-create deleted entities.
* `shouldReplace` must prefer to keep states that have greater timestamps (with some edge cases).

<div id="crdtStateDeleteEntities"><!-- just an invisible anchor to link --></div>

To support the `shouldCreate` requirement, you'll want to keep track of deleted entity IDs, in order to ignore any future state updates for those. Let's see this in more pseudocode:

```ts
const crdtDeletedEntities = new Set()

function shouldCreate(entityId) {
  return !crdtDeletedEntities.contains(entityId)
}

function deleteEntity(entityId) {
  // Mark this entity as deleted:
  crdtDeletedEntities.add(entityId)

  // Delete the state for this entity in every component:
  for (componentState of crdtState) {
    delete componentState[entityId]
  }
}
```

{{< info >}}
Note that, in the naive implementation above, the set of deleted entities will only grow. In scenes that quickly recycle entities, this can lead to an explosion in memory usage.

To avoid this, the Foundation's explorer employs a generational index to reuse IDs in a finite numerical space, limiting the amount of memory required to keep track of both active and deleted entities.
{{< /info >}}

As for the `shouldReplace` requirement, see [conflict resolution](#crdtConflicts) below.


#### Timestamps {#timestamps}

As mentioned above, when talking about CRDT timestamps we're not referring to actual Unix timestamps for a point in time. Instead, a [Lamport timestamp](https://en.wikipedia.org/wiki/Lamport_timestamp) (a special type of shared incremental counter) is used to keep track of the sequence of events by both parties.

The value of this counter is updated according to these rules:

1. Initialize the local counter to `0`.
2. Before sending a message to remote parties, increment the local counter.
3. After receiving a message from a remote party, set the local counter to the maximum between its value and the received value, plus `1`.

In pseudocode:

```ts
const localTimestamp = 0

function sendState(state) {
  send({ state, timestamp: ++localTimestamp })
}

function receiveState() {
  const { state, timestamp } = receive()
  localTimestamp = max(localTimestamp, remoteTimestamp) + 1
}
```

#### Conflict Resolution {#crdtConflicts}

When the CRDT encounters two competing states, it needs a shared resolution strategy that all parties apply identically, ensuring the same decision is reached by everyone. The Decentraland protocol uses very simple rules:

1. If the entity was deleted (and the ID never reused), ignore new state.
2. If there was no prior state, keep the new state.
3. If the new state has a greater timestamp, keep the new state.
4. If the new state has a lesser timestamp, keep the old state.
5. If both timestamps are equal, compare the states byte-by-byte and keep the lower value.

Most cases will be resolved by rules `1`, `2` and `3`.


#### Initial Synchronization

Before a scene starts running its own code, the runtime populates the CRDT with the state of all [basic entities]({{< relref "../entities" >}}) and their components.

During this initial synchronization, only the runtime can set the shared state. The scene is not allowed to make modifications until the process is complete.


#### Messaging Protocol {#messages}

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

###### `PutComponentMessage` {#PutComponentMessage}

Update the `state` of a `component` for a particular `entity`, creating unknown components and entities in the CRDT if necessary. [Resolve conflicts](#crdtConflicts) according to `timestamp`.


```goat
.----------------.-------------------.-------------------------------------------.                  
| entity: uint32 | component: uint32 | timestamp: uint32 |     state: byte[]     |
'----------------'-------------------'-------------------------------------------'
╵                       common fields                    ╵  component-dependent  ╵
```

The `state` field is a component-defined binary serialization. Most components use [protocol buffers](https://protobuf.dev) to encode messages as specified in the `.proto` files of [the Decentraland protocol package](https://github.com/decentraland/protocol). The notable exception to this rule is the `Transform` component, which (being the most common by far) has an optimized serialization format.

This additional layer of serialization has an important advantage: the CRDT protocol is agnostic to any present or future component implementations.

If the update contained in this message is applied to the CRDT, the `state` field is copied as-is into the structure.


###### `DeleteComponentMessage` {#DeleteComponentMessage}

Remove the state of `component` for an `entity`. [Resolve conflicts](#crdtConflicts) according to `timestamp`.

```goat
.----------------.-------------------.-------------------.                                          
| entity: uint32 | component: uint32 | timestamp: uint32 |                
'----------------'-------------------'-------------------'                
```

###### `DeleteEntityMessage` {#DeleteEntityMessage}

Delete `entity` (i.e. all associated component state), expecting the identifier to never be reused for a different entity.

```goat
.----------------.                                                                                  
| entity: uint32 |
'----------------'              
```

Note that there is no `timestamp` field. Since the lifespan of `entity` is over, the conflict resolution strategy for any out-of-order updates is to simply ignore them.


## Methods

The set of methods in `EngineApi` provide the interface to exchange messages and reconstruct the state of the world from scratch.


###### `crdtSendToRenderer` {#crdtSendToRenderer}

Send a serialized message from the scene to the renderer, return an array of serialized messages that the renderer has for the scene.

```ts
interface Request {
  // The serialized message for this request:
  data: byte[]
}

interface Response {
  // An array of serialized messages from the renderer (if any):
  data: byte[][]
}

function crdtSendToRenderer(Request): Promise<Response>
```

###### `crdtGetState` {#crdtGetState}

```ts
interface Request {}

interface Response {
  // Whether the state has scene-created entities:
  hasEntities: boolean

  // An array of messages that can reconstruct the CRDT state:
  data: byte[][]
}

function crdtGetState(Request): Promise<Response>
```


## Legacy Scenes

Old-style scenes (i.e. those built using the SDK version 6 or older) don't use the modern CRDT mechanism, instead calling methods in `EngineApi` that are now deprecated.

Support for these scenes is not a requirement for a protocol-compliant Decentraland application.

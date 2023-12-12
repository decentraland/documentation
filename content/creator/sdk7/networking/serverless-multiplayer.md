---
date: 2023-11-29
title: Serverless Multiplayer
description: Sync scene state between players.
categories:
  - development-guide
type: Document
aliases:
  - /creator/development-guide/sdk7/remote-scene-considerations/
url: /creator/development-guide/sdk7/serverless-multiplayer/
weight: 2
---

Decentraland runs scenes locally in a player's browser. By default, players are able to see each other and interact directly, but each player interacts with the environment independently. Changes in the environment aren't shared between players by default.

Seeing the same content in the same state is extremely important for players to interact in more meaningful ways.

There are three ways to sync the scene state, so that all players see the same:

- **Mark an entity as synced**: The easiest option. See [Marked an entity as synced](#mark-an-entity-as-synced)
- **Send Explicit MessageBus Messages**: Manually send and listen for specific messages. See [Send explicit MessageBus messages](#send-explicit-messagebus-messages)
- **Use a Server**: See [3rd party servers]({{< ref "/content/creator/sdk7/networking/authoritative-servers.md" >}}). This option is more complicated to set up, but is recommendable if players have incentives to exploit your scene.

The first two options are simpler, as they require no server. The downside is that you rely more on player's connection speeds, and the scene state is not persisted when all players leave the scene.

## Mark an Entity as Synced

{{< hint warning >}}
**📔 Note**: This feature is currently in alpha state. Its syntax could potentially undergo changes on the next few releases.
{{< /hint >}}

To mark an entity as synced, use the `syncEntity` function:

```ts
const doorEntity = engine.addEntity()

syncEntity(doorEntity, [Transform.componentId, Animator.componentId], 1)
```

The `syncEntity` function takes the following inputs:

- **entityId**: A reference to the entity to sync
- **componentIds**: A list of the components that need to be synced from that entity. This is an array that may contain as many entities as needed. All values should be `componentId` properties.
- **entityEnumId**: (optional) A unique id that is used consistently by all players, see [About enum id](#about-the-enum-id).

Not all entities or components need to be synced. Static elements like a tree that remains in the same spot don't require syncing. On entities you do sync, only the components that change over time should be synchronized. If, for example, a cube changes color on click, only the Material component needs to be synced, not the MeshRenderer or the Transform.

{{< hint info >}}
**💡 Tip**: If the data you want to share doesn't exist as a component, define a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}) that holds that data.
{{< /hint >}}

#### About the enum id

The entityEnumId of an entity must be unique. It is not necessarily the same as the local entityId assigned on `engine.addEntity()`. The entity ID is automatically generated and may vary between players. The entityEnumId of an entity must be explicitly defined in the code and be unique.

This is important to avoid inconsistencies if a race condition makes one part of the scene load before another. Maybe for player A the door in the scene is the entity _512_, but for player B that same door is entity _513_. In that case, if player A opens the door, player B instead sees the whole building move.

{{< hint info >}}
**💡 Tip**: Create an enum in your scene, to keep clear references to each syncable id in your scene.

```ts
enum Entities {
  HOUSE = 1,
  DOOR = 2,
}

syncEntity(
  doorEntity,
  [Transform.componentId, Animator.componentId],
  Entities.DOOR
)
```

Use the Entities enum to tag the entity with a unique identifier, ensuring that every client recognizes the modified entity, regardless of creation order.
{{< /hint >}}

#### Player-specific entities

If an entity is created as a result of a player interaction, and other players can only see this entity, but not affect its behavior, there is no need to define a entityEnumId.

For example, in a snowball fight scene, every time a player throws a snowball, they're instancing a new entity. Players can see each other's snowballs, but only the player that creates the ball executes the code that controls the ball's behavior. The snowball doesn't need a unique entityEnumId.

```ts
function onThrow() {
  const ball = engine.addEntity()
  Transform.create(ball, {})
  GLTFContainer.create(ball, { src: 'assets/snowBall.glb' })
  syncEntity(ball, [Transform.componentId, GLTFContainer.componentId])
}
```

#### Parented entities

The parent of an entity is normally defined via `parent` property in the `Transform` component. This property however points to the local entity id of the parent, which could vary, see [About enum id](#about-the-enum-id). To parent entities that need to be synced, or that have children that need to be synced, use the `parentEntity()` function instead of the `Transform`.

```ts
import { syncEntity, parentEntity } from '@dcl/sdk/network'
const parentEntity = engine.addEntity()
Transform.create(parentEntity, { position: somePosition })
syncEntity(parent, [])
const childEntity: Entity = engine.addEntity()
syncEntity(childEntity, [Transform.componentId])

parentEntity(childEntity, parentEntity)
```

Note that both the parent and the child are synced with `syncEntity`, so all players have a common understanding of what ids are used by both entities. This is necessary even if the parent's components may never need to change. In this example, the `syncEntity` includes an empty array of components, to avoid syncing any unnecessary components.

{{< hint warning >}}
**📔 Note**: If an entity is parented by both the `parentEntity()` and also the `parent` property in the `Transform` component, the property in the `Transform` component is ignored.
{{< /hint >}}

When parenting entities via the `parentEntity()` function, you can also make use of the following helper functions:

- **removeParent()**: Undo the effects of `parentEntity()`. It requires that you pass only the child entity. The entity's new parent becomes the scene's root entity. The original parent entity is not removed from the scene.
- **getParent()**: Returns the parent entity of an entity you passed.
- **getChildren()**: Returns the list of children of the entity you passed, as an iterable.
- **getFistChild()**: Returns the first child on the list for the entity you passed.

```ts
import { syncEntity, parentEntity } from '@dcl/sdk/network'
const parentEntity = engine.addEntity()
Transform.create(parentEntity, { position: somePosition })
syncEntity(parent, [])
const childEntity: Entity = engine.addEntity()
syncEntity(childEntity, [Transform.componentId])

// sets parentEntity as parent
parentEntity(childEntity, parentEntity)

// getParent
const getParentResult = getParent(childEntity)
// returns parentEntity

// getFirstChild
const getFistChildResult = getFistChild(parentEntity)
// returns childEntity

// getChildren
const getChildrenResult = Array.from(getChildren(parentEntity))
// returns [childEntity]

// removes parent from childEntity
removeParent(childEntity)
```

## Send Explicit MessageBus Messages

#### Initiate a message bus

Create a message bus object to handle the methods that are needed to send and receive messages between players.

```ts
import { MessageBus } from '@dcl/sdk/message-bus'

const sceneMessageBus = new MessageBus()
```

#### Send messages

Use the `.emit` command of the message bus to send a message to all other players in the scene.

```ts
import { MessageBus } from '@dcl/sdk/message-bus'

const sceneMessageBus = new MessageBus()

const myEntity = engine.addEntity()
MeshRenderer.setBox(myEntity)
MeshCollider.setBox(myEntity)

pointerEventsSystem.onPointerDown(
  {
    entity: myEntity,
    opts: { button: InputAction.IA_PRIMARY, hoverText: 'Click' },
  },
  function () {
    sceneMessageBus.emit('box1Clicked', {})
  }
)
```

Each message can contain a payload as a second argument. The payload is of type `Object`, and can contain any relevant data you wish to send.

```ts
import { MessageBus } from '@dcl/sdk/message-bus'

const sceneMessageBus = new MessageBus()

sceneMessageBus.emit('spawn', { position: { x: 10, y: 2, z: 10 } })
```

{{< hint info >}}
**💡 Tip**: If you need a single message to include data from more than one variable, create a custom type to hold all this data in a single object.
{{< /hint >}}

#### Receive messages

To handle messages from all other players in that scene, use `.on`. When using this function, you provide a message string and define a function to execute. For each time that a message with a matching string arrives, the given function is executed once.

```ts
import { MessageBus } from '@dcl/sdk/message-bus'

const sceneMessageBus = new MessageBus()

type NewBoxPosition = {
  position: { x: number; y: number; z: number }
}

sceneMessageBus.on('spawn', (info: NewBoxPosition) => {
  const myEntity = engine.addEntity()
  Transform.create(myEntity, {
    position: { x: info.position.x, y: info.position.y, z: info.position.z },
  })
  MeshRenderer.setBox(myEntity)
  MeshCollider.setBox(myEntity)
})
```

{{< hint warning >}}
**📔 Note**: Messages that are sent by a player are also picked up by that same player. The `.on` method can't distinguish between a message that was emitted by that same player from a message emitted from other players.
{{< /hint >}}

#### Full MessageBus example

This example uses a message bus to send a new message every time the main cube is clicked, generating a new cube in a random position. The message includes the position of the new cube, so that all players see these new cubes in the same positions.

```ts
import { MessageBus } from '@dcl/sdk/message-bus'

/// --- Create message bus ---
const sceneMessageBus = new MessageBus()

// Cube factory
function createCube(x: number, y: number, z: number): Entity {
  const meshEntity = engine.addEntity()
  Transform.create(meshEntity, { position: { x, y, z } })
  MeshRenderer.setBox(meshEntity)
  MeshCollider.setBox(meshEntity)

  // When a cube is clicked, send message to spawn another one
  pointerEventsSystem.onPointerDown(
    {
      entity: myEntity,
      opts: { button: InputAction.IA_PRIMARY, hoverText: 'Press E to spawn' },
    },
    function () {
      sceneMessageBus.emit('spawn', {
        position: {
          x: 1 + Math.random() * 8,
          y: Math.random() * 8,
          z: 1 + Math.random() * 8,
        },
      })
    }
  )

  return meshEntity
}

// Init
createCube(8, 1, 8)

// define type of data
type NewBoxPosition = {
  position: { x: number; y: number; z: number }
}

// on spawn message, create new cube
sceneMessageBus.on('spawn', (info: NewBoxPosition) => {
  createCube(info.position.x, info.position.y, info.position.z)
})
```

## Test a multiplayer scene locally

If you launch a scene preview and open it in two (or more) different browser windows, each open window will be interpreted as a separate player, and a mock communications server will keep these players in sync.

Interact with the scene on one window, then switch to the other to see that the effects of that interaction are also visible there.

{{< hint warning >}}
**📔 Note**: Open separate browser _windows_. If you open separate _tabs_ in the same window, the interaction won't work properly, as only one tab will be treated as active by the browser at a time.
{{< /hint >}}

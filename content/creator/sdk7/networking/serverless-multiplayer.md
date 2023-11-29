---
date: 2023-11-29
title: Serverless Multiplayer
description: Sync scene state between players.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/serverless-multiplayer/
weight: 2
---

When a player enters a Decentraland scene, each player downloads and runs that scene's code independently on their own machine.

To share changes in the scene with other players, mark entities as synced

There are other alternatives to sharing changes across all players changes:

- Use a server, see link
- Send explicit MessageBus messages

## Mark an entity as synced

```ts
const houseEntity = engine.addEntity()
syncEntity(houseEntity, [Transform.componentId], Entities.HOUSE)
```

Not all entities need to be synced, and not all components from those entities either. For example if the 3D model of a tree is always going to be in the same spot, you can leave it unsynced. You only need to sync things that will change over time.

If you have a cube that changes color when clicked, but the shape will always be a cube, you only need to sync the `Material` component, not the `MeshRenderer`. If the cube plays a sound when changing color, and you want all other player to hear that sound too, you can also sync the `AudioSource` component.

Tip: If the data you want to share doesn't exist as a component, define a custom component that holds that data! The component could be applied to a single placeholder entity in the scene.

```ts
enum Entities {
  HOUSE = 1,
  DOOR = 2,
}
```

We use the Entities enum to tag the entity with an unique identifier, so every client knows which entity you are modifying, no matter the order they are created

### About the sync id

The networkId of an entity must be unique.
Note that the networkId is not necessarily the same as the local entityId assigned on `engine.addEntity()`.

The entity id is generated automatically, and may vary between players that load the same scene, for example if a race condition makes one part of the scene load before another. Maybe for client A the door is the entity 512, but for client B its 513, so when one player opens the door, another player sees the whole building move.

The networkId MUST be explicitly defined for each entity and unique.

Tip: Create an enum in your scene, to keep clear references to each syncable id in your scene.

### Player-specific entities

There are cases where it's not necessary to assign a networkId

If a same entity is used by the code on several player´s instances (like a door), then it's important to assign a networkId to that entity.

This is not the case for entities that are created as a result of a player interaction, with code that is only executed on that player's instance, but that need to be seen by other players.

For example, in a snowball fight scene, every time a player throws a snowball, they're instancing a new entity. Players can see each other's snowballs, but only the player that creates the ball runs the code that controls the ball's behavior. In these cases, we don't need to define a networkId.

```ts
function onThrow() {
  const ball = engine.addEntity()
  Transform.create(ball, {})
  GLTFContainer.create(ball, { src: 'assets/snowBall.glb' })
  syncEntity(ball, [Transform.componentId, GLTFContainer.componentId])
}
```

The client that runs this code will create an UNIQUE entity and will be sent to the others.

## Parented entities

The parent of an entity is defined via the `Transform` component, however this points to the local entity id of the parent, which could vary (link to above). To parent an entity that should be snyced, use `parentEntity()`.

```ts
import { syncEntity, parentEntity } from '@dcl/sdk/network'
const parentEntity = engine.addEntity()
Transform.create(parentEntity, { position: somePosition })
syncEntity(parent, Transform.componentId)
const childEntity: Entity = engine.addEntity()
syncEntity(childEntity, Transform.componentId)

// create parentNetwork component. This maybe could be done in a system and use the original parent. TBD
parentEntity(childEntity, parentEntity)
```

Every client will know how to map this entity because the ParentNetwork has the pointers to the parent entity. But we are still having an issue, the parent is not defined. We need to tell the renderer that the child entity has a parent property.

getParent

removeParent

getChildren

getFistChild

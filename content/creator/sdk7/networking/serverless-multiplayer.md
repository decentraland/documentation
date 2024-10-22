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

The first two options are covered in this document. They are simpler, as they require no server. The downside is that you rely more on player's connection speeds, and the scene state is not persisted when all players leave the scene.

## Mark an Entity as Synced

In the [Scene editor]({{< ref "/content/creator/scene-editor/about-editor.md" >}}), mark an entity as synced by adding a **Multiplayer component** to it. It includes a checkbox for each of the other components on the entity, allowing you to select which ones to update.

<img src="/images/editor/multiplayer-component.png" alt="Armature" width="300"/>

To mark an entity as synced via code, use the `syncEntity` function:

```ts
const doorEntity = engine.addEntity()

syncEntity(doorEntity, [Transform.componentId, Animator.componentId], 1)
```

The `syncEntity` function takes the following inputs:

- **entityId**: A reference to the entity to sync
- **componentIds**: A list of the components that need to be synced from that entity. This is an array that may contain as many entities as needed. All values should be `componentId` properties.
- **entityEnumId**: (optional) A unique id that is used consistently by all players, see [About enum id](#about-the-enum-id).

Not all entities or components need to be synced. Static elements like a tree that remains in the same spot don't require syncing. On entities you do sync, only the components that change over time should be synchronized. For example, if a cube changes color when clicked, you should only sync the Material component, not the MeshRenderer or the Transform, as those will never change.

{{< hint info >}}
**💡 Tip**: If the data you want to share doesn't exist as a component, define a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}) that holds that data.
{{< /hint >}}

### About the enum id

The **entityEnumId** of an entity must be unique. It's not related to the local entityId assigned on `engine.addEntity()`, that is automatically generated and may vary between players running the same scene. The entityEnumId of an entity must be explicitly defined in the code and be unique.

Explicitly setting this ID is important to avoid inconsistencies if a race condition makes one part of the scene load before another. Maybe for player A the door in the scene is the entity _512_, but for player B that same door is entity _513_. In that case, if player A opens the door, player B instead sees the whole building move.

{{< hint info >}}
**💡 Tip**: Create an enum in your scene, to keep clear references to each syncable id in your scene.

```ts
enum EntityEnumId {
	DOOR = 1,
	DRAW_BRIDGE = 2,
	ELEVATOR = 3,
}

syncEntity(
	doorEntity,
	[Transform.componentId, Animator.componentId],
	EntityEnumId.DOOR
)
```

Here the EntityEnumId enum is used to tag entities with a unique identifier, ensuring that every client recognizes the modified entity, regardless of creation order.
{{< /hint >}}

#### Entities created by a player

If an entity is created as a result of a player interaction, and this entity should be synced with other players, the entity doesn't need an entityEnumId. You can use `syncEntity()` passing only the entity and the list of components. A unique value for entityEnumId is assigned automatically behind the curtains.

All entities instanced on scene initiation need to have a manually-assigned ID. That's to ensure that all players use the same ID on each. When a single player is in charge of instancing an entity, explicit IDs are not needed. Other players get updates about this new entity with an ID already assigned, so there is no risk of ID mismatches.

For example, in a snowball fight scene, every time a player throws a snowball, they're instancing a new entity that gets synced with other players. The snowball doesn't need a unique entityEnumId.

```ts
function onThrow() {
	const ball = engine.addEntity()
	Transform.create(ball, {})
	GLTFContainer.create(ball, { src: 'assets/snowBall.glb' })
	syncEntity(ball, [Transform.componentId, GLTFContainer.componentId])
}
```

#### Parented entities

The parent of an entity is normally defined via `parent` property in the `Transform` component. This property however points to the local entity id of the parent, which could vary, see [About enum id](#about-the-enum-id). To parent entities that need to be synced, or that have children that need to be synced, use the `parentEntity()` function instead of the `Transform`.

```ts
import { syncEntity, parentEntity } from '@dcl/sdk/network'

const parent = engine.addEntity()
Transform.create(parent, { position: somePosition })
syncEntity(parent, [])

const child: Entity = engine.addEntity()
syncEntity(child, [Transform.componentId])

parentEntity(child, parent)
```

Note that both the parent and the child are synced with `syncEntity`, so all players have a common understanding of what ids are used by both entities. This is necessary even if the parent's components may never need to change. In this example, the `syncEntity` includes an empty array of components, to avoid syncing any unnecessary components.

{{< hint warning >}}
**📔 Note**: If an entity is parented by both the `parentEntity()` and also the `parent` property in the `Transform` component, the property in the `Transform` component is ignored.
{{< /hint >}}

When entities are parented via the `parentEntity()` function, you can also make use of the following helper functions:

- **removeParent()**: Undo the effects of `parentEntity()`. It requires that you pass only the child entity. The entity's new parent becomes the scene's root entity. The original parent entity is not removed from the scene.
- **getParent()**: Returns the parent entity of an entity you passed.
- **getChildren()**: Returns the list of children of the entity you passed, as an iterable.
- **getFirstChild()**: Returns the first child on the list for the entity you passed.

```ts
import { syncEntity, parentEntity } from '@dcl/sdk/network'

const parent = engine.addEntity()
Transform.create(parent, { position: somePosition })
syncEntity(parent, [])

const child: Entity = engine.addEntity()
syncEntity(child, [Transform.componentId])

// sets parent as parent
parentEntity(child, parent)

// getParent
const getParentResult = getParent(child)
// returns parent

// getFirstChild
const getFirstChildResult = getFirstChild(parent)
// returns child

// getChildren
const getChildrenResult = Array.from(getChildren(parent))
// returns [child]

// removes parent from child
removeParent(child)
```

## Check the sync state

When a player just loads into a scene, they may not yet be synchronized with other players surrounding them. If the player starts altering the state of the game before they are synced, this could cause problems in your game. We recommend always checking for a player to be synchronized before they are allowed to edit anything about the scene.

You can check this state via the `isStateSyncronized()` function. This function returns a boolean, that is true if the player is already synchronized.

```ts
import { isStateSyncronized } from '@dcl/sdk/network'

const isConnected = isStateSyncronized()
```

You could for example include this check in a system, and block any interaction based on this boolean.

```ts
import { isStateSyncronized } from '@dcl/sdk/network'

export function main() {
	let isSynced: boolean = false
	let timer = 0
	const syncSystem = function (dt: number) {
		timer += dt
		if (timer > 1) {
			isSynced = isStateSyncronized()

			if (isSynced) {
				console.log('PLAYER IS SYNCED')
				engine.removeSystem(syncSystem)
			}
		}
	}
	engine.addSystem(syncSystem)

	pointerEventsSystem.onPointerDown(clickableEntity, (e) => {
		if (!isSynced) return
		// interactive actions
		// they only happen if the player is synced
	})
}
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

## Single player scenes

If your scene is deployed to a [Decentraland World]({{< ref "/content/creator/worlds/about.md" >}}), you can make it a single player scene. Players won't see each other, won't be able to chat or see the effects of each other's actions.

To do this, configure the scene's `scene.json` file to set the **fixedAdapter** to `offline:offline`. The scene will have no Communication Service at all and each user joining that world will always be alone.

**Example:**

```json
{
	"worldConfiguration": {
		"name": "my-name.dcl.eth",
		"fixedAdapter": "offline:offline"
	}
}
```

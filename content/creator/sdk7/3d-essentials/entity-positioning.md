---
date: 2018-02-5
title: Set entity positions
description: How to set the position, rotation and scale of an entity in a scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/entity-positioning/
weight: 1
---

You can set the _position_, _rotation_ and _scale_ of any entity by using the `Transform` component. This can be used on any entities, affecting where 3D objects are rendered, like primitive shapes (cube, sphere, plane, etc) and 3D models (`GltfContainer`).

<img src="/images/media/ecs-simple-components-new.png" alt="nested entities" width="400"/>


```ts
// Create a new entity
const ball = engine.addEntity()
  
// Give this entity a shape, to make it visible
SphereShape.create(ball)

// Give this entity a Transform component
Transform.create(ball, {
	  position: Vector3.create(5, 1, 5),
	  scale: Vector3.create(1, 1, 1),
	  rotation: Quaternion.Zero()
})
```

To move, rotate or resize an entity in your scene over a period of time, change the values on this component incrementally, frame by frame. See [Move entities]({{< ref "/content/creator/sdk7/3d-essentials/move-entities.md" >}}) for more details and best practices. 

<!-- You can also use the helper functions in the [utils library](https://www.npmjs.com/package/decentraland-ecs-utils) to achieve this more easily.
-->

## Position

`position` is a _3D vector_, it sets the position of the entity's center on all three axes, _x_, _y_, and _z_. See [Geometry types]({{< ref "/content/creator/sdk7/3d-essentials/special-types.md" >}}) for more details.

```ts
// Create a new entity
const ball = engine.addEntity()
  
// Create transform with a predefined position
Transform.create(ball, {
	  position: Vector3.create(5, 1, 5)
}

// Fetch a mutable version of the transform
const mutableTransform = Transform.getMutable(ball)

// Set the position with an object
mutableTransform.position = { x: 5, y: 1, z: 5 }

// Set the position with an object (alternative syntax)
mutableTransform.position = Vector3.create(2, 1, 4)

// Set each axis individually
mutableTransform.position.x = 3
mutableTransform.position.y = 1
mutableTransform.position.z = 3
```


When setting a position, keep the following considerations in mind:

- The numbers in a position vector represent _meters_ (unless the entity is a child of a scaled entity).

- A scene that is made up of a single parcel measures 16m x 16m. The center of the scene (at ground level) is at `x:8, y:0, z:8`. If the scene is made up of multiple parcels, then the center will vary depending on their arrangement.

- `x:0, y:0, z:0` refers to the _South-West_ corner of the scene's base parcel, at ground level.

  > Tip: When viewing a scene preview, a compass appears in the (0,0,0) point of the scene with labels for each axis as reference.

  > Note: You can change the base parcel of a scene by editing the `base` attribute of _scene.json_.

- To better orient yourself, use your _left_ hand: 

	- your index finger (pointing forward) is the _z_ axis
	- your middle finger (pointing sideways) is the _x_ axis
	- your thumb (pointing up) is the _y_ axis.

- If an entity is a child of another, then `x:0, y:0, z:0` refers to the center of its parent entity, wherever it is in the scene.

- Every entity in your scene must be positioned within the bounds of the parcels it occupies at all times. If an entity leaves these boundaries, it will raise an error.

  > Tip: When viewing a scene in preview mode, entities that are out of bounds are highlighted in _red_.

- Your scene is also limited in height. The more parcels that make up the scene, the higher you're allowed to build. See [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) for more details.

## Rotation

`rotation` is stored as a [_quaternion_](https://en.wikipedia.org/wiki/Quaternion), a system of four numbers, _x_, _y_, _z_ and _w_. Each of these numbers goes from 0 to 1. See [Geometry types]({{< ref "/content/creator/sdk7/3d-essentials/special-types.md" >}}) for more details.

```ts
// Create a new entity
const cube = engine.addEntity()
  
// Create transform with a predefined rotation of 0
Transform.create(cube, {
	  rotation: Quaternion.Zero()
}

// Fetch a mutable version of the transform
const mutableTransform = Transform.getMutable(cube)

// Set the rotation with an object, from euler angles
mutableTransform.rotation = Quaternion.fromEulerDegrees(0, 90, 0)

// Set the rotation with an object
mutableTransform.rotation = { x: 0.1, y: 0.5, z: 0.5, w: 0 }

// Set each axis individually
mutableTransform.rotation.x = 0
mutableTransform.rotation.y = 1
mutableTransform.rotation.z = 0.3
mutableTransform.rotation.w = 0
```


You can also set the rotation field with [_Euler_ angles](https://en.wikipedia.org/wiki/Euler_angles), the more common _x_, _y_ and _z_ notation with numbers that go from 0 to 360 that most people are familiar with. To use Euler angles, use one of the following notations:

```ts
// Create transform with a predefined rotation in Euler angles
Transform.create(cube, {
	  rotation: Quaternion.fromEulerDegrees(0, 90, 0)
}

// Fetch a mutable version of the transform
const mutableTransform = Transform.getMutable(cube)

// Set the rotation with an object, from euler angles
mutableTransform.rotation = Quaternion.fromEulerDegrees(0, 90, 0)
```

When using a _3D vector_ to represent Euler angles, _x_, _y_ and _z_ represent the rotation in that axis, measured in degrees. A full turn requires 360 degrees.

When you retrieve the rotation of an entity, it returns a quaternion by default. To obtain the rotation expressed as in Euler angles, use `.toEuler()`:

```ts
// Fetch a read-only version of the transform
const transform = Transform.getMutable(cube)

// Set the rotation with an object, from euler angles
const eulerAngle = Quaternion.toEuler(transform.rotation)
```


<!--
### Add Rotations

Another option is to perform a `rotate` operation on an existing transform, which adds to its current rotation. The `rotate` operation takes a vector that indicates a direction, and a number of degrees to rotate. In the following example, we're tilting an entity 15 degrees along the X axis, which adds to whatever rotation it initially had:

```ts
myTransform.rotate(new Vector3(1, 0, 0), 15)
```

The `rotate` operation is useful when dealing with an entity that's rotated in multiple axis, for example both X and Y. The following example sets an original rotation in the Y axis, and then rotates the Transform along the X axis:

```ts
myTransform.rotation.setEuler(0, 90, 0)
myTransform.rotate(new Vector3(1, 0, 0), 15)
```

Note that this produces a different result than if you simply set the initial rotation to `(15, 90, 0)`. In the example, the rotation along the X axis doesn't occur along the original X axis of the Transform, but instead it occurs along the _tilted_ X axis that results from the initial rotation.

-->



## Face the player

Add a _Billboard_ component to an entity so that it always rotates to face the player.

Billboards were a common technique used in 3D games of the 90s, where most entities were 2D planes that always faced the player. The same idea can also be used to rotate a 3D model.

```ts
// Create a new entity
const cube = engine.addEntity()

// Give the entity a visible shape
MeshRenderer.setBox(cube)

// Create transform with a predefined position
Transform.create(cube, {
	  position: Vector3.create(5, 1, 5)
}

// Give the entity a Billboard component
Billboard.create(cube, {})
```

You can configure how the billboard behaves with the following parameters:

- `billboardMode`: Uses a value of the `BillboardMode` to set its behavior:
	- `BillboardMode.BM_ALL_AXES`: The entity rotates to face the player on all of its rotation axis. If the player is high above the entity, the entity will face up.
	- `BillboardMode.BM_Y_AXE`: The entity has its _y_ rotation axis fixed. It only rotates left and right, not up and down. It stays perpendicular to the ground if the player is above or below the entity.
- `oppositeDirection`: Switch what side of the entity faces the player. This is useful for `TextShape` components, and for 3D models that may have been built using different conventions of what direction is _forward_.



```ts
// flat billboard
const perpendicularPlane = engine.addEntity()

Transform.create(perpendicularPlane, {
    position: Vector3.create(8, 1, 8),
  })

PlaneShape.create(perpendicularPlane)

Billboard.create(perpendicularPlane, {
  billboardMode: BillboardMode.BM_Y_AXE,
})

// text label
const textLabel = engine.addEntity()

Transform.create(textLabel, {
    position: Vector3.create(6, 1 ,6),
  })

TextShape.create(textLabel, {
    text: "This text is always readable",
  })

Billboard.create(textLabel, {
  oppositeDirection: true
})
```

{{< hint info >}}
**💡 Tip**:  Billboards are very handy to add to _text_ entities, since it makes them always legible. When using a billboard on an entity with a `TextShape` component, set `oppositeDirection` to true, so that you see the text facing the right way.
{{< /hint >}}

The `rotation` value of the entity's `Transform` component doesn't change as the billboard follows players around.

If an entity has both a `Billboard` component and `Transform` component with `rotation` values, players will see the entity rotating as a billboard. If the billboard doesn't affect all axis, the remaining axis will be rotated according to the `Transform` component.

{{< hint warning >}}
**📔 Note**   If there are multiple players present at the same time, each will see the entities with billboard mode facing them. Billboard rotations are calculated locally for each player, and don't affect what others see.
{{< /hint >}}


## Face a set of coordinates

For entity A to look at entity B: 

	1) Subtract the position of entity A from entity B to get a vector that describes the distance between them.
	2) Normalize that vector, so it has a length of 1, maintaining its direction.
	3) Use `Quaternion.lookRotation` to get a Quaternion rotation that describes rotating in that direction.
	4) Set that Quaternion as the rotation of entity A



```ts
export function turn(entity:Entity, target: ReadOnlyVector3){
	const transform = Transform.getMutable(entity)
	const difference = Vector3.subtract( target, transform.position)
	const normalizedDifference = Vector3.normalize(difference)
	transform.rotation = Quaternion.lookRotation(normalizedDifference)
}
```

<!-- 
 corr the Transform component to orient an entity fo face a specific point in space by simply passing it that point's coordinates. This is a way to avoid dealing with the math for calculating the necessary angles.

This field requires a _Vector3_ object as a value, or any object with _x_, _y_ and _z_ attributes. This vector indicates the coordinates of the position of the point in the scene to look at.

The `lookAt()` function has a second optional argument that sets the global direction for _up_ to use as reference. For most cases, you won't need to set this field. -->



## Scale

`scale` is also a _3D vector_, stored as a `Vector3` object, including the scale factor on the _x_, _y_ and _z_ axis. The shape of the entity scaled accordingly, whether it's a primitive or a 3D model.

<!--
You can either use the `set()` operation to provide a value for each of the three axis, or use `setAll()` to provide a single number and maintain the entity's proportions as you scale it.
-->

The default scale is 1, so assign a value larger to 1 to stretch an entity or smaller than 1 to shrink it.


```ts
// Create a new entity
const ball = engine.addEntity()
  
// Create transform with a predefined position
Transform.create(ball, {
	  scale: Vector3.create(5, 5, 5)
}

// Fetch a mutable version of the transform
const mutableTransform = Transform.getMutable(ball)

// Set the scale with a Vector3

mutableTransform.scale = Vector3.create(2, 2, 2)

// Set the position with an object
mutableTransform.scale = { x: 5, y: 1, z: 5 }

// Set each axis individually
mutableTransform.scale.x = 3
mutableTransform.scale.y = 3
mutableTransform.scale.z = 2
```

## Inherit transformations from parent

When an entity is nested inside another, the child entities inherit components from the parents. This means that if a parent entity is positioned, scaled or rotated, its children are also affected. The position, rotation and scale values of children entities don't override those of the parents, instead these are compounded.

You assign an entity to be parent of another by setting the `parent` field on the child entity's `Transform` component.

If a parent entity is scaled, all position values of its children are also scaled.

```ts
// Create entities
const parentEntity = engine.addEntity()
const childEntity = engine.addEntity()


// Create a transform for the parent
Transform.create(parentEntity, {
	  position: Vector3.create(3, 1, 1),
	  scale: Vector3.create(0.5, 0.5, 0.5)
	})

// Create a transform for the child, and assign it as a child
Transform.create(childEntity, {
	  position: Vector3.create(0, 1, 0),
	  parent: parentEntity
	})
```

In this example, the child entity will be scaled down to 0.5, since its parent has that scale. The child entity's position will also be relative to its parent. We have to add the parent's position plus that of the child. In this case, since the parent is scaled to half its size, the transformation of the child is also scaled down proportionally. In absolute terms, the child is positioned at `{ x: 3, y: 1.5, z: 1 }`. If the parent had a `rotation`, this would also affect the child's final position, as it changes the axis in which the child is shifted.

If a child entity has no `position` on its Transform, the default is `0,0,0`, which will leave it positioned at the same position as its parent.

You can use an invisible entity with no shape component as a parent, to wrap a set of other entities. This entity won't be visible in the rendered scene, but can be used to group its children and apply a transform to all of them.

## Attach an entity to an avatar

To fix an entity's position to an avatar, add an `AvatarAttach` component to the entity.

You can pick different anchor points on the avatar, most of these points are linked to the player's armature and follow the player's animations. For example, when using the right hand anchor point the attached entity will move when the avatar waves or swings their arms while running, just as if the player was holding the entity in their hand.

```ts
// Attach to loacl player
AvatarAttach.create(myEntity,{
    AvatarAnchorPoint: AvatarAnchorPointType.AAPT_NAME_TAG,
})

// Attach to another player, by ID
AvatarAttach.create(myEntity,{
    avatarId: '0xAAAAAAAAAAAAAAAAA',
    AvatarAnchorPoint: AvatarAnchorPointType.AAPT_NAME_TAG,
})
```

When creating an `AvatarAttach` component, pass an object with the following data:

- `avatarId`: _Optional_ The ID of the player to attach to. This is the same as the player's Ethereum address, for those players connected with an Ethereum wallet. If not speccified, it attaches the entity to the local player's avatar.
- `AvatarAnchorPoint`: What anchor point on the avatar skeleton to attach the entity, using a value from the enum `AvatarAnchorPointType`.

The following anchor points are available on the player:

- `AvatarAnchorPointType.AAPT_NAME_TAG`: Floats right above the player's name tag, isn't affected by the player's animations.

  > Note: The name tag height is dynamically adjusted based on the height of the wearables a player has on. So a player wearing a tall hat will have their name tag a little bit higher than others.

- `AvatarAnchorPointType.AAPT_POSITION`: The player's overall position.
- `AvatarAnchorPointType.AAPT_RIGHT_HAND`: Is fixed on the player's right hand
- `AvatarAnchorPointType.AAPT_LEFT_HAND`: Is fixed on the player's left hand

Entity rendering is locally determined on each instance of the scene. Attaching an entity on one player doesn't make it visible to other players who are seeing that player. If an entity is attached to the default local player, each player will experience the entity as attached to their own avatar.

{{< hint warning >}}
**📔 Note**   Entities attached to an avatar must stay within scene bounds to be rendered. If a player walks out of your scene, any attached entities stop being rendered until the player walks back in. Smart wearables don't have this limitation.
{{< /hint >}}

The `AvatarAttach` component overwrites the `Transform` component, a single entity can't have both an `AvatarAttach` and a `Transform` component at the same time.

If you need to position an entity with an offset from the anchor point on the avatar, or a different rotation or scale, attach a parent entity to the anchor point. You can then set the visible model on a child entity to that parent, and give this child its own Transform component to describe its shifts from the anchor point.

```ts
// Create parent entity
const parentEntity = engine.addEntity()
  
// Attach parent entity to player
AvatarAttach.create(parentEntity,{
	avatarId: '0xAAAAAAAAAAAAAAAAA',
    AvatarAnchorPoint: AvatarAnchorPointType.AAPT_NAME_TAG,
})

// Create child entity
let childEntity = engine.addEntity()

ConeShape.create(childEntity)

Transform.create(childEntity, {
    scale: Vector3.create(0.2, 0.2, 0.2),
    position: Vector3.create(0, 0.4, 0),
	parent: parentEntity
})
```

### Obtain an avatarId

To attach an entity to the avatar of another player, you must provide the user's ID in the field `avatarId`. There are [various ways]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data" >}}) to obtain this data.

{{< hint warning >}}
**📔 Note**   For those players connected with an Ethereum wallet, their `userId` is the same as their Ethereum address.
{{< /hint >}}

Fetch the `userId` for all other nearby players via `getConnectedPlayers()`

```ts
import { getConnectedPlayers } from "~system/Players"

executeTask(async () => {
  let players = await getConnectedPlayers()
  players.forEach((player) => {
    console.log("player is nearby: ", player.userId)
  })
})
```

Using it together with `AvatarAttach`, you could use the following code to add a cube floating over the head of every other player in the scene:

```ts
import { getConnectedPlayers } from "~system/Players"

executeTask(async () => {
  let players = await getConnectedPlayers()
  if(!players.length) return
  players.forEach((player) => {
	const myEntity = engine.addEntity()
	MeshRenderer.setBox(myEntity)
	AvatarAttach.create(myEntity, {
		anchorPointId: AvatarAnchorPoint.LEFT_HAND,
		avatarId: player.userId
  	})
  })
})
```

See other ways to fetch other user's IDs in [Get Player Data]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data" >}}).


## Scene boundaries

All entities in your scene must fit within the scene boundaries, as what's outside those boundaries is parcels of land that are owned by other players.

When running a preview of your scene, any entities outside the scene's parcels are colored red and their colliders are removed. When deployed to Decentraland, any entities outside the parcels will not be rendered at all by the engine.

The position of entities in your scene is constantly being checked as they move, if an entity leaves the scene and then returns it will be removed and then rendered normally again.

A grid on the scene's ground shows the limits of the scene, which by default rage from 0 to 16 on the _x_ and _z_ axis, and up to 20 on the _y_ axis. You're free to place entities underground, below 0 on the _y_ axis.

{{< hint info >}}
**💡 Tip**:  If your scene needs more parcels, you can add them in the project's `scene.json` file. See [Scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}) for instructions. Once added, you should see the grid extend to cover the additional parcels.
{{< /hint >}}

It's important to note that the _entire_ 3D model must be within the scene's bounds. This includes the model's _bounding box_. Some 3D models may have bounding boxes that unnecessarily extend beyond the meshes themselves, and it can sometimes be tricky to tell when this happens. When an entity extends beyond the scene's boundaries, in the preview you'll see a cube that marks these bounding boxes. The entire cube must fit within your scene.

![](/images/media/bounding-box.png)

If an entity's cube extends beyond the shape of its meshes, you might need to edit the 3D model in an external editor to reduce these margins, or to _bake_ the rotation and scale of the meshes in the model.

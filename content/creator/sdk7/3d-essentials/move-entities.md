---
date: 2018-02-12
title: Move entities
description: How to move, rotate and scale an entity gradually over time, with incremental changes.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/move-entities/
weight: 7
---

To move, rotate or resize an entity in your scene over a period of time, use the `Tween` component. The engine carries out the desired transformation smoothly, showing updates on every frame until the specified duration is over. Also the `Transform` component values of the affected entity gets updated in real time in case it's needed to make proximity checks in the scene code.

{{< hint info >}}
**💡 Tip**:
In the [Scene Editor]({{< ref "/content/creator/scene-editor/about-editor.md" >}}), you can move entities in a no-code way via **Actions**, see [Make any item smart]({{< ref "/content/creator/scene-editor/smart-items/make-any-item-smart.md" >}}).
{{< /hint >}}

The Tween component has the following functions:
- `setMove`: Move between two points
- `setRotate`: Rotate between two directions
- `setScale`: Scale between two sizes
- `setMoveContinuous`: Move constantly in the same direction
- `setRotateContinuous`: Rotate constantly in the same direction
- `setTextureMove`: Offset the texture of a material between two positions
- `setTextureMoveContinuous`: Offset the texture of a material constantly in the same direction

## Move between two points

To move an entity between two points, create a `Tween` component with the `setMove` function.

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)

Tween.setMove(myEntity, 
	Vector3.create(1, 1, 1), 
	Vector3.create(8, 1, 8), 
	2000
)
```

The movement tween takes the following information:

- `entity`: The entity to move
- `start`: A Vector3 for the starting position
- `end`: A Vector3 for the ending position
- `duration`: How many milliseconds it takes to move between the two positions

These other optonal parameters are also available:

- `faceDirection`: If true, the entity is rotated to face in the direction of the movement.
- `easingFunction`: What easing function to use. See [Non-linear tweens](#non-linear-tweens)

## Rotate between two directions

To rotate an entity between two points, create a `Tween` component with the `setRotate` function.

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)

Tween.setRotate(myEntity, 
	Quaternion.fromEulerDegrees(0, 0, 0), 
	Quaternion.fromEulerDegrees(0, 170, 0), 
	700
)
```

The rotate tween takes the following information:

- `start`: A Quaternion for the starting rotation
- `end`: A Quaternion for the ending rotation
- `duration`: How many milliseconds it takes to move between the two positions

This other optional parameter is also available:

- `easingFunction`: What easing function to use. See [Non-linear tweens](#non-linear-tweens)

### Rotate with a pivot point

When rotating an entity, the rotation is always in reference to the entity's center coordinate. To rotate an entity using another set of coordinates as a pivot point, create a second (invisible) entity with the pivot point as its position and make it a parent of the entity you want to rotate.

When rotating the parent entity, its children will be all rotated using the parent's position as a pivot point. Note that the `position` of the child entity is in reference to that of the parent entity.

```ts
const pivotEntity = engine.addEntity()
Transform.create(pivotEntity, {
	position: Vector3.create(4, 1, 4),
})

const childEntity = engine.addEntity()
Transform.create(childEntity, {
	position: Vector3.create(1, 0, 0),
	parent: pivotEntity,
})
MeshRenderer.setBox(myEntity)

Tween.setRotate(pivotEntity, 
	Quaternion.fromEulerDegrees(0, 0, 0), 
	Quaternion.fromEulerDegrees(0, 170, 0), 
	700
)
```

Note that in this example, the system is rotating the `pivotEntity` entity, that's a parent of the `childEntity` entity.

## Scale between two sizes

To change the scale of an entity between two sizes, create a `Tween` component with its mode set to `Tween.Mode.Scale`.

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)

Tween.setScale(myEntity, 
	Vector3.create(1, 1, 1), 
	Vector3.create(4, 4, 4), 
	2000
)	

```

The scale tween takes the following information:

- `start`: A Vector3 for the starting size
- `end`: A Vector3 for the ending size
- `duration`: How many milliseconds it takes to move between the two positions

This other optional parameter is also available:

- `easingFunction`: What easing function to use. See [Non-linear tweens](#non-linear-tweens)

## Non-linear tweens

Tweens can follow different **Easing Functions** that affect the rate of change over time. A **linear** function, means that the speed of the change is constant from start to finish. There are plenty of options to chose, that draw differently shaped curves depending on if the beginning and/or end start slow, and how much. An **easeinexpo** curve starts slow and ends fast, increasing speed exponentially, on the contrary an **easeoutexpo** curve starts fast and ends slow.

<img src="/images/editor/easing-functions.png" width="600"/>

{{< hint info >}}
**💡 Tip**: Experiment with different movement curves. The differences are often subtle, but we subconsciously interpret information from how things move, like weight, friction, or even personality.
{{< /hint >}}

```ts
Tween.setScale(myEntity, 
	Vector3.create(1, 1, 1), 
	Vector3.create(4, 4, 4), 
	2000,
	EasingFunction.EF_EASEOUTBOUNCE
)

```

The optional `easingFunction` parameter takes its value from the `EasingFunction` enum, that offers the following options:

- `EF_EASEBACK`
- `EF_EASEBOUNCE`
- `EF_EASECIRC`
- `EF_EASECUBIC`
- `EF_EASEELASTIC`
- `EF_EASEEXPO`
- `EF_EASEINBACK`
- `EF_EASEINBOUNCE`
- `EF_EASEINCIRC`
- `EF_EASEINCUBIC`
- `EF_EASEINELASTIC`
- `EF_EASEINEXPO`
- `EF_EASEINQUAD`
- `EF_EASEINQUART`
- `EF_EASEINQUINT`
- `EF_EASEINSINE`
- `EF_EASEOUTBACK`
- `EF_EASEOUTBOUNCE`
- `EF_EASEOUTCIRC`
- `EF_EASEOUTCUBIC`
- `EF_EASEOUTELASTIC`
- `EF_EASEOUTEXPO`
- `EF_EASEOUTQUAD`
- `EF_EASEOUTQUART`
- `EF_EASEOUTQUINT`
- `EF_EASEOUTSINE`
- `EF_EASEQUAD`
- `EF_EASEQUART`
- `EF_EASEQUINT`
- `EF_EASESINE`
- `EF_LINEAR`

## Constant rotation

To make an entity rotate constantly, use the `Tween` component with the `setRotateContinuous` function.

```ts
Tween.setRotateContinuous(myEntity, 
	Quaternion.fromEulerDegrees(0, -1, 0), 
	700
)
```

The rotate continuous tween takes the following information:

- `entity`: The entity to rotate
- `direction`: A Quaternion for the rotation
- `speed`: How many degrees per second the entity will rotate

This other optional parameter is also available:

- `duration`: How many milliseconds to sustain the rotation. After this time, the rotation will stop.

## Constant movement

To make an entity move constantly in the same direction, use the `Tween` component with the `setMoveContinuous` function.

```ts
Tween.setMoveContinuous(myEntity, 
	Vector3.create(0, 0, 1), 
	0.7
)
```

The move continuous tween takes the following information:

- `entity`: The entity to move
- `direction`: A Vector3 for the movement
- `speed`: How many meters per second the entity will move

This other optional parameter is also available:

- `duration`: How many milliseconds to sustain the movement. After this time, the movement will stop.

The move continuous tween takes the following information:

## Tween sequences

To make an entity play a series of tweens in sequence, use the `TweenSequence` component. This component requires two fields:

- `sequence`: An array with multiple tween definitions, that will be carried out sequentially. The array can be empty, in which case it only plays the current tween.
- `loop` _(optional)_: If not provided, the sequence is only played once. If the field is present, the value must be a value of the `TweenLoop` enum. Accepted values are:
  - `TL_RESTART`: When the sequence ends, it restarts. If the last state doesn't match the first state, the entity instantly jumps from one to the other.
  - `TL_YOYO`: When the sequence ends, the it goes backwards, doing all tweens in reverse until it reaches the start again. Then it begins once more.

### Move back and forth

To make a platform move constantly back and forth between two positions, leave the `sequence` array empty, and set `loop` to `TweenLoop.TL_YOYO`

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)

Tween.setMove(myEntity, 
	Vector3.create(1, 1, 1), 
	Vector3.create(8, 1, 8), 
	2000
)

TweenSequence.create(myEntity, { sequence: [], loop: TweenLoop.TL_YOYO })
```

The entity will move back and forth between the start point and the end point, with the same duration and the same easing function in both directions.

### Follow a path

To make an entity follow a more complex path with multiple points, provide a list of tween definitions in the `sequence` of a `TweenSequence` component.

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)

Tween.setMove(myEntity, 
	Vector3.create(6.5, 7, 4), 
	Vector3.create(6.5, 7, 12), 
	4000
)

TweenSequence.create(myEntity, {
	sequence: [
		{
			duration: 2000,
			easingFunction: EasingFunction.EF_LINEAR,
			mode: Tween.Mode.Move({
				start: Vector3.create(6.5, 7, 12),
				end: Vector3.create(6.5, 10.5, 12),
			}),
		},
		{
			duration: 3000,
			easingFunction: EasingFunction.EF_LINEAR,
			mode: Tween.Mode.Move({
				start: Vector3.create(6.5, 10.5, 12),
				end: Vector3.create(6.5, 10.5, 4),
			}),
		},
		{
			duration: 3000,
			easingFunction: EasingFunction.EF_LINEAR,
			mode: Tween.Mode.Move({
				start: Vector3.create(6.5, 10.5, 4),
				end: Vector3.create(6.5, 7, 4),
			}),
		},
	],
	loop: TweenLoop.TL_RESTART,
})
```

Note that when defining a tween within a TweenSequence, you need to use the more verbose format of `Tween.Mode.Move`, or `Tween.Mode.Rotate`, or `Tween.Mode.Scale` to define the tween. In this more verbose format, you need to specify:

- `duration`: How many milliseconds it takes to move between the two positions
- `easingFunction`: What easing function to use. See [Non-linear tweens](#non-linear-tweens). In this format the value is required.
- `mode`: The mode of the tween, which can be `Tween.Mode.Move`, `Tween.Mode.Rotate`, or `Tween.Mode.Scale`.

And within the `mode` field, you need to specify:

- `start`: The starting value of the tween
- `end`: The ending value of the tween


## On tween finished

Use `tweenSystem.tweenCompleted` to detect when a tween has finished. This can be useful to perform actions when a tween ends, for example to open an elevator door.

```ts
engine.addSystem(() => {
	const tweenCompleted = tweenSystem.tweenCompleted(myEntity)
	if (tweenCompleted) {
		//play sound
	}
})
```

## Simultaneous tweens

An entity can only have one `Tween` component, and each tween component can only perform one transformation at a time. For example, you can´t make an entity move sideways and also rotate at the same time. As a workaround, you can use parented entities. For example, you can have an invisible parent entity that moves sideways, with a visible child that rotates.

In the following snippet, a parent entity rotates while a child scales up.

```ts
const parentEntity = engine.addEntity()
Transform.create(parentEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(parentEntity)
Tween.setRotate(parentEntity, 
	Quaternion.fromEulerDegrees(0, 0, 0), 
	Quaternion.fromEulerDegrees(0, 170, 0), 
	5000
)

const childEntity = engine.addEntity()
Transform.create(childEntity, {
	position: Vector3.create(0, 0, 0),
	parent: parentEntity,
})
MeshRenderer.setBox(childEntity)
Tween.setScale(childEntity, 
	Vector3.create(1, 1, 1), 
	Vector3.create(4, 4, 4), 
	5000
)
```

## Pause a tween

To pause a tween, change the `playing` property to false. To resume it, change it back to true.

```ts
pointerEventsSystem.onPointerDown(
	{
		entity: button,
		opts: { button: InputAction.IA_POINTER, hoverText: 'pause' },
	},
	() => {
		let tweenData = Tween.getMutable(myEntity)
		tweenData.playing = !tweenData.playing
	}
)
```

To end a tween that doesn't need to be continued, delete the `Tween` component from the entity. If the entitiy was also using a `TweenSequence` component, delete that too.

```ts
pointerEventsSystem.onPointerDown(
	{
		entity: button,
		opts: { button: InputAction.IA_POINTER, hoverText: 'pause' },
	},
	() => {
		if( Tween.has(myEntity)){
			Tween.deleteFrom(myEntity)
		}
		if( TweenSequence.has(myEntity)){
			TweenSequence.deleteFrom(myEntity)
		}
	}
)
```

## Tweens based on a system

Instead of using the Tween component and letting the engine handle the transformation, you may prefer to do this transition incrementally, frame by frame, via a [system]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) in your scene. By moving the entity a small amount each time the function runs.

On one hand, this gives you more control for re-calculating movements on every frame. On the other hand, the code is more complicated, and players with less performant machines might experience the tween as laggy, noticing each increment.

### Move via system

The easiest way to move an entity is to gradually modify the _position_ value stored in the `Transform` component.

```ts
function SimpleMove() {
	let transform = Transform.getMutable(myEntity)
	transform.position = Vector3.add(
		transform.position,
		Vector3.scale(Vector3.Forward(), 0.05)
	)
}

engine.addSystem(SimpleMove)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)
```

In this example we're moving an entity by 0.1 meters per tick of the game loop.

`Vector3.Forward()` returns a vector that faces forward and measures 1 meter in length. In this example we're then scaling this vector down to 1/10 of its length with `Vector3.scale()`. If our scene has 30 frames per second, the entity is moving at 3 meters per second in speed.

 <img src="/images/media/gifs/move.gif" alt="Move entity" width="300"/>

### Rotate via system

The easiest way to rotate an entity is to gradually change the values in the Transform component incrementally, and run this as part of a system's function of a system.

```ts
function SimpleRotate() {
	let transform = Transform.getMutable(myEntity)
	transform.rotation = Quaternion.multiply(
		transform.rotation,
		Quaternion.fromAngleAxis(1, Vector3.Up())
	)
}

engine.addSystem(SimpleRotate)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)
```

Note that in order to combine the current rotation with each increment, we're using `Quaternion.multiply`. In quaternion math, you combine two rotations by multiplying them, NOT by adding them. The resulting rotation of multiplying one quaternion by another will be the equivalent final rotation after first performing one rotation and then the other.

In this example, we're rotating the entity by 1 degree in an upwards direction in each tick of the game loop.

{{< hint info >}}
**💡 Tip**: To make an entity always rotate to face the player, you can add a [`Billboard` component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#face-the-user" >}}).
{{< /hint >}}

 <img src="/images/media/gifs/rotate.gif" alt="Move entity" width="300"/>

### Rotate via system over a pivot point

When rotating an entity, the rotation is always in reference to the entity's center coordinate. To rotate an entity using another set of coordinates as a pivot point, create a second (invisible) entity with the pivot point as its position and make it a parent of the entity you want to rotate.

When rotating the parent entity, its children will be all rotated using the parent's position as a pivot point. Note that the `position` of the child entity is in reference to that of the parent entity.

```ts
function SimpleRotate() {
	let transform = Transform.getMutable(pivotEntity)
	transform.rotation = Quaternion.multiply(
		transform.rotation,
		Quaternion.fromAngleAxis(1, Vector3.Up())
	)
}

engine.addSystem(SimpleRotate)

const pivotEntity = engine.addEntity()
Transform.create(pivotEntity, {
	position: Vector3.create(4, 1, 4),
})

const childEntity = engine.addEntity()
Transform.create(childEntity, {
	position: Vector3.create(1, 0, 0),
	parent: pivotEntity,
})
MeshRenderer.setBox(myEntity)
```

Note that in this example, the system is rotating the `pivotEntity` entity, that's a parent of the `childEntity` entity.

 <img src="/images/media/gifs/pivot-rotate.gif" alt="Move entity" width="300"/>

### Adjust movement to delay time

Suppose that the player visiting your scene is struggling to keep up with the pace of the frame rate. That could result in the movement appearing jumpy, as not all frames are evenly timed but each moves the entity in the same amount.

You can compensate for this uneven timing by using the `dt` parameter to adjust the scale the movement.

```ts
function SimpleMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	transform.position = Vector3.add(
		transform.position,
		Vector3.scale(Vector3.Forward(), dt)
	)
}

engine.addSystem(SimpleMove)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})
MeshRenderer.setBox(myEntity)
```

The example above keeps movement at approximately the same speed as the movement example above, even if the frame rate drops. When running at 30 frames per second, the value of `dt` is 1/30.

You can also smoothen rotations in the same way by multiplying the rotation amount by `dt`.

### Move between two points via system

If you want an entity to move smoothly between two points, use the _lerp_ (linear interpolation) algorithm. This algorithm is very well known in game development, as it's really useful.

The `lerp()` function takes three parameters:

- The vector for the origin position
- The vector for the target position
- The amount, a value from 0 to 1 that represents what fraction of the translation to do.

```ts
const originVector = Vector3.Zero()
const targetVector = Vector3.Forward()

let newPos = Vector3.lerp(originVector, targetVector, 0.6)
```

The linear interpolation algorithm finds an intermediate point in the path between both vectors that matches the provided amount.

For example, if the origin vector is _(0, 0, 0)_ and the target vector is _(10, 0, 10)_:

- Using an amount of 0 would return _(0, 0, 0)_
- Using an amount of 0.3 would return _(3, 0, 3)_
- Using an amount of 1 would return _(10, 0, 10)_

To implement this `lerp()` in your scene, we recommend creating a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}) to store the necessary information. You also need to define a system that implements the gradual movement in each frame.

```ts
// define custom component
const MoveTransportData = {
	start: Schemas.Vector3,
	end: Schemas.Vector3,
	fraction: Schemas.Float,
	speed: Schemas.Float,
}

export const LerpTransformComponent = engine.defineComponent(
	'LerpTransformComponent',
	MoveTransportData
)

// define system
function LerpMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let lerp = LerpTransformComponent.getMutable(myEntity)
	if (lerp.fraction < 1) {
		lerp.fraction += dt * lerp.speed
		transform.position = Vector3.lerp(lerp.start, lerp.end, lerp.fraction)
	}
}

engine.addSystem(LerpMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})

MeshRenderer.setBox(myEntity)

LerpTransformComponent.create(myEntity, {
	start: Vector3.create(4, 1, 4),
	end: Vector3.create(8, 1, 8),
	fraction: 0,
	speed: 1,
})
```

<img src="/images/media/gifs/lerp-move.gif" alt="Move entity" width="300"/>

### Rotate between two angles via system

To rotate smoothly between two angles, use the _slerp_ (_spherical_ linear interpolation) algorithm. This algorithm is very similar to a _lerp_, but it handles quaternion rotations.

The `slerp()` function takes three parameters:

- The [quaternion](https://en.wikipedia.org/wiki/Quaternion) angle for the origin rotation
- The [quaternion](https://en.wikipedia.org/wiki/Quaternion) angle for the target rotation
- The amount, a value from 0 to 1 that represents what fraction of the translation to do.

{{< hint info >}}
**💡 Tip**: You can pass rotation values in [euler](https://en.wikipedia.org/wiki/Euler_angles) degrees (from 0 to 360) by using `Quaternion.fromEulerDegrees()`.
{{< /hint >}}

```ts
const originRotation = Quaternion.fromEulerDegrees(0, 90, 0)
const targetRotation = Quaternion.fromEulerDegrees(0, 0, 0)

let newRotation = Quaternion.slerp(originRotation, targetRotation, 0.6)
```

To implement this in your scene, we recommend storing the data that goes into the `Slerp()` function in a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}). You also need to define a system that implements the gradual rotation in each frame.

```ts
// define custom component
const RotateSlerpData = {
	start: Schemas.Quaternion,
	end: Schemas.Quaternion,
	fraction: Schemas.Float,
	speed: Schemas.Float,
}

export const SlerpData = engine.defineComponent('SlerpData', RotateSlerpData)

// define system
function SlerpRotate(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let slerpData = SlerpData.getMutable(myEntity)
	if (slerpData.fraction < 1) {
		slerpData.fraction += dt * slerpData.speed
		transform.rotation = Quaternion.slerp(
			slerpData.start,
			slerpData.end,
			slerpData.fraction
		)
	}
}

engine.addSystem(SlerpRotate)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
})

MeshRenderer.setBox(myEntity)

SlerpData.create(myEntity, {
	start: Quaternion.fromEulerDegrees(0, 0, 0),
	end: Quaternion.fromEulerDegrees(0, 180, 0),
	fraction: 0,
	speed: 0.3,
})
```

{{< hint warning >}}
**📔 Note**: You could instead represent the rotation with euler angles as `Vector3` values and use a `Lerp()` function, but that would imply a conversion from `Vector3` to `Quaternion` on each frame. Rotation values are internally stored as quaternions in the `Transform` component, so it's more efficient for the scene to work with quaternions.
{{< /hint >}}

 <img src="/images/media/gifs/lerp-rotate.gif" alt="Move entity" width="300"/>

A simpler but less efficient approach to this takes advantage of the `Quaternion.rotateTowards` function, and avoids using any custom components.

```ts
function SimpleRotate(dt: number) {
	let transform = Transform.getMutable(myEntity)
	transform.rotation = Quaternion.rotateTowards(
		transform.rotation,
		Quaternion.fromEulerDegrees(90, 0, 0),
		dt * 10
	)
	if (transform.rotation === Quaternion.fromEulerDegrees(90, 0, 0)) {
		console.log('done')
		engine.removeSystem(this)
	}
}

const simpleRotateSystem = engine.addSystem(SimpleRotate)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
	rotation: Quaternion.fromEulerDegrees(0, 0, 90),
})

MeshRenderer.setBox(myEntity)
```

In the example above `Quaternion.rotateTowards` takes three arguments: the initial rotation, the final rotation that's desired, and the maximum increment per frame. In this case, since the maximum increment is of `dt * 10` degrees, the rotation will be carried out over a period of a couple of 9 seconds.

Note that the system also checks to see if the rotation is complete and if so it removes the system from the engine. Otherwise, the system would keep making calculations on every frame, even once the rotation is complete.

### Change scale between two sizes via system

If you want an entity to change size smoothly and without changing its proportions, use the _lerp_ (linear interpolation) algorithm of the `Scalar` object.

Otherwise, if you want to change the axis in different proportions, use `Vector3` to represent the origin scale and the target scale, and then use the _lerp_ function of the `Vector3`.

The `lerp()` function of the `Scalar` object takes three parameters:

- A number for the origin scale
- A number for the target scale
- The amount, a value from 0 to 1 that represents what fraction of the scaling to do.

```ts
const originScale = 1
const targetScale = 10

let newScale = Scalar.Lerp(originScale, targetScale, 0.6)
```

To implement this lerp in your scene, we recommend creating a custom component to store the necessary information. You also need to define a system that implements the gradual scaling in each frame.

```ts
// define custom component
const ScaleTransportData = {
	start: Schemas.Number,
	end: Schemas.Number,
	fraction: Schemas.Float,
	speed: Schemas.Float,
}

export const ScaleTransformComponent = engine.defineComponent(
	'ScaleTransformComponent',
	ScaleTransportData
)

// define system
function LerpMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let lerp = ScaleTransformComponent.getMutable(myEntity)
	if (lerp.fraction < 1) {
		lerp.fraction += dt * lerp.speed
		const newScale = Scalar.lerp(lerp.start, lerp.end, lerp.fraction)
		transform.scale = Vector3.create(newScale, newScale, newScale)
	}
}

engine.addSystem(LerpMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: { x: 4, y: 1, z: 4 },
})

MeshRenderer.setBox(myEntity)

ScaleTransformComponent.create(myEntity, {
	start: 1,
	end: 2,
	fraction: 0,
	speed: 1,
})

Vector3.create(1, 1, 1)
```

 <img src="/images/media/gifs/lerp-scale.gif" alt="Move entity" width="300"/>

### Move at irregular speeds between two points via system

While using the lerp method, you can make the movement speed non-linear. In the previous example we increment the lerp amount by a given amount each frame, but we could also use a mathematical function to increase the number exponentially or in other measures that give you a different movement pace.

You could also use a function that gives recurring results, like a sine function, to describe a movement that comes and goes.

Often these non-linear transitions can breathe a lot of life into a scene. A movement that speeds up over a curve or slows down gradually can say a lot about the nature of an object or character. You could even take advantage of mathematical functions that add bouncy effects.

```ts
// define custom component
const MoveTransportData = {
	start: Schemas.Vector3,
	end: Schemas.Vector3,
	fraction: Schemas.Float,
	speed: Schemas.Float,
}

export const LerpTransformComponent = engine.defineComponent(
	'LerpTransformComponent',
	MoveTransportData
)

// define system
function LerpMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let lerp = LerpTransformComponent.getMutable(myEntity)
	if (lerp.fraction < 1) {
		lerp.fraction += dt * lerp.speed
		const interpolatedValue = interpolate(lerp.fraction)
		transform.position = Vector3.lerp(lerp.start, lerp.end, interpolatedValue)
	}
}

// map the lerp fraction to an exponential curve
function interpolate(t: number) {
	return t * t
}

engine.addSystem(LerpMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: { x: 4, y: 1, z: 4 },
})

MeshRenderer.setBox(myEntity)

LerpTransformComponent.create(myEntity, {
	start: Vector3.create(4, 1, 4),
	end: Vector3.create(8, 1, 8),
	fraction: 0,
	speed: 1,
})
```

The example above is just like the linear lerp example we've shown before, but the `fraction` field mapped to a non-linear value on every tick. This non-linear value is used to calculate the `lerp` function, resulting in a movement that follows an exponential curve.

You can also map a transition in rotation or in scale in the same way as shown above, by mapping a linear transition to a curve.

 <img src="/images/media/gifs/lerp-speed-up.gif" alt="Move entity" width="300"/>

### Follow a path via system

You can have an entity loop over an array of vectors, performing a lerp movement between each to follow a more complex path.

```ts
// define custom component
const PathTransportData = {
	path: Schemas.Array(Schemas.Vector3),
	start: Schemas.Vector3,
	end: Schemas.Vector3,
	fraction: Schemas.Float,
	speed: Schemas.Float,
	pathTargetIndex: Schemas.Int,
}

export const LerpTransformComponent = engine.defineComponent(
	'LerpTransformComponent',
	PathTransportData
)

// define system
function PathMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let lerp = LerpTransformComponent.getMutable(myEntity)
	if (lerp.fraction < 1) {
		lerp.fraction += dt * lerp.speed
		transform.position = Vector3.lerp(lerp.start, lerp.end, lerp.fraction)
	} else {
		lerp.pathTargetIndex += 1
		if (lerp.pathTargetIndex >= lerp.path.length) {
			lerp.pathTargetIndex = 0
		}
		lerp.start = lerp.end
		lerp.end = lerp.path[lerp.pathTargetIndex]
		lerp.fraction = 0
	}
}

engine.addSystem(PathMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: Vector3.create(1, 1, 1),
})

MeshRenderer.setBox(myEntity)

const point1 = Vector3.create(1, 1, 1)
const point2 = Vector3.create(8, 1, 3)
const point3 = Vector3.create(8, 4, 7)
const point4 = Vector3.create(1, 1, 7)

const myPath = [point1, point2, point3, point4]

LerpTransformComponent.create(myEntity, {
	path: myPath,
	start: Vector3.create(4, 1, 4),
	end: Vector3.create(8, 1, 8),
	fraction: 0,
	speed: 1,
	pathTargetIndex: 1,
})
```

The example above defines a 3D path that's made up of four 3D vectors. The `PathTransportData` custom component holds the same data used by the custom component in the _lerp_ example above, but adds a `path` array, with all of the points in our path, and a `pathTargetIndex` field to keep track of what segment of the path is currently in use.

The system is very similar to the system in the _lerp_ example, but when a lerp action is completed, it sets the `target` and `origin` fields to new values. If we reach the end of the path, we return to the first value in the path.

 <img src="/images/media/gifs/lerp-path.gif" alt="Move entity" width="300"/>

## Texture tweens

To make a texture slide smoothly, use the `Tween` component with the `setTextureMove` function.

```ts
Tween.setTextureMove(myEntity, 
	Vector2.create(0, 0), 
	Vector2.create(1, 0), 
	2000
)
```

The texture tween takes the following information:

- `entity`: The entity to move the texture of
- `start`: A Vector2 for the starting position
- `end`: A Vector2 for the ending position

This other optional parameter is also available:

- `duration`: How many milliseconds it takes to move between the two positions
- `movementType`: (optional), defines if the movement will be on the offset or the tiling field. By default it uses offset.
- `easingFunction`: What easing function to use. See [Non-linear tweens](#non-linear-tweens). Note: This parameter is only used if a duration is provided.

## Constant texture movement

To make a texture slide constantly, use the `Tween` component with the `setTextureMoveContinuous` function.

```ts
Tween.setTextureMoveContinuous(myEntity, 
	Vector2.create(0, 1), 
	0.7
)
```

The texture continuous tween takes the following information:

- `entity`: The entity to move the texture of
- `direction`: A Vector2 for the movement
- `speed`: How many units per second the entity will move

This other optional parameter is also available:

- `movementType`: (optional), defines if the movement will be on the offset or the tiling field. By default it uses offset.
- `duration`: How many milliseconds to sustain the movement. After this time, the movement will stop.

Read more about texture tweens in the [Texture Tweens]({{< ref "/content/creator/sdk7/3d-essentials/materials.md#texture-tweens" >}}) section.

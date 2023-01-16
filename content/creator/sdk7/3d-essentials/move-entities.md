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

To move, rotate or resize an entity in your scene over a period of time, change the _position_, _rotation_ and _scale_ values stored in an entity's `Transform` component incrementally, frame by frame. This can be used on primitive shapes (cubes, spheres, planes, etc) as well as on 3D models (glTF).

You can easily perform these incremental changes by moving entities a small amount each time the function of [system]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) runs.

<!--
{{< hint info >}}
**💡 Tip**:  You can use the helper functions in the [utils library](https://www.npmjs.com/package/decentraland-ecs-utils) to achieve most of the tasks described in this doc. The code shown in these examples is handled in the background by the library, so in most cases it only takes a single line of code to use them.
{{< /hint >}}
-->

## Move

The easiest way to move an entity is to gradually modify the _position_ value stored in the `Transform` component.

```ts
function SimpleMove() {
	let transform = Transform.getMutable(myEntity)
	transform.position = Vector3.add(transform.position, Vector3.scale(Vector3.Forward(), 0.05))
}

engine.addSystem(SimpleMove)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4)
})
MeshRenderer.setBox(myEntity)
```

In this example we're moving an entity by 0.1 meters per tick of the game loop.

`Vector3.Forward()` returns a vector that faces forward and measures 1 meter in length. In this example we're then scaling this vector down to 1/10 of its length with `Vector3.scale()`. If our scene has 30 frames per second, the entity is moving at 3 meters per second in speed.

 <img src="/images/media/gifs/move.gif" alt="Move entity" width="300"/>

## Rotate

The easiest way to rotate an entity is to gradually change the values in the Transform component incrementally, and run this as part of a system's function of a system.


```ts
function SimpleRotate() {
	let transform = Transform.getMutable(myEntity)
	transform.rotation = Quaternion.multiply(transform.rotation, Quaternion.fromAngleAxis(1, Vector3.Up()))
}

engine.addSystem(SimpleRotate)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4)
})
MeshRenderer.setBox(myEntity)
```

Note that in order to combine the current rotation with each increment, we're using `Quaternion.multiply`. In quaternion math, you combine two rotations by multiplying them, NOT by adding them. The resulting rotation of multiplying one quaternion by another will be the equivalent final rotation after first performing one rotation and then the other.

In this example, we're rotating the entity by 1 degree in an upwards direction in each tick of the game loop.


{{< hint info >}}
**💡 Tip**:  To make an entity always rotate to face the player, you can add a [`Billboard` component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#face-the-user" >}}).
{{< /hint >}}

 <img src="/images/media/gifs/rotate.gif" alt="Move entity" width="300"/>

## Rotate over a pivot point

When rotating an entity, the rotation is always in reference to the entity's center coordinate. To rotate an entity using another set of coordinates as a pivot point, create a second (invisible) entity with the pivot point as its position and make it a parent of the entity you want to rotate.

When rotating the parent entity, its children will be all rotated using the parent's position as a pivot point. Note that the `position` of the child entity is in reference to that of the parent entity.

```ts
function SimpleRotate() {
	let transform = Transform.getMutable(pivotEntity)
  transform.rotation = Quaternion.multiply(transform.rotation, Quaternion.fromAngleAxis(1, Vector3.Up()))
}

engine.addSystem(SimpleRotate)

const pivotEntity = engine.addEntity()
Transform.create(pivotEntity, {
	position: Vector3.create(4, 1, 4)
})

const childEntity = engine.addEntity()
Transform.create(childEntity, {
	position: Vector3.create(1, 0, 0),
	parent: pivotEntity
})
MeshRenderer.setBox(myEntity)
```

Note that in this example, the system is rotating the `pivotEntity` entity, that's a parent of the `childEntity` entity.

 <img src="/images/media/gifs/pivot-rotate.gif" alt="Move entity" width="300"/>

## Adjust movement to delay time

Suppose that the player visiting your scene is struggling to keep up with the pace of the frame rate. That could result in the movement appearing jumpy, as not all frames are evenly timed but each moves the entity in the same amount.

You can compensate for this uneven timing by using the `dt` parameter to adjust the scale the movement.

```ts
function SimpleMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	transform.position = Vector3.add(transform.position, Vector3.scale(Vector3.Forward(), dt))
}

engine.addSystem(SimpleMove)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4)
})
MeshRenderer.setBox(myEntity)
```

The example above keeps movement at approximately the same speed as the movement example above, even if the frame rate drops. When running at 30 frames per second, the value of `dt` is 1/30.

You can also smoothen rotations in the same way by multiplying the rotation amount by `dt`.

## Move between two points

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
const COMPONENT_ID = 2046

const MoveTransportData = {
  start: Schemas.Vector3,
  end: Schemas.Vector3,
  fraction: Schemas.Float,
  speed: Schemas.Float,
}

export const LerpTransformComponent = engine.defineComponent(MoveTransportData, COMPONENT_ID)


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
	position: Vector3.create(4, 1, 4)
})

MeshRenderer.setBox(myEntity)

LerpTransformComponent.create(myEntity, {
  start: Vector3.create(4, 1, 4),
  end: Vector3.create(8, 1, 8),
  fraction: 0,
  speed: 1
})
```

<img src="/images/media/gifs/lerp-move.gif" alt="Move entity" width="300"/>



## Rotate between two angles

To rotate smoothly between two angles, use the _slerp_ (_spherical_ linear interpolation) algorithm. This algorithm is very similar to a _lerp_, but it handles quaternion rotations.

The `slerp()` function takes three parameters:

- The [quaternion](https://en.wikipedia.org/wiki/Quaternion) angle for the origin rotation
- The [quaternion](https://en.wikipedia.org/wiki/Quaternion) angle for the target rotation
- The amount, a value from 0 to 1 that represents what fraction of the translation to do.

{{< hint info >}}
**💡 Tip**:  You can pass rotation values in [euler](https://en.wikipedia.org/wiki/Euler_angles) degrees (from 0 to 360) by using `Quaternion.fromEulerDegrees()`.
{{< /hint >}}

```ts
const originRotation = Quaternion.fromEulerDegrees(0, 90, 0)
const targetRotation = Quaternion.fromEulerDegrees(0, 0, 0)

let newRotation = Quaternion.slerp(originRotation, targetRotation, 0.6)
```

To implement this in your scene, we recommend storing the data that goes into the `Slerp()` function in a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}). You also need to define a system that implements the gradual rotation in each frame.


```ts
// define custom component
const COMPONENT_ID = 2046

const RotateSlerpData = {
  start: Schemas.Quaternion,
  end: Schemas.Quaternion,
  fraction: Schemas.Float,
  speed: Schemas.Float,
}


export const SlerpData = engine.defineComponent(RotateSlerpData, COMPONENT_ID)


// define system
function SlerpRotate(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let slerpData = SlerpData.getMutable(myEntity)
	if (slerpData.fraction < 1) {
		slerpData.fraction += dt * slerpData.speed
		transform.rotation = Quaternion.slerp(slerpData.start, slerpData.end, slerpData.fraction)
	}
}

engine.addSystem(SlerpRotate)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4)
})

MeshRenderer.setBox(myEntity)

SlerpData.create(myEntity, {
  start: Quaternion.fromEulerDegrees(0, 0, 0),
  end: Quaternion.fromEulerDegrees(0, 180, 0),
  fraction: 0,
  speed: 0.3
})
```

{{< hint warning >}}
**📔 Note**:  You could instead represent the rotation with euler angles as `Vector3` values and use a `Lerp()` function, but that would imply a conversion from `Vector3` to `Quaternion` on each frame. Rotation values are internally stored as quaternions in the `Transform` component, so it's more efficient for the scene to work with quaternions.
{{< /hint >}}

 <img src="/images/media/gifs/lerp-rotate.gif" alt="Move entity" width="300"/>


A simpler but less efficient approach to this takes advantage of the `Quaternion.rotateTowards` function, and avoids using any custom components.

```ts
function SimpleRotate(dt: number) {
	let transform = Transform.getMutable(myEntity)
	transform.rotation = Quaternion.rotateTowards(transform.rotation, Quaternion.fromEulerDegrees(90, 0, 0), dt *10)
  if(transform.rotation === Quaternion.fromEulerDegrees(90, 0, 0)){
    console.log("done")
    engine.removeSystem(this)
  }
}

const simpleRotateSystem = engine.addSystem(SimpleRotate)

const myEntity = engine.addEntity()
Transform.create(myEntity, {
	position: Vector3.create(4, 1, 4),
	rotation: Quaternion.fromEulerDegrees(0, 0, 90)
})

MeshRenderer.setBox(myEntity)
```

In the example above `Quaternion.rotateTowards` takes three arguments: the initial rotation, the final rotation that's desired, and the maximum increment per frame. In this case, since the maximum increment is of `dt * 10` degrees, the rotation will be carried out over a period of a couple of 9 seconds.

Note that the system also checks to see if the rotation is complete and if so it removes the system from the engine. Otherwise, the system would keep making calculations on every frame, even once the rotation is complete.


## Change scale between two sizes

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
const COMPONENT_ID = 2046

const ScaleTransportData = {
  start: Schemas.Number,
  end: Schemas.Number,
  fraction: Schemas.Float,
  speed: Schemas.Float,
}

export const ScaleTransformComponent = engine.defineComponent(ScaleTransportData, COMPONENT_ID)


// define system
function LerpMove(dt: number) {
	let transform = Transform.getMutable(myEntity)
	let lerp = ScaleTransformComponent.getMutable(myEntity)
	if (lerp.fraction < 1) {
		lerp.fraction += dt * lerp.speed
    const newScale =  Scalar.lerp(lerp.start, lerp.end, lerp.fraction)
		transform.scale = Vector3.create(newScale, newScale, newScale)
	}
}

engine.addSystem(LerpMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: {x: 4, y: 1, z: 4}
})

MeshRenderer.setBox(myEntity)

ScaleTransformComponent.create(myEntity, {
  start: 1,
  end: 2,
  fraction: 0,
  speed: 1
})

Vector3.create(1, 1, 1)
```

 <img src="/images/media/gifs/lerp-scale.gif" alt="Move entity" width="300"/>


## Move at irregular speeds between two points

While using the lerp method, you can make the movement speed non-linear. In the previous example we increment the lerp amount by a given amount each frame, but we could also use a mathematical function to increase the number exponentially or in other measures that give you a different movement pace.

You could also use a function that gives recurring results, like a sine function, to describe a movement that comes and goes. 

Often these non-linear transitions can breathe a lot of life into a scene. A movement that speeds up over a curve or slows down gradually can say a lot about the nature of an object or character. You could even take advantage of mathematical functions that add bouncy effects.

```ts
// define custom component
const COMPONENT_ID = 2046

const MoveTransportData = {
  start: Schemas.Vector3,
  end: Schemas.Vector3,
  fraction: Schemas.Float,
  speed: Schemas.Float,
}

export const LerpTransformComponent = engine.defineComponent(MoveTransportData, COMPONENT_ID)

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
function interpolate(t: number){
	return t * t
}

engine.addSystem(LerpMove)

// create entity
const myEntity = engine.addEntity()

Transform.create(myEntity, {
	position: {x: 4, y: 1, z: 4}
})

MeshRenderer.setBox(myEntity)

LerpTransformComponent.create(myEntity, {
  start: Vector3.create(4, 1, 4),
  end: Vector3.create(8, 1, 8),
  fraction: 0,
  speed: 1
})
```



The example above is just like the linear lerp example we've shown before, but the `fraction` field mapped to a non-linear value on every tick. This non-linear value is used to calculate the `lerp` function, resulting in a movement that follows an exponential curve.

You can also map a transition in rotation or in scale in the same way as shown above, by mapping a linear transition to a curve.

 <img src="/images/media/gifs/lerp-speed-up.gif" alt="Move entity" width="300"/>

## Follow a path

You can have an entity loop over an array of vectors, performing a lerp movement between each to follow a more complex path.

```ts
// define custom component
const COMPONENT_ID = 2046

const PathTransportData = {
  path: Schemas.Array(Schemas.Vector3),
  start: Schemas.Vector3,
  end: Schemas.Vector3,
  fraction: Schemas.Float,
  speed: Schemas.Float,
  pathTargetIndex: Schemas.Int
}

export const LerpTransformComponent = engine.defineComponent(PathTransportData, COMPONENT_ID)


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
	position: Vector3.create(1, 1, 1)
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
  pathTargetIndex: 1
})
```

The example above defines a 3D path that's made up of four 3D vectors. The `PathTransportData` custom component holds the same data used by the custom component in the _lerp_ example above, but adds a `path` array, with all of the points in our path, and a `pathTargetIndex` field to keep track of what segment of the path is currently in use.

The system is very similar to the system in the _lerp_ example, but when a lerp action is completed, it sets the `target` and `origin` fields to new values. If we reach the end of the path, we return to the first value in the path.

 <img src="/images/media/gifs/lerp-path.gif" alt="Move entity" width="300"/>

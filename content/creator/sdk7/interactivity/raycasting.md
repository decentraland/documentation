---
date: 2018-02-27
title: Raycasting
description: Use raycasting to trace a line in space and query for collisions with entities in the scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/raycasting/
weight: 5
---


Raycasting is a fundamental tool in game development. With raycasting, you can trace an imaginary line in space, and query if any entities are intersected by the line. This is useful for calculating lines of sight, trajectories of bullets, pathfinding algorithms and many other applications.

When a player pushes the pointer button, or the primary or secondary button, a ray is traced from the player's position in the direction they are looking, see [button events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}) for more details about this. This document covers how to trace an invisible ray from any arbitrary position and direction, independent of player actions, which you can use in many other scenarios.

Please note that as a general rule, all raycasts in the SDK will only hit objects with colliders. So if you want to detect ray hits against a model that you've imported, that model should contain [collider meshes](/creator/3d-models/colliders), or you should add a [MeshCollider component]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). 

It's also a good practice to assign custom [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}) to 3D models, so that rays only need to calculate collisions against the relevant entities, instead of against everything that has a collider.


## Create a ray

A Raycast component describes the invisible ray that is used to query for intersecting entities. The ray is traced starting at the entity's position, as defined by the Transform component and affected by that of any parent entities. The direction can be defined in various ways, 

Rays are defined using the following data:


- `direction`: _Vector3_ or _Entity_ describing the direction of the ray. Its behavior will depend on the mode of the ray:
	- `LOCAL_DIRECTION`: A direction relative to the forward-facing direction of the entity, affected also by the transformation of any parent entities. This is useful to detect obstacles in front of vehicles honoring their heading.
	- `GLOBAL_DIRECTION`: Ignores the entity's rotation, and faces a direction as if the entity's rotation was 0. This is useful to i.e. always point down.
	- `GLOBAL_TARGET`: Traces a line between the entity's position and a target global position in the scene. It ignores the entity's rotation.
	- `TARGET_ENTITY`:  Traces a line between the entity's position and the position of a second target entity. It ignores the rotation of either entities.
- `maxDistance`: _number_ to set the length with which this ray will be traced.
- `queryType`: _RaycastQueryType_ enum value, to define if the ray will return all hit entities or just the first. The following options are available:
	- `RaycastQueryType.RQT_QUERY_ALL`: only returns the first hit entity, starting from the origin point.
	- `RaycastQueryType.RQT_HIT_FIRST`: returns all hit entities, from the origin through to the max distance of the ray.
- `collisionMask`: Only detect collisions with certain collision layers. Use this together with a custom collision layer, or to only detect the physics or pointer events layer. See [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}). By default, all layers are detected.
- `originOffset`: Instead of starting the raycast from the entity's origin position, add an offset to start the query from a relative position. You can for example use a small offset to prevent the ray colliding against the entity's own 3D model.
- `continuous`: If true, will keep running a raycast query on every frame. If false, the ray will only be used on the current frame. By default this value is false.

{{< hint warning >}}
**📔 Note**: The `continuous` property should be used with caution, as running a raycast query on every frame can be very expensive for performance. When possible, use a system (or the `interval` function in the Utils library) to run raycast queries at a regular more sparse interval, see [recurrent raycasting](#recurrent-raycasting).
{{< /hint >}}



```typescript
const ray1 = engine.addEntity()

Transform.create(ray1, {
	position: Vector3.create(8, 1, 0)
})

// only return first entity
Raycast.createOrReplace(ray1, {
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_HIT_FIRST
})

const ray2 = engine.addEntity()

Transform.create(ray2, {
	position: Vector3.create(8, 1, 0)
})

// return all entities
Raycast.createOrReplace(ray2, {
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})
```


## Raycast Results

After creating a Raycast component, the entity that this component is added to will have a `RaycastResult` component. This component includes information about any hits of the ray. Set up a system to check for this data.

The `RaycastResult` component contains the following data:

- `globalOrigin`: The position where the ray was originated, relative to the scene.
- `direction`: The global direction that the ray was pointing, as a `Vector3`.
- `hits`: An array with one object for each entity that was hit. If there were no hit entities, this array is empty. If the raycast used `RaycastQueryType.RQT_HIT_FIRST`, this array will only contain one object.

Each object in the `hits` array includes:

- `entityId`: Id number of the entity that was hit by the ray.
- `meshName`: _String_ with the internal name of the specific mesh in the 3D model that was hit. This is useful when a 3D model is composed of multiple meshes.
- `position`: _Vector3_ for the position where the ray intersected with the hit entity (relative to the scene)
- `length`: Length of the ray from its origin to the position where the hit against the entity occurred.
- `normalHit`: _Quaternion_ for the angle of the normal of the hit in world space.
- `globalOrigin`: _Vector3_ for the position where the ray originates (relative to the scene)
- `direction`: The global direction that the ray was pointing, as a `Vector3`.

The example below shows how you can access results from an individual entity using a system:

```typescript

const rayEntity = engine.addEntity()

Transform.create(rayEntity, {
	position: Vector3.create(8, 1, 0)
})

// return all entities
Raycast.createOrReplace(rayEntity, {
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})

engine.addSystem(() => {
	const rayResult = RaycastResult.get(rayEntity)
	console.log(rayResult.hits)
})
```

The next example shows how you can access `RaycastResult` components from all entities in the scene, using a [component query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}).

```typescript
engine.addSystem(() => {
	for (const [_, result] of engine.getEntitiesWith(RaycastResult)) {
		console.log(result.hits)
	}
})
```

{{< hint warning >}}
**📔 Note**:  The results of a raycast do not arrive on the same tick of the game loop that you created the raycast. The results may take one or multiple ticks to arrive.
{{< /hint >}}


In a scene where you use multiple kinds of rays for different purposes (like for path finding, line-of-sight checking, projectile tracing, etc), you might want to use different [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}), to avoid calculating irrelevant collisions.


## Recurrent raycasting

If your scene recurrently performs raycasting, then you should be careful about how it affects your scene's performance. You can use the `continuous` property to run a query on every tick of the game loop, but depending on the use case, it's often better to send at wider intervals, like just once a second, or every fifth of a second.


```typescript
// custom components
const CubeOscilator = engine.defineComponent(
  "CubeOscilator",
  {
    t: Schemas.Float
  }
)

const TimerComponent = engine.defineComponent(
  "TimerComponent",
  {
    t: Schemas.Float
  }
)

const RAY_INTERVAL = 0.1

// check rays
engine.addSystem((dt) => {
  for (const [entity] of engine.getEntitiesWith(TimerComponent)) {
    const timer = TimerComponent.getMutable(entity)
    timer.t += dt

    if (timer.t > RAY_INTERVAL) {
      timer.t = 0

      Raycast.createOrReplace(entity, {
        direction: Vector3.create(0, 0, 1),
        maxDistance: 16,
        queryType: RaycastQueryType.RQT_HIT_FIRST
      })
    }
  }

  for (const [_, result] of engine.getEntitiesWith(RaycastResult)) {
    console.log("ray hit : ", result.hits.length)
  }
})

TimerComponent.create(engine.addEntity())


// oscillating cube system
engine.addSystem((dt) => {
  for (const [entity, cube] of engine.getEntitiesWith(
    CubeOscilator,
    Transform
  )) {
    CubeOscilator.getMutable(entity).t += dt
    Transform.getMutable(entity).position.y = 2 + Math.cos(cube.t)
  }
})

// create cube
const cubeEntity = engine.addEntity()
Transform.create(cubeEntity, { position: { x:8, y:1, z:8 } })
CubeOscilator.create(cubeEntity)
MeshRenderer.setBox(cubeEntity)
MeshCollider.setBox(cubeEntity)
```




The example above runs a recurring raycast every 0.1 seconds. It uses a timer component and a system's `dt` property to time these evenly. It also includes a cube that oscillates up and down, controlled by another system, to move in and out of the path of the ray.

{{< hint info >}}
**💡 Tip**: Use the `interval` function in the Utils library for a simpler way to run a function at a fixed interval.
{{< /hint >}}
<!-- TODO: link to utils -->



## Collide with the player

You can't directly hit the player with a ray, but what you can do as a workaround is position an invisible entity occupying the same space as the player using the [`AvatarAttach component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#attach-an-entity-to-an-avatar">}}), and check collisions with that cube.


<!--

## Hit other avatars


PhysicsCast.hitFirstAvatar( query:RaycastQuery,
			    hitCallback:(e:RaycastHitAvatar) => {} )

PhysicsCast.hitAllAvatars( query:RaycastQuery,
			  hitCallback:(e:RaycastHitAvatars) => {} )


-->

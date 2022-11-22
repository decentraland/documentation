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



## Create a ray

A Raycast component describes the invisible ray that will be used to query for entities. Rays are defined using the following data:

- `timestamp`: _number_ with the time of sending the ray
- `origin`: _Vector3_ with the coordinates in scene space to start the ray from. 
- `direction`: _Vector3_ describing the direction of the ray (as if the ray started from _0,0,0_).
- `maxDistance`: _number_ to set the length with which this ray will be traced.
- `queryType`: _RaycastQueryType_ enum value, to define if the ray will return all hit entities or just the first. The following options are available:
	- `RaycastQueryType.RQT_QUERY_ALL`: only returns the first hit entity, starting from the origin point.
	- `RaycastQueryType.RQT_HIT_FIRST`: returns all hit entities, from the origin through to the max distance of the ray.

> Note: The `origin` and `direction` are not affected if the entity that holds the `Raycast` component also has a Transform, or if the entity has a parent entity with a Transform. The ray is traced in scene space, relative to the scene's _0, 0, 0_ point. 


<!-- TODO: Remove timestamp?? -->

```typescript
let originPos = Vector3.create(2, 1, 4)
let direction = Vector3.create(0, 1, 1)

// only return first entity
Raycast.createOrReplace(engine.addEntity(), {
  timestamp: 123,
  origin: Vector3.create(8, 1, 0),
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_HIT_FIRST
})

// return all entities
Raycast.createOrReplace(engine.addEntity(), {
  timestamp: 123,
  origin: Vector3.create(8, 1, 0),
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})
```

> Tip: The `Raycast` component must be added to an entity when created. If don't need to reference that entity again, you can do as in the example above, and instance a new entity while creating the component.


## Results results

After creating a Raycast component, the entity that this component is added to will have a `RaycastResult` component. This component includes information about any hits of the ray. Set up a system to check for this data.

The `RaycastResult` component contains a `hits` array, with one object for each entity that was hit. If there were no hit entities, this array is empty. If the raycast used `RaycastQueryType.RQT_HIT_FIRST`, this array will only contain one object.

Each object in the `hits` array includes:

- `entityId`: Id number of the entity that was hit by the ray.
- `meshName`: _String_ with the internal name of the specific mesh in the 3D model that was hit. This is useful when a 3D model is composed of multiple meshes.
- `origin`: _Vector3_ for the position where the ray originates (relative to the scene)
- `position`: _Vector3_ for the position where the ray intersected with the hit entity (relative to the scene)
- `length`: Length of the ray from its origin to the position where the hit against the entity occurred.
- `normalHit`: _Quaternion_ for the angle of the normal of the hit in world space.


The example below shows how you can access results from an individual entity using a system:

```typescript
let originPos = Vector3.create(2, 1, 4)
let direction = Vector3.create(0, 1, 1)


const rayEntity = engine.addEntity()

Raycast.createOrReplace(rayEntity, {
  timestamp: 123,
  origin: Vector3.create(8, 1, 0),
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})

engine.addSystem(() => {
	const rayResult = RaycastResult.get(rayEntity)
	log(rayResult.hits)
})
```

The next example shows how you can access `RaycastResult` components from all entities in the scene, using a [component query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}).

```typescript
let originPos = Vector3.create(2, 1, 4)
let direction = Vector3.create(0, 1, 1)


const rayEntity = engine.addEntity()

Raycast.createOrReplace(rayEntity, {
  timestamp: 123,
  origin: Vector3.create(8, 1, 0),
  direction: Vector3.create(0, 0, 1),
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})

engine.addSystem(() => {
	for (const [_, result] of engine.getEntitiesWith(RaycastResult)) {
		log(result.hits)
	}
})
```

> Note: The results of a raycast do not arrive on the same tick of the game loop that you created the raycast. The results may take one or multiple ticks to arrive.

In a scene where you use multiple kinds of rays for different purposes (like for path finding, line-of-sight checking, projectile tracing, etc), you might want to add custom components as flags to each kind of entity that holds `Raycast` components. Then you can query for these separately, and deal with each in a different way.






## Recurrent raycasting

If your scene recurrently performs raycasting, then you should be careful about how it affects your scene's performance.

For example, you might not need to send a new ray on _every_ tick of the game loop. Depending on the use case, it might make more sense to send just one a second, or every half-second.

<!-- 
TODO: not true anymore, right?

Both the `hitAll` and `hitFirst` methods have a third argument that takes a _raycast id_. All raycast queries that share a same id are handled in a lossy queue, so that if these requests pile up over time then only the latest one to arrive is processed. This can potentially save a lot of resources and makes your scene run a lot more smoothly. 

In some cases you may want to have several separate raycast queries running at the same time, for example you might have a character that sends multiple rays in different directions to check for walls as it walks around. In these cases you should make sure that each raycast query has a separate id. Otherwise, if these different queries share a same id, the results of each might overwrite one another and valuable information will be lost on every frame.

-->

```typescript
// custom components
const CubeOscilator = engine.defineComponent(
  {
    t: Schemas.Float
  },
  212
)

const TimerComponent = engine.defineComponent(
  {
    timeStamp: Schemas.Int,
    t: Schemas.Float
  },
  213
)

// check rays
engine.addSystem((dt) => {
  for (const [entity] of engine.getEntitiesWith(TimerComponent)) {
    const timer = TimerComponent.getMutable(entity)
    timer.t += dt

    if (timer.t > 0.1) {
      timer.timeStamp++
      timer.t = 0

      Raycast.createOrReplace(entity, {
        timestamp: timer.timeStamp,
        origin: Vector3.create(8, 1, 0),
        direction: Vector3.create(0, 0, 1),
        maxDistance: 16,
        queryType: RaycastQueryType.RQT_HIT_FIRST
      })
    }
  }

  for (const [_, result] of engine.getEntitiesWith(RaycastResult)) {
    log("ray hit : ", result.hits.length)
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


<!--
This example runs two raycast queries on every frame of the scene. Since they each have a different id, the requests from the first query and from the second query are handled on different queues that are independent from the other.

-->

## Collide with the player

You can't directly hit the player with a ray, but what you can do as a workaround is position an invisible entity occupying the same space as the player using the [`AvatarAttach component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#attach-an-entity-to-an-avatar">}}), and check collisions with that cube.


<!--

## Hit avatars


PhysicsCast.hitFirstAvatar( query:RaycastQuery,
			    hitCallback:(e:RaycastHitAvatar) => {} )

PhysicsCast.hitAllAvatars( query:RaycastQuery,
			  hitCallback:(e:RaycastHitAvatars) => {} )


## Cast a sphere


-->

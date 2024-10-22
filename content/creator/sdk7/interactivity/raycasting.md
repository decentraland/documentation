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

Raycasting is a fundamental tool in game development. With raycasting, you can trace an imaginary line in space, and query if any entities are intersected by that line. This is useful for calculating lines of sight, trajectories of bullets, pathfinding algorithms and many other applications.

When a player pushes the pointer button, or the primary or secondary button, a ray is traced from the player's position in the direction they are looking, see [button events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}) for more details about this. This document covers how to trace an invisible ray from any arbitrary position and direction, independent of player actions, which you can use in many other scenarios.

Please note that raycasts only hit objects with colliders. So if you want to detect ray hits against a 3D model, either:

- The model must contain [collider meshes]({{< ref "/content/creator/3d-modeling/colliders.md">}}).
- The `GLTFContainer` must be configured to use the [visible geometry with collision masks]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#colliders-on-3d-models" >}}).
- Add a [MeshCollider component]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}).

It's also a good practice to assign custom [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}) to 3D models, so that rays only need to calculate collisions against the relevant entities, instead of against everything that has a collider.

## Create a ray

All rays have a point of origin and a direction. The point of origin is based on an entity's position, taking the values on the entity's Transform component. The direction of a ray can be defined in 4 different ways: 

- **local**: A direction relative to the forward-facing direction of the entity, affected also by the transformation of any parent entities. This is useful to detect obstacles in front of vehicles honoring their heading. 
- **global**: Ignores the entity's rotation, and faces a direction as if the entity's rotation was 0. This is useful to i.e. always point down. 
- **global target**: Traces a line between the entity's position and a target global position in the scene. It ignores the entity's rotation. Useful for example to create tower defense games, each tower's turret can point to a pin-pointed coordinate in space. 
- **target entity**: Traces a line between the entity's position and the position of a second target entity. It ignores the rotation of either entities.

The following code creates a raycast with a local direction:

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
  position: Vector3.create(4, 1, 4),
})

raycastSystem.registerLocalDirectionRaycast(
  {
    entity: myEntity,
    opts: { direction: Vector3.Forward() },
  },
  function (raycastResult) {
    // callback function
  }
)
```

Use the following functions to create raycasts by providing the direction in different ways:

- `raycastSystem.registerLocalDirectionRaycast()`: creates a raycast with a **local** direction. The `direction` field expects a `Vector3` that describes a vector relative to the entity and its rotation (e.g. `Vector3.Forward()` would end up using the entity's transform forward vector)
- `raycastSystem.registerGlobalDirectionRaycast()`: creates a raycast with a **global** direction. The `direction` field expects a `Vector3` that describes the global direction.
- `raycastSystem.registerGlobalTargetRaycast()`: creates a raycast with a direction defined by a **global target** position. The `target` field expects a `Vector3` that describes a global position in the scene.
- `raycastSystem.registerTargetEntityRaycast()`: creates a raycast with a direction defined towards a **target entity** position. The `targetEntity` field expects a reference to an entity, this entity's position will be used as the target of the ray.

The following optional fields are available when creating a ray with any of the above methods:

- `maxDistance`: _number_ to set the length with which this ray will be traced. If not set, the default is 16 meters.
- `queryType`: _RaycastQueryType_ enum value, to define if the ray will return all hit entities or just the first. The following options are available:
  - `RaycastQueryType.RQT_HIT_FIRST`: _(default)_ only returns the first hit entity, starting from the origin point.
  - `RaycastQueryType.RQT_QUERY_ALL`: returns all hit entities, from the origin through to the max distance of the ray.
- `originOffset`: Instead of starting the raycast from the entity's origin position, add an offset to start the query from a relative position. You can for example use a small offset to prevent the ray colliding against the entity's own collider. If not set, the default is `Vector3.Zero()`.
- `collisionMask`: Only detect collisions with certain collision layers. Use this together with a custom collision layer, or to only detect the physics or pointer events layer. See [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}). If not set, the default layer used is `ColliderLayer.CL_PHYSICS`.
- `continuous`: If true, will keep running a raycast query on every frame. If false, the ray will only be used on the current frame. If not set, the default is false.

- When setting the direction with a local or glocal direction, the `direction` field defaults to `Vector3.Forward()`.
- When setting the direction with a global target, the `globalTarget` field defaults to `Vector3.Zero()`.
- When setting the direction with an entity target, the `targetEntity` field defaults to the scene's root entity, located at `Vector3.Zero()`.

{{< hint warning >}}
**📔 Note**: The `continuous` property should be used with caution, as running a raycast query on every frame can be very expensive for performance. When possible, use a system (or the `interval` function in the Utils library) to run raycast queries at a regular more sparse interval, see [recurrent raycasting](#recurrent-raycasting).
{{< /hint >}}

Below are examples using each of the four methods to determine the ray direction:

```ts
// LOCAL DIRECTION RAYCAST
raycastSystem.registerLocalDirectionRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      direction: Vector3.Forward(),
      maxDistance: 30,
    },
  },
  function (raycastResult) {
    console.log(raycastResult.hits)
  }
)
// GLOBAL DIRECTION RAYCAST
raycastSystem.registerGlobalDirectionRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      direction: Vector3.Forward(),
      maxDistance: 30,
    },
  },
  function (raycastResult) {
    console.log(raycastResult.hits)
  }
)
// GLOBAL TARGET POSITION RAYCAST
raycastSystem.registerGlobalTargetRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      globalTarget: Vector3.Zero(),
    },
  },
  (raycastResult) => {
    console.log(raycastResult.hits)
  }
)
// TARGET ENTITY RAYCAST
const targetEntity = engine.addEntity()
Transform.create(targetEntity, { position: Vector3.create(8, 1, 10) })

raycastSystem.registerTargetEntityRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      targetEntity: targetEntity,
    },
  },
  (raycastResult) => {
    console.log(raycastResult.hits)
  }
)
```

{{< hint warning >}}
**📔 Note**: `raycastSystem`, `RaycastQueryType` and `ColliderLayer` must be imported via

> `import { raycastSystem, RaycastQueryType, ColliderLayer } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

## Raycast result

The callback function that handles the raycast receives an object containing data about the ray itself, and any entities that were hit.

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

The following example iterates over the entities that were hit:

```ts
const myEntity = engine.addEntity()
Transform.create(myEntity, {
  position: Vector3.create(4, 1, 4),
})

raycastSystem.registerLocalDirectionRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      direction: Vector3.Forward(),
      maxDistance: 30,
    },
  },
  function (raycastResult) {
    if (raycastResult.hits.length > 0) {
      for (const hit of raycastResult.hits) {
        if (hit.entityId) {
          console.log('hit entity ', hit.entityId)
        }
      }
    } else {
      console.log('no entities hit')
    }
  }
)
```

{{< hint warning >}}
**📔 Note**: You can get a raycast result from hitting an entity on a different scene. This may be especially useful when creating portable experiences or smart wearables, that can react to the surroundings.

However, note that currently you can only obtain raycast responses when the collision is with conent in a scene done with SDK7. Older SDK6 scenes won't return any hit result.
{{< /hint >}}


## Collision layers

It's a good practice to only check for collisions against entities that are relevant, to make the scene more performant. The `collisionMask` field allows to to list only specific collision layers, which can include the physics layer (that blocks player movement), the pointer layer (which is used for pointer events), and 8 custom layers that you can assign freely to whatever your needs are. See [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}). By default, all layers are detected.

By default, the `collisionMask` field is set to respond to both the layers `ColliderLayer.CL_POINTER` and `ColliderLayer.CL_PHYSICS`. You can change this value to list only one of those, or to include custom layers. Use the `|` separator to list multiple options.

```ts
raycastSystem.registerLocalDirectionRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      direction: Vector3.Forward(),
      maxDistance: 30,
      collisionMask:
        ColliderLayer.CL_CUSTOM1 |
        ColliderLayer.CL_CUSTOM3 |
        ColliderLayer.CL_POINTER,
    },
  },
  (raycastResult) => {
    log(raycastResult.hits)
  }
)
```

## Recurrent raycasting

When using the functions of the `raycastSystem`, the default behavior is to create a single ray, that will query for collisions once. As an alternative, you can set the `continuous` field to _true_ to run a query and the callback function on every tick of the game loop.

The following example will keep running the raycast query from this point onwards

```ts
raycastSystem.registerLocalDirectionRaycast(
  {
    entity: myEntity,
    opts: {
      queryType: RaycastQueryType.RQT_QUERY_ALL,
      direction: Vector3.Forward(),
      maxDistance: 30,
      continuous: true,
    },
  },
  function (raycastResult) {
    log(raycastResult.hits)
  }
)
```

{{< hint warning >}}
**📔 Note**: The `continuous` property should be used with caution, as running a raycast query on every frame can be very expensive for performance.
{{< /hint >}}

When not needed anymore, remove any recurrent raycasts. To do so, you must use `raycastSystem.removeRaycasterEntity`.

```ts
raycastSystem.removeRaycasterEntity(myEntity)
```

When possible, use a system (or the `interval` function in the Utils library) to run raycast queries at a regular more sparse interval, like just once a second, or every fifth of a second.

```typescript
// custom components
const CubeOscilator = engine.defineComponent('CubeOscilator', {
  t: Schemas.Float,
})

const TimerComponent = engine.defineComponent('TimerComponent', {
  t: Schemas.Float,
})

const RAY_INTERVAL = 0.1

// check rays
engine.addSystem((dt) => {
  for (const [entity] of engine.getEntitiesWith(TimerComponent)) {
    const timer = TimerComponent.getMutable(entity)
    timer.t += dt

    if (timer.t > RAY_INTERVAL) {
      timer.t = 0
      raycastSystem.registerGlobalDirectionRaycast(
        {
          entity: myEntity,
          opts: {
            queryType: RaycastQueryType.RQT_HIT_FIRST,
            direction: Vector3.Forward(),
            maxDistance: 16,
          },
        },
        function (raycastResult) {
          log(raycastResult.hits)
        }
      )
    }
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
Transform.create(cubeEntity, { position: { x: 8, y: 1, z: 8 } })
CubeOscilator.create(cubeEntity)
MeshRenderer.setBox(cubeEntity)
MeshCollider.setBox(cubeEntity)
```

The example above runs a recurring raycast every 0.1 seconds. It uses a timer component and a system's `dt` property to time these evenly. It also includes a cube that oscillates up and down, controlled by another system, to move in and out of the path of the ray.

{{< hint info >}}
**💡 Tip**: Use the `interval` function in the [SDK Utils library](https://github.com/decentraland/sdk7-utils) for a simpler way to run a function at a fixed interval.
{{< /hint >}}

## Raycasts via a system

Another way to perform recurrent raycasts is to execute them from within the recurring function of a system. This allows you to have a lot more control about when and how these work. Instead of registering a callback function, you can perform a raycast query with `raycastSystem.registerRaycast` and then check the data returned by this operation, all within the function of the system.

Please note that since the raycast is executed in a system, the result will only be available the next tick, needing two runs of the system. One to register the raycast for the next frame, and the next frame process its result.

```ts
engine.addSystem((deltaTime) => {
		const result = raycastSystem.registerRaycast(
			entity,
			localDirectionOptions({
				collisionMask: ColliderLayer.CL_CUSTOM1 | ColliderLayer.CL_CUSTOM3 | ColliderLayer.CL_POINTER,
				originOffset: Vector3.create(0, 0.4, 0),
				maxDistance: RAY_POWER,
				queryType: raycastQueryType,
				direction: Vector.forward()
				continuous: true // don't overuse the 'continuous' property as raycasting is expensive on performance
			})
		)
		if (result) // do something
	})
```

## Collide with the player

You can't directly hit the player's avatar or those of other players with a ray, but what you can do as a workaround is position an invisible entity occupying the same space as a player using the [AvatarAttach component]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#attach-an-entity-to-an-avatar">}}), and check collisions with that cube.

## Raycasts from the player

To trace a ray from the player's position in the direction faced by the camera, you can trace a ray using the camera or the avatar [Reserved entities]({{< ref "/content/creator/sdk7/architecture/entities-components.md#reserved-entities">}}).

{{< hint info >}}
**💡 Tip**: For most cases, you might be better off using [Pointer eveents]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md">}}) instead of raycasts.
{{< /hint >}}

The following example traces a ray from the player's camera position forward, using the `engine.CameraEntity` entity.

```ts
raycastSystem.registerGlobalDirectionRaycast(
  {
    entity: engine.CameraEntity,
    opts: {
      queryType: RaycastQueryType.RQT_HIT_FIRST,
      direction: Vector3.rotate(
        Vector3.Forward(),
        Transform.get(engine.CameraEntity).rotation
      ),
    },
  },
  function (raycastResult) {
    console.log(raycastResult)
  }
)
```

{{< hint warning >}}
**📔 Note**: Keep in mind that in 3rd person the cursor could in the future not behave the same as in 1st person. It's recommended to only use this if the player is in 1st person.
{{< /hint >}}

## Advanced syntax

### Create a raycast component

A Raycast component describes the invisible ray that is used to query for intersecting entities. The ray is traced starting at the entity's position, as defined by the Transform component and affected by that of any parent entities. The direction can be defined in various ways,

Rays are defined using the following data:

- `direction`: An object that contains a `$case` field to select the type of direction, and an additional field that will depend on this type, that determines this direction. The following are the accepted values for `$case`:
  - `LOCAL_DIRECTION`: A direction relative to the forward-facing direction of the entity, affected also by the transformation of any parent entities. This is useful to detect obstacles in front of vehicles honoring their heading. The rotation is defined by the `localDirection` field, as a `Vector3` that describes a rotation.
  - `GLOBAL_DIRECTION`: Ignores the entity's rotation, and faces a direction as if the entity's rotation was 0. This is useful to i.e. always point down. The rotation is defined by the `globalDirection` field, as a `Vector3` that describes a rotation.
  - `GLOBAL_TARGET`: Traces a line between the entity's position and a target global position in the scene. It ignores the entity's rotation. Useful to create tower defense games, each tower's turret can point to a pin-pointed coordinate in space. The target is defined by the `globalTarget` field, as a `Vector3` that describes the global position.
  - `TARGET_ENTITY`: Traces a line between the entity's position and the position of a second target entity. It ignores the rotation of either entities. The target is defined by the `targetEntity` field, holding a reference to the entity.
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

The following example uses a global rotation to determine the direction, and only returns the first entity that is hit on the frame that the ray is sent.

```typescript
const entity1 = engine.addEntity()

Transform.create(entity1, {
  position: Vector3.create(8, 1, 0)
})

Raycast.createOrReplace(entity1, {
  direction: {
    $case: "globalDirection",
    globalDirection: Vector3.create(0, 0, 1)
  }
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_HIT_FIRST
})
```

The example below launches a ray in the forward-facing direction of the entity, returning only the first item hit. It does so continuously. It also includes a minor offset of 0.5 to prevent the ray from hitting the entity's own collider.

```typescript
const entity1 = engine.addEntity()

Transform.create(entity1, {
  position: Vector3.create(8, 1, 0)
})

Raycast.createOrReplace(entity1, {
  direction: {
    $case: "localDirection",
    localDirection: Vector3.Forward()
  }
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_HIT_FIRST,
  originOffset: Vector3.create(0.5, 0, 0),
  continuous: true
})
```

This example traces a ray between two entities. It returns all entities that are hit in between.

```ts
const entity1 = engine.addEntity()

Transform.create(entity1, {
  position: Vector3.create(8, 1, 0)
})

const entity2 = engine.addEntity()

Transform.create(entity2, {
  position: Vector3.create(0, 1, 8)
})

Raycast.createOrReplace(entity1, {
  direction: {
    $case: "targetEntity",
    targetEntity: entity2
  }
  maxDistance: 16,
  queryType: RaycastQueryType.RQT_QUERY_ALL
})
```

### Raycast results component

{{< hint warning >}}
**📔 Note**: The easiest way to deal with raycast results is to use `raycastEventSystem`, and register a callback function as part of the same statement that creates the ray. The`RaycastResult` component is used internally by that that interface, but also exposed to enable more advanced custom logic.
{{< /hint >}}

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
  direction: {
    $case: "globalDirection",
    globalDirection: Vector3.create(0, 0, 1)
  }
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
**📔 Note**: The results of a raycast do not arrive on the same tick of the game loop that you created the raycast. The results may take one or multiple ticks to arrive.
{{< /hint >}}

In a scene where you use multiple kinds of rays for different purposes (like for path finding, line-of-sight checking, projectile tracing, etc), you might want to use different [collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#collision-layers" >}}), to avoid calculating irrelevant collisions.

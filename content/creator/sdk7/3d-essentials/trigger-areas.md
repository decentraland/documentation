---
date: 2025-08-01
title: Trigger Areas
description: Learn how to use trigger areas in your scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/trigger-areas/
weight: 7
---


Trigger areas allow you to react to the event of a player entering or leaving an area, or of any other entity entering or leaving an area. This is a fundamental tool for creating interactive scenes. Use them for things like opening a door when the player approaches, or to score a point when a ball enters a goal.

## Using trigger areas

To use trigger areas you need to add a `TriggerArea` component to an entity, then use a `triggerAreaEventsSystem` to react to the events.

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity)

Transform.create(triggerEntity, {
  position: Vector3.create(8, 0, 8),
  scale: Vector3.create(1, 1, 1),
})

triggerAreaEventsSystem.onTriggerEnter(triggerEntity, function(result) {
  console.log('Player entered trigger area!')
})
```

## Trigger area shapes

Trigger areas can be either a box or a sphere.


```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

// Box
TriggerArea.setBox(triggerEntity)

// Sphere
TriggerArea.setSphere(triggerEntity)
```

Tip: The sphere is the easiest shape to calculate for the engine, as it's achieved by checking the distance from the center of the sphere. If in doubt, use a sphere.

To alter the size of the trigger area, you can use the `scale` property of the `Transform` component.

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity)

Transform.create(triggerEntity, {
  scale: Vector3.create(4, 2, 4),
})
```

### Debugging

To debug your scene and see the area covered by the trigger area, you can add a `MeshShape` component to the entity with the trigger area, and set the shape to the one you want to debug. The dimensions of the default mesh will match the dimensions of the trigger area.

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity)

MeshShape.setBox(triggerEntity)

Transform.create(triggerEntity, {
  position: Vector3.create(8, 0, 8),
})
```

## Trigger area events

You can use the `triggerAreaEventsSystem` to react to the different events of a trigger area:

- `onTriggerEnter`: Triggered when an entity enters the trigger area.
- `onTriggerExit`: Triggered when an entity leaves the trigger area.
- `onTriggerStay`: Triggered while an entity is in the trigger area, every frame.


```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity)

// On enter
triggerAreaEventsSystem.onTriggerEnter(triggerEntity, function(result) {
  console.log('Player entered trigger area!')
})

// On exit
triggerAreaEventsSystem.onTriggerExit(triggerEntity, function(result) {
  console.log('Player exited trigger area!')
})

// On stay
triggerAreaEventsSystem.onTriggerStay(triggerEntity, function(result) {
  console.log('Player is in trigger area!')
})
```

## Trigger area layers

Use the optional second argument of the `TriggerArea` component to set the layers that will activate the trigger area.

By deault, the trigger area is activated only by the player, via the layer `ColliderLayer.CL_PLAYER`. You can change this to any other collision layer by passing it as the second argument of the `TriggerArea` component.

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

// Trigger area
const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity, ColliderLayer.CL_CUSTOM1)

Transform.create(triggerEntity, {
  position: Vector3.create(8, 0, 8),
})

// Entity that will activate the trigger area
const movingEntity = engine.addEntity()

Transform.create(movingEntity, {
  position: Vector3.create(8, 0, 8),
})

MeshCollider.setBox(movingEntity, ColliderLayer.CL_CUSTOM1)
```

Allowed values are the same as the ones for the `MeshCollider` component. See [Collision layers]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#Collision-layers" >}}) for more details.

- `ColliderLayer.CL_PHYSICS`
- `ColliderLayer.CL_POINTER`
- `ColliderLayer.CL_CUSTOM1` through to `CL_CUSTOM8`
- `ColliderLayer.CL_NONE`

Tip: The layers `CL_CUSTOM1` through to `CL_CUSTOM8` don't have any special behavior on their own, you can use them for whatever suits your scene best.

You can also set up a trigger area to detect multiple layers at once.

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

const triggerEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity, ColliderLayer.CL_CUSTOM1 | ColliderLayer.CL_CUSTOM2)

Transform.create(triggerEntity, {
  position: Vector3.create(8, 0, 8),
})
```

This will activate the trigger area when any entity with the layers `CL_CUSTOM1` or `CL_CUSTOM2` enters the trigger area.

## Trigger event responses

When a trigger area event is triggered, you can use the `result` parameter to get information about both the entity that was triggered and the entity that triggered the event.

The following properties are available in the `result` parameter:


- `triggeredEntity`: The ID of the entity that was triggered (this is the entity that owns the trigger area)
- `triggeredEntityPosition`: The position of the entity that was triggered
- `triggeredEntityRotation`: The rotation of the entity that was triggered
- `eventType`: The type of trigger event (ENTER, EXIT, STAY)
- `timestamp`: The timestamp of the trigger event
- `trigger`: An object with the following fields:
    - `entity`: The ID of the entity that triggered the trigger (the entity that entered the trigger area)
    - `layer`: The collision layer of the entity that triggered the trigger
    - `position`: The position of the entity that triggered the trigger
    - `rotation`: The rotation of the entity that triggered the trigger
    - `scale`: The scale of the entity that triggered the trigger

```ts
import { engine } from '@dcl/sdk/ecs'
import { TriggerArea } from '@dcl/sdk/triggers'

// Trigger area
const triggeredEntity = engine.addEntity()

TriggerArea.setBox(triggerEntity)

Transform.create(triggerEntity, {
  position: Vector3.create(8, 0, 8),
})

// Entity that will trigger the trigger area
const triggerEntity = engine.addEntity()

const triggeredEntity = engine.addEntity()

Transform.create(triggeredEntity, {
  position: Vector3.create(8, 0, 8),
})

// On enter
triggerAreaEventsSystem.onTriggerEnter(triggerEntity, function(result) {
  console.log('An entity entered trigger area!', result.triggeredEntity)
  console.log('Triggered entity position: ', result.triggeredEntityPosition)
  console.log('Triggered entity rotation: ', result.triggeredEntityRotation)
  console.log('Event type: ', result.eventType)
  console.log('Timestamp: ', result.timestamp)
  console.log('Trigger entity: ', result.trigger.entity)
  console.log('Trigger layer: ', result.trigger.layer)
  console.log('Trigger position: ', result.trigger.position)
  console.log('Trigger rotation: ', result.trigger.rotation)
  console.log('Trigger scale: ', result.trigger.scale)
})
```
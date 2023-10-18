---
date: 2018-02-14
title: Advanced button events
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/advanced-button-events/
weight: 10
---

If you need the interaction in your scene to follow custom logic that is not compatible with the [Register callback]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) or the [System based]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approaches, you can deal with the raw input event data directly. This approach is the hardest, but the most flexible.



## The PointerEventsResult component


When a pointer event is detected by the engine, the entity that was clicked is assigned a `PointerEventsResult` component. This component contains all the raw data about the hit event, and stores historic data about previous events.

The helpers in `Input`, like `inputSystem.wasJustClicked` or  `inputSystem.getInputCommand` are good for most simple scenarios, but if you need to get more details about the hit event, check the raw data in the `PointerEventsResult`.

The `PointerEventsResult` stores a `commands` array, containing one object for each pointer event it stores. It stores a list of up to 30 events, newer events are stored at the end of the array. Once the list reaches a length of 30, it starts discarding old events for each new one that comes in.

Each event in the `commands` array has the following data:

- `analog`: Flag to mark if the event is from an analog or a digital input. Digital inputs have a value of _1_, analog inputs (like a joy stick) have a value of _0_.
- `button`: Which button id was pressed. The number corresponds to the `InputAction` enum, that lists all of the available buttons.
- `state`: Type of pointer event, from the enum `PointerEventType`. _0_ refers to `PointerEventType.PET_DOWN`, _1_ to `PointerEventType.PET_UP`, _2_ to `PointerEventType.PET_HOVER_ENTER`, _3_ to `PointerEventType.PET_HOVER_LEAVE`

- `timestamp`: A [lamport timestamp](https://en.wikipedia.org/wiki/Lamport_timestamp) to identify each button event. 

	> Note: This timestamp is not numbered based on the current time. Think of it as a counter that starts at 0 and is incremented by 1 for each event.

- `hit`: An object that contains the following data about the hit event:

	- `entityId`: Id number of the entity that was hit by the ray.
	- `meshName`: _String_ with the internal name of the specific mesh in the 3D model that was hit. This is useful when a 3D model is composed of multiple meshes.
	- `origin`: _Vector3_ for the position where the ray originates (relative to the scene)
	- `position`: _Vector3_ for the position where the ray intersected with the hit entity (relative to the scene)
	- `length`: Length of the ray from its origin to the position where the hit against the entity occurred.
	- `normalHit`: _Vector3_ with a normalized direction vector, describing the angle of the normal of the hit in world space.


```ts
function PointerReadingSystem() {
  const clickedCubes = engine.getEntitiesWith(PointerEventsResult)
  for (const [entity] of clickedCubes) {

    const result = PointerEventsResult.getOrNull(entity)
    if(result){
      console.log("POINTER EVENT DATA:", result.commands)
    }
  }
}

engine.addSystem(PointerReadingSystem)
```



## Track player movements


In real-time multiplayer games where the timing of player movements is critical, you may want to keep track of each player's position using a 3rd party server as the source of truth. You can improve response time by listening to the button in advance and predict their effects in your server before the avatar has shifted position.

This approach helps compensate for network delays, but is sure to result in discrepancies, so you should also regularly poll the player's current position to make corrections. Balancing these predictions and corrections may require plenty of fine-tuning.


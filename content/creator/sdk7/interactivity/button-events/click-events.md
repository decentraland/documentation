---
date: 2018-02-14
title: About input actions
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/click-events/
weight: 1
---


A Decentraland scene can detect input actions from all of the buttons that are used to control the player's avatar. These include pointer clicks, several action buttons, and the keys that are used to move the avatar around. Button events can come from a mouse, a touch screen, a VR controller or some other device, these are all interpreted the same by the SDK.

You can detect input actions against an entity. This involves pressing a button while the player's cursor is pointing at that entity's collider. You can also detect _global_ input event, that involve pressing activating the input at any time, without consideration for where the pointer is aiming.

{{< hint warning >}}
**📔 Note**   An entity must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}) to respond to input actions. If an entity has no collider, you can give it a `MeshCollider` component to make it clickable.
{{< /hint >}}


There are several different ways to handle input actions, depending on the use case.

- [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}): The easiest way to add interaction to a single entity. Write a single statement to set up a callback function and hover feedback.
- [**System-based**]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}): Ideal for handling multiple entities with similar behavior. Use a system to iterate over similar entities and query for input actions on each, handling them all with the same logic. Hover feedback needs to be set up separately. This approach is also required for handling global input actions.
- [**Advanced**]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}): Read the raw response data on each entity, including time-stamps and an event history of input events. This can be useful for defining custom interaction patterns.

## Hover Feedback

Whichever method you use, it's important to make players aware that an entity is interactive. Otherwise, they might completely miss out on the experience you built. It's not a good experience to be clicking on every object hoping for one to respond. Users of Decentraland are used to the pattern that any interactive items offer feedback on hover, so they will discard an item with no feedback as non-interactive.

The default way to add feedback is to display a hover hint on the UI whenever the player passes their cursor over the entity.  You can implement this behavior by adding a `PointerHoverFeedback` component to an entity.  The [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) approach makes this even easier, as you don't have to explicitly create this component.

You could also implement [custom] ways of feedback, for example you could play a sound, making the entity change color, spin or or enlarge while being pointed at, etc. Whatever you do, make sure that it's a clear signifier.


## Obstacles

Button events cast rays that only interact with the first entity on their path, as long as the entity is closer than its distance limit.

For an entity to be intercepted by the ray of a button event, the entity's 3d model must either have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). Either the entity's 3d model must include a collider mesh, or the entity must have a `CollierMesh` component.

If another entity's collider is standing on the way of the entity that the player wants to interact with it, the player won't be able to click the entity that's behind, unless the entity's `MeshCollider` component is configured to allow clicking through it.

## Pointer buttons


The following inputs can be handled by any of the approaches to detect input events.

- `InputAction.IA_POINTER`: **left-mouse button** on a computer.
- `InputAction.IA_PRIMARY`: **E** key on a computer.
- `InputAction.IA_SECONDARY`: **F** key on a computer.
- `InputAction.IA_ACTION_3`: **1** key on a computer.
- `InputAction.IA_ACTION_4`: **2** key on a computer.
- `InputAction.IA_ACTION_5`: **3** key on a computer.
- `InputAction.IA_ACTION_6`: **4** key on a computer.
- `InputAction.IA_JUMP`: **Space** key on a computer.
- `InputAction.IA_FORWARD`: **W** key on a computer.
- `InputAction.IA_LEFT`: **A** key on a computer.
- `InputAction.IA_RIGHT`: **D** key on a computer.
- `InputAction.IA_BACK`: **S** key on a computer.
- `InputAction.IA_WALK`: **Shift** key on a computer.


Each `InputAction` is abstracted away from the literal input in the keyboard so that it can be mapped to different inputs depending on the device. For this same reason, not all buttons on the keyboard can be tracked for button events, only the buttons that are used for movement and interaction. This intentional limitation is to ensure that all content is compatible in the future with VR controllers, other kinds of game controllers, and mobile devices. 

## Types of pointer events

Each input can produce the following types of pointer events. Each of the following is a value in the `PointerEventType` enum.

- `DOWN`: Player pushes down a specific button while having the cursor pointing at the entity's collider.
- `UP`: Player releases a specific button while having the cursor pointing at the entity's collider.
- `HOVER_ENTER`: Player's cursor starts pointing at the entity's collider.
- `HOVER_LEAVE`: Player's cursor stops pointing at the entity's collider.

<!-- > Note: A _click_ event, as detected by the `inputSystem.wasJustClicked` helper function, is a combination of a `DOWN` event followed by an `UP` event. Note that as this event may take several ticks of the game loop to be completed, it can't be detected in a single frame, and therefore can only be detected thanks to a helper function. -->



## Data from an input action

All input actions include data about the event, including things like the button that was activated, and where the pointer was pointing at at the time.

The following information can be obtained from any input event:

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
	- `normalHit`: _Quaternion_ for the angle of the normal of the hit in world space.


This data is accessed in different ways depending on what approach you're using to handle input actions.

Using the [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) approach, the first parameter passed to the callback function contains this entire data structure.

```ts
pointerEventsSystem.onPointerDown(
  myEntity,
  function (cmd) {
      console.log(cmd.hit.entityId)
  },
)
```

Using the [**System-based**]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approach, use `inputSystem.getInputCommand()` to fetch this data.

```ts
engine.addSystem(() => {
  const cmd = inputSystem.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)
  if(cmd){
 	console.log(cmd.hit.entityId)
  }
})
```

Using the [**Advanced**]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}) approach, the `PointerEventsResults` contains an array with a recent history of all pointer events against that entity.

```ts
engine.addSystem(() => {
  const pointerEvents = engine.getEntitiesWith(PointerEventsResult)
  for (const [entity] of pointerEvents) {
      const poninterEvents = PointerEventsResult.get(entity)

	  if(poninterEvents.commands.length > 0){
		console.log(poninterEvents.commands[0].hit.entityId)
	  }   
  }
})
```


<!-- 
When using `Input.getClick`, it returns an object with a `down` and an `up` object, each of these with all the same data structure returned by `inputSystem.getInputCommand`. The `down` object contains the data relevant to the moment when the moment when button was pushed down, the `up` object for when the button went up. -->

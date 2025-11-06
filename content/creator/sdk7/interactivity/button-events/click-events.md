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
**📔 Note**: Entities must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}) to respond to input actions. `MeshRenderer` models must also be given a `MeshCollider` component. Models from a `GLTFContainer` may have their own embedded collision geometry, or they can be configured to use their visible geometry, they can also be given a `MeshCollider` component.
{{< /hint >}}

There are several different ways to handle input actions, depending on the use case.

- [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}): The easiest way to add interaction to a single entity. Write a single statement to set up a callback function and hover feedback.
- [**System-based**]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}): Ideal for handling multiple entities with similar behavior. Use a system to iterate over similar entities and query for input actions on each, handling them all with the same logic. Hover feedback needs to be set up separately. This approach is also required for handling global input actions.
- [**Advanced**]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}): Read the raw response data on each entity, including time-stamps and an event history of input events. This can be useful for defining custom interaction patterns.

## Use the Scene Editor

The easiest way to handle click events on an entity is to use the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}). Use the no-code **On Click** or **On Input Action** Triggers on an item to call actions when clicking on it. Or use **On Global Click**, **On Global Primary** or **On Global Secondary** Triggers to react to global button events. See [Make any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}}).

## Simple example

To detect clicks on an entity, use `pointerEventsSystem.onPointerDown`.

```ts
pointerEventsSystem.onPointerDown(
	{
		entity: myEntity,
		opts: { button: InputAction.IA_PRIMARY, hoverText: 'Click' },
	},
	function () {
		console.log('clicked entity')
	}
)
```

See [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) for more information.

## Hover Feedback

It's important to make players aware that an entity is interactive. Otherwise, they might completely miss out on the experience you built. It's not a good experience to be clicking on every object hoping for one to respond.

When you use the [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) method, two kinds of feedback are displayed whenever the player passes their cursor over the object:

- The entity's edge is highlighted (only on the Decentraland 2.0 Desktop client). The highlight is green if the entity is close enough to click, red if the entity is too far away.
- A hover hint appears near the cursor with UI text, signalling what will happen if they click.

When using the [**System-based**]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) method, you can achieve the same results by adding a `PointerEvents` component to the clickable entities.

Both the entity highlight and the hover hint can be disabled via properties in these methods and components.

You could also implement [advanced custom hints]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md#advanced-custom-hints" >}}), for example you could play a sound, making the entity change color, spin or enlarge while being pointed at, etc. Whatever you do, make sure that it's a clear signifier.

## Obstacles

Button events cast rays that only interact with the first entity on their path that is subscribed to the pointer events collision layer, as long as the entity is closer than its distance limit.

For an entity to be intercepted by the ray of a pointer event, either:

- The model must contain [collider meshes]({{< ref "/content/creator/3d-modeling/colliders.md">}}).
- The `GLTFContainer` must be configured to use the [visible geometry with collision masks]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#colliders-on-3d-models" >}}).
- The entity must have a [MeshCollider component]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}).

If another entity's collider is standing on the way of the entity that the player wants to interact with it, the player won't be able to click the entity that's behind, unless the entity has no collider, or this collider is configured to not respond to the pointer events collision layer.

```ts
// clickable entity
const clickableEntity = engine.addEntity()
MeshRenderer.setBox(clickableEntity)
MeshCollider.setBox(clickableEntity)
Transform.create(clickableEntity, { position: Vector3.create(8, 1, 8) })

pointerEventsSystem.onPointerDown(
	{
		entity: clickableEntity,
		opts: {
			button: InputAction.IA_POINTER,
			hoverText: 'Click',
		},
	},
	function () {
		console.log('clicked entity')
		const t = Transform.getMutable(clickableEntity)
		t.scale.y += 0.2
	}
)

// non-blocker for clicks
const nonBlocker = engine.addEntity()
MeshRenderer.setBox(nonBlocker)
MeshCollider.setBox(nonBlocker, ColliderLayer.CL_PHYSICS)
Transform.create(nonBlocker, { position: Vector3.create(10, 1, 8) })

// blocker for clicks
const blocker = engine.addEntity()
MeshRenderer.setBox(blocker)
MeshCollider.setBox(blocker, ColliderLayer.CL_POINTER)
Transform.create(blocker, { position: Vector3.create(8, 1, 10) })
```

{{< hint warning >}}
**📔 Note**: For an entity to not only intercept a pointer event, but also to return data, the entity also needs to have a `PointerEvents` component. The `pointerEventsSystem` helpers also take care of this requirment.
{{< /hint >}}

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
- `InputAction.IA_BACKWARD`: **S** key on a computer.
- `InputAction.IA_WALK`: **Control** key on a computer.

Each `InputAction` is abstracted away from the literal input in the keyboard so that it can be mapped to different inputs depending on the device. For this same reason, not all buttons on the keyboard can be tracked for button events, only the buttons that are used for movement and interaction. This intentional limitation is to ensure that all content is compatible in the future with VR controllers, other kinds of game controllers, and mobile devices.

## Types of pointer events

Each input can produce the following types of pointer events. Each of the following is a value in the `PointerEventType` enum.

- `DOWN`: Player pushes down a specific button while having the cursor pointing at the entity's collider.
- `UP`: Player releases a specific button while having the cursor pointing at the entity's collider.
- `HOVER_ENTER`: Player's cursor starts pointing at the entity's collider.
- `HOVER_LEAVE`: Player's cursor stops pointing at the entity's collider.

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
pointerEventsSystem.onPointerDown({ entity: myEntity }, function (cmd) {
	console.log(cmd.hit.entityId)
})
```

Using the [**System-based**]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approach, use `inputSystem.getInputCommand()` to fetch this data.

```ts
engine.addSystem(() => {
	const cmd = inputSystem.getInputCommand(
		InputAction.IA_POINTER,
		PointerEventType.PET_DOWN,
		myEntity
	)
	if (cmd) {
		console.log(cmd.hit.entityId)
	}
})
```

{{< hint warning >}}
**📔 Note**: For an entity to not only intercept a pointer event, but also to return data, the entity also needs to have a `PointerEvents` component. The `pointerEventsSystem` helpers also take care of this requirment.
{{< /hint >}}

Using the [**Advanced**]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}) approach, the `PointerEventsResults` contains an array with a recent history of all pointer events against that entity.

```ts
engine.addSystem(() => {
	const pointerEvents = engine.getEntitiesWith(PointerEventsResult)
	for (const [entity] of pointerEvents) {
		const poninterEvents = PointerEventsResult.get(entity)

		if (poninterEvents.commands.length > 0) {
			console.log(poninterEvents.commands[0].hit.entityId)
		}
	}
})
```

## Lock or unlock the cursor

Players in Decentraland's desktop client can toggle between two distinct interaction modes with their cursor: 

- Locked cursor: moving the mouse shifts the camera and click events occur in the corssair at the center of the screen  moving the mouse or pointer directly 
- Unlocked cursor: the cursor is free to move independently of the camera, and players can click anywhere on the screen to interact with either the 3D space or the UI

These modes of interaction are ideal for different kinds of game mechanics, and you may want to make players adopt one or the other depending on what suits your scene best. You may also want to momentarily ensure the player's cursor is unlocked to allow them to interact with a UI, this is especially helpful for new players that aren't familiar with how this is controlled.

To change the player's cursor state, use the `PointerLock` component on any entity in your scene.

```ts
import {PointerLock} from '@dcl/sdk/ecs'

pointerLockEntity = engine.addEntity();
    
PointerLock.create(pointerLockEntity, {isPointerLocked: false});
```

{{< hint warning >}}
**📔 Note**: It's best to create a single entity in your scene who's only function is to manage the pointer state. 

If your scene contains multiple entities with a `PointerLock`, they should all get updated by the engine whenever the state changes.
{{< /hint >}}

You can also query the player's cursor state, and react to that. The following example enforces that the cursor is always unlocked.

```ts
import {PointerLock} from '@dcl/sdk/ecs'

export function main() {
	pointerLockEntity = engine.addEntity();

    PointerLock.create(pointerLockEntity, {isPointerLocked: false});

    PointerLock.onChange(pointerLockEntity, (pointerLock) => {
		    if (!pointerLock) return
		    if(pointerLock.isPointerLocked){
			    PointerLock.getMutable(pointerLockEntity).isPointerLocked = false
		   }
	})
}
```



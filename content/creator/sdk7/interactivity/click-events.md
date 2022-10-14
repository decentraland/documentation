---
date: 2018-02-14
title: Button events
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
aliases:
  - /sdk-reference/event-handling/
  - /development-guide/event-handling/
  - /development-guide/click-events/
type: Document
url: /creator/development-guide/click-events/
---


A Decentraland scene can detect button events from all of the buttons that are used to control the player's avatar. These include pointer clicks, several action buttons, and the keys that are used to move the avatar around. Button events can come from a mouse, a touch screen, a VR controller or some other device, these are all interpreted the same by the SDK.

## Simple pointer events

You can detect pointer events on any entity that has a collider. There are a couple of handy helper functions that allow you to query if a particular entity was just interacted with, or if an entity is currently being interacted with.

> Note: The entity must have a [collider](/creator/development-guide/colliders) to respond to button events. If an entity has no collider, give it a `MeshCollider` component to make it clickable.


### Check for button presses

Check if an entity was triggered by a pointer event in the last frame by using the `wasEntityClicked()` within a [system](/creator/development-guide/system). 

The `wasEntityClicked()` function requires that you pass it an entity and a specific button to check for events.

```ts
engine.addSystem(() => {
    if (wasEntityClicked(myEntity, InputAction.IA_POINTER)){
      log("Entity was just clicked")
    }
})
```

The example above checks on every tick if a single hard-coded entity was pressed with the pointer button (left mouse button).

`wasEntityClicked()` returns _true_ only if the indicated button was pressed down in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_.

It's always a good practice to add a `PointerEvents` component to an entity that you want a player to interact with, so that the player has prior feedback that the entity is interactive. See [Pointer event feedback](#pointer-event-feedback) to learn how you can add hover hints on interactive entities.


> Note: `wasEntityClicked()` helps disambiguate several corner cases that might occur, especially if the player clicks fast. For example, if the button was pushed down and up since the last tick, this should be considered a new click event, even if the button is currently no longer down. Also, if the button was down on the last tick, but was raised and then pushed down again since the last tick, this should be considered a new click event. 


See [advanced pointer event results](#advanced-pointer-event-results) for ways to obtain more detailed data from pointer events.

### Check for clicks

They include button down and button up events

TODO

### Check for active buttons

Check if a button is currently being held down while aiming at an entity by using `isPointerEventActive()` within a system. 

```ts
engine.addSystem(() => {
    if (isPointerEventActive(myEntity, InputAction.IA_POINTER)){
      log("Entity is currently being clicked")
    }
})
```

`isPointerEventActive()` returns _true_ if the button is currently being held down, no matter when the button was pushed down.


### Handle multiple entities

If your scene has multiple entities that might be affected by pointer events, it makes sense to write a system that iterates over all of them.

```ts
function killSystem() {
  const clickedCubes = engine.getEntitiesWith(PointerEvents)
  for (const [entity] of clickedCubes) {
    if (wasEntityClicked(entity, InputAction.IA_PRIMARY)) {
		engine.removeEntity(entity)
    }
  }
}
engine.addSystem(killSystem)
```

This example uses a [component query](/creator/development-guide/querrying-components) to iterate over all the entities with a `PointerEvents` component. It then checks each with `wasEntityClicked()`, and if so removes the entity from the engine.

Instead of iterating over _all_ the entities with a `PointerEvents` component in a single system, you might want to instead write different systems to handle entities that should behave in different ways.

```ts
function openDoorSystem() {
  const clickedDoors = engine.getEntitiesWith(PointerEvents, IsDoor)
  for (const [entity] of clickedDoors) {
    if (wasEntityClicked(entity, InputAction.IA_PRIMARY)) {
		openDoor(entity)
    }
  }
}
engine.addSystem(openDoorSystem)
```

This example iterates over all entities that have a custom component named `IsDoor`, and checks each to see if they were pressed with the primary button (E on a keyboard).


In the example above, the system iterates over the entities that have both a `PointerEvents` component and a custom `IsDoor` flag component, that is added to all doors in your scene. The system allows you to run the same code for every door that has been clicked.



## Pointer event feedback


To display UI hints while pointing at an entity, you must give the entity a `PointerEvents` component.


```ts
// create entity
const myEntity = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(myEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
        }
      }
    ]
})
```

Whenever the player's cursor points at the colliders in this entity, the UI will display a hover hint to indicate that the entity can be interacted with. See the sections below for details on what you can configure.

The `PointerEvents` component requires that you define at least one pointer event. You can potentially add multiple ones as an array. Each pointer event must specify at least what kind of event to listen for (eg: button down, button up), and which button to listen for.

TODO: image


### Types of pointer events

There are various types of pointer event that can be detected. Configure the `PointerEvents` component to include the events you're interested in detecting. Refer to these events through the `PointerEventType` enum.

The following events are available:

- `DOWN`: Player pushes down a specific button while having the cursor pointing at the entity's collider.
- `UP`: Player releases a specific button while having the cursor pointing at the entity's collider.
- `HOVER_ENTER`: Player's cursor starts pointing at the entity's collider.
- `HOVER_LEAVE`: Player's cursor stops pointing at the entity's collider.

A single `PointerEvents` component can detect as many of these events as needed, by including an object for each.

```ts
PointerEvents.create(myEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
        }
      }, {
        eventType: PointerEventType.PET_UP,
        eventInfo: {
          button: InputAction.IA_POINTER,
        }
      }, {
        eventType: PointerEventType.PET_HOVER_ENTER,
        eventInfo: {}
      }, {
        eventType: PointerEventType.PET_HOVER_LEAVE,
        eventInfo: {}
      }
    ]
  })
```



### Pointer buttons

The following buttons can be registered as pointer events:

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


```ts
PointerEvents.create(myEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_PRIMARY,
        }
      }, {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_SECONDARY,
        }
      }
    ]
})
```

A single `PointerEvents` component can detect button events from different buttons.

> Note: Each `InputAction` is abstracted away from the literal input in the keyboard so that it can be mapped to different inputs depending on the device. For this same reason, not all buttons on the keyboard can be tracked for button events, only the buttons that are used for movement and interaction. This intentional limitation is to ensure that all content is compatible in the future with VR controllers, other kinds of game controllers, and mobile devices. 


### Hint messages

When a player hovers the cursor over an item with an `PointerEvents` component, the cursor changes shape to hint to the player that the entity is interactive.

You can also display a toast message in the UI that lets the player know what happens if they interact with the entity.

```ts
// create entity
const chest = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(chest, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  showFeedback: true
		  hoverText: "Open",
        }
      }
    ]
})
```


In the example above, the pointer event includes some additional arguments:

- `showFeedback`: Boolean to turn the hover hints on or off. It's _true_ by default.
- `hoverText`: String to display in the UI while the player points at the entity. By default, this string spells _Interact_, unless `showFeedback` is _false_.

> TIP: The `hoverText` string should describe the action that happens when interacting. For example `Open`, `Activate`, `Grab`, `Select`. These strings should be as short as possible, to avoid stealing too much focus from the player.

If an entity has multiple pointer events on it, the hover hints for each of these are displayed radially around the cursor.

The `hoverText` of an `.UP` pointer event is only displayed while the player is already holding down the corresponding key and pointing at the entity.

<!-- TODO: Confirm -->

If an entity has both a `DOWN` pointer event and an `UP` pointer event, the hint for the `DOWN` action is shown while the button is not being pressed. The hint switches to the one from the `UP` event only when the button is pressed and remains pressed.

```ts
// create entity
const entity = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(entity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Drag",
        }
      }, {
        eventType: PointerEventType.PET_UP,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Drop",
        }
      }
    ]
})
```


### Max distance

Pointer events have a max range of interaction. If a player is too far away from an entity, the pointer event won't be activated and the hover hint won't be displayed next to the cursor.

By default, entities are only clickable when the player is within a close range of the entity, at a maximum distance of _10 meters_. You can change the maximum distance by setting the `maxDistance` property of a pointer event.

```ts
// create entity
const myEntity = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(myEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  maxDistance: 6
        }
      }
    ]
})
```

The example above sets the maximum distance to _6 meters_.


> Note: The `maxDistance` is measured in meters from meters from the player's camera. Keep in mind that in 3rd person the camera is a bit further away, so make sure the distance you set works well in both modes.


### Ray Obstacles

Button events cast rays that only interact with the first entity on their path, as long as the entity is closer than its distance limit.

For an entity to be intercepted by the ray of a button event, the entity's 3d model must either have a collider mesh, or the entity must have a `CollierMesh` component.

If another entity's collider is standing on the way of the entity that the player wants to click, the player won't be able to click the entity that's behind, unless the entity's `MeshCollider` component is configured to allow clicking through it.


<!-- TODO -->

### Multiple buttons on an entity

<!-- TODO -->


You may want to make an entity respond to different buttons in different ways. Each entity can only have _one_ `PointerEvents` component, but it can include multiple objects in its `pointerEvents` array, one for each event to respond to.



```ts
// create entity
const NPCEntity = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(NPCEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Attack",
        }
      },
	  {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_PRIMARY,
		  hoverText: "Greet",
        }
      },
	  {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_SECONDARY,
		  hoverText: "Give gem",
        }
      },
    ]
})
```

Players will see multiple labels, one for each pointer event, displayed radially around the cursor.



### Differentiate meshes inside a model

<!-- TODO -->


Often, _.glTF_ 3D models are made up of multiple meshes, that each have an individual internal name. All button events events include the information of what specific mesh was clicked, so you can use this information to trigger different click behaviors in each case.

To see how the meshes inside the model are named, you must open the 3D model with an editing tool, like [Blender](https://www.blender.org/) for example.

<img src="/images/media/mesh-names.png" alt="Mesh internal names in an editor" width="250"/>

> Tip: You can also learn the name of the clicked mesh by logging it and reading it off console.

You access the `meshName` property as part of the `hit` object, that's returned by the click event.

In the example below we have a house model that includes a mesh named `firePlace`. We want to turn on the fireplace only when its corresponding mesh is clicked.

```ts
houseEntity.addComponent(
  new OnPointerDown(
    (e) => {
      log("button A Down", e.hit.meshName)
      if (e.hit.meshName === "firePlace") {
        // light fire
        fireAnimation.play()
      }
    },
    { button: InputAction.IA_POINTER, showFeeback: false }
  )
)
```

> Note: Since the `OnPointerDown` component belongs to the whole entity, the on-hover feedback would be seen when hovering over any part of the entity. In this case, any part of the house, not just the fireplace. For that reason, we set the `showFeedback` argument of the `OnPointerDown` component to _false_, so that no on-hover feedback is shown. For a better player experience, it's recommended to instead have the fireplace as a separate entity and maintain the on-hover feedback.

## Advanced pointer events

When a pointer event is detected by the engine, the entity that was clicked is assigned a `PointerEventsResult` component. This component contains all the raw data about the hit event, and stores historic data about previous events.

The `wasEntityClicked()` function is a handy helper is good for most simple scenarios, but if you need to get more details about the hit event, check the `PointerEventsResult`.

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
	- `normalHit`: _Quaternion_ for the angle of the normal of the hit in world space.


<!-- TODO: meshName not currently in `hit`, will it be included? -->


```ts
function PointerReadingSystem() {
  const clickedCubes = engine.getEntitiesWith(PointerEventsResult)
  for (const [entity] of clickedCubes) {

    const result = PointerEventsResult.getOrNull(entity)
    if(result){
      log("POINTER EVENT DATA:", result.commands)
    }
  }
}

engine.addSystem(PointerReadingSystem)

```



### Global buttons advanced

<!-- TODO -->



### Tracking player movements


In real-time multiplayer games where the timing of player movements is critical, you may want to keep track of each player's position using a 3rd party server as the source of truth. You can improve response time by listening to the button in advance and predict their effects in your server before the avatar has shifted position.

This approach helps compensate for network delays, but is sure to result in discrepancies, so you should also regularly poll the player's current position to make corrections. Balancing these predictions and corrections may require plenty of fine-tuning.





## Advanced Custom hints

You can otherwise use `HOVER_ENTER` and `HOVER_LEAVE` pointer events to hint that something is interactable in some custom way. For example, you could play a subtle sound when `HOVER_ENTER` event is activated. You could also show a glowing highlight around the entity when a `HOVER_ENTER` event is activated, and hide it when `HOVER_LEAVE` is activated. It could also be used for specific gameplay mechanics.


> TIP: Note that all entities with a `PointerEvents` component by default show a UI hint when hovered over. If this conflicts with the feedback you want to show, you can disable this UI hint by setting the `showFeeback` property on the pointer event to false.

```ts
// create entity
const entity = engine.addEntity()

// give entity a PointerEvents component
PointerEvents.create(entity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  showFeedback: false
        }
      },
	   {
        eventType: PointerEventType.PET_HOVER_ENTER,
        eventInfo: {
        }
      },
	   {
        eventType: PointerEventType.PET_HOVER_LEAVE,
        eventInfo: {
        }
      }
    ]
})

```

<!-- TODO: trigger actions based on hover events -->























<!-- TODO: everything from here down -->


## Global button events

The _BUTTON_DOWN_ and _BUTTON_UP_ events are fired whenever the player presses or releases an input controller button.

These events are triggered every time that the buttons are pressed or released, regardless of where the player's pointer is pointing at, as long as the player is standing inside the scene's boundaries.

It also tracks keys used for basic avatar movement whilst in the scene.

Instance an `Input` object and use its `subscribe()` method to initiate a listener that's subscribed to one of the button events. Whenever the event is caught, it executes a provided function.

The `subscribe()` method takes four arguments:

- `eventName`: The type of action, this can be either `"BUTTON_DOWN"` or `"BUTTON_UP"`
- `buttonId`: Which button to listen for.
  The following buttons can be tracked for both BUTTON_DOWN and BUTTON_UP events:

      - `POINTER` (left mouse click on PC)
      - `PRIMARY` (_E_ on PC)
      - `SECONDARY`(_F_ on PC)
      - `JUMP`(_space bar_ on PC)
      - `FORWARD`(_W_ on PC)
      - `LEFT`(_A_ on PC)
      - `RIGHT`(_D_ on PC)
      - `BACK`(_S_ on PC)
      - `WALK`(_Shift_ on PC)
      - `ACTION_3`(_1_ on PC)
      - `ACTION_4`(_2_ on PC)
      - `ACTION_5`(_3_ on PC)
      - `ACTION_6`(_4_ on PC)

- `useRaycast`: Boolean to define if raycasting will be used. If `false`, the button event will not contain information about any `hit` objects that align with the pointer at the time of the event. Avoid setting this field to `true` when information about hit objects is not required, as it involves extra calculations.
- `fn`: The function to execute each time the event occurs.

> Note: Other keys on the PC keyboard aren't tracked for future cross-platform compatibility, as this limited set of keys can be mapped to a joystick. For detecting key-strokes when writing text, check the [UIInputBox](/creator/development-guide/onscreen-ui).

```ts
// Instance the input object
const input = Input.instance

// button down event
input.subscribe("BUTTON_DOWN", InputAction.IA_POINTER, false, (e) => {
  log("pointer Down", e)
})

// button up event
input.subscribe("BUTTON_UP", InputAction.IA_POINTER, false, (e) => {
  log("pointer Up", e)
})
```

The example above logs messages and the contents of the event object every time the pointer button is pushed down or released.

The event objects of both the `BUTTON_DOWN` and the `BUTTON_UP` contain various useful properties. See [Properties of button events](#properties-of-button-events) for more details.

> Note: The code for subscribing an input event only needs to be executed once, the `subscribe()` method keeps polling for the event. Don't add this into a system's `update()` function, as that would register a new listener on every frame.

### Detect hit entities

If the third argument of the `subscribe()` function (`useRaycast`)is true, and the player is pointing at an entity that has a collider, the event object includes a nested `hit` object. The `hit` object includes information about the collision and the entity that was hit.

Raycasting is not available when detecting basic movement keys. It's only available when tracking the following buttons:

- `POINTER`
- `PRIMARY`
- `SECONDARY`
- `ACTION_3`
- `ACTION_4`
- `ACTION_5`
- `ACTION_6`

The ray of a global button event only detects entities that have a collider mesh. Primitive shapes have a collider mesh on by default, 3D models need to have one built into them.

> Tip: See [Colliders](/creator/3d-modeling/colliders) for details on how to add collider meshes to a 3D model.

```ts
input.subscribe("BUTTON_DOWN", InputAction.IA_POINTER, true, (e) => {
  if (e.hit) {
    let hitEntity = engine.entities[e.hit.entityId]
    hitEntity.addComponent(greenMaterial)
  }
})
```

The example above checks if any entities were hit, and if so it fetches the entity and applies a material component to it.

The event data returns a string for the `entityId`. If you want to reference the actual entity by that ID to affect it in some way, use `engine.entities[e.hit.entityId]`.


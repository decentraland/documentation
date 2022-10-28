---
date: 2018-02-14
title: Button events
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/click-events/
weight: 1
---


A Decentraland scene can detect button events from all of the buttons that are used to control the player's avatar. These include pointer clicks, several action buttons, and the keys that are used to move the avatar around. Button events can come from a mouse, a touch screen, a VR controller or some other device, these are all interpreted the same by the SDK.

You can detect button events against an entity. This involves pressing the button while the player's cursor is pointing at that entity's collider. You can also detect _global_ button event, that involve pressing the button at any time, without consideration for where the pointer is aiming.

> Note: An entity must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}) to respond to button events. If an entity has no collider, you can give it a `MeshCollider` component to make it clickable.

There are several different ways to handle button events, depending on the use case.

- **Register a callback**: The easiest way to add interaction to a single entity. Write a single statement to set up a callback function and hover feedback.
- **System-based**: Ideal for handling multiple entities with similar behavior. Use a system to iterate over similar entities and query for button events on each, handling them all with the same logic. Hover feedback needs to be set up separately. This approach is required for handling global button events.
- **Advanced**: Read the raw response data on each entity, including time-stamps and an event history of button events. This can be useful for defining custom interaction patterns.

## Register a callback

The easiest way to handle button events is to register a callback function with `EventSystem.onPointerDown()`

This statement requires three parameters:

- The entity to handle
- A function to run each time the entity is clicked
- An object

```ts
EventsSystem.onPointerDown(
  entity,
  function () {
    createCube(1 + Math.random() * 8, Math.random() * 8, 1 + Math.random() * 8)
    EventsSystem.removeOnPointerDown(entity)
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Click'
  }
)
```


## Check for button events


Check for button events by running one of the helper functions on the input `Input` namespace on every tick within a [system]({{< ref "/content/creator/sdk7/architecture/systems.md">}}).

For example, the following system uses the `Input.wasJustClicked()` function to check if the pointer was clicked.

```ts
engine.addSystem(() => {
    if (Input.wasJustClicked(InputAction.IA_POINTER)){
      log("Pointer button just clicked")
    }
})
```

The following helper functions are available:

- `Input.wasJustClicked`
- `Input.wasInputJustActive`
- `Input.isActionDown`
- `Input.getClick`
- `Input.getInputCommand`

See the sections below for more details on each.

In any of these functions, you can pass a second parameter to detect pointer events that were done while pointing at a specific entity's colliders.

```ts
engine.addSystem(() => {
    if (Input.wasJustClicked(InputAction.IA_POINTER, myEntity)){
      log("Entity was just clicked")
    }
})
```

When handling button events on an entity, always provide feedback to the player, so that the player is aware that an entity can be interacted with. If you add a `PointerHoverFeedback` component to an entity, players will see a hint while hovering their cursor on that entity. See [Pointer event feedback](#pointer-event-feedback) to learn how you can add hover hints on interactive entities.

```ts
// create entity
const myEntity = engine.addEntity()

// give the entity hover feedback
PointerHoverFeedback.create(myEntity, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Open",
        }
      }
    ]
})

// handle click events on the entity
engine.addSystem(() => {
    if (Input.wasJustClicked(InputAction.IA_POINTER, myEntity)){
      log("Entity was just clicked")
    }
})
```

TODO: screenshot

### Check for button presses

Use `Input.wasInputJustActive` to detect button down and button up events on any of the inputs tracked by the SDK.


```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN)){
      log("The pointer button was just pressed down")
    }
})
```

The example above checks on every tick if a single hard-coded entity was pressed with the pointer button (left mouse button).

`Input.wasInputJustActive()` returns _true_ only if the indicated button was pressed down in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_.

TODO: check this
> Note: The player needs to be standing inside the scene's boundaries for the pointer event to be detected. The player's cursor also needs to be locked, buttons pressed while having the free cursor aren't detected.

The `Input.wasInputJustActive` function takes the following arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons](#pointer-buttons) for supported options.
- `PointerEventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events](#types-of-pointer-events) for supported options.
- `Entity` _(optional)_: What entity to check these events on. If no value is provided, it will check for global presses of the button, regardless of where the player's cursor was pointing at.

The following example checks for button presses against a particular entity.

```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)){
      log("The pointer button was just pressed down on myEntity")
    }
})
```


> TIP: See [Data from a pointer event](#data-from-a-pointer-event) for ways to obtain more detailed data from pointer events.

You can also check for pointer up events in much the same way, by using `PointerEventType.PET_UP`. 


```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_UP, myEntity)){
      log("The pointer button was just raised while pointing at myEntity")
    }
})
```

> Note: When checking pointer up events against a specific entity, it doesn't take into consideration where the cursor was pointing at when the button was pushed down. It only considers where the cursor is pointing at when the button is raised.

TODO:

To obtain data about a pointer event, beyond just its occurrence, use `Input.getInputCommand`. 


### Check for clicks

A click is defined as pushing a button down, and then shortly after letting it rise again. The event is only recognized as a click when the button is raised up again.

```ts
engine.addSystem(() => {
    if (Input.wasJustClicked(InputAction.IA_POINTER, myEntity)){
      log("Entity was just clicked")
    }
})
```

The example above checks on every tick if a single hard-coded entity was clicked with the pointer button (left mouse button).

`Input.wasJustClicked()` returns _true_ only if the indicated button was first pressed down, and then pulled up in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_. 

If the click event is being checked against a specific entity, both the button down and the button up events must be performed while pointing at the entity's collider to be considered a click.

> Note: If you want to check only for the button down event, and don't care about the button up event, use the `Input.wasInputJustActive()` with `PointerEventType.PET_UP`. See [Check for button presses](#check-for-button-presses)


The `Input.wasJustClicked` function takes the following arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons](#pointer-buttons) for supported options.
- `Entity` _(optional)_: What entity to check clicks on. If no value is provided, it will check for global clicks of the button, regardless of where the player's cursor was pointing at.


`Input.wasJustClicked()` helps disambiguate several corner cases that might occur, especially if the player clicks fast. If the button was pushed down and up all in the time since the last tick, this should be considered a new click event. Also, if the button was down, then was raised and then pushed down again in the time since the last tick, we should detect a click event.


TODO

To obtain data about a click event, beyond just its occurrence, use `Input.getClick`. 


### Check for active buttons


Check if a button is currently being held down while aiming at an entity by using `Input.isActionDown()` within a system. 

```ts
engine.addSystem(() => {
    if (Input.isActionDown(InputAction.IA_POINTER)){
      log("Pointer is currently down")
    }
})
```

`Input.isActionDown()` returns _true_ if the button is currently being held down, no matter when the button was pushed down, and no matter where to player's cursor is pointing at.


The `Input.isActionDown` function takes a single argument:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons](#pointer-buttons) for supported options.


### Types of pointer events


There are various types of pointer event that can be detected.

The following types of events are available in the `PointerEventType` enum.

- `DOWN`: Player pushes down a specific button while having the cursor pointing at the entity's collider.
- `UP`: Player releases a specific button while having the cursor pointing at the entity's collider.
- `HOVER_ENTER`: Player's cursor starts pointing at the entity's collider.
- `HOVER_LEAVE`: Player's cursor stops pointing at the entity's collider.

> Note: A _click_ event, as detected by the `Input.wasJustClicked` helper function, is a combination of a `DOWN` event followed by an `UP` event. Note that as this event may take several ticks of the game loop to be completed, it can't be detected in a single frame, and therefore can only be detected thanks to a helper function.


### Pointer buttons

The following buttons can be handled on pointer events:

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

### Handle multiple entities

If your scene has multiple entities that might be affected by pointer events, it makes sense to write a system that iterates over all of them.

```ts
function killSystem() {
  const clickedCubes = engine.getEntitiesWith(PointerHoverFeedback)
  for (const [entity] of clickedCubes) {
    if (Input.wasJustClicked(InputAction.IA_PRIMARY, entity)) {
		engine.removeEntity(entity)
    }
  }
}
engine.addSystem(killSystem)
```

This example uses a [component query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) to iterate over all the entities with a `PointerHoverFeedback` component. It then checks each of these entities with `Input.wasJustClicked`. If a click is detected, it removes the entity from the engine.

Instead of iterating over _all_ the entities with a `PointerHoverFeedback` component in a single system, you might want to instead write different systems to handle entities that should behave in different ways. The recommended approach is to mark different types of entities with a [custom component]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}).

```ts
function openDoorSystem() {
  const clickedDoors = engine.getEntitiesWith(IsDoor)
  for (const [entity] of clickedDoors) {
    if (Input.wasJustClicked(InputAction.IA_PRIMARY, entity)) {
		openDoor(entity)
    }
  }
}
engine.addSystem(openDoorSystem)
```

This example iterates over all entities that have a custom component named `IsDoor`, and checks each to see if they were clicked with the primary button (E on a keyboard). The system allows you to run the same code for every door that can be clicked.


<!-- 
TODO:
Does is make sense to add `PointerHoverFeedback` to the equation? so do `engine.getEntitiesWith(IsDoor, PointerHoverFeedback)`. That way you only query entities with at least one pointer interaction

In the example above, the system iterates over the entities that have both a `PointerHoverFeedback` component and a custom `IsDoor` flag component, that is added to all doors in your scene.  -->



## Show feedback


To display UI hints while pointing at an entity, give the entity a `PointerHoverFeedback` component.


```ts
// create entity
const myEntity = engine.addEntity()

// give entity a PointerEvents component
PointerHoverFeedback.create(myEntity, {
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

> Note: The `PointerHoverFeedback` component just handles the displaying of hover feedback. To handle the button events themselves with custom logic, see [Check for events](#check-for-events).

TODO: image

The `PointerHoverFeedback` component requires that you define at least one pointer event. You can potentially add multiple ones as an array. Each pointer event can be configured with the following:

- `eventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events](#types-of-pointer-events) for supported options.
- `eventInfo`: An object that can contain the following fields:

	- `button` (_required_): Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons](#pointer-buttons) for supported options.
	- `hoverText` _(optional)_: What string to display in the UI.
	- `maxDistance`  _(optional)_: Only show feedback when the player is closer than a certain distance from the entity. Default is _10 meters_.


A single `PointerHoverFeedback` component can hold multiple pointer events, that can detect different events for different buttons. Each entity can only have _one_ `PointerHoverFeedback` component, but it can include multiple objects in its `pointerEvents` array, one for each event to respond to.


```ts
PointerHoverFeedback.create(NPCEntity, {
    pointerEvents: [
	  {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Greet",
        }
      }, {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_PRIMARY,
		  hoverText: "Choke",
        }
	  }, {
        eventType: PointerEventType.PET_UP,
        eventInfo: {
          button: InputAction.IA_PRIMARY,
		  hoverText: "Stop Choke",
        }
      }, {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_SECONDARY,
		  hoverText: "Give gem",
        }
      }
    ]
})
```

Players will see multiple labels, one for each pointer event, displayed radially around the cursor.

TODO: Image with multiple hints


### Hint messages

When a player hovers the cursor over an item with an `PointerHoverFeedback` component, the cursor changes shape to hint to the player that the entity is interactive.

You can also display a toast message in the UI that lets the player know what happens if they interact with the entity.

```ts
// create entity
const chest = engine.addEntity()

// give entity a PointerEvents component
PointerHoverFeedback.create(chest, {
    pointerEvents: [
      {
        eventType: PointerEventType.PET_DOWN,
        eventInfo: {
          button: InputAction.IA_POINTER,
		  hoverText: "Open",
        }
      }
    ]
})
```


In the example above, the pointer event includes a value for `hoverText`. This field defines the string to display in the UI while the player points at the entity. By default, this string spells _Interact_.

> TIP: The `hoverText` string should describe the action that happens when interacting. For example `Open`, `Activate`, `Grab`, `Select`. These strings should be as short as possible, to avoid stealing too much focus from the player.

If an entity has multiple pointer events on it, the hover hints for each of these are displayed radially around the cursor.

The `hoverText` of an `.UP` pointer event is only displayed while the player is already holding down the corresponding key and pointing at the entity.

<!-- TODO: Confirm -->

If an entity has both a `DOWN` pointer event and an `UP` pointer event, the hint for the `DOWN` action is shown while the button is not being pressed. The hint switches to the one from the `UP` event only when the button is pressed and remains pressed.

```ts
// create entity
const entity = engine.addEntity()

// give entity a PointerEvents component
PointerHoverFeedback.create(entity, {
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
PointerHoverFeedback.create(myEntity, {
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

## Obstacles

Button events cast rays that only interact with the first entity on their path, as long as the entity is closer than its distance limit.

For an entity to be intercepted by the ray of a button event, the entity's 3d model must either have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). Either the entity's 3d model must include a collider mesh, or the entity must have a `CollierMesh` component.

If another entity's collider is standing on the way of the entity that the player wants to click, the player won't be able to click the entity that's behind, unless the entity's `MeshCollider` component is configured to allow clicking through it.

## Data from a pointer event



When using the `Input.getInputCommand`, the following data comes back:

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


TODO: examples examples



TODO: check this:
The event data returns a string for the `entityId`. If you want to reference the actual entity by that ID to affect it in some way, use `engine.entities[e.hit.entityId]`.



When using `Input.getClick`, it returns an object with a `down` and an `up` object, each of these with all the same data structure returned by `Input.getInputCommand`. The `down` object contains the data relevant to the moment when the moment when button was pushed down, the `up` object for when the button went up.


TODO: example example example



### Differentiate meshes inside a model


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

## Advanced


### Track player movements


In real-time multiplayer games where the timing of player movements is critical, you may want to keep track of each player's position using a 3rd party server as the source of truth. You can improve response time by listening to the button in advance and predict their effects in your server before the avatar has shifted position.

This approach helps compensate for network delays, but is sure to result in discrepancies, so you should also regularly poll the player's current position to make corrections. Balancing these predictions and corrections may require plenty of fine-tuning.


### Advanced custom hints

The [`PointerHoverFeedback`](#hint-messages) component adds UI hints when the player's cursor starts hovering over an entity. This is easy to set up, and it's also good that it's consistent with what players are used to seeing in other scenes.

In some cases, you might want to otherwise use `HOVER_ENTER` and `HOVER_LEAVE` pointer events to hint that something is interactable in some custom way. For example, you could play a subtle sound when `HOVER_ENTER` event is activated. You could also show a glowing highlight around the entity when a `HOVER_ENTER` event is activated, and hide it when `HOVER_LEAVE` is activated. It could also be used for specific gameplay mechanics.


```ts
TODO

```

### The PointerEventsResult component


When a pointer event is detected by the engine, the entity that was clicked is assigned a `PointerEventsResult` component. This component contains all the raw data about the hit event, and stores historic data about previous events.

The helpers in `Input`, like `Input.wasJustClicked` or  `Input.getInputCommand` are good for most simple scenarios, but if you need to get more details about the hit event, check the raw data in the `PointerEventsResult`.

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

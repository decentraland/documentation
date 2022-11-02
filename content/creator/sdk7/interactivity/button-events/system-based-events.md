---
date: 2018-02-14
title: System based events
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/system-based-events/
weight: 3
---


If your scene has multiple similar entities that are all activated using the same logic, you can write a single system to iterates over all of them and describe that behavior only once. This is also the most performant and more [data oriented]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}) approach.

If all you want to do is click or push a button on a single entity to activate it, the easiest way is to use the [Register a callback]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) approach.

To set more specific custom logic, you might want to deal with the raw data and use the [Advanced]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}) approach.

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.

## Using a system

Check for button events by running one of the helper functions on the input `Input` namespace on every tick within a [system]({{< ref "/content/creator/sdk7/architecture/systems.md">}}).

For example, the following system uses the `Input.wasInputJustActive()` function to check if the pointer was clicked. On every tick, it checks if the button was pressed. If `Input.wasInputJustActive()` returns _true_, the system runs some custom logic in response.

```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER)){
      // Logic in response to button press
    }
})
```

The following helper functions are available in the `Input` namespace, and can be called similarly on every tick:

- `Input.wasInputJustActive`: Returns true if an input action ocurred since the last tick.
- `Input.isActionDown`: Returns true if an input is currently being held down. It will return true on every tick until the button goes up again.
- `Input.getInputCommand`: Returns an object with data about the input action.

See the sections below for more details on each.

When handling button events on an entity, always provide feedback to the player, so that the player is aware that an entity can be interacted with. If you add a `PointerHoverFeedback` component to an entity, players will see a hint while hovering their cursor on that entity. See [Pointer event feedback](#pointer-event-feedback) to learn how you can add hover hints on interactive entities.


### Global input events

Use `Input.wasInputJustActive` to detect button down and button up events on any of the inputs tracked by the SDK.


```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN)){
      // Logic in response to button press
    }
})
```

The example above checks on every tick if a single hard-coded entity was pressed with the pointer button (left mouse button).

`Input.wasInputJustActive()` returns _true_ only if the indicated button was pressed down in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_.

TODO: check this:

> Note: The player needs to be standing inside the scene's boundaries for the pointer event to be detected. The player's cursor also needs to be locked, buttons pressed while having the free cursor aren't detected.

The `Input.wasInputJustActive` function takes the following required arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `PointerEventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#types-of-pointer-events" >}}) for supported options.


### Activate an entity

To detect button events while pointing at a particular entity, pass a third optional argument to `Input.wasInputJustActive` to specify what entity to check against.

The following example checks for button presses against a particular entity.

```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)){
		// Logic in response to button press on myEntity
    }
})
```

The `Input.wasInputJustActive` function takes the following arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `PointerEventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#types-of-pointer-events" >}}) for supported options.
- `Entity` _(optional)_: What entity to check these events on. If no value is provided, it will check for global presses of the button, regardless of where the player's cursor was pointing at.

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.

> TIP: See [Data from a pointer event](#data-from-a-pointer-event) for ways to obtain more detailed data about a pointer event.

### Input button up

You can also check for pointer up events in much the same way, by using `PointerEventType.PET_UP`. 

```ts
engine.addSystem(() => {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_UP, myEntity)){
      // Logic in response to button up while pointing at myEntity
    }
})
```

> Note: When checking pointer up events against a specific entity, it doesn't take into consideration where the cursor was pointing at when the button was pushed down. It only considers where the cursor is pointing at when the button is raised.


<!-- 
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

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `Entity` _(optional)_: What entity to check clicks on. If no value is provided, it will check for global clicks of the button, regardless of where the player's cursor was pointing at.


`Input.wasJustClicked()` helps disambiguate several corner cases that might occur, especially if the player clicks fast. If the button was pushed down and up all in the time since the last tick, this should be considered a new click event. Also, if the button was down, then was raised and then pushed down again in the time since the last tick, we should detect a click event.


TODO

To obtain data about a click event, beyond just its occurrence, use `Input.getClick`.  -->


### Check for active buttons


Check if a button is currently being held down while aiming at an entity by using `Input.isActionDown()` within a system. 

```ts
engine.addSystem(() => {
    if (Input.isActionDown(InputAction.IA_POINTER)){
       // Logic in response to button being held down
    }
})
```

`Input.isActionDown()` returns _true_ if the button is currently being held down, no matter when the button was pushed down, and no matter where to player's cursor is pointing at.


The `Input.isActionDown` function takes a single argument:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.


### Handle multiple entities

If your scene has multiple entities that are affected by pointer events in the same way, it makes sense to write a system that iterates over all of them.

```ts
engine.addSystem(() => {
  const clickedCubes = engine.getEntitiesWith(PointerHoverFeedback)
  for (const [entity] of clickedCubes) {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
		 // Logic in response to interacting with an entity
    }
  }
})
```

This example uses a [component query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) to iterate over all the entities with a `PointerHoverFeedback` component. It then checks each of these entities with `Input.wasInputJustActive`, iterating over them one by one. If an input action is detected on any of these entities, it carries out custom logic.

Instead of iterating over _all_ the entities with a `PointerHoverFeedback` component in a single system, you might want to write different systems to handle entities that should behave in different ways. The recommended approach is to mark different types of entities with specific [custom components]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}), and iterate over them in separate systems.

```ts
engine.addSystem(() => {
  const clickedDoors = engine.getEntitiesWith(IsDoor)
  for (const [entity] of clickedDoors) {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
		openDoor(entity)
    }
  }
})

engine.addSystem(() => {
  const pickedUpGems = engine.getEntitiesWith(IsGem)
  for (const [entity] of pickedUpGems) {
    if (Input.wasInputJustActive(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
		pickUp(entity)
    }
  }
})
```

This example has one system that iterates over all entities that have a custom component named `IsDoor` and another that iterates over all entities that have a custom component named `isGem`. In both systems, it checks every matching entity to see if they were activated with the pointer button.

This way of organizing your scene's code is very [data oriented]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}) and should result in a very efficient use of memory resources.


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

TODO: image


> Note: The `PointerHoverFeedback` component just handles the displaying of hover feedback. To handle the button events themselves with custom logic, see [Using-a-system](#check-for-events).

The `PointerHoverFeedback` component requires at least one pointer event. Each pointer event can be configured with the following:

- `eventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#types-of-pointer-events" >}}) for supported options.
- `eventInfo`: An object that can contain the following fields:

	- `button` (_required_): Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
	- `hoverText` _(optional)_: What string to display in the UI.
	- `maxDistance`  _(optional)_: Only show feedback when the player is closer than a certain distance from the entity. Default is _10 meters_.


A single `PointerHoverFeedback` component can hold multiple pointer events, that can detect different events for different buttons. Each entity can only have _one_ `PointerHoverFeedback` component, but this component can include multiple objects in its `pointerEvents` array, one for each event to respond to.


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

The example below combines using `PointerHoverFeedback` to show hover hints, together with a system that actually handles the player's action with custom logic.

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
    if (Input.wasInputJustActive(InputAction.IA_POINTER, myEntity)){
      // Custom logic in response to an input action
    }
})
```


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

Some entities can be intentionally only interactive at a close range. If a player is too far away from an entity, the hover hint won't be displayed next to the cursor.

TODO: Check this
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

The example above sets the maximum distance for hover hints to _6 meters_. Make sure that the logic for handling the input actions also follows the same rules. See [Data from a pointer event](#data-from-a-pointer-evetn) for how to obtain the distance of an input action.


> Note: The `maxDistance` is measured in meters from meters from the player's camera. Keep in mind that in 3rd person the camera is a bit further away, so make sure the distance you set works well in both modes.


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

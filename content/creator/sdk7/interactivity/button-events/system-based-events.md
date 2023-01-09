---
date: 2018-02-14
title: System based events
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/system-based-events/
weight: 3
---


If your scene has multiple similar entities that are all activated using the same logic, you can write a single system to iterates over all of them and describe that behavior only once. This is also the most performant and more [data oriented]({{< ref "/content/creator/sdk7/architecture/data-oriented-programming.md" >}}) approach.

If all you want to do is click or push a button on a single entity to activate it, the easiest way is to use the [Register a callback]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) approach.

To set more specific custom logic, you might want to deal with the raw data and use the [Advanced]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}) approach.

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.

## Using a system

Check for button events by running one of the helper functions on the input `inputSystem` namespace on every tick within a [system]({{< ref "/content/creator/sdk7/architecture/systems.md">}}).

For example, the following system uses the `inputSystem.isTriggered()` function to check if the pointer was clicked. On every tick, it checks if the button was pressed. If `inputSystem.isTriggered()` returns _true_, the system runs some custom logic in response.

```ts
engine.addSystem(() => {
    if (inputSystem.isTriggered(InputAction.IA_POINTER)){
      // Logic in response to button press
    }
})
```

The following helper functions are available in the `inputSystem` namespace, and can be called similarly on every tick:

- `inputSystem.isTriggered`: Returns true if an input action ocurred since the last tick.
- `inputSystem.isPressed`: Returns true if an input is currently being pressed down. It will return true on every tick until the button goes up again.
- `inputSystem.getInputCommand`: Returns an object with data about the input action.

See the sections below for more details on each.

When handling button events on an entity, always provide feedback to the player, so that the player is aware that an entity can be interacted with. If you add a `PointerHoverFeedback` component to an entity, players will see a hint while hovering their cursor on that entity. See [Show feedback](#show-feedback) to learn how you can add hover hints on interactive entities.


### Global input events

Use `inputSystem.isTriggered` to detect button down and button up events on any of the inputs tracked by the SDK.


```ts
engine.addSystem(() => {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_DOWN)){
      // Logic in response to button press
    }
})
```

The example above checks on every tick if a single hard-coded entity was pressed with the pointer button (left mouse button).

`inputSystem.isTriggered()` returns _true_ only if the indicated button was pressed down in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_.

<!-- TODO: check this outside playground: -->

> Note: The player needs to be standing inside the scene's boundaries for the pointer event to be detected. The player's cursor also needs to be locked, buttons pressed while having the free cursor aren't detected.

The `inputSystem.isTriggered` function takes the following required arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `PointerEventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#types-of-pointer-events" >}}) for supported options.


### Activate an entity

To detect button events while pointing at a particular entity, pass a third optional argument to `inputSystem.isTriggered` to specify what entity to check against.

The following example checks for button presses against a particular entity.

```ts
engine.addSystem(() => {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)){
		// Logic in response to button press on myEntity
    }
})
```

The `inputSystem.isTriggered` function takes the following arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `PointerEventType`: What type of event to listen for, as a value from the `PointerEventType` enum. See [Types of pointer events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#types-of-pointer-events" >}}) for supported options.
- `Entity` _(optional)_: What entity to check these events on. If no value is provided, it will check for global presses of the button, regardless of where the player's cursor was pointing at.

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.

{{< hint info >}}
**💡 Tip**:  See [Data from a pointer event](#data-from-a-pointer-event) for ways to obtain more detailed data about a pointer event.
{{< /hint >}}

### Input button up

You can also check for pointer up events in much the same way, by using `PointerEventType.PET_UP`. 

```ts
engine.addSystem(() => {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_UP, myEntity)){
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
    if (inputSystem.wasJustClicked(InputAction.IA_POINTER, myEntity)){
      console.log("Entity was just clicked")
    }
})
```

The example above checks on every tick if a single hard-coded entity was clicked with the pointer button (left mouse button).

`inputSystem.wasJustClicked()` returns _true_ only if the indicated button was first pressed down, and then pulled up in the current tick of the game loop. If the button was not pushed down, or it was already down from the previous tick, it returns _false_. 

If the click event is being checked against a specific entity, both the button down and the button up events must be performed while pointing at the entity's collider to be considered a click.

> Note: If you want to check only for the button down event, and don't care about the button up event, use the `inputSystem.isTriggered()` with `PointerEventType.PET_UP`. See [Check for button presses](#check-for-button-presses)


The `inputSystem.wasJustClicked` function takes the following arguments:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
- `Entity` _(optional)_: What entity to check clicks on. If no value is provided, it will check for global clicks of the button, regardless of where the player's cursor was pointing at.


`inputSystem.wasJustClicked()` helps disambiguate several corner cases that might occur, especially if the player clicks fast. If the button was pushed down and up all in the time since the last tick, this should be considered a new click event. Also, if the button was down, then was raised and then pushed down again in the time since the last tick, we should detect a click event.


To obtain data about a click event, beyond just its occurrence, use `Input.getClick`.  -->


### Check for pressed buttons


Check if a button is currently being pressed down by using `inputSystem.isPressed()` within a system. 

```ts
engine.addSystem(() => {
    if (inputSystem.isPressed(InputAction.IA_POINTER)){
       // Logic in response to button being held down
    }
})
```

`inputSystem.isPressed()` returns _true_ if the button is currently being held down, no matter when the button was pushed down, and no matter where the player's cursor is pointing at. Otherwise it returns _false_.


The `inputSystem.isPressed` function takes a single argument:

- `InputAction`: Which input to listen for, as a value from the `InputAction` enum. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.


### Handle multiple entities

If your scene has multiple entities that are affected by pointer events in the same way, it makes sense to write a system that iterates over all of them.

```ts
engine.addSystem(() => {
  const activatedEntites = engine.getEntitiesWith(PointerHoverFeedback)
  for (const [entity] of activatedEntites) {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
		 // Logic in response to interacting with an entity
    }
  }
})
```

This example uses a [component query]({{< ref "/content/creator/sdk7/architecture/querying-components.md" >}}) to iterate over all the entities with a `PointerHoverFeedback` component. It then checks each of these entities with `inputSystem.isTriggered`, iterating over them one by one. If an input action is detected on any of these entities, it carries out custom logic.

Instead of iterating over _all_ the entities with a `PointerHoverFeedback` component in a single system, you might want to write different systems to handle entities that should behave in different ways. The recommended approach is to mark different types of entities with specific [custom components]({{< ref "/content/creator/sdk7/architecture/custom-components.md" >}}), and iterate over them in separate systems.

```ts
engine.addSystem(() => {
  const activatedDoors = engine.getEntitiesWith(IsDoor)
  for (const [entity] of activatedDoors) {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
		openDoor(entity)
    }
  }
})

engine.addSystem(() => {
  const pickedUpGems = engine.getEntitiesWith(IsGem)
  for (const [entity] of pickedUpGems) {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_DOWN, entity)) {
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
<!-- 
TODO: image -->


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

<!-- TODO: Image with multiple hints -->

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
    if (inputSystem.isTriggered(InputAction.IA_POINTER, myEntity)){
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

{{< hint info >}}
**💡 Tip**:  The `hoverText` string should describe the action that happens when interacting. For example `Open`, `Activate`, `Grab`, `Select`. These strings should be as short as possible, to avoid stealing too much focus from the player.
{{< /hint >}}

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

<!-- TODO: Check this -->

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

// implement a system to handle the pointer event
engine.addSystem(() => {
  // fetch data about the pointer event
  const cmd = inputSystem.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)

  // check if the click was close enough
  if(cmd.hit.length < 6){
	// do something
  }
})
```

The example above sets the maximum distance for hover hints to _6 meters_. Make sure that the logic for handling the input actions also follows the same rules. See [Data from input action](#data-from-input-action) for how to obtain the distance of an input action.

> Note: The `maxDistance` is measured in meters from meters from the player's camera. Keep in mind that in 3rd person the camera is a bit further away, so make sure the distance you set works well in both modes.


## Advanced custom hints

The `PointerHoverFeedback` component easily adds UI hints when the player's cursor starts hovering over an entity. It's generally a good thing that hints behave consistently with what players are used to seeing in other Decentraland scenes. However, in some cases you might want to signal that something is interactive in a custom way. For example, you could play a subtle sound when the player starts hovering over the entity. You could also show a glowing highlight around the entity while hovering, and hide it when no longer hovering. It could also be used for specific gameplay mechanics.

Use the `inputSystem.isTriggered()` function together with the `PointerEventType.PET_HOVER_ENTER` and `PointerEventType.PET_HOVER_LEAVE` events to carry out custom behaviors whenever the player's cursor starts pointing at the entity's collider, and whenever the cursor stops pointing at it.

The example below enlarges entities to a size of _1.5_ when the cursor starts pointing at their collider, and sets them back at a size of _1_ when the cursor leaves them.


```ts
engine.addSystem(() => {
  const meshEntities = engine.getEntitiesWith(MeshRenderer)
  for (const [entity] of meshEntities) {
    if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_HOVER_ENTER, entity)) {
      Transform.getMutable(entity).scale = Vector3.create(1.5, 1.5, 1.5)
    }

     if (inputSystem.isTriggered(InputAction.IA_POINTER, PointerEventType.PET_HOVER_LEAVE, entity)) {
      Transform.getMutable(entity).scale = Vector3.create(1, 1, 1)
    }
  }
})

```


## Data from input action

Fetch data from an input action, such as the button that was pressed, the entity that was hit, the direction and length of the ray, etc. See ({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#data-from-an-input-action" >}}) for a description of all of the data available.

To fetch this data, use `inputSystem.getInputCommand`. This function returns the full data structure with data about the input event.

```ts
engine.addSystem(() => {
  const cmd = inputSystem.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)
  if(cmd){
	console.log(cmd.hit.entityId)
  }
})
```

If there was no input action that matches the query, then `inputSystem.getInputCommand` returns undefined. Make sure that you handle this scenario in your logic.

### Max click distance

To enforce a maximum distance, so that an entity is only clickable at close range, fetch `hit.length` property of the event data.

```ts
// implement a system to handle the pointer event
engine.addSystem(() => {
  // fetch data about the pointer event
  const cmd = inputSystem.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)

  // check if the click was close enough
  if(cmd && cmd.hit.length < 6){
	// do something
  }
})
```

> Note: If you ignore any events that are far away,  make sure you set the `maxDistance` parameter on the `PointerHoverFeedback` component to behave consistently. 


### Different meshes inside a model

Often, _.glTF_ 3D models are made up of multiple meshes, that each have an individual internal name. All button events events include the information of what specific mesh was clicked, so you can use this information to trigger different click behaviors in each case.

To see how the meshes inside the model are named, you must open the 3D model with an editing tool, like [Blender](https://www.blender.org/) for example.

<img src="/images/media/mesh-names.png" alt="Mesh internal names in an editor" width="250"/>

{{< hint info >}}
**💡 Tip**:  You can also learn the name of the clicked mesh by logging it and reading it off console.
{{< /hint >}}

You access the `meshName` property as part of the `hit` object, that's returned by the click event.

In the example below we have a house model that includes a mesh named `firePlace`. We want to turn on the fireplace only when its corresponding mesh is clicked.

```ts
engine.addSystem(() => {
  const cmd = inputSystem.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)
  if(cmd && cmd.hit.meshName === "firePlace"){
        // light fire
	}
})
```

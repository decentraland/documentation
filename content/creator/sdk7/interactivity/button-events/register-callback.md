---
date: 2018-02-14
title: Register callback
description: Learn how to handle user clicks in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/register-callback/
weight: 2
---

The easiest way to handle button events is to register a callback function for a particular entity. Every time that entity is interacted with using a specific button, the callback function is called.

If you need to add the same behavior to multiple similar entities, consider using the [System-based]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approach instead of adding callbacks to each entity. The system-based approach can result in more efficiency as you iterate over a list of similar entities. 

The Register callback approach is especially useful if you want to describe a behavior that affects a single entity, as it's more straight forward. 

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.


## Pointer down

Use `EventSystem.onPointerDown()` to detect presses of a specific button.

This statement requires three parameters:

- `entity`: The entity to handle
- `cb`: A callback function to run each time a button down event occurs while pointing at the entity
- `opts`: An object with additional data:
	- `button`: Which button to listen for. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options. If no button is specified, then all buttons are listened to, including movement buttons like forward and jump.
	- `hoverText`: What string to display in the hover feedback hint. "Interact" by default.
	- TODO: hideFeedback

```ts
EventsSystem.onPointerDown(
  entity,
  function () {
    log("clicked entity")
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Click'
  }
)
```

The above command leaves the callback function registered, and will be called as an [asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}) every time the related button event occurs. Do not run this recurrently within a system.


## Feedback

It's very important to give players some kind of indication that an entity can be interacted with. When registering an input action with the `EventsSystem`, by default players will see a hover feedback with an icon for the button they need to press and a string that reads "Interact". You can customize this.

The hover feedback on the UI displays a different icon depending on what input you select in the `button` field. On PC, it displays an icon with an `E` for `InputAction.IA_PRIMARY`, an `F` for `InputAction.IA_SECONDARY`, and a mouse for `InputAction.IA_POINTER`.

Change the string by changing the `hoverText` value. Keep this string short, so that it's quick to read and isn't too intrusive on the screen.


```ts
EventsSystem.onPointerDown(
  entity,
  function () {
    log("opened door")
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Open door'
  }
)
```

TODO: screenshot

### Change existing feedback

When registering an input action with the `EventsSystem`, this is creating a `PointerHoverFeedback` component and adding it to the interactive entity behind the scenes. This component handles the behavior of the UI hover hint. To change the behavior of the hover feedback, modify this component. See [Show feedback]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md#show-feedback" >}}) for more about how to deal with this component.

```ts
const hoverFeedback = PointerHoverFeedback.getMutable(myEntity)

hoverFeedback.pointerEvents[0].eventInfo.hoverText = "Close door"
```

## Pointer up

Use `EventsSystem.onPointerUp` to register a callback function that gets called when the indicated player lets the button up while pointing at the entity.

```ts
EventsSystem.onPointerUp(
  myEntity,
  function () {
    log("button up")
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Button up',
  }
)
```

This statement requires three parameters:

- `entity`: The entity to handle
- `cb`: A callback function to run each time a button up event occurs while pointing at the entity
- `opts`: An object with additional data:
	- `button`: Which button to listen for. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options. If no button is specified, then all buttons are listened to, including movement buttons like forward and jump.
	- `hoverText`: What string to display in the hover feedback hint. "Interact" by default.
	- TODO: hideFeedback

A same entity can have two different callbacks registered, one for `EventsSystem.onPointerDown` and one for `EventsSystem.onPointerUp`.

> Note: The hover feedback for a button up event is only displayed when the button is currently pushed down. If the player points at the entity without holding the button down, they will see no feedback, or the feedback for the button down event, if any.


<!-- 
## Click events

EventsSystem.onClick(entity, fn, { button, hoverText }) -->

## Remove callbacks

To remove a callback function, use `EventsSystem.removeOnPointerDown` or `EventsSystem.removeOnPointerUp`.

```ts
EventsSystem.removeOnPointerDown(myEntity)

EventsSystem.removeOnPointerUp(myEntity)
```

Once removed, the hover feedback on the entity should no longer be displayed, and the entity should no longer be interactive.


## Data from event

Fetch additional data about the action event, like the id of the entity that was hit, or the angle of the ray, by using `Input.getInputCommand()`.


```ts
EventsSystem.onPointerDown(
  myEntity,
  function () {
    const eventData = Input.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)
    log(eventData.hit.entityId)
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Click'
  }
)
```



See [LINK]
TODO link

### Handle multiple buttons

You can't register more than one `onPointerDown` on a single entity. Ideally you should use the [System-based]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approach, as this allows you to handle as many different inputs as you wish, and display a UI hover feedback hint for each.

As an alternative, you can use the Register callback approach and leave the `button` field undefined. This is not ideal, as the hover hint shows a single string and won't specify what action to activate. Note that this will make the callback function run for every input action including movement keys, so you must filter out only the actions you care about. Fetch which input was activated via `Input.getInputCommand`.


TODO: example


```ts

```



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

If you need to add the same behavior to multiple similar entities, consider using the [System-based]({{< ref "/content/creator/sdk7/interactivity/button-events/system-based-events.md" >}}) approach instead of adding callbacks to each entity. Or if you need to set more specific custom logic, you might want to deal with the raw data and use the [Advanced]({{< ref "/content/creator/sdk7/interactivity/button-events/advanced-button-events.md" >}}) approach.

For an entity to be interactive, it must have a [collider]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md" >}}). See [obstacles]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#obstacles" >}}) for more details.


## Pointer down

Use `EventSystem.onPointerDown()` to detect presses of a specific button.

This statement requires three parameters:

- The entity to handle
- A function to run each time the entity is clicked
- An object with additional data:
	- `button`: Which button to listen for. If no button is provided, then all buttons are listened to. See [Pointer buttons]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md#pointer-buttons" >}}) for supported options.
	- `hoverText`: What string to display in the hover feedback hint.
	- TODO: hideFeedback

Note: the selected button changes an icon in the hover feedback

```ts
EventsSystem.onPointerDown(
  entity,
  function () {
    createCube(1 + Math.random() * 8, Math.random() * 8, 1 + Math.random() * 8)
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Click'
  }
)
```

> Note: see others

When it runs, async

Note, to handle multiple buttons see system

Select button, default behavior all buttons
advise against (even forward triggers it)



## Feedback

default

text

## Pointer up

EventsSystem.onPointerDown(entity, fn)
EventsSystem.onPointerUp(entity, fn)



## Click events

EventsSystem.onClick(entity, fn, { button, hoverText })

## Remove callbacks

EventsSystem.removeOnPointerDown(entity)
EventsSystem.removeOnPointerUp(entity)


## Data from event


```ts
EventsSystem.onPointerDown(
  myEntity,
  function () {
    createCube(1 + Math.random() * 8, Math.random() * 8, 1 + Math.random() * 8)
    const eventData = Input.getInputCommand(InputAction.IA_POINTER, PointerEventType.PET_DOWN, myEntity)
    log(eventData.hit.entityId)
  },
  {
    button: InputAction.IA_PRIMARY,
    hoverText: 'Click'
  }
)
```

### Handle multiple buttons

fetch data, add an if

otherwise use a system
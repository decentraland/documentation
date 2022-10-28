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

---
date: 2018-02-14
title: About button events
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


---
date: 2024-07-25
title: Make any item smart
description: Configure any item to behave like a smart item.
categories:
  - scene-editor
type: Document
url: /creator/editor/make-any-item-smart
weight: 4
---

# Making any item smart

{{< youtube qXjQxMC97H0 >}}

Smart items are just regular items with an **Action** and/or **Trigger** component. You can add these components to any item in your scene. You can also import your own custom 3D models and add the same to those.

To add components to an item click the **Plus Icon** next to the item name, and select what component to add from the dropdown list.

<img src="/images/editor/add-component.png" width="300"/>

This allows for a huge amount of creative possibilities. Turn a candle into a lever that opens up a secret passage behind a book shelf, play mysterious sounds from inside a well, make diamonds into collectable items that shrink to 0 when clicked. There are tons of imaginative ways to combine these mechanics!

{{< hint info >}}
**💡 Tip**: When a player interacts with an item, you should show some kind of feedback to make that interaction clear. If the model doesn't have any animations, consider at least playing a sound. In some cases it might work to make the item do a slight tween in scale and then return to its original scale, as a form of feedback.
{{< /hint >}}

# See also

- [Smart items - Basics]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}})
- [Smart items - Advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md#making-any-item-smart" >}})
- [States and conditions]({{< ref "/content/creator/scene-editor/smart-items/states-and-conditions.md" >}})
- [Combine with code]({{< ref "/content/creator/scene-editor/smart-items/combine-with-code.md" >}})

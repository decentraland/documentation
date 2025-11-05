---
date: 2024-07-25
title: Trigger Area
description: React to the player's position
categories:
  - scene-editor
type: Document
url: /creator/scene-editor/interactivity/trigger-area
weight: 2
---

To trigger an action when the player walks into or out of an area, use the Trigger Area [Smart Item]({{< ref "/content/creator/scene-editor/interactivity/smart-items.md" >}}).

<img src="/images/editor/trigger.png" width="150"/>

The orange cube you see while editing your scene is only visible in the Scene Editor, it becomes invisible when running a preview of the scene. You can easily adjust and scale the orange cube to cover exactly the area you need.

If any part of the player's body overlaps with this orange cube, the assigned event will be called.

Use the **On Player Enters Area** and **On Player Leaves Area** trigger types on the item's **Triggers** component. The actions on these trigger events are activated every time that the player enters or leaves the area.

<img src="/images/editor/on_player_enters.png" width="300"/>

You can add as many different actions on the same trigger event, this will activate them all simultaneously.

{{< hint info >}}
**💡 Tip**: If the trigger areas in your scene start getting in the way of editing other content, remember you can always lock and/or hide them from the [Entity Tree]({{< ref "/content/creator/scene-editor/get-started/scene-editor-essentials.md#the-entity-tree" >}}).

  <img src="/images/editor/hide-trigger.png" width="200"/>
{{< /hint >}}

You can also add **Trigger conditions**, so that the actions are only carried out if certain conditions are met in the scene. For example, you could have a trigger area that opens a sliding door when the player walks in; you could use a condition there to check the state of a lever that acts as a power switch, and only open the door if the power is on. See [States and conditions]({{< ref "/content/creator/scene-editor/interactivity/states-and-conditions.md" >}}) for more details.

<img src="/images/editor/trigger-conditions-trigger-area.png" width="300"/>

Multiple trigger areas can overlap, and don't affect each other.

{{< hint info >}}
**📔 Note**:
You can also use **On Player Enters Area** and **On Player Leaves Area** trigger events on any other smart item, but keep in mind that it can be challenging to know the area covered by the trigger.

The size of the triggerable area doesn't relate to the item's visible shape or its colliders, it's always a cube of 1m on each side, affected by the scale of the item.
{{< /hint >}}

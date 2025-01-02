---
date: 2025-01-02
title: Custom Items
description: Create your own custom items to reuse on any of your scenes.
categories:
  - scene-editor
type: Document
url: /creator/editor/custom-items
weight: 8
---

Define a Custom Item to reuse it easily on any of your scenes.

## How to Define a Custom Item

Right-click on an entity on the [Entity Tree], or select several entities and then right-click on them. Select **Create Custom Item**.

{{< hint info >}}
**💡 Tip**: The Custom can include any number of entities. Any nested entities are automatically included.

You can also select several entities at a same hiererchical level
{{< /hint >}}

This action takes a snapshot of the state of every component on the selected entities, except for its position, rotation, and scale. This includes **Actions**, **Triggers**, **Multiplayer**, **Visibility**, and any other component. The original entities aren't affected.

Note:
Any smart item actions and triggers will self-reference their own copy. For example, if you define a Custom Item that includes an elevator and buttons, the buttons on each copy of the elevator will control the copy of the elevator they belong to, not the original copy.

The item will now be listed on the **Custom Items** tab. If no Custom Items exist, this tab is not displayed.

The Custom Item is named after the parent entity selected. To rename it, right click on the Custom Item definition on the **Custom Items** tab and select **Rename**.

## Using Custom Items

Simply drag the item from the **Custom Items** tab into your scene. Each copy you add will be independent. You can alter any copy of a Custom Item, even the original copy, and this won't impact the template. Newly created copies will still refer to the state of the item when it was first defined.

Notice that Custom Items are displayed with a different icon on the Entity Tree. At the top of the Item properties menu on the right, you'll also see a mention of which Custom Item they were created from.

To delete a custom item, right-click on the item on the **Custom Items** menu and select **Delete**. This action doesn't affect any existing copies of the item on your scenes, orphaned Custom Items remain on your scene unchanged. Deleting a Custom Item definition only removes it from the Custom Items tab.

You can't modify the definition of a Custom Item that's already created, you should create a new one and delete the original.

## Sharing Custom Items

You can share your custom items with other creators, so they can use them on their own scenes.

Custom Items are stored on your local machine, in folder x x

Any **Asset** used by the item is also stored in the Custom Item's folder, for easy reuse on other scenes. This includes any 3D models, images, sounds, and videos referenced by the item.

Simply copy the full folder, and tell the other user to paste the folder on their own Custom Item location on their machine. This folder should include everything they need to use your Custom Item. Users may need to close and re-open the project to update the list after adding the folder.

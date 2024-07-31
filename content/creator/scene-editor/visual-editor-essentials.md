---
date: 2024-07-25
title: Visual Editor Essentials
description: How to use the Visual Editor
categories:
  - scene-editor
type: Document
url: /creator/editor/visual-editor-essentials
weight: 2
---

TODO: Move around

TODO: overall layout: item tree, canvas, item properties, asset packs

TODO: Set ground

TODO: Add items

TODO: position items

TODO: local assets
warning that when you place an item it's added to folder, delete
link to import-items

## Scene size

You can edit the size of your scene by clicking the _pencil icon_ and then changing the number or rows and columns.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

Scenes in Decentraland occupy one or several adjacent LAND parcels. Each LAND parcel measures 16x16 meters.

Set the number of parcels for the rows and columns and click **Apply layout** to see it affect your scene on the visual editor.

<img src="/images/editor/scene-layout.png" alt="Scene name" width="124"/>

To build something to deploy to LAND parcels you own, make sure the shape of the scene matches the shape of where you want it deployed.

{{< hint info >}}
**💡 Tip**: You can toggle each tile on the grid off by clicking on it. This allows you to draw non-rectangular shapes for your scene layout.

<img src="/images/editor/non-rectangular.png" alt="Scene name" width="124"/>

{{< /hint >}}

If you own a Decentraland NAME, you can also deploy your scene to a [Decentraland World]({{< ref "/content/creator/worlds/about.md" >}}). In that case, you'll have an unlimited number of parcels, but you will have a size limit in MB.

See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) to better understand the different options.

## The entity tree

On the left margin, you'll see a tree structure with all of the entities in the scene. This includes all of the items you add, as well as a few default ones.

Instead of selecting an item by clicking on it from the 3D view of the scne, you can select it from the tree view. Click the right-mouse button on an entity to reveal more options: you can rename, delete, or duplicate, also create a child entity, or add a component to the entity.

Entities follow a hierarchy that can have as many levels as you want. Establish a parent-child relationship between two entities by dragging one item onto another on the tree. A child entity inherits the position of the parent, so when the parent moves, it carries any children with it. This can be practical while building a scene, for example you can set glasses and plates as children of a table, and then move the table without needing to readjust anything else. It can also be important when interacting with the scene, for items to move together.

<img src="/images/editor/item-hierarchy.png" alt="Scene name" width="124"/>

You can also minimize or expand the children of an entity to keep the view simple, this action has no effect on the scene.

### Special entities

The scene includes a couple of special entities that you can see in the entity tree.

- **Scene**: This refers to the root entity, everything you add in the scene is a child of this entity. You can open it to view [scene settings](#scene-settings).
- **Player**: The player's avatar. You can add special components to this entity that can change gameplay mechanics. You can also drag other entities to be children of the avatar. If an entity is a child of the avatar, its position will be fixed to the player. Use this for example to add a floating marker over the player's head, that follows the player around.
- **Camera**: The player's camera. You can drag other entities to be children of the camera. If an entity is a child of the camera, its position will be fixed on screen. Use this for example to display a gun in a shooter game, that is always in view even if the player points up or down.

### Lock or hide items

You might find it handy to sometimes lock an item, to prevent accidentally selecting and moving it. This is especially useful for background items, like the ground, or a building. To lock an item, look for it on the entity tree on the left, hover over it, and select the lock icon. You can toggle this behavior on and off via that same icon.

You might also want to hide an item that could obstruct your view while placing others. This is especially useful to hide the roof or a building, while working on the interiors. Hidden items are only hidden in the Editor window, not to players entering the scene. To hide an item, look for it on the item tree on the left, hover over it, and select the eye icon. You can toggle this behavior on and off via that same icon.

![](/images/editor/hide-lock-item.png)

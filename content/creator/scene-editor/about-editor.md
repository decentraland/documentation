---
date: 2024-07-25
title: Scene Editor
description: The scene Editor is a simple visual tool that lets you create and publish Decentraland scenes.
categories:
  - scene-editor
type: Document
url: /creator/editor/about-scene-editor
weight: 1
---

The Scene Editor is a powerful tool that combines a simple no-code interface with the ability to write code to customize your scenes further.

See [Editor Installation]({{< ref "/content/creator/scene-editor/editor-installations.md" >}}) to get started.

<!-- TODO: Link to install -->

<!-- TODO: update video -->

{{< youtube PF7smSBxVOc >}}

## Create scene

To create a new scene, open the Scene Editor and press the go to scenes section in the builder and press _Create scene_ button. You will be able to create a scene from scratch or use any of the available templates.

Scenes in Decentraland occupy one or several adjacent LAND parcels. Each LAND parcel measures 16x16 meters.

To build something to deploy to LAND parcels you own, make sure the shape of the scene matches the shape of where you want it deployed.

<!-- TODO: Note about importing an existing scene. If your scene is on the web editor, download it and unzip. You can also import scenes built with code -->

## Moving around

To find your way around the Scene Editor:

- Use **A** and **W** to move close or far. You can also use the mouse scroll wheel, or **+** and **-** keys
- Use **S** and **D** to move sideways.
- Click the mouse and drag to rotate. You can click either with the Right or the Left button. It's recommended to use the Right button, since with the Left you might accidentally select an item.
- Press **Space bar** to reset the camera back to the default position

## Scene size

Scenes in Decentraland occupy one or several adjacent LAND parcels. Each LAND parcel measures 16x16 meters.

To build something to deploy to LAND parcels you own, make sure the shape of the scene matches the shape of where you want it deployed.

<!-- TODO about WORLDS, link to doc about where to publish -->

You can edit the size of your scene by clicking the _pencil icon_ and then changing the number or rows and columns.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

<!-- TODO screenshot and instructions for changing size
maybe link to whole doc showing size settings, and types of scenes WORLD vs Genesis City?
 -->

## Set the Ground

The scene's ground can use various different textures. You can find these in the different themed asset packs in the item menu.

Items of type **Ground** have a paint bucket icon on them. If you drag one of these into your scene, it covers all of your scene's ground with copies of this item.

<img src="/images/editor/ground.png" width="500" />

You can also add a single copy of the item by holding **Shift** while you drag the ground onto the scene.

<img src="/images/editor/ground-entities.png" width="300" />

The collection of ground items appear in the [entity tree](#the-entity-tree) inside a folder. Each one of them is locked, to prevent accidentally selecting. [Untoggle](#lock-or-hide-items) the items to move or edit them.

## Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene. There’s a great variety!

You can also use the search box. Note that when you're inside an asset pack, the search only looks in that asset pack.

To place an item, click and drag the item to a specific location in the scene. All your changes are saved automatically.

## Position items

Click and drag a selected item to move it freely around the scene at ground level.

<!-- TODO: image of gizmos -->

To move an item with more precision, use the _Move tool_, on the top menu. Each arrow lets you move the item in a single axis at a time. With this tool you can also position things above the ground level.

To rotate an item, select the _Rotate tool_ on the top menu. A gizmo appears on the selected item, and you can use each of the hoops to rotate the item on one axis at a time.

To make an item larger or smaller, select the _scale_ tool on the top menu, then click on the center of the gizmo and drag in or out. This tool also lets you stretch an item in a single axis to change its proportions, to do this click on one of the axis of the gizmo and drag it.

<!-- TODO: Image of scale gizmo -->

{{< hint info >}}
**💡 Tip**: To have greater precision while moving, rotating or scaling an item, press and hold the _Shift_ key while making adjustments.
{{< /hint >}}

To delete an item from the scene, select it and click the _Delete_ tool.

To duplicate an item, select it and hit **Ctrl + C** and then **Ctrl + V**. You can also find the item on the [entity tree](#the-entity-tree) to right-click and select the option **Duplicate**. The new item will be perfectly overlapping the original.

To select multiple items at the same time, press and hold the _Control_ key while selecting them. You can then move, rotate, scale, duplicate or delete all of them in a single action.

## Preview

To test your scene and experience it like a player, click the _Preview scene_ button on the top-right corner. This will open a new window with the Decentraland Desktop Explorer, running just your scene. There you can move around the scene and interact with interactive items.

<!-- TODO: DOWNLOAD EXPLORER -->

![](/images/preview-scene.png)

## Scene settings

Click the \*Pencil icon\*\* on the top-right of the screen. This opens a series of scene-level properties to edit.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

This opens up the scene menu, where you can configure multiple properties including title and thumbnail, scene category and age rating, player spawn locations, and feature toggles. See [Scene Metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}).

<!-- TODO talk about naming and other things -->

## Publish scene

Once you're happy with the scene, press _Publish scene_.

- Select _My world_ to make your scene available in any of your [worlds]({{< ref "/content/creator/worlds/about.md" >}}).

- Select _My Land_ if you own land, or have been given deploy permissions by an owner. Then select the parcels where you want it deployed on the map. Parcels where you are allowed to deploy are shown in pink.

## Scene limitations

Decentraland scenes need to follow certain limitations, to be able to run them one next to another. There is a maximum number of materials, textures, triangles, etc, that is proportional to the number of parcels in the scene. See [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) for more details.

If the content in your scene exceeds any of these limits, the editor will notify this on the bottom-left corner.

<img src="/images/editor/triangle-limit1.png" width="300" />

You can expand this menu to view details.

<img src="/images/editor/triangle-limit2.png" width="300" />

{{< hint info >}}
**💡 Tip**: If you're building a Decentraland World, you can always add more parcels to increase your limits.
{{< /hint >}}

The content in a Decentraland scene must also avoid spilling onto neighbor parcels. If any of the models in your scene extend beyond the limits, the editor will mark these in red.

<img src="/images/editor/out-of-bounds.png" width="300" />

Note that these checks don't look at the visible geometry of the meshes, but rather they look at the bounding boxes of these meshes, as this is more performant. Learn more about [Bounding Boxes]({{< ref "/content/creator/3d-modeling/meshes.md#bounding-boxes" >}}).

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

<!-- TODO: add links for more at the end
smart items, combine with code, etc -->

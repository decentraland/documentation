---
date: 2024-07-25
title: Scene Editor Essentials
description: How to use the Scene Editor
categories:
  - scene-editor
type: Document
url: /creator/editor/scene-editor-essentials
weight: 2
---

The Scene Editor's UI is divided into a few different sections, with different purposes.

<img src="/images/editor/editor-layout.png" width="500" />

- **Canvas**: Manipulate items directly and see what your scene looks like.
- **Entity tree**: Contains a list of all items in the scene and their hierarchy.
- **Properties**: Displays details about the currently selected item.
- **Resources**: Shows resources that are available to use.

## Moving around

To find your way around the Scene Editor:

- Use **A** and **W** to move close or far. You can also use the mouse scroll wheel, or **+** and **-** keys
- Use **S** and **D** to move sideways.
- Click the mouse and drag to rotate. You can click either with the Right or the Left button.
- Press **Space bar** to reset the camera back to the default position

## Set the Ground

The scene's ground can use various different textures. You can find these in the different themed asset packs in the item menu.

Items of type **Ground** have a paint bucket icon on them. If you drag one of these into your scene, it covers all of your scene's ground with copies of this item.

<img src="/images/editor/ground.png" width="500" />

You can also add a single copy of the item by holding **Shift** while you drag the ground onto the scene.

<img src="/images/editor/ground-entities.png" width="200" />

The collection of ground items appear in the [entity tree](#the-entity-tree) inside a folder. Each one of them is locked, to prevent accidentally selecting. [Untoggle](#lock-or-hide-items) the items to move or edit them.

## Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene.

<img src="/images/editor/asset-packs.png" alt="Scene name"/>

You can also use the search box. Note that when you're inside an asset pack, the search only looks in that asset pack.

To place an item, click and drag it in from the asset pack menu into a location on your scene in the canvas. You'll

<img src="/images/editor/drop-item.gif" alt="Scene name" width="300"/>

{{< hint info >}}
**💡 Tip**: Your changes are saved automatically whenever you add, move, or edit properties of any of the items in your scene.
{{< /hint >}}

To duplicate an item, select it and hit **Ctrl + C** and then **Ctrl + V**. You can also find the item on the [entity tree](#the-entity-tree) to right-click and select the option **Duplicate**. The new item will be perfectly overlapping the original.

To delete an item from the scene, select it press the _Delete_ key.

See [Import items]({{< ref "/content/creator/scene-editor/import-items.md" >}}) for adding your own custom 3D models from disk.

{{< hint warning >}}
**📔 Note**: Once you dragged a 3D model into your scene, it's downloaded into your project folder and remains there even if you delete it. These unused models can increase the size of your scene.

Open the **Local Assets** tab to delete any unused models.
{{< /hint >}}

## Position items

{{< youtube cNl02PFPdcQ >}}

Click and drag a selected item to move it freely around the scene at ground level.

You can also use the tools on the top menu:

<img src="/images/editor/gizmos.png" alt="Scene name" width="124"/>

- **Move tool**: Each arrow lets you move the item in a single axis at a time. With this tool you can also position things above the ground level.

- **Rotate tool**: A gizmo appears on the selected item, and you can use each of the hoops to rotate the item on one axis at a time.

- **Scale tool**: Click on the center of the gizmo and drag in or out to enlarge. This tool also lets you stretch an item in a single axis to change its proportions, to do this click on one of the axis of the gizmo and drag it.

<img src="/images/editor/move-items.gif" alt="Scene name" width="300"/>

To have greater precision while moving, rotating or scaling an item, press and hold the _Shift_ key while making adjustments.

To change the movement granularity and other settings, click the downward arrow on the right of the tools. The following settings are available:

- **Snap**: Toggle the grid on or off. When off, the behavior of **Shift** is inverted: you don't follow the grid by default, you do if you hold **Shift**.
  - **Position**: The size of movement increments in meters when **Snap** is on.
  - **Rotation**: The size of rotation increments in degree when **Snap** is on.
  - **Scale**: The size of scale increments when **Snap** is on.
- **Align to world**: Refers to the axis of movement and rotation. They can either always align with the world, or align with the object's orientation. If aligned to world, the axis don't change with the object's orientation.
  - **Position**: Does the Move tool axis align with the direction that the object faces? Or with the world?
  - **Rotation**: Do the Rotate tool axis align with the object's orientation, or with the world?

To select multiple items at the same time, press and hold the _Control_ key while selecting them. You can then move, rotate, scale, duplicate or delete all of them in a single action.

## Smart items

Smart items are special items that come with built-in interactive behaviors. See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for more details.

<img src="/images/editor/smart-items.jpg" width="300"/>

## The entity tree

On the left margin, you'll see a tree structure with all of the entities in the scene. This includes all of the items you add, as well as a few default entities.

{{< hint info >}}
**💡 Tip**: Everything in a scene is an Entity, they are the basic building blocks of scenes. Items are Entities that have at least a position and a visible shape.
{{< /hint >}}

Instead of selecting an item by clicking on it from the 3D view of the scne, you can select it from the tree view. Click the right-mouse button on an entity to reveal more options: you can rename, delete, or duplicate, also create a child entity, or add a component to the entity.

Entities follow a hierarchy that can have as many levels as you want. Establish a parent-child relationship between two entities by dragging one item onto another on the tree. A child entity inherits the position of the parent, so when the parent moves, it carries any children with it. This can be practical while building a scene, for example you can set glasses and plates as children of a table, and then move the table without needing to readjust anything else. It can also be important when interacting with the scene, for items to move together.

<img src="/images/editor/item-hierarchy.png" alt="Scene name" width="200"/>

You can also minimize or expand the children of an entity to keep the view simple, this action has no effect on the scene.

### Special entities

The scene includes a couple of special entities that you can see in the entity tree.

- **Scene**: This refers to the root entity, everything you add in the scene is a child of this entity. You can open it to view [scene settings](#scene-settings).
- **Player**: The player's avatar. You can add special components to this entity that can change gameplay mechanics. You can also drag other entities to be children of the avatar. If an entity is a child of the avatar, its position will be fixed to the player. Use this for example to add a floating marker over the player's head, that follows the player around.
- **Camera**: The player's camera. You can drag other entities to be children of the camera. If an entity is a child of the camera, its position will be fixed on screen. Use this for example to display a gun in a shooter game, that is always in view even if the player points up or down.

### Lock or hide items

You might find it handy to sometimes lock an item, to prevent accidentally selecting and moving it. This is especially useful for background items, like the ground, or a building. To lock an item, look for it on the entity tree on the left, hover over it, and select the lock icon. You can toggle this behavior on and off via that same icon.

You might also want to hide an item that could obstruct your view while placing others. This is especially useful to hide the roof or a building, while working on the interiors. Hidden items are only hidden in the Scene Editor's canvas window, not to players entering the scene. To hide an item, look for it on the entity tree on the left, hover over it, and select the eye icon. You can toggle this behavior on and off via that same icon.

<img src="/images/editor/hide-lock-item.png" alt="Scene name" width="200"/>

## Properties panel

Select an item by clicking on it on the canvas or the entity tree. You'll then see its components displayed on the properties panel, on the right of the screen. Different items have different components that each display specific settings.

<img src="/images/editor/components-in-editor.png" alt="Scene name" width="200"/>

Most non-interactive items have the following components:

- **Transform**: Sets position, rotation, and scale of the item.
- **GLTF**: What 3D model to load.

[Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) can include other components.

See [Components]({{< ref "/content/creator/scene-editor/components.md" >}}) to learn more.

## Scene limitations

Decentraland scenes need to follow certain limitations, to be able to run them one next to another. There is a maximum number of materials, textures, triangles, etc, that is proportional to the number of parcels in the scene. See [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) for more details.

If the content in your scene exceeds any of these limits, the Scene Editor will notify this on the bottom-left corner.

<img src="/images/editor/triangle-limit1.png" width="250" />

You can expand this menu to view details.

<img src="/images/editor/triangle-limit2.png" width="300" />

{{< hint info >}}
**💡 Tip**: If you're building a Decentraland World, you can always increase the [scene size]({{< ref "/content/creator/scene-editor/scene-editor-essentials.md#scene-sizes" >}}) to increase your limits.
{{< /hint >}}

The content in a Decentraland scene must also avoid spilling onto neighbor parcels. If any of the models in your scene extend beyond the limits, the Scene Editor will mark these in red.

<img src="/images/editor/out-of-bounds.png" width="250" />

These checks don't look at the visible geometry of the meshes, but rather they look at the bounding boxes of these meshes, as this is more performant. Learn more about [Bounding Boxes]({{< ref "/content/creator/3d-modeling/meshes.md#bounding-boxes" >}}).

## Scene settings

Click the \*Pencil icon\*\* on the top-right of the screen. This opens a series of scene-level properties to edit.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="64"/>

Here you can configure multiple properties including title and thumbnail, scene size, scene category and age rating, player spawn locations, and feature toggles.

See [Scene Settings]({{< ref "/content/creator/scene-editor/scene-settings.md" >}}).

## See also

- See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for how to add simple interactivity to your scene.
- See [Combine with code]({{< ref "/content/creator/scene-editor/smart-items/combine-with-code.md" >}}) for how to edit the code of your scene.
- See [Publish scene]({{< ref "/content/creator/scene-editor/publish-scene.md" >}}) for how to publish your scene to Decentraland.

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

<!-- TODO: overall layout: item tree, canvas, item properties, asset packs

diagram with main sections and brief bullets w description of each

Entity Tree:
Main canvas:
Item configuration:
Asset packs/local files

-->

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

<img src="/images/editor/ground-entities.png" width="300" />

The collection of ground items appear in the [entity tree](#the-entity-tree) inside a folder. Each one of them is locked, to prevent accidentally selecting. [Untoggle](#lock-or-hide-items) the items to move or edit them.

## Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene.

<img src="/images/editor/asset-packs.png" alt="Scene name" width="124"/>

You can also use the search box. Note that when you're inside an asset pack, the search only looks in that asset pack.

To place an item, click and drag it in from the asset pack menu into a location on your scene in the visual editor. You'll

<img src="/images/editor/drop-item.gif" alt="Scene name" width="124"/>

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

## Position items

Click and drag a selected item to move it freely around the scene at ground level.

You can also use the tools on the top menu:

<img src="/images/editor/gizmos.png" alt="Scene name" width="124"/>

- **Move tool**: Each arrow lets you move the item in a single axis at a time. With this tool you can also position things above the ground level.

- **Rotate tool**: A gizmo appears on the selected item, and you can use each of the hoops to rotate the item on one axis at a time.

- **Scale tool**: Click on the center of the gizmo and drag in or out to enlarge. This tool also lets you stretch an item in a single axis to change its proportions, to do this click on one of the axis of the gizmo and drag it.

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

## Item configuration

When an item is selected, you'll see its components displayed on the right tab. Different items have different components.

Most non-interactive items have the following components:

- **Transform**: Sets the position, rotation, and scale of the item. If the item has a parent, these value are relative to the parent's.
- **GLTF**: What 3D model to load. It includes the local path to the file for this 3D model. It also includes some properties for configuring [colliders]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#colliders-on-3d-models" >}}) on the model.

[Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) can include other components, see [Smart items advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md" >}}).

To add components to an item, click the **+** sign at the top of the item configuration tab and select the component from the list. See [Make any item smart]({{< ref "/content/creator/scene-editor/smart-items/make-any-item-smart.md" >}})

## Scene settings

Click the \*Pencil icon\*\* on the top-right of the screen. This opens a series of scene-level properties to edit.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

Here you can configure multiple properties including title and thumbnail, scene size, scene category and age rating, player spawn locations, and feature toggles.

See [Scene Metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}).

#### Scene details

The **Details** tab lets you configure several fields about your scene. These fields are shown to players that might visit your scene, for example when expanding the location on the map, when being prompted to teleport, or when sharing a link to the scene on social media. Make sure you make the information here attractive and accurate to drive more traffic to your scene!

<img src="/images/thumbnail-image.png" width="500" />

The following fields are available:

- **Name**
- **Description**
- **Thumbnail**

{{< hint info >}}
**💡 Tip**: If no thumbnail is provided, it uses the automatic capture you see on the scene's card. We recommend uploading a more attractive image
{{< /hint >}}

- **Age rating**
- **Categories**
- **Author**
- **Email**

See [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}) for more details on these fields.

#### Layout

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

You can also click the **Set Coordinates (Advanced)** button to manually list the coordinates of your scene. Remember that these coordinates must all be adjacent to be valid.

See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) to better understand the different options.

#### Scene restrictions

You can disable certain functionalities on your scene if you chose, in case they might be abused or clash with the kind of experience you want to create.

<img src="/images/editor/scene-restrictions.png" alt="Scene name" width="300"/>

- **Silence voice chat**: Prevent players on your scene from using voice chat.
- **Disable portable experiences**: Prevent players from using [Smart Wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}) or [Portable Experiences]({{< ref "/content/creator/sdk7/projects/portable-experiences.md" >}}).

#### Spawn points

The Spawn Settings in the Settings tab define where players spawn when they access your scene directly, either by directly typing in the coordinates into the browser or teleporting.

<img src="/images/editor/spawn-settings.png" alt="Scene name" width="124"/>

Your scene might have objects that can block players from moving if they happen to spawn right over them, like trees or stairs, or your scene might have an elevated terrain. It would be a bad experience for players if they spawned over something that doesn't let them move. That's why you have the option to set multiple spawn positions in ad-hoc locations.

The position is comprised of coordinates inside the scene. These numbers refer to a position within the parcel, similar to what you'd use in a Transform component.

{{< hint warning >}} 📔 Note: All spawn points must be within the parcels that make up the scene. You can't spawn a player outside the space of these parcels. {{< /hint >}}

Check the Random Offset box to randomly offset the spawning players around the spawn point, with a maximum value. This prevents all players from appearing overlapping each other when they spawn, which looks especially bad in crowded scenes. The Max Offset value is the maximum possible distance from the original spawn point, in both the X or Z axis.

Set the Camera Target to set the direction in which players start looking when they jump into your scene. This allows you to have better control over their first impression.

Click **Add Spawn Point** to include as many spawn points as you want. Players will randomly appear in one of those.

## See also

- See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for how to add simple interactivity to your scene.
- See [Combine with code]({{< ref "/content/creator/scene-editor/smart-items/combine-with-code.md" >}}) for how to edit the code of your scene.
- See [Publish scene]({{< ref "/content/creator/scene-editor/publish-scene.md" >}}) for how to publish your scene to Decentraland.

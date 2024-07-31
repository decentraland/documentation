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

See [Editor Installation]({{< ref "/content/creator/scene-editor/editor-installation.md" >}}) to get started.

<!-- TODO: update video -->

{{< youtube PF7smSBxVOc >}}

## Create a scene

To create a new scene, open the Scene Editor and press the _Create scene_ button.

See [Manage scenes]({{< ref "/content/creator/scene-editor/manage-scenes.md" >}}) for more details.

<!-- TODO: image -->

<!-- TODO: in the future talk about templates -->

<!-- TODO: the scene starts out as a 1x1
or if you're on a template, the size of the template

see Visual Editor Essentials for how to change -->

## Moving around

To find your way around the Scene Editor:

- Use **A** and **W** to move close or far. You can also use the mouse scroll wheel, or **+** and **-** keys
- Use **S** and **D** to move sideways.
- Click the mouse and drag to rotate. You can click either with the Right or the Left button.
- Press **Space bar** to reset the camera back to the default position

## Set the Ground

Navigate the **Asset Packs** to find a ground you like. Items of type **Ground** have a paint bucket icon on them. If you drag one of these into your scene, it covers all of your scene's ground with copies of this item.

<img src="/images/editor/ground.png" width="700" />

See [Visual editor essentials]({{< ref "/content/creator/scene-editor/visual-editor-essentials.md#set-the-ground" >}}) for more details.

## Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene.

<img src="/images/editor/asset-packs.png" alt="Scene name"/>

To place an item, click and drag it in from the asset pack menu into a location on your scene in the visual editor.

<img src="/images/editor/drop-item.gif" alt="Scene name"/>

{{< hint info >}}
**💡 Tip**: Use **Ctrl + C** and then **Ctrl + V** to duplicate an item.

Use the **Delete** key to delete items.
{{< /hint >}}

## Position items

Click and drag a selected item to move it freely around the scene at ground level.

<!-- TODO: move tool gif -->

You can also use the tools on the top menu to _Move_, _Rotate_ or _Scale_ items.

<img src="/images/editor/gizmos.png" alt="Scene name" width="124"/>

See [Visual editor essentials]({{< ref "/content/creator/scene-editor/visual-editor-essentials.md#position-items" >}}) for more details.

## Smart items

Smart items are special items that come with built-in interactive behaviors. See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for more details.

<img src="/images/editor/smart-items.jpg"/>

## Preview

To test your scene and experience it like a player, click the _Preview scene_ button on the top-right corner. This will open a new window with the Decentraland Desktop Explorer, running just your scene. There you can move around the scene and interact with interactive items.

<!-- TODO: DOWNLOAD EXPLORER -->

![](/images/preview-scene.png)

## Scene settings

Click the \*Pencil icon\*\* on the top-right of the screen. This opens a series of scene-level properties to edit.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="124"/>

This opens up the scene menu, where you can configure multiple properties including title and thumbnail, scene size, scene category and age rating, player spawn locations, and feature toggles.

See [Visual editor essentials]({{< ref "/content/creator/scene-editor/visual-editor-essentials.md#scene-settings" >}}) for more details.

<!-- TODO talk about naming and other things -->

## Scene limitations

Decentraland scenes need to follow certain limitations, to be able to run them one next to another. There is a maximum number of materials, textures, triangles, etc, that is proportional to the number of parcels in the scene. See [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) for more details.

If the content in your scene exceeds any of these limits, the editor will notify this on the bottom-left corner.

<img src="/images/editor/triangle-limit1.png" width="300" />

You can expand this menu to view details.

<img src="/images/editor/triangle-limit2.png" width="300" />

{{< hint info >}}
**💡 Tip**: If you're building a Decentraland World, you can always increase the [scene size]({{< ref "/content/creator/scene-editor/visual-editor-essentials.md#scene-sizes" >}}) to increase your limits.
{{< /hint >}}

The content in a Decentraland scene must also avoid spilling onto neighbor parcels. If any of the models in your scene extend beyond the limits, the editor will mark these in red.

<img src="/images/editor/out-of-bounds.png" width="300" />

Note that these checks don't look at the visible geometry of the meshes, but rather they look at the bounding boxes of these meshes, as this is more performant. Learn more about [Bounding Boxes]({{< ref "/content/creator/3d-modeling/meshes.md#bounding-boxes" >}}).

## Publish scene

Once you're happy with your scene, press _Publish scene_.

- Select _My world_ to make your scene available in one of your [worlds]({{< ref "/content/creator/worlds/about.md" >}}).

- Select _My Land_ if you own land, or have been given deploy permissions by an owner. Then select the parcels where you want it deployed on the map. Parcels where you are allowed to deploy are shown in pink.

See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) to better understand the different options.

<!-- TODO: add links for more at the end
smart items, combine with code, etc -->

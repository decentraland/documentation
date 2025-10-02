---
date: 2024-07-25
title: Editing Scenes
description: The scene Editor is a simple visual tool that lets you create and publish Decentraland scenes.
categories:
  - scene-editor
type: Document
url: /creator/editor/about-scene-editor
aliases:
  - /creator/web-editor
weight: 1
---

The Creator Hub includes a powerful Scene Editor that combines a simple no-code interface with the ability to write code to customize your scenes further.

<img src="/images/editor/icon-creator-hub.png" alt="Header" width="128"/>

See [Creator Hub Installation]({{< ref "/content/creator/scene-editor/editor-installation.md" >}}) to get started.

<!-- TODO: update video -->

{{< youtube 52LiG-4VI9c >}}

## Create a scene

To create a new scene, open the Creator Hub and press the _Create scene_ button.

<img src="/images/editor/create-scene.png" width="150" alt="Scene name"/>

You can then select what template to use as a starting point. You can pick a blank scene or a project with some initial content.

Then you'll be asked to name your scene, and choose a location to save it.

See [Manage scenes]({{< ref "/content/creator/scene-editor/manage-scenes.md" >}}) for more details.

## Moving around

To find your way around the Scene Editor:

- Use **A** and **W** to move close or far. You can also use the mouse scroll wheel, or **+** and **-** keys
- Use **S** and **D** to move sideways.
- Use **Q** and **E** to move up and down.
- Use the **Left Mouse Button** to click and select items and to move them around.
- Use the **Right Mouse Button** and drag to rotate the camera.
    {{< hint info >}}
    **💡 Tip**: You can also rotate the camera by pressing **Alt** on Windows, or **Option** on Mac while dragging. This is especially handy when using a trackpad instead of a mouse.
    {{< /hint >}}
- Press **Space bar** to reset the camera back to the default position



## Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene.

<img src="/images/editor/asset-packs.png" alt="Scene name"/>

To place an item, click and drag it in from the asset pack menu into a location on your scene in the canvas.

<img src="/images/editor/drop-item.gif" width="300" alt="Scene name"/>

Click and drag a selected item to move it freely around the scene at ground level. See [Scene editor essentials]({{< ref "/content/creator/scene-editor/scene-editor-essentials.md#position-items" >}}) for more details.

{{< hint info >}}
**💡 Tip**: Some items are **Smart items**, these come with built-in interactive behaviors. See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for more details.
{{< /hint >}}

<img src="/images/editor/smart-items.jpg"/>

## Preview

To test your scene and experience it like a player, click the _Preview_ button on the top-right corner. This will open a new window with the Decentraland Desktop Explorer, running just your scene. There you can move around the scene and interact with interactive items.

{{< hint warning >}}
**📔 Note**: If you don't have it installed on your machine, download the **Decentraland Launcher** from [Decentraland.org](https://decentraland.org).
{{< /hint >}}

<img src="/images/editor/preview-button.png" width="150" alt="Scene name"/>

Configure different preview options from the dropdown menu next to the **Preview** button:

- **Open Console Window During Preview**: Opens a new window with the console output of the scene. This is useful to debug errors in the scene.
- **Skip Auth Screen**: Skips the account selection screen and automatically logs you in with your currently logged in account. This is disabled by default, enable it if you want to test multiple accounts.
- **Landscape Terrain Enabled**: Toggles the landscape around the scene. This is enabled by default, disable it to lower the scene's memory footprint.

## Scene settings

Click the **Pencil icon** on the top-right of the screen. This opens a series of scene-level properties to edit, including name, thumbnail, scene size, and more.

<img src="/images/editor/pencil-icon.png" alt="Scene name" width="64"/>

See [Scene Settings]({{< ref "/content/creator/scene-editor/scene-settings.md" >}}) for more details.

## Publish your scene

Once you're happy with your scene, press _Publish scene_.

 <img src="/images/editor/publish-options.png" alt="Scene name" width="500"/>

See [Publish scene]({{< ref "/content/creator/scene-editor/publish-scene.md" >}}) for more details.

## See also

- See [Scene Editor Essentials]({{< ref "/content/creator/scene-editor/scene-editor-essentials.md" >}}) for more details about the Scene Editor's interface.
- See [Smart items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for how to add simple interactivity to your scene.
- See [Combine with code]({{< ref "/content/creator/scene-editor/smart-items/combine-with-code.md" >}}) for how to edit the code of your scene.
- See [Publish scene]({{< ref "/content/creator/scene-editor/publish-scene.md" >}}) for how to publish your scene to Decentraland.

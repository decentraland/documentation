---
title: Let’s build the metaverse together
date: 2022-02-08
description: Creators intro
categories:
  - development-guide
type: Document
url: /creator
aliases:
  - /content-intro/
  - /development-guide/content-intro/
weight: 2
---

All creators are welcome! In Decentraland you have a wide range of Creative possibilities, for people of different talents and skill levels!

## The Creator Hub

The Creator Hub is the recommended tool for creators of all knowledge levels. It's a desktop application that lets you create:

- [Wearables & Smart Wearables](#wearables)
- [Emotes](#emotes)
- [Scenes](#scenes)

<img src="/images/editor/scene-editor.png" width="750" />

Download the Creator Hub [here](https://decentraland.org/download/creator-hub).

## Wearables

Wearables are items of clothing that player avatars can wear. These are sold as NFTs and purchased in the [Marketplace](https://decentraland.org/marketplace/browse?section=wearables&vendor=decentraland&page=1&sortBy=newest&status=on_sale).

Learn everything about [Creating wearables]({{< ref "/content/creator/wearables-and-emotes/wearables/creating-wearables.md" >}}).

You can also combine a wearable with code from the SDK to create a [smart wearable]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). This turns on a global scene whenever the player puts on the wearable. See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) to better understand the different options.

## Emotes

Emotes are animations that a player's avatar can do. These are sold as NFTs and purchased in the [Marketplace](https://decentraland.org/marketplace/browse?assetType=item&section=emotes&vendor=decentraland&page=1&sortBy=newest&status=on_sale).

Learn everything about [Creating emotes]({{< ref "/content/creator/wearables-and-emotes/emotes/creating-emotes.md" >}}).

## Scenes

3D content in Decentraland is made up of scenes, each scene occupies a finite amount of space and is displayed one next to the other for players to freely walk through them.

The Creator Hub lets you create scenes with an easy drag-and-drop interface, and also edit code to have full control over the interactions. You can run previews, debug, edit code, and publish.

[Learn more]({{< ref "/content/creator/scene-editor/about-editor.md" >}})

### 3D Art

Decentraland scenes are made up of 3D models.

- Chose from the wide catalog of default assets in the Scene Editor. These are ready to go and optimized for using in Decentraland

  <img src="/images/intro/items.png" width="600" />

- Craft your own 3D models using Blender or your preferred 3D tools. Then import them into the Scene Editor.

  <img src="/images/intro/blender.png" width="600" />

{{< hint warning >}}
**📔 Note**: Content in Decentraland should stay within certain [size limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) to ensure your scene runs smoothly.

See [3D modeling]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}) for tips and tricks for optimizing, and information about supported features and formats for 3D models.
{{< /hint >}}

### Interactivity

To make your scene interactive:

- \*_No Code_: Use the UI of the Scene Editor to drop [Smart Items]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) into your scene. These are models that come pre-built with their own behavior, and are highly customizable. You can also assign the same behaviors to your own custom models (no code required).

  <img src="/images/intro/smart-items.png" width="500" />

- **Code**: For developers that want to incorporate custom logic, use the SDK to write code and do anything you can imagine. Learn to use the SDK:

  - [SDK Quick start]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}): follow this mini tutorial for a quick crash course.
  - [Development workflow]({{< ref "/content/creator/sdk7/getting-started/dev-workflow.md" >}}): read this to understand scene creation from end to end.
  - [Examples](https://studios.decentraland.org/resources?sdk_version=SDK7): dive right into working example scenes.

    <img src="/images/intro/sdk-code.png" width="500" />

  {{< hint warning >}}
  **📔 Note**: You will also need to have <img src="/images/editor/vscode.png" alt="Header" width="25" href="https://code.visualstudio.com/"/> [Vs Studio Code](https://code.visualstudio.com/) installed.
  {{< /hint >}}

### Publishing scenes

You don't need to own any tokens to start building your scene with the Scene Editor. To publish your scene, you can chose from the following options:

- **LAND in Genesis City**: This is the main open world in Decentraland, which is split up in 16x16 meter parcels. Buy one or several adjacent parcels in the [Marketplace](https://decentraland.org/marketplace/lands), and deploy your scene there.
- **Decentraland Worlds**: [Worlds]({{< ref "/content/creator/worlds/about.md" >}}) are your own spaces in the metaverse. All you need is to own a [Decentraland name](https://decentraland.org/marketplace/names/claim), and you can publish a scene as big as you want!

See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) to better understand the different options.

See [publishing]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) for details and special options when publishing a scene, to either Genesis City or Worlds.

### Alternative tools

There are also some community-built tools that can help you create Decentraland scenes:

- [**In-World Builder**](https://decentraland.org/play/?realm=https%3A%2F%2Fworlds.dcl-iwb.co%2Fworld%2FBuilderWorld.dcl.eth): Create a scene without leaving the Decentraland explorer. Use various default items or upload your own, without needing to deploy or own land.
- [**Virtual Land Manager**](https://vlm.gg/): Control various aspects of your scene in real time, including highly customized controls. Includes analytics: View historical user activity, track custom interactions, export lists of players in scene, and more.
- [**DCL Edit**](https://dcl-edit.com/): Drag and drop 3d models into your scene. You can then work on adding interactivity to the resulting scene using the SDK.
- [**Unity Exporter Toolkit**](https://github.com/PolygonalMind/dcl-dev-exportersdk7-release): Build in Unity, with a number of pre-built interactive modules. Export a fully-working Decentraland scene.

The following **deprecated tools** are also available:

- **Web Editor:** Use an easy drag and drop interface to create scenes. [Learn more]({{< ref "/content/creator/sdk7/web-editor/web-editor.md" >}}).

- **Visual Studio Code Extension:** An extension to VS Studio Code that lets you create scene, run previews, deploy, and manage dependencies. It also lets you open a drag-and-drop editor inside a VS Code window. [Learn more]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#vs-code-extension" >}}).

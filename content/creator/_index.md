---
title: Let’s build the metaverse together
date: 2022-02-08
description: Run multiple DCL projects at a time
categories:
  - development-guide
type: Document
url: /creator
aliases:
  - /content-intro/
  - /development-guide/content-intro/
weight: 2
---


3D content in Decentraland is made up of scenes, each scene occupies a finite amount of space and is displayed one next to the other for players to freely walk through them. 

The Decentraland SDK is a collection of tools to allow you to create scenes.

- Follow the [Quick start]({{< ref "/content/creator/scenes/getting-started/sdk-101.md" >}}) tutorial for a quick crash course.
- Read the [Development workflow]({{< ref "/content/creator/scenes/getting-started/dev-workflow.md" >}}) to understand the full process of creating a scene, publishing and promoting it.
- Check out scene [examples](https://github.com/decentraland-scenes/Awesome-Repository#examples).

> Note: The currently stable version of the SDK is 6.x. Everything documented under the **scenes** section refers to that stable version. To try out the new version 7 of the SDK (which is still in Alpha), read the documents under the **SDK7 Scenes (alpha)** section. This section is right below the scenes section, non-expanded by default.

### The Decentraland Editor

The Editor is an all-in-one content creation tool. It's intended for users of any knowledge level, combining a graphical interface with code editing capabilities. Both technical and non-technical creators will benefit from using it.

[Learn more]({{< ref "/content/creator/scenes/getting-started/installation-guide.md#the-decentraland-editor" >}}).

### Other scene creation tools

There are a number of tools that can help with arranging 3d models into position in a Decentraland scene. You still need to resort to the SDK to add interactivity to these items, but setting positions visually is a big help.

- [**DCL Edit**](https://dcl-edit.com/): A community-built tool that allows you to drag and drop 3d models into your scene. You can then work on adding interactivity to the resulting scene using the SDK.
- [**Legacy Builder**](https://builder.decentraland.org): a simple drag and drop editor. No coding required, some items include built-in functionality. You can start a scene with the Builder, and then export it to continue working on it with the SDK.

  Read the [documentation]({{< ref "/content/creator/builder/builder-101.md" >}}).

  > Note: If a scene is created by or modified by the SDK, you can't import it into the Builder. You can only go from the Builder to the SDK, not in the other direction.

### 3D Modeling

You can use any 3rd party modeling tool to create 3D models that can be used in Decentraland scenes. It's easy to [import them into the Builder]({{< ref "/content/creator/builder/import-items.md" >}}).

See [3D modeling]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}) for tips and tricks, and information about supported features and formats for 3D models.


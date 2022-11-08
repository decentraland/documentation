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

Decentraland is made up of _parcels_ of LAND, each 16 meters by 16 meters. A _scene_ is an experience that is built on one or several parcels.

Scenes are displayed one next to the other and players can freely walk from one to the other. Each scene is its own contained little world, items from one scene can't extend out into another scene, and the code for each scene is sandboxed from all others.

Each parcel of land is tokenized as an NFT. To be allowed to [publish]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) a scene to a land parcel, you either need to own that NFT or be given permissions by the owner.

<!--
You can also create smart wearables, which are wearable items of clothes that come with their own behavior. Players that put on that wearable can access a whole other layer of experiences on top of Decentraland. -->

## The Decentraland SDK

The Decentraland SDK allows you to create your scene by writing in TypeScript (JavaScript + types).

- Follow the [SDK 101]({{< ref "/content/creator/scenes/getting-started/sdk-101.md" >}}) tutorial for a quick crash course.

- Read the [documentation]({{< ref "/content/creator/scenes/architecture/entities-components.md" >}}) to grasp some of the fundamental concepts.

- Check out scene [examples](https://github.com/decentraland-scenes/Awesome-Repository#examples).

## Graphical editing tools

There are a number of tools that can help with arranging 3d models into position in a Decentraland scene. You still need to resort to the SDK to add interactivity to these items, but setting positions visually is a big help.

- [**DCL Edit**](https://dcl-edit.com/): A community-built tool that allows you to drag and drop 3d models into your scene. You can then work on adding interactivity to the resulting scene using the SDK.

- [**Legacy Builder**](https://builder.decentraland.org): a simple drag and drop editor. No coding required, some items include built-in functionality. You can start a scene with the Builder, and then export it to continue working on it with the SDK.

  Read the [documentation]({{< ref "/content/creator/builder/builder-101.md" >}}).

  > Note: If a scene is created by or modified by the SDK, you can't import it into the Builder. You can only go from the Builder to the SDK, not in the other direction.

## 3D Modeling

You can use any 3rd party modeling tool to create 3D models that can be used in Decentraland scenes. It's easy to [import them into the Builder]({{< ref "/content/creator/builder/import-items.md" >}}).

See [3D modeling]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}) for tips and tricks, and information about supported features and formats for 3D models.

## Design your experience

No matter which tools you'll use, it's always recommended that you think carefully about what you want to build before you start building it. Read the [Design experiences]({{< ref "/content/creator/scenes/design-experience/mvp-guidelines.md" >}}) section to better understand the context, limitations and possibilities that you'll have as your design space when creating a scene for Decentraland.

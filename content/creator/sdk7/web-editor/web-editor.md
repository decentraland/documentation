---
date: 2023-08-16
title: Web Editor
description: The Web Editor is a simple visual tool that lets you create and publish Decentraland scenes.
aliases:
  - /web-editor
categories:
  - web-editor
type: Document
url: /creator/web-editor
weight: 1
---

The Web Editor is a simple visual tool that lets you create and publish Decentraland scenes without the need to install anything.

To access the web editor simply visit the [builder page](https://builder.decentraland.org/scenes) and go to **scenes** section. 

## Create scene

To create a scene, go to scenes section in the builder and press _Create scene_ button. You will be able to create a scene from scratch or use any of the available templates.

Scenes in Decentraland occupy one or several adjacent LAND parcels. Each LAND parcel measures 16x16 meters.

To build something to deploy to LAND parcels you own, make sure the shape of the scene matches the shape of where you want it deployed.

{{< hint warning >}}
📔 Note: The scene creation flow currently only supports rectangular-shaped scenes.
{{< /hint >}}

#### Add items

Navigate the themed asset pack categories on the menu on the bottom to find different items that you can place on your scene. There’s a great variety!

To place an item, click and drag the item to a specific location in the scene. All your changes are saved automatically.

## Preview in explorer

To test your scene and experience it like a player, click the _Preview scene_ button on the top-right corner. This will open a scene preview on a new page, where you can move around the scene and interact with interactive items.

![](/images/preview-scene.png)

## Publish scene

Once you're happy with the scene, press _Publish scene_.

- Select _My world_ to make your scene available in any of your [worlds]({{< ref "/content/creator/worlds/about.md" >}}).

- Select _My Land_ if you own land, or have been given deploy permissions by an owner. Then select the parcels where you want it deployed on the map. Parcels where you are allowed to deploy are shown in pink.

## Download scene

While editing a scene, press the download scene icon to download the contents of the scene as a .zip file. In the scene selector screen, you can also press the three dots icon and select Download scene.

![](/images/download-scene.png)

You can then share this scene with another Builder user, or edit the scene with more freedom by using the Decentraland SDK.

## Upload scene

In the scene selector screen, press Upload scene, then drag one or several .zip files from exported Builder scenes and press Upload.

If a scene is too large to upload, try this:

1. Decompress the scene .zip file.
2. Look for the builder.json inside the uncompressed folder. Compress that single file into a new .zip file.
3. Upload this new .zip file.

{{< hint warning >}}
📔 Note: You can only upload scenes that have been built with the Builder. You can’t upload a scene that was built with the SDK or modified with it.
{{< /hint >}}

## Migrate from SDK6 to SDK7

Scenes created with the Builder in SDK6 can be easily migrated to SDK7 using the builder. To do this:

1. Select an SDK6 scene from the project list
2. Press the **Edit scene** button
3. Select "Use decentraland web editor (SDK7)" option
4. Press the **Migrate now** button. If needed, you can also save a copy of the scene in SDK6. 

{{< hint danger >}}
**❗Warning**  
If the migrated scene contains smart items, these will be removed from the scene. Smart items are not seamlessly migrated.  
{{< /hint >}}

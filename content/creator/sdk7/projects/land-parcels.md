---
date: 2024-05-07
title: Land parcels
description: How parcels of land work in Decentraland.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/land-parcels/
weight: 2
---

When [deploying]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) a scene, the content is uploaded to the coordinates of the parcels in the scene. A scene can include a single parcel, or a list of up to dozens of them. Each parcel represents 16x16 meters in the open world.

All of the entities in the scene must fit entirely within these parcels. If any entities extends beyond, when running a preview you'll see the entity enclosed in a red frame, to make this visible. When the scene is published the entity won't render at all. See [position entities]({{< ref "/content/creator/sdk7/3d-essentials/entity-positioning.md#scene-boundaries" >}})
 for more details.

<img src="/images/3d-model-animations/3d-essentials/09-bounding-box.png" width="300"/>

When publishing content to **Genesis Plaza**, parcels are tied to LAND tokens. You must own the corresponding tokens for each coordinate in your list of parcels, or have deploy permissions granted to you by the owner. When publishing to a [world]({{< ref "/content/creator/worlds/about.md" >}}), you can position your scene on any coordinates you want, but you must own the NAME token associated to that world, or be given deploy permission by the owner. See [Kinds of project]({{< ref "/content/creator/sdk7/projects/kinds-of-project.md" >}}) for more info.

The number of parcels in your scene conditions its limitations. The more parcels in the scene, the more MB of content it's allowed to fit, and the more triangles, materials, etc you can use up. See [Scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}). When publishing to **Genesis Plaza**, adding more parcels requires purchasing them, when publishing to Worlds, you can just modify the scene's settings to add more.

## On the Web Editor

<img src="/images/editor/scene-size-web.png" width="300"/>

## On the Desktop Editor

Edit this on the second tab of the scene menu in the Editor.

<img src="/images/editor/scene-parcels.png" alt="Scene name" width="300"/>

The default scene has its coordinates set to _0,0_, this information is not necessary to change while developing a scene offline, unless you need to occupy multiple parcels. You will need to change this before deploying, to coordinates where you do have deploy permissions.

## On the json file

You can change the scene coordinates on the `scene.json` file:

```json
 "scene": {
    "parcels": [
      "54,-14"
    ],
    "base": "54,-14"
  }
```

See [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#scene-parcels" >}}) for more details.

## Via the command line

You can set the parcels in your scene by running the `npx update-parcels` command in your scene folder. This is especially useful for large scenes, as you don't need to list every parcel involved.

**Single parcel**

Pass a single argument with the scene coords. This coordinate is also set as the base parcel.

`npx update-parcels <parcel>`

For example:

`npx update-parcels 15,-26`

**Multiple parcels**

Pass two arguments: the South-West and the North-East parcels. The South-West parcel is also set as the base parcel.

`npx update-parcels <parcel> <parcel>`

{{< hint info >}}
**💡 Tip**: The South-West parcel is always the one with the lowest numbers on both the _X_ and _Y_ coordinates.
{{< /hint >}}

For example:

`npx update-parcels 15,-26 17,-24`

This command generates a 3x3 scene, with its base parcel in `15,-26`.

**Customize Base Parcel**

Pass three arguments: the South-West and the North-East parcels, and the parcel to use as a base parcel.

`npx update-parcels <parcel> <parcel> <parcel>`

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

**Non-square scenes**

The above commands all generate rectangular-shaped scenes. Decentraland scenes can have L shapes or other configurations. You can generate a larger square with `npx update-parcels` and then manually remove excess parcels from the `scene.json` file.

{{< hint warning >}}
**📔 Note**: The base parcel must be one of the parcels in the scene.
{{< /hint >}}

---
date: 2018-01-06
title: Scene limitations
description: How many things can I put on my scene?
aliases:
  - /documentation/scene-limitations/
  - /builder/scene-limitations/
  - /development-guide/scene-limitations/
  - /creator/builder/scene-limitations
  - /creator/development-guide/scene-limitations
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/scene-limitations/
weight: 2
---

In order to improve performance in the metaverse, we have established a set of limits that every scene must follow. These limits are per-parcel. So the larger the scene, the higher these limits are set.

When working with the [Creator Hub]({{< ref "/content/creator/scene-editor/editor-installation.md" >}}), you can see stats about the resources used by 3D models in your scene, together with the limits for your scene.

<img src="/images/editor/triangle-limit1.png" width="250" />

You can expand this menu to view details.

<img src="/images/editor/triangle-limit2.png" width="300" />

{{< hint info >}}
**💡 Tip**: For a reference table of all specific numbers per parcel count, see:

[Reference table](https://docs.google.com/spreadsheets/d/1BTm0C20PqdQDAN7vOQ6FpnkVncPecJt-EwTSNHzrsmg/edit#gid=0)
{{< /hint >}}

## Scene limitation rules

Below are the maximum number of elements that a scene is allowed to render at the same time:

> _n_ represents the number of parcels that a scene occupies.

- **Triangles:** `n x 10000` Total amount of triangles for all the models in the scene.
- **Entities:** `n x 200` Amount of entities in the scene.
- **Bodies:** `n x 300` Amount of meshes in the scene.
- **Materials:** `log2(n+1) x 20` Amount of materials in the scene. It includes materials imported as part of models.
- **Textures:** `log2(n+1) x 10` Amount of textures in the scene. It includes textures imported as part of models.
- **Height:** `log2(n+1) x 20` Height in meters.

  > Important: Only entities that are currently being rendered in the scene are counted for these limits. If your scene switches between 3D models, what matters is the rendered models at any point in time, not the total sum. Player avatars and any items brought by a player from outside the scene don't count for calculating these limits either.

- **Total file size:** In Genesis City -`15 MB per parcel - 300 MB max`. For Worlds, see [World size](#world-size). Total size of the files uploaded to the content server. Includes 3D models and audio. Doesn't include files that aren't uploaded, such as node.js packages. You can see the full list of files being published and their sizes before you confirm a deployment.

- **File count:** `200 files per parcel` Total count of the files uploaded. Includes 3D models and audio. Doesn't include files that aren't uploaded, such as node.js packages.

- **Max file size** `50 MB per file` No individual file of any type in the scene can exceed 50 MB. Small scenes are restricted further because the file mustn't exceed their Total File Size limit (For example, a single-parcel scene is limited to 15 MB total).

## Optimizing

See [Performance Optimization]({{< ref "/content/creator/sdk7/optimizing/performance-optimization.md" >}}) for tips about how you can keep your scene below these limits and make it run smoother for players.

## Scene boundaries

When running a preview, any content that is located outside the parcel boundaries is highlighted in red when rendered. If any content is outside these boundaries, that part of your content won't be rendered when players visit your scene.

If the tip of a large object leaves the boundaries, this tip will be sliced off the object.

A single parcel scene measures 16 meters x 16 meters. If the scene has multiple parcels, the dimensions vary depending on the arrangement of the parcels.

It's possible to position entities underground, to either hide them or to have only a portion of them emerge. A scene can't have tunnels that go below the default ground height, players can't travel below the `y = 0` height.

## Shader limitations

3D models used in decentraland must use supported shaders and materials. See [3D model materials]({{< ref "/content/creator/3d-modeling/materials.md">}}) for a list of supported shaders.

## Lighting

The scene's lighting conditions can't be changed for all players from the default setting, although each individual player is free to change their own skybox settings from the Explorer UI.

## Texture size constraints

Texture sizes must use width and height numbers (in pixels) that match the following numbers:

```
1, 2, 4, 8, 16, 32, 64, 128, 256, 512 1024
```

> This sequence is made up of powers of two: `f(x) = 2 ^ x` . 512 is the maximum number we allow for a texture size. This is a fairly common requirement among other rendering engines, it's there due internal optimizations of the graphics processors.

The width and height don't need to have the same number, but they both need to belong to this sequence.

**The recommended size for textures is 1024x1024**, we have found this to be the optimal size to be transported through domestic networks and to provide reasonable loading/quality experiences.

Examples of other valid sizes:

```
32x32
64x32
512x256
512x512
1024x1024
```

{{< hint warning >}}
**📔 Note**: Although textures of arbitrary sizes sometimes work, they are also often rendered with bugs and are more unstable. We strongly advise that all your textures match these sizes.
{{< /hint >}}

## World Size

Decentraland [Worlds]({{< ref "/content/creator/worlds/about.md" >}}) have different limitations, since they are loaded as single scenes.

- Worlds published to Decentraland NAMEs have at least `100 MB`. That number can be increased by owning additional NAMEs, LAND, and MANA on that same account.

- Worlds published to ENS domains have a limit of `25MB` that cannot be expanded.

See [Worlds Size Limit]({{< ref "/content/creator/worlds/about.md#worlds-size-limit" >}}) for more details.

Total size of the files uploaded to the content server. Includes 3D models and audio. Doesn't include files that aren't uploaded, such as node.js packages. You can see the full list of files being published and their sizes before you confirm a deployment.

All other limits in worlds are per parcel, including triangles, materials, etc.
Since adding more parcels to a world is free, you can add up to 45x45 parcels to your scene, and have the corresponding limits to that parcel count.

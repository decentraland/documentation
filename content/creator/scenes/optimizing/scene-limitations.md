---
date: 2018-01-06
title: Scene limitations
description: How many things can I put on my scene?
aliases:
  - /documentation/scene-limitations/
  - /builder/scene-limitations/
  - /development-guide/scene-limitations/
  - /creator/builder/scene-limitations
categories:
  - development-guide
type: Document
url: /creator/development-guide/scene-limitations
weight: 2
---

In order to improve performance in the metaverse, we have established a set of limits that every scene must follow. If a
scene exceeds these limitations, then the parcel won't be loaded and the preview will display an error message.

For a straight-forward reference of what limitations you'll have for a specific number of parcels, check the following table:

[Reference table](https://docs.google.com/spreadsheets/d/1BTm0C20PqdQDAN7vOQ6FpnkVncPecJt-EwTSNHzrsmg/edit#gid=0)

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

- **File size:** `15 MB per parcel - 300 MB max` Total size of the files uploaded to the content server. Includes 3D models and audio. Doesn't include files that aren't uploaded, such as node.js packages.

- **File count:** `200 files per parcel` Total count of the files uploaded. Includes 3D models and audio. Doesn't include files that aren't uploaded, such as node.js packages.

- **Max file size** `50 MB per file` No individual file of any type in the scene can exceed 50 MB, no matter how many parcels the scene has.

## Optimizing

See [Performance Optimization]({{< ref "/content/creator/scenes/optimizing/performance-optimization.md" >}}) for tips about how you can keep your scene below these limits and make it run smoother for players.


<!--

## Query scene limitations via code

From a scene's code, you can query both the limitations that apply to the scene and how much the scene is currently using. This is especially useful with scenes where the content changes dynamically. For example, in a scene where you add a new entity each time the player clicks, you could stop adding entities when you reach the scene limits.

To use this functionality, you must first import `EntityController` into your scene.

```ts
import { querySceneLimits } from "@decentraland/EntityController"
```

#### Obtain scene limitations

Run `this.entityController.querySceneLimits()` to obtain the limits of your scene. The limits are calculated for your scene based on how many parcels it occupies, according to the _scene.json_ file. The values returned by this command don't change over time, as the scene's size is always the same.

The `querySceneLimits()` is [asynchronous]({{< ref "/content/creator/scenes/programming-patterns/async-functions.md" >}}), so we recommend calling it using the `executeTask()` function, including an `await` statement.

```ts
executeTask(async () => {
  try {
    const limits = await querySceneLimits()
    log('limits' + limits)
  }
})
```

The `querySceneLimits()` function returns a promise of an object with the following properties, all of type _number_.


```ts
// import controller
import { querySceneLimits } from '@decentraland/EntityController'


// get limits object
executeTask(async () => {
  try {
    const limits = await querySceneLimits()

    // print maximum triangles
    log(limits.triangles)

    // print maximum entities
    log(limits.entities)

    // print maximum bodies
    log(limits.bodies)

    // print maximum materials
    log(limits.materials)

    // print maximum textures
    log(limits.textures)
  }
}
```


For example, if your scene has only one parcel, logging `limits.triangles` should print `10000`.

#### Obtain the current use

Just as you can check via code the maximum allowed values for your scene, you can also check how much of that is currently used by the scene. You do this by running `this.querySceneMetrics()`. The values returned by this command change over time as your scene renders different content.

The `querySceneMetrics()` is asynchronous, so we recommend calling it using the `executeTask()` function, including an `await` statement.

```ts
executeTask(async () => {
  try {
    const limits = await querySceneMetrics()
    log('limits' + limits)
  }
})
```

The `querySceneMetrics()` function returns a promise of an object with the following properties, all of type _number_.


```ts
// import controller
import { querySceneMetrics } from '@decentraland/EntityController'


// get limits object
executeTask(async () => {
  try {
    const limits = await querySceneMetrics()

    // print maximum triangles
    log(limits.triangles)

    // print maximum entities
    log(limits.entities)

    // print maximum bodies
    log(limits.bodies)

    // print maximum materials
    log(limits.materials)

    // print maximum textures
    log(limits.textures)
  }
}
```

For example, if your scene is only rendering one box entity at the time, logging `limits.entities` should print `1`.

-->

## Scene boundaries

When running a preview, any content that is located outside the parcel boundaries is highlighted in red when rendered. If any content is outside these boundaries, you won't be allowed to deploy this scene to Decentraland.

If the tip of a large object leaves the boundaries, this object is considered out of bounds too.

A single parcel scene measures 16 meters x 16 meters. If the scene has multiple parcels, the dimensions vary depending on the arrangement of the parcels.

It's possible to position entities underground, to either hide them or to have only a portion of them emerge. A scene can't have tunnels that go below the default ground height, players can't travel below the `y = 0` height. 

## Shader limitations

3D models used in decentraland must use supported shaders and materials. See [3D model materials]({{< ref "/content/creator/3d-modeling/materials.md" >}}) for a list of supported shaders.

## Lighting

The scene's lighting conditions can't be changed from the default setting.

## Texture size constraints

Texture sizes must use width and height numbers (in pixels) that match the following numbers:

```
1, 2, 4, 8, 16, 32, 64, 128, 256, 512
```

> This sequence is made up of powers of two: `f(x) = 2 ^ x` . 512 is the maximum number we allow for a texture size. This is a fairly common requirement among other rendering engines, it's there due internal optimizations of the graphics processors.

The width and height don't need to have the same number, but they both need to belong to this sequence.

**The recommended size for textures is 512x512**, we have found this to be the optimal size to be transported through domestic networks and to provide reasonable loading/quality experiences.

Examples of other valid sizes:

```
32x32
64x32
512x256
512x512
```

{{< hint warning >}}
**📔 Note**   Although textures of arbitrary sizes sometimes work, they are also often rendered with bugs and are more unstable. We strongly advise that all your textures match these sizes.
{{< /hint >}}

<!--
## File amount limitations

When deploying your scene, you can't upload more than 100 files to IPFS, as having too many files in a scene will make it take too long to load in the client.

If you have more than 100 files in your scene folder, it's likely that many of those files aren't being used directly when loading the scene. You can make the CLI ignore specific files from the scene folder and not upload them to IPFS by specifying them in the _dclignore_ file for the scene. Learn more about it in [Scene files]({{< ref "/content/creator/scenes/projects/scene-files.md" >}}).
-->

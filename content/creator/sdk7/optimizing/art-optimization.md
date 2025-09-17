---
date: 2021-01-11
title: Art optimization
description: Optimize your scene's art to load fast and run smoothly for all players.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/art-optimization/
weight: 1
---

There are several aspects you can optimize in your scenes' art to ensure the best possible experience for players who visit them. This document covers some best practices when building 3D models, textures, and other art assets that can make a big difference in how fast your scene loads and how smoothly it runs for players.

See [Code optimization]({{< ref "/content/creator/sdk7/optimizing/performance-optimization.md" >}}) for more information on how to optimize your scene's code.

Keep in mind that many players may be visiting Decentraland using hardware that is not built for gaming, and via the browser, which limits how much of the hardware's processing power is available to use. The experience of visiting your scene should be smooth for everyone.

The Decentraland explorer enforces many optimizations at engine level. These optimizations make a big difference, but the challenge of rendering multiple user-generated experiences simultaneously is a big one. We need your help to make things run smoothly.

## Monitor Performance

The best metric to know how well a scene is performing is the FPS (Frames Per Second). When running a scene in preview, open the debug panel to see it. You should aim to always have 30 FPS or more.

To see the current FPS (Frames Per Second) of the explorer

1) Open the debug panel, on the top-right corner of the screen.

<img src="/images/debug-panel.png" width="100" />

2) Check  Average FPS in the **PERFORMANCE** tab.

<img src="/images/FPS.png" width="300" />

Check this value periodically, as it may vary over time depending on what you're doing in your scene.

Keep in mind that the performance you experience in preview may differ from that in production:

- Surrounding neighboring scenes might have a negative impact
- If multiple players are in the scene, rendering all their avatars can have a negative impact on the FPS
- The compression of the scenes' 3D models into asset bundles can have a positive impact
- Some players visiting your scene may be running on less powerful hardware

It's always a good practice to try deploying your scene first to the [test environment]({{< ref "/content/creator/sdk7/publishing/publishing.md#the-test-server">}}) to do some more thorough testing.

Always ask players for feedback. Never take for granted that how you experience the scene is the same for everyone else.


## Keep an eye on metrics

When working with the [Creator Hub]({{< ref "/content/creator/scene-editor/editor-installation.md" >}}), you can see stats about the resources used by 3D models in your scene, and if they pass any of the [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}).

<img src="/images/triangle-limit1.png" width="250" />

You can expand this menu to view details.

<img src="/images/triangle-limit2.png" width="300" />

Here are some tips for improving on these metrics:

## Transparent materials

Transparent materials are always more expensive in terms of performance than opaque materials. Avoid using blended transparencies. Blended transparencies have to bypass quite a few of the rendering optimizations. If possible, favor opaque or alpha tested geometry. See [Alpha materials]({{< ref "/content/creator/3d-modeling/materials.md#Alpha" >}}) and [Transparent Maps]({{< ref "/content/creator/3d-modeling/textures.md#Transparent-Maps" >}}) for more details.

## Merging meshes

Merging meshes is a great way to reduce the number of draw calls and improve performance. Instead of executing one draw call per mesh, you can merge them into a single draw call.

This however is not always ideal in cases where the meshes might not all be visible at the same time. If the meshes are separate, the engine is able to cull the ones that are not visible. See [Meshes on large scenes]({{< ref "/content/creator/3d-modeling/meshes.md#Meshes-on-large-scenes" >}}) for more details.

## Face Culling

Face culling is a great way to improve performance. It allows the engine to skip rendering the faces that are not visible. Only untoggle **backface culling** in your models if you need a model to be renderer in both sides (for example, a group of leafs of a tree made by 3D planes).

## Texture atlases

Texture atlases are a great way to reduce the number of textures in your scene. It allows you to share the same texture across multiple models. See [Shared textures betewen GlTF models]({{< ref "/content/creator/3d-modeling/textures.md#Shared-textures-betewen-GlTFs-models" >}}) for more details.

You could even use a single texture as an atlas map, shared across all models in the scene. It's better to have 1 large shared texture of 1024x1024 pixels instead of several small ones.

{{< hint warning >}}
**📔 Note**: Avoid using the same image file for both the albedo texture and the normal map or the emissive map of a material. Use separate files, even if identical. Assigning a same image file to different types of texture properties may introduce unwanted visual artifacts when compressed to asset bundles.
{{< /hint >}}


## Other Best practices


- _.glb_ is a compressed format, it will always weigh less than a _.gltf_. On the other hand, with _.gltf_ it's easy to share texture images by exporting textures as a separate file. You can have the best of both worlds by using the [following pipeline](https://github.com/AnalyticalGraphicsInc/gltf-pipeline), that allows you to have _.glb_ models with external texture files.

- Avoid skinned meshes. They can drag down the performance significantly.

{{< hint info >}}
**💡 Tip**: Read more on 3D model best practices in the [3D Modeling Section](/creator/3d-modeling/3d-models
{{< /hint >}}

## Asset Bundle conversion

After your scene is deployed, the Decentraland content servers run a process to compress every _.gltf_ and _.glb_ model in your scene to asset bundle format. This format is _significantly_ lighter, making scenes a lot faster to load and smoother to run on the browser. This proces is carried out automatically, so you don't need to do anything to trigger it, the process may typically take 15 minutes or more.

{{< hint warning >}}
**📔 Note**: If you make _any_ change to a 3D model file, even if just a name change, it will be considered a new file, and must be converted to asset bundle format again.

When planning an event in Decentraland, make sure you deploy your scene several hours in advance, so that the models are all converted to asset bundles by then.
{{< /hint >}}
---
date: 2024-07-25
title: Import custom items
description: Import your own 3D models and smart items to use in your scenes.
categories:
  - scene-editor
type: Document
url: /creator/editor/import-items
aliases:
  - /builder/import-items/
---

You can import your own 3D models into the Scene Editor. Pick models from a wide selection of free or paid sources on the internet, or to create your own custom models.

## Import an asset

To import a 3D model, an image, a sound file, or a video into your scene from your local disk:

1. Click the **+\*** icon on the top-right of the **Local Assets** screen.

2. Drag the file or files onto the window. You can also click the upload icon to open a file browser window.

3. Check the model thumbnail and click **Import**.

  <img src="/images/editor/import-model.png" width="500" />

You can now find your asset in the **Local Assets** tab, under the **scene** folder.

- For 3D models, drag the `.glb` or `.gltf` files onto the canvas to add them as items on your scene.

- Other kinds of assets like images and sound files can be dragged onto the fields of an item.

## Supported models

All 3D models need to be in _.glTF_ or _.glb_ format. You can convert other formats into these formats with various different editors and tools. See [3D modeling]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}) for recommendations and tips.

All materials in the models need to be either _basic material_ or _PBR_, and all textures need to be in sizes that are powers of two (ex: 256, 512). See [Scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}) for details.

All 3D model files must each occupy less than 50 MB to be usable in a scene. Larger files aren't supported.

#### Free libraries for 3D models

Instead of building your own 3D models, you can also download them from several free or paid libraries.

To get you started, below is a list of libraries that have free or relatively inexpensive content:

- [SketchFab](https://sketchfab.com/)
- [Clara.io](https://clara.io/)
- [Archive3D](https://archive3d.net/)
- [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/)
- [Thingiverse](https://www.thingiverse.com/) (3D models made primarily for 3D printing, but adaptable to Virtual Worlds)
- [ShareCG](https://www.sharecg.com/)

{{< hint warning >}}
**📔 Note**: Pay attention to the license restrictions that the content you download has.
{{< /hint >}}

You can also use Generative AI tools to generate your own 3D models. Check out:

- [Meshy](https://www.meshy.ai/)
- [Luma AI](https://lumalabs.ai/genie)
- [TRipo3D](https://www.tripo3d.ai/app)

Note that in several of these sites, you can choose what format to download the model in. Always choose _.glTF_ format if available. If not available, you must convert them to _.glTF_ before you can use them in a scene. For that, we recommend importing them into Blender and exporting them with one of the available _.glTF_ export add-ons.

## Colliders

You might find that when running a preview the player can walk through your imported 3D models. This is likely because the models are missing a _collider mesh_ to define a collision geometry. See [colliders]({{< ref "/content/creator/3d-modeling/colliders.md" >}}) for more details and instructions.

{{< hint info >}}
**💡 Tip**: Instead of editing the model to add a _collider mesh_, a simpler alternative is to add an _Invisible wall_ smart item with approximately the same shape to stand in its place.
{{< /hint >}}

## Animations

If an imported model includes animations, the first animation that's packed into the model will be played in a loop.

Note that you don't have any control over when the animation starts or stops, or which one is played in case of several animations.

If there are multiple players in the scene, they may be seeing the animation out of sync from each other.

To change this behavior, you can include an **Animator** component.

<!-- TODO: explain animator, maybe create whole doc about adding components? -->

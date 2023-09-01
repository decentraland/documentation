---
date: 2023-8-30
title: 3D Model Essentials
description: Learn what assets and components are supported in external 3D models and how to configure them before importing them to Decentraland.
aliases:
  - /sdk-reference/external-3d-models/
  - /development-guide/external-3d-models/
  - /3d-modeling/3d-models/
categories:
  - 3d-modeling
type: Document
url: /creator/3d-modeling/3d-models
weight: 1
---

<img src="/images/3d-models-and-animations/3d-essentials/01-3d-essentials-banner.png" width="600" />

When importing 3D models into Decentraland, it's important to make sure they're in either glTF format. These models can include a variety of supported features. This section is all about how to make them compatible with Decentraland and following best practices.

Please note that all models, shaders, and textures must comply with the **[scene limitations](https://docs.decentraland.org/creator/development-guide/scene-limitations/)**.

# **Supported 3D Model Formats**

All 3D models in Decentraland must be in glTF format. **[glTF](https://www.khronos.org/gltf)** (GL Transmission Format) is an open project by Khronos providing a common, extensible format for 3D assets that is both efficient and highly interoperable with modern web technologies.

glTF models can have either a *.gltf* or a *.glb* extension. glTF files are human-readable, you can open one in a text editor and read it like a JSON file. This is useful, for example, to verify that animations are properly attached and to check for their names. glb files are binary, so they’re not readable but they are considerably smaller in size, which is good for the scene’s performance.

We recommend using *.gltf* while you’re working on a scene, but then switching to *.glb* when uploading it.

The following aspects of a 3D model can either be embedded in a *glTF* file or referenced externally:

- Textures can either be embedded or referenced from an external image file.
- Binary data about geometry, animations, and other buffer-related aspects of the model can either be embedded or referenced from an external *.bin* file.

> **📔 Note**: Animations *must* be embedded inside the *glTF* file to use in Decentraland.

# **Why We Use glTF**

We use glTF because it provides a powerful set of features that includes:

- Hierarchical objects
- Skeletal structure and animation
- Robust pipeline for materials and shaders
- Scene information such light sources and cameras (which can be used in future developments).

Compared to *COLLADA*, the supported features are very similar. However, because glTF focuses on providing a “transmission format” rather than an editor format, it is more interoperable with web technologies.

# **Export And Convert glTF**

## **Export To glTF From Blender**

Blender has a native gltf exporter.

To export select the models you want to be contained on the .glb file then go to File - Export - glTF 2.0

<img src="/images/3d-models-and-animations/3d-essentials/02-export-glt-from-blender.png" width="400" /> <img src="/images/3d-models-and-animations/3d-essentials/03-exporting-options.png" width="200" />

_On the side panel check “Selected Objects” in case you want to export only the selected objects in the scene. Also, on the Mesh Dropdown select Apply Modifiers (if they were), then Export._

#### **Export To glTF From 3D Studio Max**

3D Studio Max doesn't support exporting to glTF by default, but you can install a plugin to enable it.

1. Download the plugin from [this link](https://github.com/BabylonJS/Exporters/tree/master/3ds%20Max).
2. Install the plugin by following [these instructions](http://doc.babylonjs.com/resources/3dsmax#how-to-install-the-3ds-max-plugin).
3. Export glTF files using the plugin by following [these instructions](http://doc.babylonjs.com/resources/3dsmax_to_gltf).

#### **Export To glTF From Maya**

Maya doesn't support exporting to glTF by default, but you can install a plugin to enable it.

1. Install the plugin by following [these instructions](http://doc.babylonjs.com/resources/maya).
2. Export glTF files using the plugin by following [these instructions](http://doc.babylonjs.com/resources/maya_to_gltf#pbr-materials).

{{< hint warning >}}
**📔 Note**: As an alternative, you can try [this other plugin](https://github.com/WonderMediaProductions/Maya2glTF) too.
{{< /hint >}}

#### **Export To glTF From Unity**

Unity doesn't support exporting to glTF by default, but you can install a plugin to enable it.

Download the plugin from [this link](https://github.com/sketchfab/Unity-glTF-Exporter).

{{< hint warning >}}
**📔 Note**: As an alternative, you can try [this other plugin](https://assetstore.unity.com/packages/tools/utilities/collada-exporter-for-unity2017-99793) too.
{{< /hint >}}

#### **Export To glTF From SketchUp**

SketchUp doesn't support exporting to glTF by default, but you can install a plugin to enable it.

Download the plugin from [this link](https://extensions.sketchup.com/en/content/gltf-exporter).

#### **Convert FBX Into glTF**

*.fbx* is a very popular standard for 3D models. It’s not supported by our engine, but you can easily export an *.fbx* model to *.gltf* format.

We recommend using these tools:

- **[Blender](https://www.blender.org/download/)**: An easy way to convert .fbx to glTF is by importing the .fbx to a scene using Blender and then export it from there.
- **[Facebook’s CLI tool](https://github.com/facebookincubator/FBX2glTF)**: this is the most robust alternative, but requires using the command line.
- **[Blackthread](https://blackthread.io/gltf-converter)**: This the most complete web based tool. Less robust than the CLI, but a lot easier to use.
- **[Modelconverter](https://modelconverter.com/convert.html)**: Another easy-to-use web based tool.

# **Preview a glTF Model**

A quick and easy way to preview the contents of a glTF model before importing it into a scene is to use the **[Babylon.js Sandbox](https://sandbox.babylonjs.com/)**. Just drag and drop the glTF file (and its *.bin* file if applicable) into the canvas to view the model.

In the sandbox you can also preview the animations that are embedded in the model, select which to display by picking it out of a dropdown menu.

<img src="/images/3d-models-and-animations/3d-essentials/04-preview-gltf.png" width="600" />

## **Analyse glTF**

One great tool to analyze your glTFs is using **[glTF Sample Viewer](https://github.khronos.org/glTF-Sample-Viewer-Release/)**. This tool allows you to inspect channels, textures, reaction to different light environments, preview animations and so much more! Ideal for single models.

<img src="/images/3d-models-and-animations/3d-essentials/05-gltf-sample-viewer.png" width="600" />

Another helpful tool is **[gltf.report/](https://gltf.report/)**. Simply drag and drop your models onto the website to view the contents of the glTF package and assess which parts of the model can be optimized.

This tool can be especially useful for large files containing multiple models, textures, and animations. For instance, by organizing textures by size, you can easily identify which textures are using up the most resources.

<img src="/images/3d-models-and-animations/3d-essentials/05-gltf-report.png" width="600" />

# **Optimize a glTF**

The following tool offers some optimizations that will make 3D models lighter and faster to download for players in your scene.

[glTF pipeline](https://github.com/AnalyticalGraphicsInc/gltf-pipeline)

Among other things, it converts _.gltf_ format into _.glb_, which is binary and so occupies a lot less. It also places texture files outside the 3D model, which allows you to use the same texture on multiple models.

{{< hint warning >}}
**📔 Note**: _.glb_ format by default always has textures embedded in the file. The engine can't recognize two embedded textures as the same, they need to be external files that share a same hash.
{{< /hint >}}

## See also

The following pages also cover topics related to 3D models for Decentraland:

- [Meshes]({{< ref "/content/creator/3d-modeling/meshes.md" >}})
- [Materials]({{< ref "/content/creator/3d-modeling/materials.md" >}})
- [Textures]({{< ref "/content/creator/3d-modeling/textures.md" >}})
- [Colliders]({{< ref "/content/creator/3d-modeling/colliders.md" >}})
- [Animations]({{< ref "/content/creator/3d-modeling/animations.md" >}})

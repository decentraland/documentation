---
date: 2018-02-11
title: Files in a scene
description: Default files created in a new scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/scene-files/
weight: 2
---

After [creating a new scene]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}) using the CLI, the scene folder will have a series of files with default content.

## Default files in a local scene

Scenes include the following files:

- **src/index.ts**: The entry point of the scene.
- **scene.json**: The manifest that contains metadata for the scene.
- **package.json** and **package-lock.json**: Specify the versions of all dependencies of the scene.
- **tsconfig.json**: Typescript configuration file.
- **.dclignore**: Lists what files in your project not to deploy to IPFS.

### index.ts

This is the entry point to your scene's code. You could fit your entire scene's logic into this file, although for clarity in most cases we recommend spreading out your code over several other _.ts_ files.

In most cases, you'll only need to edit this and other .ts files to create your scene. It contains the code that generates the [entities, components]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}) and [systems]({{< ref "/content/creator/sdk7/architecture/systems.md" >}}) of your scene.

When running the scene, the contents of your `.ts` files are compiled to a single minified `.js` file, `bin/scene.js`.

{{< hint warning >}}
**📔 Note**: You can use another tool or language instead of TypeScript, so long as your scripts are contained within a single Javascript file (bin/scene.js). All provided type declarations are made in TypeScript, and other languages and transpilers are not officially supported.
{{< /hint >}}

### scene.json

The _scene.json_ file is a JSON formatted manifest for a scene in the world. A scene can span a single or multiple LAND parcels. The _scene.json_ manifest describes what objects exist in the scene, a list of any assets needed to render it, contact information for the parcel owner, and security settings.

For more information see [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#metadata">}}). You can also read the original [specification proposal](https://github.com/decentraland/proposals/blob/master/dsp/0020.mediawiki) for this metadata.

All of this metadata is optional for previewing the scene locally, but part of it is needed for deploying. You can change this information manually at any time.

### package.json

This file provides information to NPM that allows it to identify the project, as well as handle the project's dependencies. Decentraland scenes require one main package:

- **@dcl/sdk**: The fundamental dependency of the Decentraland SDK, including definitions and types for the engine, components, systems, etc.
- **@dcl/js-runtime**: A series of type declarations that makes the integration of @dcl/sdk smoother.

Your scene may include any number of other packages, for example to include [libraries](https://studios.decentraland.org/resources?sdk_version=SDK7&resource_type=Library) that can help make the writing of code easier, or enable special functionalities.

### package-lock.json

This file lists the versions of all the other dependencies of the project. These versions are locked, meaning that the compiler will use literally the same minor release listed here.

You can change any package version manually by editing this file.

#### tsconfig.json

Directories containing a _tsconfig.json_ file are root directories for TypeScript Projects. The _tsconfig.json_ file specifies the root files and options required to compile your project from TypeScript into JavaScript.

When installing any additional libraries to your scene, an entry should be added automatically to this file. For installing Decentraland utils libraries, it shouldn't be necessary to manually do any changes to this file.

## Recommended file locations

Keep in mind that when you deploy your scene to Decentraland, any assets or external libraries that are needed to use your scene must be either packaged inside the scene folder or available via a remote server.

Anything that is meant to run in the player's client must located inside the scene folder. You shouldn't reference files or libraries that are installed elsewhere in your local machine, because they won't be available to the deployed scene.

We suggest using these folder names consistently for storing the different types of assets that your scene might need:

- 3D models: `/models`
- Videos: `/videos`
- Sound files: `/sounds`
- Image files for textures (except for glTF models): `/materials`
- _.ts_ definitions for components `/src/components`
- _.ts_ definitions for systems `/src/systems`

{{< hint warning >}}
**📔 Note**: Supporting files for glTF models, like their texture image files or _.bin_ files, should always be placed in the same folder as the model's _.gltf_ or _.glb_ file.
{{< /hint >}}

{{< hint warning >}}
**📔 Note**: We recommend using always lower case names for all folders and file names, to avoid possible issues.
{{< /hint >}}

## The dclignore file

All scenes include a _.dclignore_ file, this file specifies what files in the scene folder to ignore when deploying a scene to Decentraland.

For example, you might like to keep the Blender files for the 3D models in your scene inside the scene folder, but you want to prevent those files from being deployed to Decentraland. In that case, you could add `*.blend` to _.dclignore_ to ignore all files with that extension.

| What to ignore | Example     | Description                                                                             |
| -------------- | ----------- | --------------------------------------------------------------------------------------- |
| Specific files | `BACKUP.ts` | Ignores a specific file                                                                 |
| Folders        | `drafts/`   | Ignores entire contents of a folder and its subfolders                                  |
| Extensions     | `*.blend`   | Ignores all files with a given extension                                                |
| Name sections  | `test*`     | Ignores all files with names that match the query. In this case, that start with _test_ |

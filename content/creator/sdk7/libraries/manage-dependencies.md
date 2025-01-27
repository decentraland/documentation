---
date: 2022-11-08
title: Manage dependencies
description: How to add libraries to a scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/libraries/manage-dependencies
weight: 2
---

A lot of times, your scene might need functionality that is already encapsulated in a reusable library. Using external libraries can make your work a lot easier.

You can import external libraries into a Decentraland project and then reference the systems, components, or functions described in these libraries.

Check the [Examples page](https://studios.decentraland.org/resources?sdk_version=SDK7&resource_type=Library) to find a series of libraries, both created by the Decentraland Foundation and by community members, that solve common problems.

<!-- TODO: in the future on the Creator hub -->

## On the VS Code extension

{{< hint warning >}}
**📔 Note**: The Decentraland Visual Studio Code Extension is deprecated. We encourage you to use the [Creator Hub]({{< ref "/content/creator/scene-editor/about-editor.md" >}}) together with Visual Studio Code without the extension.
{{< /hint >}}

### Install a dependency

Make sure you've [installed the VS Code Extension]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#vs-code-extension" >}}).

1. Open your scene's folder using Visual Studio Code.

{{< hint warning >}}
**📔 Note**: The Visual Studio window must be at the root folder of the scene project.
{{< /hint >}}

2. Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

3. Click the `+` icon on the header of the **Dependencies** view.

4. Visual Studio opens an input box at the top of the screen. Provide the name of the dependency you wish to install and hit enter. The dependency is then installed to your scene. For example `@dcl-sdk/utils`.

{{< hint warning >}}
**📔 Note**: If you wish to install a specific version of a dependency (and not the default latest version), you can specify this as part of the name with an `@` at the end. For example `@dcl-sdk/utils@1.0.4`.
{{< /hint >}}

### Update a dependency

Click the refresh icon on the header of the **Dependencies** section. All dependencies on the scene are updated to the versions indicated on your scene's `package.json` file. If dependencies point to the `@latest` version, then this action installs the current latest stable release.

If a dependency in your scene's `package.json` points to a specific version number, then you need to either:

- Reinstall as a new dependency, clicking the plus sign and specifying the library name with `@latest` at the end. For example `@dcl-sdk/utils@latest`.

- Manually change the `package.json` file so that the dependency version points to `@latest`. Then click the update icon again.

### Remove a dependency

Hover over a dependency to see a trash icon. Press this icon to remove an unused dependency from the scene.

You can also click the `-` icon on the header of the **Dependencies** section, and then write the name of the dependency you wish to delete.

## Via the CLI

### Install

To install a library in your project folder, run `npm i` and the library name in your project's root path. For example:

`npm i @dcl-sdk/utils`

{{< hint warning >}}
**📔 Note**: You may need to run `npm run start` or `npm run build` after installing the library for the library's dependencies to get installed.
{{< /hint >}}

### Update

If your `package.json` file lists the version of the scene as `@latest`, then run `npm i` to update all libraries to their corresponding latest versions.

If your `package.json` references a specific version number, you can update it by running the command to install the library, adding `@` and the version number in the end. For example:

`npm i @dcl-sdk/utils@1.7.5`

### Uninstall

To delete a library from your scene's dependencies run `npm rm` and the library name. For example:

`npm rm @dcl-sdk/utils`

It's a good practice to remove any libraries that you're not using. Unused libraries still occupy space in the scene, affecting the player's experience of downloading and running your scene.

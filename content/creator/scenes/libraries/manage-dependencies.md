---
date: 2022-11-08
title: Manage dependencies
description: How to add libraries to a scene
categories:
  - development-guide
type: Document
aliases:
  - /creator/editor/manage-dependencies
  - /creator/development-guide/manage-dependencies
  - /creator/development-guide/libraries/manage-dependencies
url: /creator/development-guide/scene/libraries/manage-dependencies
weight: 1
---

A lot of times, your scene might need functionality that is already encapsulated in a reusable library. Using external libraries can make your work a lot easier.

You can import external libraries into a Decentraland project and then reference the systems, components, or functions described in these libraries.

{{< hint warning >}}
**📔 Note**:  Not all Typescript or Javascript dependencies are supported in Decentraland projects. Libraries should be tagged with `decentralandLibrary` in their `package.json`.
{{< /hint >}}

Check the [Awesome repository](https://github.com/decentraland-scenes/Awesome-Repository#libraries) to find a series of libraries, both created by the Decentraland Foundation and by community members, that solve common problems.



## Via the Editor


### Install a dependency

Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/scenes/getting-started/installation-guide.md#the-decentraland-editor" >}}).

1) Open your scene's folder using Visual Studio Code. 

{{< hint warning >}}
**📔 Note**:  The Visual Studio window must be at the root folder of the scene project.
{{< /hint >}}

2) Open the Decentraland Editor tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

3) Click the `+` icon on the header of the **Dependencies** view.

4) Visual Studio opens an input box at the top of the screen. Provide the name of the dependency you wish to install and hit enter. The dependency is then installed to your scene. For example `react`.

{{< hint warning >}}
**📔 Note**:  If you wish to install a specific version of a dependency (and not the default latest version), you can specify this as part of the name with an `@` at the end. For example `@dcl/ecs-scene-utils@1.7.5`.
{{< /hint >}}

5) If it is a Decentraland library (ie. `decentraland-ecs-utils`) select `Yes`, otherwise `No`.

### Update a dependency

Click the refresh icon on the header of the **Dependencies** section. All dependencies on the scene are updated to the versions indicated on your scene's `package.json` file. If dependencies point to the `@latest` version, then this action installs the current latest stable release. 

If a dependency in your scene's `package.json` points to a specific version number, then you need to either:

- Reinstall as a new dependency, clicking the plus sign and specifying the library name with `@latest` at the end. For example `@dcl/ecs-scene-utils@latest`.

- Manually change the `package.json` file so that the dependency version points to `@latest`. Then click the update icon again.

### Remove a dependency

Hover over a dependency to see a trash icon. Press this icon to remove an unused dependency from the scene.

You can also click the `-` icon on the header of the **Dependencies** section, and then write the name of the dependency you wish to delete.


## Via the CLI

### Install

To install a library in your project folder, run `npm i` and the library name in your project's root path. If the library is a Decentraland library, add `-B` at the end, to install it like a bundled dependency. For example:

`npm i @dcl/ecs-scene-utils -B`

{{< hint warning >}}
**📔 Note**:  You may need to run `dcl start` or `dcl build` after installing the library for the library's dependencies to get installed.
{{< /hint >}}

### Update

If your `package.json` file lists the version of the scene as `@latest`, then run `npm i` to update all libraries to their corresponding latest versions.

If your `package.json` references a specific version number, you can update it by running the command to install the library, adding `@` and the version number in the end. For example:

`npm i @dcl/ecs-scene-utils@1.7.5 -B`

### Uninstall

To delete a library from your scene's dependencies run `npm rm` and the library name. For example:

`npm rm @dcl/ecs-scene-utils`

It's a good practice to remove any libraries that you're not using. Unused libraries still occupy space in the scene, affecting the player's experience of downloading and running your scene.

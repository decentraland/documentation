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

{{< hint danger >}}
**❗Warning**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md" >}}).
{{< /hint >}}

A lot of times, your scene might need functionality that is already encapsulated in a reusable library. Using external libraries can make your work a lot easier.

You can import external libraries into a Decentraland project and then reference the systems, components, or functions described in these libraries.

{{< hint warning >}}
**📔 Note**: Not all Typescript or Javascript dependencies are supported in Decentraland projects. Libraries should be tagged with `decentralandLibrary` in their `package.json`.
{{< /hint >}}

Check the [Awesome repository](https://github.com/decentraland-scenes/Awesome-Repository#libraries) to find a series of libraries, both created by the Decentraland Foundation and by community members, that solve common problems.

## Install

To install a library in your project folder, run `npm i` and the library name in your project's root path. If the library is a Decentraland library, add `-B` at the end, to install it like a bundled dependency. For example:

`npm i @dcl/ecs-scene-utils -B`

{{< hint warning >}}
**📔 Note**: You may need to run `dcl start` or `dcl build` after installing the library for the library's dependencies to get installed.
{{< /hint >}}

## Update

If your `package.json` file lists the version of the scene as `@latest`, then run `npm i` to update all libraries to their corresponding latest versions.

If your `package.json` references a specific version number, you can update it by running the command to install the library, adding `@` and the version number in the end. For example:

`npm i @dcl/ecs-scene-utils@1.7.5 -B`

## Uninstall

To delete a library from your scene's dependencies run `npm rm` and the library name. For example:

`npm rm @dcl/ecs-scene-utils`

It's a good practice to remove any libraries that you're not using. Unused libraries still occupy space in the scene, affecting the player's experience of downloading and running your scene.

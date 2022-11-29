---
date: 2022-10-25
title: Manage-dependencies
description: How to install and manage project dependencies via the Decentraland Editor
categories:
  - editor
type: Document
url: /creator/editor/manage-dependencies
weight: 10
---


A lot of times, your scene might need functionality that is already encapsulated in a reusable library. Using external libraries can make your work a lot easier.

You can import external libraries into a Decentraland project and then reference the systems, components, or functions described in these libraries.

Check the [Awesome repository](https://github.com/decentraland-scenes/Awesome-Repository#libraries) to find a series of libraries, both created by the Decentraland Foundation and by community members, that solve common problems.


### Install a dependency


Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/editor/installation-guide.md" >}}).

1) Open your scene's folder using Visual Studio Code. 

> Note: The Visual Studio window must be at the root folder of the scene project.

2) Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

3) Click the plus sign on the header of the **Dependencies** section.

4) Visual Studio opens an input box at the top of the screen. Provide the name of the dependency you wish to install and hit enter. The dependency is then installed to your scene.

> Note: If you wish to install a specific version of a dependency (and not the default latest version), you can specify this as part of the name with an `@` at the end. For example `@dcl/ecs-scene-utils@1.7.5`.

### Update a dependency

Click the refresh icon on the header of the **Dependencies** section. All dependencies on the scene are updated to the versions indicated on your scene's `package.json` file. If dependencies point to the `@latest` version, then this action installs the current latest stable release. 

If a dependency in your scene's `package.json` points to a specific version number, then you need to either:

- Reinstall as a new dependency, clicking the plus sign and specifying the library name with `@latest` at the end. For example `@dcl/ecs-scene-utils@latest`.

- Manually change the `package.json` file so that the dependency version points to `@latest`. Then click the update icon again.

### Remove a dependency

Hover over a dependency to see a trash icon. Press this icon to remove an unused dependency from the scene.

You can also click the `-` icon on the header of the **Dependencies** section, and then write the name of the dependency you wish to delete.



---
date: 2022-11-08
title: Manage dependencies
description: How to add libraries to a scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/scene/libraries/manage-dependencies
weight: 1
---

TODO: Flesh out

What dependencies are


> Note: Not all Typescript or Javascript dependencies are supported

Link to awesome repo

## In the Editor

Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

### Install a dependency

1) Click the plus sign on the header of the **Dependencies** section.

2) Visual Studio opens an input box at the top of the screen. Provide the name of the dependency you wish to install and hit enter. The dependency is then installed to your scene.

> Note: If you wish to install a specific version of a dependency (and not the default latest version), you can specify this as part of the name with an `@` at the end. For example `@dcl/ecs-scene-utils@3.3.0`.

### Update a dependency

Click the refresh icon on the header of the **Dependencies** section. All dependencies on the scene are updated to the versions indicated on your scene's `package.json` file. If dependencies point to the `@latest` version, then this action installs the current latest stable release. 

If a dependency in your scene's `package.json` points to a specific version number, then you need to either:

- Reinstall as a new dependency, clicking the plus sign and specifying the library name with `@latest` at the end. For example `@dcl/ecs-scene-utils@latest`.

- Manually change the `package.json` file so that the dependency version points to `@latest`. Then click the update icon again.

### Remove a dependency

Hover over a dependency to see a trash icon. Press this icon to remove an unused dependency from the scene.

You can also click the `-` icon on the header of the **Dependencies** section, and then write the name of the dependency you wish to delete.

## Via the CLI

install

update

uninstall

decentraland dependencies

you might need to run the scene or run dcl build for the library's dependencies to be fully installed
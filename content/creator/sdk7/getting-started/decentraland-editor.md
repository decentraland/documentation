---
date: 2022-12-19
title: Decentraland Editor
description: About the Decentraland Editor
type: Document
aliases:
  - /creator/development-guide/editor/editor-beta-testing-guidelines/
  - /creator/development-guide/editor/
url: /creator/development-guide/sdk7/editor/
weight: 3
---

## Install the editor

See the [Installation guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#the-decentraland-editor" >}}).

{{< hint warning >}}
**📔 Note**: There are two versions of the editor, the **Decentraland Editor SDK6** and the **Decentraland Editor SDK7**. As their names suggest, each version of the editor is meant for working on Decentraland scenes built with different SDK versions. You can have both extensions installed in your same instance of Visual Studio Code, and use them accordingly depending on what project you're working with.
{{< /hint >}}

## About the Decentraland Editor

The Decentraland editor is an extension of Visual Studio Code, built for easing the experience of creating Decentraland scenes.

Ultimately the editor will offer many no-code options for placing items, and setting component parameters via graphical UIs. The first version of the editor aims for simplifying the experience of coding scenes by removing the command line from the list of tools you need to use. It offers UI options for:

- **Create projects**: Scaffold a new project of various types: scene, library, portable experience, and smart item. See [Create a project]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}).
- **Run scenes**: preview your scenes within VSCode, or launch in a browser. See [Run preview]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}).
- **Debug scenes**: Add breakpoints to the code, to pause execution and see current state of all variables at that point in time. See [Debug in preview]({{< ref "/content/creator/sdk7/debugging/debug-in-preview.md#add-breakpoints-in-the-decentraland-editor" >}}).
- **Publish scenes**: publish your scene to the world. See [Publishing]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}).
- **Manage dependencies**: add, remove, and list the libraries and dependencies that your project is using. See [Manage dependencies]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md" >}}).
- **Preview models**: Open a gltf or .glb model to see an interactive preview.
- **Drag and drop entities visually (Alpha)**: Use the **Visual Editor** view to drag and drop entities into place, and configure some of their components via UI.
- **Reference entities added visually in your code**: Entities that are added using the Visual Editor can then be referenced in your code to add interactivity to them. See [Get an entity by name]({{< ref "/content/creator/sdk7/architecture/entities-components.md#get-an-entity-by-name" >}}).

## Reporting issues

If you run into any bugs, please report an issue in the [Editor](https://github.com/decentraland/editor-sdk7) repository.

We ask you to please detail how to reproduce the issue as much as possible.

## Submit feedback

Once you've had a chance to try the new editor, please fill in the [feedback form](https://form.typeform.com/to/aODGpdoQ)

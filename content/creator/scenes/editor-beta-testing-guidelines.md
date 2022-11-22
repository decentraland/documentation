---
date: 2022-11-07
title: Editor Beta testing guidelines
description: Instructions to try out the Decentraland Editor
categories:
  - development-guide
type: Document
url: /creator/development-guide/scene/editor-beta-testing-guidelines/
weight: 2000
---


The Decentraland Editor is currently being tested as a beta release. We're gathering feedback from the community, to ensure the release doesn't present any major issues and that the experience of using it is good.

We encourage you to test and experiment with this editor as much as possible.

## Install the editor

See the [Installation guide]({{< ref "/content/creator/scenes/getting-started/installation-guide.md" >}}).

## About the Decentraland Editor

The Decentraland editor is an extension of Visual Studio Code, built for easing the experience of creating Decentraland scenes.

Ultimately the editor will offer many no-code options for placing items, and setting component parameters via graphical UIs. The first version of the editor aims for simplifying the experience of coding scenes by removing the command line from the list of tools you need to use. It offers UI options for:

- **Create projects**: Scaffold a new project of various types: scene, library, portable experience, and smart item. See [Quick start]({{< ref "/content/creator/scenes/getting-started/sdk-101.md" >}}).
- **Run scenes**: preview your scenes within VSCode, or launch in a browser. See [Run preiview]({{< ref "/content/creator/scenes/getting-started/preview-scene.md#using-the-editor" >}})
- **Debug scenes**: Add breakpoints to the code, to pause execution and see current state of all variables at that point in time. See [Debug in preview]({{< ref "/content/creator/scenes/debugging/debug-in-preview.md#using-the-editor" >}}).
- **Publish scenes**: publish your scene to the world. See [Publishing]({{< ref "/content/creator/scenes/publishing/publishing.md#via-the-editor" >}}).
- **Manage dependencies**: add, remove, and list the libraries and dependencies that your project is using. See [Manage dependencies]({{< ref "/content/creator/scenes/libraries/manage-dependencies.md" >}}).
- **Preview models**: Open a gltf or .glb model to see an interactive preview.

## Documentation

Find the full documentation for the Editor in this branch of the Documentation site. Navigate the tree under **scenes** to find information about every functionality of the editor.

Note that the contents of this document are in an [unpublished branch](https://editor.new-docs-6m4.pages.dev/creator/development-guide/scene/editor-beta-testing-guidelines/) of the Decentraland documentation.

## Test cases

**Walkthrough**

1. After installing the extension you should be taken to a Walkthrough to create a Decentraland scene.
2. Complete the 4 steps of the Walkthrough (5 steps if you open VSCode on an empty workspace).
3. Close VSCode and open it again, you should be in the "Get Started" screen. You should see the Walkthrough on the Walkthroughs section (if you already finished it, it will probably be under "More...").

**Create Project**

1. Open VSCode in an empty folder.
2. Click on the Decentraland icon on the left sidebar.
3. Click on `Create Project`.
4. Select the project type `Scene`.
5. Wait for scene to be created.

**Run Scene**

1. Open VSCode in a Decentraland scene project.
2. Click on the Decentraland icon on the left sidebar.
3. Click on `Run Scene`.
4. You should be able to interact with the scene in the webview within VSCode.
5. Click on the `Open in browser` button in the top right corner of the scene tab.
6. You should be able to interact with the scene in a newly opened browser.

**Debug Scene**

1. Open VSCode in a Decentraland scene project.
2. Click on the Debugger icon on the left sidebar.
3. Click on `Run and Debug` and select `Decentraland` (this step might not be necessary if you already have a `.vscode/launch.json` file).
4. Click on `Run`. A browser should open.
5. Try setting a breakpoint and interacting with the scene in a way it will step on that line. If you are using the rotating cube scene, try setting a breakpoint in the line `26` of the `game.ts` file (first line inside `spawnCube`). Then go to the scene and click on the rotating cube. The program should stop and you should be taken to the breakpoint you just set. You can see the values of the variables in the scope on the left (like `x`, `y` and `z` in the cube example). You can modify the values and resume execution with the blue play button.

**Publish Scene**

1. Open VSCode in a Decentraland scene project.
2. Edit the `scene.json` to set it on a parcel that you own or have permission to deploy.
3. Click on the Decentraland icon on the left sidebar.
4. Click on `Publish Scene` (if you have parcels in testnet, then instead click on the three dot menu at the top right of the sidebar, next to the green reload arrow button, select `Deploy Scene To Custom Catalyst` and enter `peer.decentraland.zone`).
5. Connect your wallet. You can only use Fortmatic, WalletConnect or WalletLink from within VSCode. If you need to use MetaMask, click on the `Open in browser` button in the top right corner.
6. Click on `Sign & Deploy` and complete the publish flow.

**Install/Uninstall Dependencies**

1. Open VSCode in a Decentraland scene project.
2. Click on the Decentraland icon on the left sidebar.
3. Click on the `+` icon in the Dependencies view. 
4. Enter an npm package (like `react`).
5. If it is a Decentraland library (ie. `decentraland-ecs-utils`) select `Yes`, otherwise `No`.
6. The dependency should appear shortly in the list
7. Click on the trash icon that appears when you hover the dependency to uninstall it.
8. The dependency should disappear shortly.


## Reporting issues


If you run into any bugs, please report an issue in the [Editor](https://github.com/decentraland/editor) repository.

We ask you to please detail how to reproduce the issue as much as possible.


## Submit feedback

Once you've had a chance to try the new editor, please fill in the [feedback form](https://form.typeform.com/to/aODGpdoQ)
---
date: 2022-10-25
title: Run a preview
description: How to run a preview and debug using the Decentraland Editor
categories:
  - editor
type: Document
url: /creator/editor/preview-scene
weight: 4
---

To run a scene preview using the Decentraland Editor:

Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/editor/installation-guide.md" >}}).


1) Open your scene's folder using Visual Studio Code. 

	> Note: The Visual Studio window must be at the root folder of the scene project.

2) Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

3) Click the **Run Scene** button.

	This opens a new tab in Visual Studio Code, running the Decentraland scene, just like in a web browser tab.

Optionally click **Open in browser**, over the top margin of the tab to run the preview in a web browser window.

Learn more about what you can do while previewing a scene in [preview a scene]({{< ref "/content/creator/scenes/getting-started/preview-scene.md" >}}).

## Debug

Using the Decentraland Editor, you can add breakpoints to your scene's code. When running a preview, whenever the code passes through these breakpoints, it pauses execution. A **Debug** panel opens, showing the current values of all variables at that point in time.

This is especially useful to validate that the data at a given point in time is what you expect. You can also modify the values of any variable manually and resume execution with the blue play button, using those new variables. This is great to test corner cases, to make sure the scene behaves as expected on every scenario, which might otherwise be a lot harder to reproduce.

1. Open VSCode in a Decentraland scene project.
2. Click on the Debugger icon on the left sidebar.
3. Click on `Run and Debug` and select `Decentraland` (this step might not be necessary if you already have a `.vscode/launch.json` file).
4. Click on `Run`. A browser should open.
5. Try setting a breakpoint and interacting with the scene in a way it will step on that line. 

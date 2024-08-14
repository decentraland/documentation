---
date: 2018-02-11
title: Scene from example
description: Create a new scene from an existing example
categories:
  - development-guide
type: Document
url: /creator/development-guide/scene-from-example
weight: 4
---

Create a new Decentraland scene project based on an example to start out with a solid base. You can use this to reuse game mechanics, art assets, or anything that may be included in the parent project.

1. Make sure you've [installed the Decentraland VS Code Extension]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#vs-code-extension" >}})

2. Open a Visual Studio Code window on an _empty folder_.
3. Select the Decentraland tab on Visual Studio's left margin sidebar, and click **Create Project**
4. Select the option **From GitHub Repository**. Then paste a URL to the GitHub repository you want to clone.

Use examples from the [Example scenes]({{< ref "/content/creator/tutorials/examples.md#deploy-to-the-test-environment">}}) page. Many of these are specially designed to be great starting places for certain kinds of scenes.

{{< hint info >}}
**💡 Tip**: To avoid downloading the entire repo, with dozens of scenes, copy just the URL to a project folder. Right click on the **View Code** link and copy that link address, then paste that into the new project prompt. For example:

`https://github.com/decentraland/sdk7-goerli-plaza/tree/main/reward-claim`
{{< /hint >}}

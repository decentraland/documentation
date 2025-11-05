---
date: 2024-07-25
title: Combine with code
description: Combine content created on the Scene Editor with the power of writing code.
categories:
  - scene-editor
type: Document
url: /creator/scene-editor/code/overview
aliases:
  - /creator/editor-plus-code
weight: 1
---

{{< youtube 55H37rygD7M >}}

The Creator Hub plus custom code is a very powerful combination for creating content. You can use the canvas to visually position items intuitively, and then write code that interacts with these items with complete freedom. You can even place a smart item, that has its own default behavior, and write code that reacts to when the item is activated.

For example, you can take advantage of an existing lever smart item, that already comes with its sounds and animations and states, and write code that detects when the lever is pulled to run your own custom logic.

See [Reference items in code]({{< ref "/content/creator/scene-editor/code/reference-items.md" >}}) for how to fetch items by name or by tags from your code.

## Editing code

You must install a code editor on your machine to edit the code of your scene. The recommended options are:

- <img src="/images/editor/vscode.png" alt="Header" width="25"/> [Visual Studio Code](https://code.visualstudio.com/): This is the recommended option for experienced developers.

- <img src="/images/editor/cursor-icon.png" alt="Header" width="25"/> [Cursor AI](https://www.cursor.com/): This is a powerful code editor that is integrated with AI. It lets you pick different AI models to help you write code, all of them are free. This is a good option for developers who are new to Decentraland or TypeScript, or if you want to save time writing code.

{{< hint warning >}}
**📔 Note**: If you are on macOS, make sure the code editor app is in the Applications directory.
{{< /hint >}}

Once installed, you may need to select your Code Editor in the settings of the Creator Hub. To do this,

1. Open the wheel icon in the top-right of the screen 
<img src="/images/editor/settings-icon.png" alt="Header" width="25"/>

2. Under **Code editor of choice**, select your Code Editor. You may find your editor listed in the dropdown, or you may need to select **Chose from your device** to find it.


## Open a scene's code

Once you installed a code editor on your machine, and selected it in the settings of the Creator Hub, you can click the **< > CODE** button to open it on your scene project.

<img src="/images/editor/code-button.png" width="200"/>

This opens a separate window with the code editor. On the left margin you can navigate the files and folder structure of your project.

<img src="/images/editor/files-on-vs-studio.png" alt="Scene name" width="200"/>

Add your custom code in the `index.ts` file under `/src`, inside the `main()` function. You can otherwise add custom code outside that function or create new `.ts` files inside the `/src` folder, but these must be somehow referenced inside the `main()` function of `index.ts`.

{{< hint warning >}}
**📔 Note**: If you have VS Code or Cursor installed but the **CODE** button doesn't open it, it may be that VS Code is not properly configured on your machine to open via the command line. In most cases, this is handled as part of the default installation, but in case it's not, see [these instructions from VS](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line) to enable VS Code from the command line.
{{< /hint >}}

If you have a preview window open running your scene, whenever you change the code in your files and save, the scene reloads automatically with your changes.

## Using AI with Cursor

If you are using Cursor, you can use the AI assistant to help you write code. To do this,

1. Open the Cursor AI assistant by clicking the **AI** button in the top-right of the screen
<img src="/images/editor/cursor-icon.png" alt="Header" width="128"/>

2. There you can prompt the AI assistant to help you write code. You can also select a model to use from the dropdown.

Decentraland provides a context folder for the AI assistant to help you write code, this context folder is located at `/dclcontext` in your scene project. The AI assistant will know to search this context whenever generating code, to get familiar with the Decentraland SDK.

This folder is updated with the latest context files every time your scene's dependencies are updated. You can also force update this folder by running the following:

```
npx sdk-commands get-context-files
```


{{< hint info >}}
**💡 Tip**: You can also add your own context files to this folder to help the AI assistant understand your scene and project. If you do, make sure to add them to a new file in that folder, as the default files are overwritten when SDK updates happen.
{{< /hint >}}


## Version control

We recommend that you create a repo for your project on GitHub, and use it to keep track of your project's versions and to work collaboratively with others.

If you're not familiar with how to do this, see [Quickstart for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories), or use the [GitHub desktop appliacation](https://desktop.github.com/download/) for an simpler UI-based flow.

{{< hint warning >}}
**📔 Note**: Upload the entire project folder to a GitHub repo, but make sure the `/node-modules` or `/bin` folders and the `package-lock.json` file are all included in the `.gitignore` file, to avoid syncing them. This should be the case if you configure the repo to be of type `node`. These files are all auto-generated, and the content may differ for different machines.
{{< /hint >}}

## See also

- [Smart items - Basics]({{< ref "/content/creator/scene-editor/interactivity/smart-items.md" >}})
- [Smart items - Advanced]({{< ref "/content/creator/scene-editor/interactivity/smart-items-advanced.md" >}})
- [States and conditions]({{< ref "/content/creator/scene-editor/interactivity/states-and-conditions.md" >}})
- [Making any item smart]({{< ref "/content/creator/scene-editor/interactivity/make-any-item-smart.md" >}})

- [SDK Quick start]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}): follow this mini tutorial for a quick crash course.
- [Development workflow]({{< ref "/content/creator/sdk7/getting-started/dev-workflow.md" >}}): read this to understand scene creation from end to end.
- [Examples](https://studios.decentraland.org/resources?sdk_version=SDK7): dive right into working example scenes.

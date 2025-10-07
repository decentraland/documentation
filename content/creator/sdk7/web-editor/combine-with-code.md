---
date: 2024-01-04
title: Export to desktop
description: Combine content created on the Scene Editor with the power of writing code.
categories:
  - web-editor
type: Document
url: /creator/editor-plus-code
weight: 5
---

Use the [Creator Hub]({{< ref "/content/creator/scene-editor/about-editor.md" >}}) together with custom code to take your content to the next level. You can use the Scene Editor in the Creator Hub to position items intuitively, and then write code that interacts with these items with complete freedom. You can even place a smart item, that has its own default behavior, and write code that reacts to when the item is activated.

For example, you can take advantage of an existing lever smart item, that already comes with its sounds and animations and states, and write code that detects when the lever is pulled to run your own custom logic.

## Export your project

To edit the code in a scene created with the [Web Editor]({{< ref "/content/creator/sdk7/web-editor/web-editor.md" >}}), you must export the scene to your machine and open it with the Creator Hub.

{{< hint warning >}}
**📔 Note**: If you don't have the Creator Hub installed, follow the steps in the following page before your start.

[Install Creator Hub]({{< ref "/content/creator/scene-editor/editor-installation.md" >}})
{{< /hint >}}

1. Click the **Download icon** on the top menu of the Web Editor while editing the scene.

  <img src="/images/editor/export.png" width="256" />

2. This will download a _.zip_ file, extract it.
3. Open the **Creator Hub**, go into the **Scene Editor** section.
4. Click the **Import** button and select the path to your exported project folder.

Once you're done, you can keep working on your project inside the Creator Hub, with a visual interface that looks a lot like the Web Editor.

You can also edit the files under the `/src` folder to add behavior with code to your scene.

See [Combine with code]({{< ref "/content/creator/scene-editor/combine-with-code.md" >}}) for how to edit the code of your scene.

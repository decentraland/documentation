---
date: 2022-06-29
title: Debug in production
description: How you can debug your scene that is running inside Decentraland
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/debug-in-prod/
weight: 2
---

When running a scene that's already deployed to land in Decentraland, there are a number of things you can try out to debug it.

## Before deploying

### Preview

Before you deploy your scene to Decentraland, make sure the scene runs well in preview using the latest version of the Decentraland SDK. See [debug in preview]({{< ref "/content/creator/sdk7/debugging/debug-in-preview.md" >}}).

Although there should always be backwards compatibility of content built with older SDK versions, some platform-level aspects are subject to change over time. For example, lighting, avatar animations, skybox textures, global UIs, etc. By running a preview with the latest SDK version, you're using a newer version of the engine, which should render your scene in a way that's closer to what's used in production.

### The test server

You can deploy scenes to a test server as a staging environment, before publishing them to the live content servers. This server is not frequented by any players that visit Decentraland normally. To enter this server you must manually write its URL, but keep in mind that it's not a private environment.

See [The test server]({{< ref "/content/creator/sdk7/publishing/publishing.md#the-test-server">}}) for details.

## Quick reload

If you need to reload the scene you're standing on, write the following into the chat and push enter:

`/reload`

## About the publishing pipeline

Keep in mind that after each publish, an internal process optimizes all 3D models before they can be rendered. This takes around 15 minutes. If you visit the scene before this is done, the scene may appear broken. This process may run even if the 3D models were all previously published.

You can check the current state of this process for your scene using [this tool](https://decentraland.github.io/opscli/). If the conversion is complete, all three variations of the assets should have green lights.

## Scene logs

When using Decentraland normally, it's not possible to open the console to check for debug messages. To make the console available, you must open decentraland with the `scene-console` parameter. You can then toggle the console by pressing the backtick key on your keyboard: **`**. This key is left of the 1 key on most english language keyboards.

To open Decentraland with the `scene-console` parameter, either:

- Write the following deep link into a browser window: `decentraland://?position=0,0&scene-console`. This will open the Decentraland desktop application if you have it installed.
- Write the following on the command line:
  - **macOS**: `open Decentraland.app --args --position 0,0 --scene-console`
  - **winOS**: `"C:\Users\[YOUR-USER]\Downloads\Decentraland_windows64\Decentraland.exe" --position 0,0 --scene-console`

{{< hint info >}}
**💡 Tip**: Change the **position** parameter to the coordinates of your scene, to load directly into your scene.
{{< /hint >}}

When running Decentraland with the `scene-console`, you can open the console in two ways:

- Press the **`** key for a short console
- Press Shift + **\`** to open a larger view of the console


Messages from each active scene will be logged to the console.

<!-- ## Access debug information

To view the full stack trace of each error message, you must deploy the scene with source maps included. With this you can also navigate the source code and even break points, all from the browser with the scene in production.

To do this, remove the following line from the `.dclignore` file in your scene before you publish the scene:

```
bin/*.map
```

{{< hint danger >}}
**❗Warning** Having the source maps uploaded as part of your scene might make it easier for bad actors to exploit your scene, or steal your code. Make sure you understand the risks of doing this.
{{< /hint >}}



### See debug panel

To view scene stats, add the following URL parameter:

`&SCENE_DEBUG_PANEL`

This will enable the option of opening a panel that displays stats that update in real time, including material count, entity count, processed messages, etc. See [view scene stats]({{< ref "/content/creator/sdk7/debugging/debug-in-preview.md#view-scene-stats">}}) for details.

With this flag enabled, you'll see a hint on the top-right corner of the screen, and you can press Y to open up this panel and see stats for the scene you're currently standing on.

{{< hint warning >}}
**📔 Note**: As accessing this implies changing the URL, it's not available when running the scene n the Desktop client.
{{< /hint >}}

### See FPS panel

To see the current FPS (Frames Per Second) of the explorer, type `/showfps` into the chat window, and this will display the FPS panel.

Keep in mind that these FPS values may vary depending on the machine you're using, and may also be affected by neighboring scenes.

It's still a valuable way to assess the performance of the scene more objectively.

They count the frame per second of the Decentraland explorer, not of a single scene. You can try to isolate what effect neighbors have on the FPS by reducing the line of sight property on the settings, to load less content at a time. -->

## Report a bug

If you encounter a problem that is not with your scene, but instead with the Decentraland SDK in general, please see [Report a bug]({{< ref "/content/creator/sdk7/debugging/report-bug.md">}}).

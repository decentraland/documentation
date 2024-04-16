---
date: 2018-02-11
title: Manage Builder scenes
description: Getting started with the Builder
categories:
  - builder
type: Document
aliases:
  - /builder/manage-scenes/
url: /creator/builder/manage-scenes
---

## Export a scene

While editing a scene, press the _Download scene_ icon to download the contents of the scene as a _.zip_ file. In the scene selector screen, you can also press the _three dots_ icon and select _Download scene_.

![](/images/media/builder-export.png)

You can then share this scene with another Builder user, or edit the scene with more freedom by using the Decentraland SDK.

See [SDK 101]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}) if you're not yet familiar with coding with the Decentraland SDK.

## Upload a scene

In the scene selector screen, press _Upload scene_, then drag one or several _.zip_ files from exported Builder scenes and press _Upload_.

If a scene is too large to upload, try this:

1. Decompress the scene _.zip_ file.
2. Look for the `builder.json` inside the uncompressed folder. Compress that single file into a new _.zip_ file.
3. Upload this new _.zip_ file.

{{< hint warning >}}
**📔 Note**: You can only upload scenes that have been built with the Builder. You can't upload a scene that was built with the SDK or modified with it.
{{< /hint >}}

## Delete a scene

In the scene selector screen, press the _three dots_ icon and select _Delete scene_.

## Scene storage

If your Builder account is accessed via an in-browser wallet, like Metamask or Dapper, all of your existing scenes are saved and updated to a cloud storage that you can access from any other device where you're logged in.

If you don't have your account connected to an in-browser wallet, your scenes are stored in the browser's cache storage. They won't be available if you log in from another device. Be careful not to clear the browser's storage, as you will lose your scenes. We advise exporting your scenes to keep a backup in your local disk.

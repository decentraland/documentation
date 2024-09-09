---
date: 2024-07-25
title: Manage scenes
description: Managing your scene projects
categories:
  - scene-editor
type: Document
aliases:
  - /builder/manage-scenes/
url: /creator/editor/manage-scenes
weight: 3
---

Each of your available scenes is shown as a card. Open the card to edit that scene, from there you can preview it or publish it too.

## Create a scene

Click **Create scene** to create a new scene. This may take a minute or two, as it downloads dependencies and sets up a folder on your local machine with everything it needs. This will then open your scene in the [Scene Editor]({{< ref "/content/creator/scene-editor/scene-editor-essentials.md" >}}).

Click the three dots on a scene's card and click **Duplicate** to make a copy of an existing scene.

<!-- TODO future:
create from template -->

To rename your scene, open it and click the pencil icon to change the **Name** field and other properties.

## Import a scene

The scene manager displays the scenes it finds in the default path on your machine.

To add a scene that is elsewhere on your local disk, click **Import scene** and find the path to the project folder. The imported scene will now be available as a new card in the scene manager screen.

The imported scene does not get moved in your local disk.

{{< hint warning >}}
**📔 Note**: Do not manually rename or move the folder of an imported scene directly from your file manager. The Scene Editor will no longer be able to find the imported scene in its new path.
{{< /hint >}}

Scenes you created on the [web editor]({{< ref "/content/creator/sdk7/web-editor/web-editor.md" >}}) are stored in the cloud. To work on these scenes from the desktop Scene Editor, you must [export]({{< ref "/content/creator/sdk7/web-editor/web-editor.md#download-scene" >}}) the scene from the Web Editor, unzip it into a folder, and then import it on the desktop Scene Editor.

## Delete a scene

In the scene selector screen, press the _three dots_ icon and select _Delete_.

This removes the scene from your Scene Editor home screen, but doesn't delete the files from your machine.

If you wish to delete the project files, you must do this manually. By default projects created via the Scene Editor are kept inside a `.decentraland` folder under your user directory. You can navigate here by clicking the three dots on a project card and selecting **Open folder**.

<!-- TODO:
You can change the directory?

Advanced recommendation: upload your scene to a repo?

-->

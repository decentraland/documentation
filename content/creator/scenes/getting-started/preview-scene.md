---
date: 2018-01-01
title: Preview your scene
description: What you can see in a scene's preview
aliases:
  - /documentation/preview-scene/
  - /getting-started/preview-scene/
  - /development-guide/preview-scene/
  - /creator/editor/preview-scene
categories:
  - development-guide
type: Document
set: getting-started
url: /creator/development-guide/preview-scene
weight: 4
---

{{< hint danger >}}
**❗Warning**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}).
{{< /hint >}}

Once you have [built a new scene]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}) or downloaded a [scene example](https://github.com/decentraland-scenes/Awesome-Repository#examples) you can preview it locally.

## Using the Scene Editor

Make sure you've [installed the Creator Hub]({{< ref "/content/creator/scene-editor/editor-installation.md" >}}).

1. Open your scene project.
2. Click the **Preview** button on the top-right corner. This will open a new window with the Decentraland Desktop Explorer, running just your scene. There you can move around the scene and interact with interactive items.

<img src="/images/editor/preview-button.png" width="150" alt="Scene name"/>

## Using the VS Code Extension

To run a scene preview using the VS Code Extension:

Make sure you've [installed the Decentraland VS Code Extension]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#vs-code-extension" >}}).

1. Open your scene's folder using Visual Studio Code.

   > Note: The Visual Studio window must be at the root folder of the scene project.

2. Open the Decentraland tab on Visual Studio. Note that the bottom section lists all of your project's currently installed dependencies.

3. Click the **Run Scene** button.

   This opens a new browser tab running the Decentraland scene.

## Using the CLI

### Before you begin

Please make sure you first install the CLI tools by running the following command:

```bash
npm install -g decentraland
```

See the [Installation Guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}) for more details instructions.

### Preview a scene

To preview a scene run the following command on the scene's main folder:

```bash
dcl start
```

Any dependencies that are missing are installed and then the CLI opens the scene in a new browser tab automatically. It creates a local web server in your system and points the web browser tab to this local address.

Every time you make changes to the scene, the preview reloads and updates automatically, so there's no need to run the command again.

{{< hint warning >}}
**📔 Note**: Some scenes depend on an external server to store a shared state for all players in the scene. When previewing one of these scenes, you'll likely have to also run the server locally on another port. Check the scene's readme for instructions on how to launch the server as well as the scene.
{{< /hint >}}

### Parameters of the preview command

You can add the following flags to the `dcl start` command to change its behavior:

- `--port` to assign a specific port to run the scene. Otherwise it will use whatever port is available.
- `--no-debug` Disable the debug panel, that shows scene and performance stats
- `--no-browser` to prevent the preview from opening a new browser tab.
- `--w` or `--no-watch` to not open watch for filesystem changes and avoid hot-reload
- `--c` or `--ci` To run the parcel previewer on a remote unix server
- `--web3` Connects preview to browser wallet to use the associated avatar and account
- `--skip-version-checks` Avoids checking if the scene's ECS library version matches your CLI version, and launches the preview anyway.
- `--desktop-client` Runs the preview in the Decentraland Desktop client

{{< hint warning >}}
**📔 Note**: To preview old scenes that were built for older versions of the SDK, you must set the corresponding version of `decentraland-ecs` in your project's `package.json` file.
{{< /hint >}}

## Upload a scene to decentraland

Once you're happy with your scene, you can upload it and publish it to Decentraland, see [publishing]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) ) for instructions on how to do that.

## Preview scene size

The scene size shown in the preview is based on the scene's configuration. By default, the scene occupies a single parcel (16 x 16 meters).

If you're building a scene to be uploaded to several adjacent parcels, you can edit the _scene.json_ file to reflect this, listing multiple parcels in the "parcels" field. Placing any entities outside the bounds of the listed parcels will display them in red.

```json
 "scene": {
    "parcels": [
      "0,0",
      "0,1",
      "1,0",
      "1,1"
    ],
    "base": "0,0"
  },
```

You can also change the coordinates by running the `dcl coords` command from the command line, this is especially useful on large scenes with many parcels. See [set parcels via the command line]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#set-parcels-via-the-command-line">}}) for more details.

{{< hint info >}}
**💡 Tip**: While running the preview, the parcel coordinates don't need to match those that your scene will really use, as long as they're adjacent and are arranged into the same shape. You will have to replace these with the actual coordinates later when you [deploy the scene](#upload-a-scene-to-decentraland).
{{< /hint >}}

## Run preview in Desktop

To run a preview scene in the Desktop native client, instead of in the web browser:

1. Make sure you have downloaded and installed the [Windows](https://decentraland.org/download/) or [Mac](https://github.com/decentraland/explorer-desktop-launcher/releases/latest/download/Decentraland.dmg) desktop client.

2. Run the preview with:

   `dcl start --desktop-client`

3. Copy the URL provided by the console output under **Desktop Client** and paste in your browser.

   > Note: The Browser might ask you for permission to open an external executable: Decentraland. Select **Open**.

4. You'll see the following screen. Check that the URL is correct, then click **Continue** to launch the preview.

   ![](/images/media/desktop-preview.png)

   If you need to manually add anything to the URL, to change the default way the scene runs, tick the box **Add custom URL parameters** and write those in the dialog below.

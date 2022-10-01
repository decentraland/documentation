---
date: 2018-01-01
title: Preview your scene
description: What you can see in a scene's preview
aliases:
  - /documentation/preview-scene/
  - /getting-started/preview-scene/
  - /development-guide/preview-scene/
categories:
  - development-guide
type: Document
set: getting-started
url: /creator/development-guide/preview-scene
---

Once you have [built a new scene](https://docs.decentraland.org/#create-your-first-scene) or downloaded a [scene example](https://github.com/decentraland-scenes/Awesome-Repository#examples) you can preview it locally.

## Before you begin

Please make sure you first install the CLI tools by running the following command:

```bash
npm install -g decentraland
```

See the [Installation Guide](/creator/development-guide/installation-guide) for more details instructions.

## Preview a scene

To preview a scene run the following command on the scene's main folder:

```bash
dcl start
```

Any dependencies that are missing are installed and then the CLI opens the scene in a new browser tab automatically. It creates a local web server in your system and points the web browser tab to this local address.

Every time you make changes to the scene, the preview reloads and updates automatically, so there's no need to run the command again.

> Note: Some scenes depend on an external server to store a shared state for all players in the scene. When previewing one of these scenes, you'll likely have to also run the server locally on another port. Check the scene's readme for instructions on how to launch the server as well as the scene.

## Upload a scene to decentraland

Once you're happy with your scene, you can upload it and publish it to Decentraland, see [publishing](/creator/development-guide/publishing) ) for instructions on how to do that.

You can also upload a preview to a free 3rd party server, [see instructions here](/creator/development-guide/deploy-third-party).

## Parameters of the preview command

You can add the following flags to the `dcl start` command to change its behavior:

- `--port` to assign a specific port to run the scene. Otherwise it will use whatever port is available.
- `--no-debug` Disable the debug panel, that shows scene and performance stats
- `--no-browser` to prevent the preview from opening a new browser tab.
- `--w` or `--no-watch` to not open watch for filesystem changes and avoid hot-reload
- `--c` or `--ci` To run the parcel previewer on a remote unix server
- `--web3` Connects preview to browser wallet to use the associated avatar and account
- `--skip-version-checks` Avoids checking if the scene's ECS library version matches your CLI version, and launches the preview anyway.
- `--desktop-client` Runs the preview in the Decentraland Desktop client

> Note: To preview old scenes that were built for older versions of the SDK, you must set the corresponding version of `decentraland-ecs` in your project's `package.json` file.

## Preview scene size

The scene size shown in the preview is based on the scene's configuration, you set this when building the scene using the CLI. By default, the scene occupies a single parcel (16 x 16 meters).

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

> Tip: While running the preview, the parcel coordinates don't need to match those that your scene will really use, as long as they're adjacent and are arranged into the same shape. You will have to replace these with the actual coordinates later when you [deploy the scene](#upload-a-scene-to-decentraland).

## Run preview in Desktop

To run a preview scene in the Desktop native client, instead of in the web browser: 


1) Make sure you have downloaded and installed the [Windows](https://decentraland.org/download/) or [Mac](https://github.com/decentraland/explorer-desktop-launcher/releases/latest/download/Decentraland.dmg) desktop client.

2) Run the preview with:

	`dcl start --desktop-client`

3) Copy the URL provided by the console output under **Desktop Client** and paste in your browser.

	> Note: The Browser might ask you for permission to open an external executable: Decentraland. Select **Open**.

4) You'll see the following screen. Check that the URL is correct, then click **Continue** to launch the preview.

	![](/images/media/desktop-preview.png)

	If you need to manually add anything to the URL, to change the default way the scene runs, tick the box **Add custom URL parameters** and write those in the dialog below.

 
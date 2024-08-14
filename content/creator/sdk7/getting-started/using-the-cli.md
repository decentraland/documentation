---
date: 2022-02-21
title: Using the CLI
description: How to use the Decentraland CLI to run, deploy, etc
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/cli
weight: 15
---

To build scenes for Decentraland you an either use

- The [Creators Hub]({{< ref "/content/creator/scene-editor/editor-installation.md" >}})
- The Command Line Interface (CLI)

Both tools allow you to compile and preview your scene in an "off-chain" development environment. After testing your scene locally, you can upload your content to the content server, linking it with your LAND or WORLD.

Although the Scene Editor in the Creators Hub is easier to use, the CLI allows you more flexibility, and can be easily used in automated processes.

{{< hint warning >}}
**📔 Note**: The Scene Editor runs the same command-line operations behind the curtains.
{{< /hint >}}

{{< hint info >}}
**💡 Tip**: See [Instalation guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md#creators-hub" >}}) for instructions on how to install the Scene Editor.
{{< /hint >}}

## Before you Begin

To deal with the scene via the command line, please install the following dependencies before you run CLI commands with the scene:

- [Node.js](https://nodejs.org) (version 8 or later)

## Initiate a new project

Run `npx @dcl/sdk-commands init` on an empty folder to populate it with the default files of a Decentraland project.

The CLI then prompts you to chose what kind of project, if you want to build a [scene]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}), a [workspace]({{< ref "/content/creator/sdk7/projects/workspaces.md" >}}) or a [smart wearable]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}). If selecting a scene, the CLI prompts you about what base project to use as a starting point.

## Update the SDK version of a scene

Run the following command on the scene folder:

```bash
npm i @dcl/sdk@latest
```

You can confirm that it worked by checking the `package.json` file for the scene, and looking for the `@dcl/sdk` version there.

## Run a preview

Run `npm run start` on the root level of a scene, workspace, or smart wearable project to open a preview in a browser window.

See [preview scenes]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}) for details and special options when running a preview.

## Build

Run `npm run build` to build your project. Decentraland scenes are written in TypeScript, but they are built to minified JavaScript when published. See [coding scenes]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md" >}}) for more details.

The build command is optional, as it also runs in the background before deploying (although you can add a flag to skip it).

The build command runs more rigurous type checks than those that run with `npm run start`, running it can sometimes be helpful to debug a scene.

## Deploy a scene

Run `npm run deploy` to publish your scene to Decentraland. This command opens a browser window where you can sign with your wallet to authorize the deployment.

See [publishing]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) for details and special options when publishing a scene.

## Troubleshooting

If you run into issues, see the [troubleshooting]({{< ref "/content/creator/sdk7/debugging/troubleshooting.md" >}}) section.

<!--


#### Optional: Install Git

Mac OS and linux-based machines should have git installed by default, these steps should only be relevant to Windows based machines.

1.  Download [git](https://git-scm.com/download/win) (you'll likely want the 64-bit Windows version)
2.  The installation process will prompt you to choose severla options, we recommend the following:
	1.  Install **git bash**
	2.  For default text editor, select **Use the Nano editor by default**
	3.  For path environment, select **Use Git from the Windows Command Prompt**
	4.  For SSH executable, select **Use OpenSSH**
	5.  For HTTPS transport backend, select **Use the OpenSSL library**
	6.  For line ending conversions, select **Checkout Windows-style, commit Unix-style line endings**
	7.  For the terminal emulator to use with Git Bash select **Use MinTTY**
	8.  On the final installation screen select the following options
		- **Enable file system caching**
		- **Enable Git Credential Manager**
		- **Enable symbolic links**

-->

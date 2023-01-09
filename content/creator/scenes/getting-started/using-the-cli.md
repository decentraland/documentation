---
date: 2022-02-21
title: Using the CLI
description: How to use the Decentraland CLI to run, deploy, etc
categories:
  - development-guide
type: Document
url: /creator/development-guide/cli
weight: 15
---


To build scenes for Decentraland you an either use 

- The Decentraland Editor
- The Command Line Interface (CLI)

Both tools allow you to compile and preview your scene in an "off-chain" development environment. After testing your scene locally, you can upload your content to the content server, linking it with your LAND.

Although the Editor is easier to use, the CLI allows you more flexibility, and can be easily used in automated processes.

{{< hint warning >}}
**📔 Note**   The Editor uses the CLI behind the scenes.
{{< /hint >}}

{{< hint info >}}
**💡 Tip**:  See [Instalation guide]({{< ref "/content/creator/scenes/getting-started/installation-guide.md" >}}) for instructions on how to install the Editor.
{{< /hint >}}

The Decentraland CLI is distributed via [npm](https://www.npmjs.com/get-npm?utm_source=house&utm_medium=homepage&utm_campaign=free%20orgs&utm_term=Install%20npm).



## Before you Begin

Please install the following dependencies before you install the CLI:

- [Node.js](https://nodejs.org) (version 8 or later)

## Install the CLI

Open the _Terminal_ app and run the following command:

```bash
npm install -g decentraland
```

Once the installation is complete, the `dcl` command will be globally available.

## Update the CLI on any platform

To update the CLI to the latest supported version, we recommend first uninstalling the CLI and then reinstalling a fresh version. To do this, run the following commands:

```bash
// uninstall
npm rm decentraland -g

// install
npm install -g decentraland
```

## Update the SDK version of a scene

If your CLI is up to date, the new projects you create with it will use the latest version of the SDK.

The SDK version used by your existing projects doesn't change by updating the CLI. You need to manually update the SDK version in the projects.

Run the following command on the scene folder:

```bash
npm i decentraland-ecs@latest
```

You can confirm that it worked by checking the `package.json` file for the scene, and looking for the `decentraland-ecs` version there.

## Initiate a new project

Run `dcl init` on an empty folder to populate it with the default files of a Decentraland project.

The CLI then prompts you to chose what kind of project, if you want to build a [scene]({{< ref "/content/creator/scenes/projects/scene-metadata.md" >}}), a [workspace]({{< ref "/content/creator/scenes/projects/workspaces.md" >}}) or a [smart wearable]({{< ref "/content/creator/scenes/projects/smart-wearables.md" >}}). If selecting a scene, the CLI prompts you about what base project to use as a starting point.

## Run a preview

Run `dcl start` on the root level of a scene, workspace, or smart wearable project to open a preview in a browser window.

See [preview scenes]({{< ref "/content/creator/scenes/getting-started/preview-scene.md" >}}) for details and special options when running a preview.

## Build

Run `dcl build` to build your project. Decentraland scenes are written in TypeScript, but they are built to minified JavaScript when published. See [coding scenes]({{< ref "/content/creator/scenes/getting-started/coding-scenes.md" >}}) for more details.

The build command is optional, as it also runs in the background before deploying (although you can add a flag to skip it).

The build command runs more rigurous type checks than those that run with `dcl start`, running it can sometimes be helpful to debug a scene.

## Deploy a scene

Run `dcl deploy` to publish your scene to Decentraland. This command opens a browser window where you can sign with your wallet to authorize the deployment.

See [publishing]({{< ref "/content/creator/scenes/publishing/publishing.md" >}}) for details and special options when publishing a scene.



## Troubleshooting

If you run into issues, see the [troubleshooting]({{< ref "/content/creator/scenes/debugging/troubleshooting.md" >}}) section.



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

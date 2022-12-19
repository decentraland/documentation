---
date: 2018-01-01
title: CLI Installation Guide
description: Step-by-step guide to installing the SDK
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/installation-guide/
weight: 2
---


To build scenes for Decentraland you an either use 

- The Decentraland Editor
- The Command Line Interface (CLI)

Both tools allow you to compile and preview your scene in an "off-chain" development environment. After testing your scene locally, you can upload your content to the content server, linking it with your LAND.

## The Decentraland Editor


The Decentraland Editor is a Visual Studio extension, that allows you to build, preview and deploy Decentraland scenes.

To install the Decentraland Editor:

1) Install [Visual Studio Code](https://code.visualstudio.com/), if you don't have it already.

2) Open Visual Studio Code, and open the extensions marketplace. Search for the **Decentraland Editor** extension and click **Install**. You'll then need to restart Visual Studio to use the extension.

## The CLI


The Decentraland CLI is distributed via [npm](https://www.npmjs.com/get-npm?utm_source=house&utm_medium=homepage&utm_campaign=free%20orgs&utm_term=Install%20npm).

> Note: The Editor uses the CLI behind the scenes. Although the Editor is easier to use, there are some scenarios where you might need to use the CLI directly, like when building automatic publishing flows.

## Before you Begin

Please install the following dependencies before you install the CLI:

- [Node.js](https://nodejs.org) (version 8 or later)

## Install the CLI

Open the _Terminal_ app and run the following command:

```bash
npm install -g decentraland
```

> Tip: You can run this command on any folder, as it affects the installation globally.

Once the installation is complete, the `dcl` command will be globally available.

## Run updates

### Update the CLI

New versions of the CLI are launched periodically. If you've been already using the CLI for some time, you may require to update to access the latest features or bug fixes.

To update the CLI to the latest supported version, we recommend first uninstalling the CLI and then reinstalling a fresh version. To do this, run the following commands on any folder:

```bash
// uninstall
npm rm decentraland -g

// install
npm install -g decentraland
```

> Tip: You can run these commands on any folder, as it affects the installation globally.

### Update the SDK version of a scene

If your CLI is up to date, the new projects you create with it will use the latest version of the SDK.

The SDK version used by an existing project won't change automatically. So even if your CLI is up to date, you may need to also separately update older projects to use the latest SDK version.

Run the following command on the scene folder:

```bash
npm i decentraland-ecs@latest
```

You can confirm that it worked by checking the `package.json` file for the scene, and looking for the `decentraland-ecs` version there.

## Troubleshooting

If you run into issues, see the [troubleshooting](/development-guide/troubleshooting) section.



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

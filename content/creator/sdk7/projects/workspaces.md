---
date: 2022-02-08
title: Workspaces
description: Run multiple DCL projects at a time
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/workspaces/
  - /creator/development-guide/workspaces/
url: /creator/development-guide/sdk7/workspaces/
weight: 3
---

Run multiple Decentraland projects in preview by grouping these into a workspace. Run multiple adjacent scenes to see how they fit, or also run multiple [smart wearables]({{< ref "/content/creator/sdk7/projects/smart-wearables.md" >}}) together to see how they interact with each other and with different scenes.

Running multiple projects in a workspace provides a much more complete testing alternative, to ensure different content works well together. A workspace is a debugging feature, it doesn't affect the experience in the published scene.

{{< hint warning >}}
**📔 Note**: The **Creator Hub** doesn't currently support handling Workspaces.
{{< /hint >}}

## Create a workspace

<!--
1. Create a top-level folder to hold the workspace.

2. Inside this folder, add one folder at root level for each project you want to work with. You can drag in existing folders with scenes or smart wearables. For new folders, run `npx sdk-commands init` inside each, to create a Decentraland project.

   > Note: Make sure that the parcels on each of the scenes don't overlap.

3. Standing on the workspace folder, run the following, to create the necessary files:

   `dcl workspace init`

-->

1. Download the [Goerli Plaza](https://github.com/decentraland/sdk7-goerli-plaza) repo.
2. Create a separate top-level folder to hold the workspace.
3. From the Goerli Plaza repo, copy the following files over to your workspace:
	- `dcl-workspace.json`
	- `package.json`
	- `.gitignore`
4. Inside this folder, add one folder at root level for each project you want to work with. You can drag in existing folders with scenes or smart wearables. For new folders, run `npx sdk-commands init` inside each, to create a Decentraland project.

   > Note: Make sure that the parcels on each of the scenes don't overlap.
5. Standing on the workspace folder, run the following, to create the necessary files:

   `npm run update-parcels && npm run sync && npm run test && npm run format`

You can confirm that the projects are part of the workspace by running `dcl workspace ls`.

## Run a workspace

Run `npm run start` on the root folder of the workspace. This runs all of the projects at the same time, viewable in a single preview window. This preview behaves just like when previewing a single scene.

Any smart wearables in the workspace are available to try on by looking for them in the backpack.

## Add projects

Once a workspace is created, you can add additional projects `dcl workspace add`, including the relative address of the folder you want to add. For example `dcl workspace add my-other-example`.

You can also add a project that is not inside the workspace folder, by using the absolute path.

{{< hint warning >}}
**📔 Note**: The folder must already contain a decentraland project initatied with `npx sdk-commands init`. It can't be an empty folder.
{{< /hint >}}

You can also edit the `dcl-workspace.json` file manually to add or remove projects. Modify the file to include the relative paths to each of the projects in the workspace in the `folders` array.

```json
{
	"folders": [
		{
			"path": "example-scene"
		},
		{
			"path": "example-scene2"
		}
	]
}
```

---
date: 2022-06-29
title: Troubleshooting
description: Fixes for common problems
categories:
  - development-guide
type: Document
aliases:
  - /development-guides/troubleshooting/
url: /creator/development-guide/troubleshooting
weight: 3
---


# Issues when running preview

### Issue: Can't run any scene preview, error message says mentions **Permissions denied** or **EACCES**

Your operating system doesn't allow you edit permissions on the folder where you want to run the project. When running the scene, some dependencies need to be installed, but it's forbidden. You need to configure the folder's permissions to allow your Windows/Mac/Linux user account to edit files in them.

Useful resources:

- [docs.npmjs](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally)
- [letscodepare](https://letscodepare.com/blog/npm-resolving-eacces-permissions-denied)

### Issue: Can't run a particular scene preview, error says **Error: Error while building the project**

If you're running a scene that was shared with you, make sure that this scene wasn't shared containing a `node_modules` or `bin` folder, or a `package-lock.json` file. These files contain dependencies that use versions that are specific to your OS and machine, they should be generated when running the scene for the first time. Delete these folders & file manually, then run `dcl start` again.


### Issue: Running `dcl start` runs, no error message, but no browser window opens and no URL in the output to open the preview

Make sure your Node version is up to date. It must be 16 or newer.

### Issue: Running `dcl start` opens a browser tab, but the loading screen never finishes loading, or I see a red error banner that says "critical error".

- Make sure you have the latest version of the Decentraland SDK installed in your project. Run:

	`npm i decentraland-ecs@latest`

- Make sure you also have the latest version of the Decentraland CLI installed globally on your machine. Run:

	`npm i -g decentraland@latest`

### Issue: The scene runs, in the console I see `Cyclic dependencies` warnings.

These refer to files in your scene that reference each other mutually. This is not necessarily a problem, but is not a recommendable pattern for writing software, as it can lead to hard to debug race conditions and other issues. Your scene is likely to work well in spite of these warnings.

Ideally, the loading of the code in your scene should follow a clear sequential order. Code that has cyclic dependencies might suffer a chicken & the egg problem, where the compiler doesn't know which to initiate first. Often this is resolved without issues, but it's a good practice to avoid. 

To fix these dependencies, you often must resort to calling functions or object constructors passing references to already instanced entities/objects in the function arguments; Instead of hard-coding references to these entities/objects in the function, which may or may not already be instanced. 

# Issues when deploying

### Issue: You don't have permissions to deploy to these parcels

- Make sure that the `scene.json` file of your scene correctly lists the coordinates where you want to deploy.

- Make sure that Metamask is correctly set up to use the right wallet to sign the transaction. This may either be the wallet that owns the LAND tokens, or might have operator permissions granted by the owner.

### Issue: Running `dcl deploy` fails

- If you're working on an old scene, make sure the `scene.json` file doesn't include legacy sections, such as `communications` or `policy`. Delete these sections entirely.

- Check the spawn points of your scene, all three x,y,z coordinates of a spawn point must either be a number or a range. Either all three are numbers or all three are ranges. It's not supported to have ranges for some but numbers for others. 

	For example this is not supported:

	`"position": {"x": [1,4], "y": 0, "z": [1,4]}`

	This is supported:

	`"position": {"x": [1,4], "y": [0,0], "z": [1,4]}`


- The default catalyst server that you're assigned to deploy to might be down or having issues. You can force the `dcl deploy` command to deploy to a specific catalyst server instead. To deploy to a specific server, on the Decentraland Editor: 
	1. Click on the three dot menu at the top right of the sidebar, next to the green reload arrow button, select `Deploy Scene To Custom Catalyst`
	2. Enter the address of the server, for example `peer-testing.decentraland.org`
	3. Approve the transaction


	To do this via the CLI:

	`dcl deploy --target-content <server-name>`

	For example:

	`dcl deploy --target-content peer-ec1.decentraland.org`

	See [catalyst-monitor](https://decentraland.github.io/catalyst-monitor/) for a status check of all the servers in the catalyst network. You can also copy the addresses of each one, from the top of each card.

- Check your scene's `package.json`. A common problem is that there's a `bundleDependencies` and also a `bundledDependencies` (extra d) section. This can sometimes result from running different Node versions on the same project. Delete `bundleDependencies`, which relates to older Node versions.
 
### Issue: Running `dcl deploy` or `dcl build` reports type errors

Your scene might have type errors reported by TypeScript, for example stating that a certain variable might be type `any` or that `undefined` or `null` are not allowed. When running `dcl deploy`, it also runs `dcl build`, which is a bit more strict with these checks than `dcl start`.

Unlike JavaScript, TypeScript enforces strict typing of all variables. Even though your scene is written in such a way that for example a certain value will never be `undefined`, TypeScript needs to know what would happen in that scenario, or you need to explicitly clarify that the value can only be for example a string.

As an alternative, you can run `dcl deploy --skip-build` to skip the running of `dcl build`, and prevent these checks from running.


### Issue: I deployed my scene but I don't see the changes when I enter Decentraland

- Keep in mind that it can take a few minutes for new content to be propagated throughout all of the servers in the catalyst network, give it a little time.

- See [Verify Deployment Success]({{< ref "/content/creator/scenes/getting-started/preview-scene.md#verify-deployment-success" >}}) for instructions on how you can ensure that the content was properly propagated to all servers.

### Issue: Once deployed, some 3d models are missing

- Make sure the 3d models are all within the scene boundaries, even their bounding boxes. When running in preview, any 3d models that extend beyond the scene boundaries are marked in red and their bounding boxes are marked. In the deployed scene, these models aren't rendered at all, as they could be intruding into the parcels of your neighbors.


### Issue: Once deployed, my 3d models look different


- If the textures look different, keep in mind that textures in 3d models are capped to a maximum size of 512x512 pixels. This conversion is carried out to ensure that Decentraland runs smoothly for everyone.

- If models look different, there could be an issue with the conversion of the models to asset bundles. Read more about asset bundle compression [here]({{< ref "/content/creator/scenes/optimizing/performance-optimization.md#asset-bundle-conversion" >}}). 

	To validate this, try running the scene with the URL parameter `&DISABLE_ASSET_BUNDLES`. If the models look fine with this flag, the issue must be related to a bug in the conversion of the model.

	Note that the generation of compressed asset-bundle versions of your models is a process that takes the servers time (about an hour). You can check if the models are being loaded as compressed asset bundles or not by accessing the scene via the following URL:  `https://play.decentraland.zone/?renderer-branch=feat%2Fab-view`. Compressed models are tinted green, non-compressed are tinted red.

### Issue: My scene has poor FPS in production, even though it runs smoothly in preview.

Your scene's performance could be affected by neighboring scenes that follow bad practices, as they also run in parallel.  You can validate that this is the case by opening the settings and setting the line of sight to a minimum, so that only 1 parcel around your current scene is loaded.

You can reduce the line of sight even further by running your scene with the parameter `&LOS=0`, to not load any surrounding scenes at all.

If you just deployed your scene, the burden when loading the scene might also be reduced once the servers convert the 3d models in the scene to compressed asset bundles. You can check if the models are being loaded as compressed asset bundles or not by accessing the scene via the following URL:  `https://play.decentraland.zone/?renderer-branch=feat%2Fab-view`. Compressed models are tinted green, non-compressed are tinted red.

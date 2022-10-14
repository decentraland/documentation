---
date: 2021-05-17
title: Development Workflow
description: Recommended procedure for developing and testing a scene
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/dev-workflow/
url: /creator/development-guide/dev-workflow/
---

This document outlines the recommended steps involved in developing a scene for Decentraland, going from testing in the local environment to deploying to production.

## Before you begin

Please make sure you first install the CLI tools by running the following command:

```bash
npm install -g decentraland
```

See the [Installation Guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}) for more details instructions.

Make sure you also own or have deploy rights on at least one parcel of land in Decentraland.

## Local preview

To preview a scene run the following command on the scene's main folder:

```bash
dcl start
```

See [Preview your scene]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}) for more details. Check the [Debug a scene]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md#debug-a-scene">}}) for tips on how to debug any issues.

## Deploy to the test environment

Deploy your scene to the test server.

```bash
dcl deploy --target peer-testing.decentraland.org
```

To access scenes deployed to the test server, enter [_play.decentraland.org/?&CATALYST=peer-testing.decentraland.org_](https://play.decentraland.org/?&CATALYST=peer-testing.decentraland.org).

Players aren't directed to this server, so it's a safe place to test out the full flow of a scene without distractions, including multiplayer interactions, wearables, blockchain mainnet interactions and everything you'd find in the production environment.

> Note: The catalyst test server works like any other node in the catalyst network. This server only receives updates from the rest of the network, it doesn't push any changes. All scenes available in the production environment are in this server, but scenes deployed to this server don't get propagated to other servers.

Content deployed to the test server is not private. It could potentially be visited by anyone who intentionally enters this server.

> Tip: If you want to hide your content from any possible leaks, you might want to consider launching your own Catalyst server, and not submit it to the DAO for adding to the network. That way this server behaves just like the test server, but its address isn't known to others. See the [How to run a catalyst]({{< ref "/content/contributor/tutorials/how-to-run-a-catalyst.md">}}) for instructions on how to do this.


## Upload a scene to decentraland

Once you're happy with your scene, it's time to publish it to the production environment. There all players will have access to it if they visit the scene's coordinates.

```
dcl deploy
```

Check that your scene has all the necessary metadata: name, description, a preview image, spawn points. See [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}) for details.

See [publishing]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) for more details.

> Tip: To give your new scene more visibility, consider creating an inaugural event in the [events page](https://events.decentraland.org/en/).


## Latest SDK changes

When developing a new scene, you use the `@latest` stable SDK release by default.

You can install the `@next` SDK release if you want to leverage or preview upcoming features that didn't yet make it into the latest stable release.

To do so, run the following on your scene:

`npm i decentraland-ecs@next`

> Note: Keep in mind that the @next version might suffer issues from time to time. The syntax and name of new features might change before it's released in a stable version.

You can also access the latest unreleased features by loading the version dynamically via URL parameters. Add the following to the preview URL: `&kernel-branch=main&renderer-branch=master`.

You can also access your scene in the test environment with the features from `@next` by accessing the `.zone` client.

After deploying your scene to the test server, enter the following address to view your scenes using the unreleased SDK features:

[_play.decentraland.zone/?&CATALYST=peer-testing.decentraland.org&ENV=org_](https://play.decentraland.zone/?&CATALYST=peer-testing.decentraland.org&ENV=org).

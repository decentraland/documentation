---
date: 2021-05-17
title: Development workflow
description: Recommended procedure for developing and testing a scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/dev-workflow/
weight: 2
---

This document outlines the steps recommended for developing a scene for Decentraland, from ideation to publishing and beyond.

<!-- diagram? icons? -->

- [Install the Decentraland Editor](#install-the-decentraland-editor)
- [Design your experience](#design-your-experience)
- [Where to publish](#where-to-publish)
- [Templates and examples](#templates-and-examples)
- [Art Assets](#art-assets)
- [Run a local preview](#run-a-local-preview)
- [Publish to the test server](#publish-to-the-test-server)
- [Publish to Decentraland](#publish-to-decentraland)
- [Promote](#promote)
- [Iterate](#iterate)
- [Giving back](#giving-back)


## Install the Decentraland Editor

Make sure you have the Decentraland Editor installed. 

- [Installation Guide]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}).


## Design your experience

Think about how much space you need to take up, what kind of distribution, what kinds of mechanics you want players to be able to carry out, etc. The following documents can serve as a guide:


- [UX & UI Guide]({{< ref "/content/creator/sdk7/design-experience/ux-ui-guide.md" >}})
- [Design constraints for games]({{< ref "/content/creator/sdk7/design-experience/design-games.md" >}})
- [Scene MVP guidelines]({{< ref "/content/creator/sdk7/design-experience/mvp-guidelines.md" >}})

## Where to publish

In Decentraland, content is published to adjacent plots of land in a finit amount of space. Players can freely walk from one to the other. Each scene is its own contained little world, items from one scene can't extend out into another scene, and the code for each scene is sandboxed from all others.

Permission to publish to each of these is controlled via tokens. You don't need land to develop a scene, but you will need access to land once you're ready to publish. You can also publish to Decentraland Worlds (beta), which are isolated scenes.

The following options are available:

- [Rent LAND]({{< ref "/content/player/marketplace/rentals.md" >}})
- [Purchase LAND]({{< ref "/content/player/marketplace/marketplace.md" >}})
- Obtain permissions from a land owner
- Publish to a Decentraland World, see [worlds]({{< ref "/content/creator/worlds/about.md" >}}) to learn more.
	> NOTE: The Worlds feature is still in beta.

See [Publishing options]({{< ref "/content/creator/sdk7/publishing/publishing-options.md" >}}) for more details.


## Templates and examples

When creating a new scene, choose amongst several base template scenes that include some basic code and 3d models. Use these to get started faster.

- [Awesome repository](https://github.com/decentraland-scenes/Awesome-Repository): here you can find a large collection of example scenes, each showcasing different mechanics that you can borrow. You can also clone any of these scenes and use it as a starting point.
- [Helper libraries](https://github.com/decentraland-scenes/Awesome-Repository#Libraries): these can simplify many common tasks.

## Art assets

If you're an experienced artist or you have access to someone who is, you can create custom `.gltf` or `.glb` models for your scene. See [3D model essentials]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}) for tips on how to create 3D models for Decentraland.

There are many sources to obtain free or paid art assets. For example:

- [SketchFab](https://sketchfab.com/)
- [Clara.io](https://clara.io/)
- [Archive3D](https://archive3d.net/)
- [SketchUp 3D Warehouse](https://3dwarehouse.sketchup.com/)
- [Thingiverse](https://www.thingiverse.com/) (3D models made primarily for 3D printing, but adaptable to Virtual Worlds)
- [ShareCG](https://www.sharecg.com/)
- [CGTrader](https://CGTrader.com)

## Run a local preview

To run a preview of your scene, open a Visual Studio Code window on your project's root folder and click the **Preview** button on the Decentraland Editor tab.

- [Preview your scene]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md" >}}) ) for more details. 
- Check the [Debug a scene]({{< ref "/content/creator/sdk7/getting-started/preview-scene.md#debug-a-scene" >}}) for tips on how to debug any issues.

> TIP: If you get stuck trying to debug an issue, visit the [Decentraland Discord server](https://dcl.gg/discord) to get help from other developers.

_Optional_: Your scene`s mechanics might rely on a 3rd party server to carry out player validations, permanent data storage, or other functionalities. See [Use an authoritative server]({{< ref "/content/creator/sdk7/networking/remote-scene-considerations.md#use-an-authoritative-server" >}}))

## Publish to the test server

Deploy your scene to a test server. This server is not private but only accessible via a specific URL, so players won't bump into your tested scene involuntarily.

- [Publish to the test server]({{< ref "/content/creator/sdk7/publishing/publishing.md#the-test-server" >}}).

## Publish to Decentraland

Once you're happy with your scene, it's time to publish it to the production environment. There all players will have access to it if they visit the scene's coordinates.

- [Publish to prod]({{< ref "/content/creator/sdk7/publishing/publishing.md#to-publish-the-scene" >}}).

> NOTE: Before you do, check that your scene has all the necessary metadata: name, description, a preview image, spawn points. See [scene metadata]({{< ref "/content/creator/sdk7/projects/scene-metadata.md" >}}) for details.


## Promote

Once your scene is out there, you want to give it visibility and have people visit it. There are a number of ways you can shine a spotlight on it:

- Share it on social media
- [Events page](https://events.decentraland.org/en/): create an event to promote your scene 
- [Places page](https://places.decentraland.org/): ensure your scene is well positoned here, encourage players to vote your scene to get more visibility 

<!-- - Make a proposal in the DAO to mark your scene as a [Point Of Interest (POI)]({{< ref "/content/player/dao/dao-userguide.md#binding-proposals" >}}) -->


## Iterate

One great advantage of Decentraland is that you can easily iterate over your scenes. Measure your scene's success with players, then keep publishing changes as you perfect the experience for your players.

- [Scene analytics]({{< ref "/content/creator/sdk7/other/scene-analytics.md" >}}).


## Giving back

Decentraland is a community project, the community of creators learns together and leverage each other's creations. Consider the following:

- Join the [Decentraland Discord server](https://dcl.gg/discord) and help other developers in need of advice.
- Share your scene's code as an open source repo on GitHub.
- Build a minimal example to share a specific reusable mechanic, as an open source repo on GitHub.
- Make a PR to the Awesome Repository to include your scenes.
- Write a library that encapsulates the complexity of common challenges, so others can overcome them easily.
---
date: 2022-11-04
title: SDK7 alpha testing guidelines
description: Play live audio streams in your scene.
categories:
  - development-guide
aliases: 
  - /creator/development-guide/sdk7/beta-testing-guidelines/
type: Document
url: /creator/development-guide/sdk7/alpha-testing-guidelines/
weight: 2000
---

SDK version 7 is currently being tested as an alpha release. We're gathering feedback from the community, to ensure the release doesn't present any major issues and that the experience of using it is good.

We encourage you to test and experiment with this new SDK as much as possible, but please don't build any events or important scenes that rely on content written with SDK7. As things are still in a alpha stage, breaking changes are still possible.

## Documentation

Find the full documentation for SDK7 in under the **SDK7** section of the documentation.

## Using the playground

To try out SDK7, visit [the playground](https://playground.decentraland.org/). Write SDK7 code on the left of the screen, and see the resulting scene on the right. As you change the code, the scene is updated automatically.

If you run into any issues, please copy a URL to the current setup of your scene with the **Share** button, and [report an issue](#reporting-issues) including that link to your code.

## Running in preview

To run a scene using SDK7 in preview

1. Make sure you have the latest version of the Decentraland command line
   ```bash
   npm i -g decentraland@latest
   ```
2. In a new directory, create a new SDK7 project
   ```bash
   dcl init --template https://github.com/decentraland/sdk7-scene-template/archive/refs/heads/main.zip
   ```
3. Run previews with `dcl start`, the same as with older versions. Edit or add any additional files you want into the folder structure to build out your scene.

> Note: Notice that scenes that use SDK7 don't have the `decentraland-ecs` package installed. Instead, they have the `@dcl/sdk` package.

## In production

You can deploy scenes with SDK7 using `dcl deploy` the same as any scene with SDK6.

> Note: Please note that this is not yet a stable version. Breaking changes are possible, so avoid using this version for scenes that are of critical importance.

## Example scenes

You can find more example scenes written with SDK7 here:

- [SDK7 Scene Template](https://github.com/decentraland/sdk7-scene-template)
- [Goerli Plaza](https://github.com/decentraland-scenes/sdk7-goerli-plaza)

## Pending features

The SDK7 alpha includes almost complete feature parity with everything that's possible with older versions of the SDK. A few features have been left out of the initial scope, in order to tackle them before the first official non-alpha release. The following features are not available in the current alpha:

- Video texture
- Textures on UI elements
- Button events on UI elements
- Input boxes on the UI
- Trigger the playing of an emote on the avatar

A couple of features are intended to be re-implemented in future releases following Data Oriented Programming principles. These for now are still exposed as legacy functions that are marked as deprecated.

- Functions to get player data, like `getUserData`, `getPlayersInScene`, or
- Functions to get data about the context, like `getDecentralandTime`, `getCurrentRealm`, `getPlatform`, `getPortableExperiencesLoaded`
- Observables for player events like `onEnterSceneObservable`, `onLeaveSceneObservable`, `onPlayerExpressionObservable`, `onPlayerClickedObservable`, `onPointerLockedStateChange`, `onIdleStateChangedObservable`, or `onProfileChanged`
- Observables for other events like `onSceneReadyObservable`, `onRealmChangedObservable`
- The MessageBus

## Reporting issues

See the list of existing known issues [here](https://github.com/orgs/decentraland/projects/20/views/13).

If you run into any bugs, please report an issue in the [SDK](https://github.com/decentraland/sdk/issues) repository.

We ask you to please detail how to reproduce the issue as much as possible. The ideal way to report a bug is to include a link to the [playground](https://decentraland.github.io/sdk-playground/), showcasing a minimal scene where this issue can be observed. Click the **Share** button in the playground to copy a URL that includes the code that you're currently using. That way, the issue is 100% reproducible by whoever is debugging it.

## Submit feedback

Once you've had a chance to try the new SDK, please fill in the [feedback form](https://form.typeform.com/to/YDwCljEz).

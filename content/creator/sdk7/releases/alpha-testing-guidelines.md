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


## Documentation

Find the full documentation for SDK7 in under the **SDK7** section of the documentation.

## Using the playground

To easily try out SDK7, visit [the playground](https://playground.decentraland.org/). Write SDK7 code on the left of the screen, and see the resulting scene on the right. As you change the code, the scene is updated automatically.

If you run into any issues, please copy a URL to the current setup of your scene with the **Share** button, and [report an issue](#reporting-issues) including that link to your code.

## Using SDK 7

Install the SDK 7 version of the editor on VS Studio Code. To install it, simply search in the extension market for **Decentraland Editor SDK7**.

{{< hint warning >}}
**📔 Note**:  Notice that scenes that use SDK7 don't have the `decentraland-ecs` package installed. Instead, they have the `@dcl/sdk` package.
{{< /hint >}}

## In production

You can deploy scenes with SDK7 via the **Publish Scene** button on the Editor.


## Example scenes

You can find more example scenes written with SDK7 here:

- [SDK7 Scene Template](https://github.com/decentraland/sdk7-scene-template)
- [Goerli Plaza](https://github.com/decentraland-scenes/sdk7-goerli-plaza)

<!-- ## Pending features

A couple of features are intended to be re-implemented in future releases following Data Oriented Programming principles. These for now are still exposed as legacy functions that are marked as deprecated.

- Functions to get player data, like `getUserData`, `getPlayersInScene`, or
- Functions to get data about the context, like `getDecentralandTime`, `getRealm`, `getPlatform`, `getPortableExperiencesLoaded`
- Observables for player events like `onEnterSceneObservable`, `onLeaveSceneObservable`, `onPlayerExpressionObservable`, `onPlayerClickedObservable`, `onPointerLockedStateChange`, `onIdleStateChangedObservable`, or `onProfileChanged`
- Observables for other events like `onSceneReadyObservable`, `onRealmChangedObservable`
- The MessageBus -->

## Reporting issues

See the list of existing known issues [here](https://github.com/orgs/decentraland/projects/20/views/13).

If you run into any bugs, please report an issue in the [SDK](https://github.com/decentraland/sdk/issues) repository.

We ask you to please detail how to reproduce the issue as much as possible. The ideal way to report a bug is to include a link to the [playground](https://decentraland.github.io/sdk-playground/), showcasing a minimal scene where this issue can be observed. Click the **Share** button in the playground to copy a URL that includes the code that you're currently using. That way, the issue is 100% reproducible by whoever is debugging it.

## Submit feedback

Once you've had a chance to try the new SDK, please fill in the [feedback form](https://form.typeform.com/to/YDwCljEz).

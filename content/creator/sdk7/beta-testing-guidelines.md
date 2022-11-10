---
date: 2022-11-04
title: SDK7 Beta testing guidelines
description: Play live audio streams in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/beta-testing-guidelines/
weight: 2000
---


SDK version 7 is currently being tested as a beta release. We're gathering feedback from the community, to ensure the release doesn't present any major issues and that the experience of using it is good.

We encourage you to test and experiment with this new SDK as much as possible, but please don't build any events or important scenes that rely on content written with SDK7. As things are still in a beta stage, breaking changes are still possible.

## Documentation

Find the full documentation for SDK7 in this branch of the Documentation site. Navigate the tree under **SDK7** to find information about every component and thing you can do.

Note that this is an unpublished branch of the Decentraland documentation, under [sdk7.new-docs-6m4.pages.dev](https://sdk7.new-docs-6m4.pages.dev).

## Using the playground

To try out SDK7, visit [the playground](https://decentraland.github.io/sdk-playground/). Write SDK7 code on the left of the screen, and see the resulting scene on the right. As you change the code, the scene is updated automatically.

If you run into any issues, please copy a URL to the current setup of your scene with the **Share** button, and [report an issue](#reporting-issues) including that link to your code.


## Running in preview

To run a scene using SDK7 in preview

1) Make sure you have the @next version of the CLI

`npm i -g decentraland@next`

2) Manually copy this [template scene](https://github.com/decentraland/ecs7-template) into a new folder.

3) Run previews with `dcl start`, the same as with older versions. Edit or add any additional files you want into the folder structure to build out your scene. 

> Note: Notice that scenes that use SDK7 don't have the `decentraland-ecs` package installed. Instead, they have the `@dcl/sdk` package.

## In production

You can deploy scenes with SDK7 using `dcl deploy` the same as any scene with SDK6.

> Note: Please note that this is not yet a stable version. Breaking changes are possible, so avoid using this version for scenes that are of critical importance.

## Example scenes

You can find more example scenes written with SDK7 here:

- [Goerli plaza](https://github.com/decentraland-scenes/sdk7-goerli-plaza)


## Reporting issues

If you run into any bugs, please report an issue in the [SDK](https://github.com/decentraland/sdk/issues) repository.

We ask you to please detail how to reproduce the issue as much as possible. The ideal way to report a bug is to include a link to the [playground](https://decentraland.github.io/sdk-playground/), showcasing a minimal scene where this issue can be observed. Click the **Share** button in the playground to copy a URL that includes the code that you're currently using. That way, the issue is 100% reproducible by whoever is debugging it.


## Submit feedback

Once you've had a chance to try the new SDK, please fill in the [feedback form](https://form.typeform.com/to/YDwCljEz).
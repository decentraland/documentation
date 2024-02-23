---
date: 2022-11-04
title: SDK7 feedback guidelines
description: Guidelines on how to provide feedback about SDK7
categories:
  - development-guide
aliases:
  - /creator/development-guide/sdk7/beta-testing-guidelines/
  - /creator/development-guide/sdk7/alpha-testing-guidelines/
type: Document
url: /creator/development-guide/sdk7/testing-guidelines/
weight: 20
---

## Documentation

Find the full documentation for SDK7 in under the **SDK7** section of the documentation.

## Using the playground

To easily try out SDK7, visit [the playground](https://playground.decentraland.org/). Write SDK7 code on the left of the screen, and see the resulting scene on the right. As you change the code, the scene is updated automatically.

If you run into any issues, please copy a URL to the current setup of your scene with the **Share** button, and [report an issue](#reporting-issues) including that link to your code.

## Using SDK 7

Install the SDK 7 version of the editor on VS Studio Code. To install it, simply search in the extension market for **Decentraland Editor SDK7**.

{{< hint warning >}}
**📔 Note**: Notice that scenes that use SDK7 don't have the `decentraland-ecs` package installed. Instead, they have the `@dcl/sdk` package.
{{< /hint >}}

## In production

You can deploy scenes with SDK7 via the **Publish Scene** button on the Editor.

## Example scenes

You can find more example scenes written with SDK7 here:

- [SDK7 Scene Template](https://github.com/decentraland/sdk7-scene-template)
- [Goerli Plaza](https://github.com/decentraland/sdk7-goerli-plaza)

## Reporting issues

If you encounter a problem, please see [Report a bug]({{< ref "/content/creator/sdk7/debugging/report-bug.md">}}).

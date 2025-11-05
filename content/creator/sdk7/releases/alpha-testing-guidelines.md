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

Install the [Creator Hub]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}).

{{< hint warning >}}
**📔 Note**: Notice that scenes that use SDK7 don't have the `decentraland-ecs` package installed. Instead, they have the `@dcl/sdk` package.
{{< /hint >}}

## In production

You can deploy scenes with SDK7 via the **Publish** button on the Scene Editor.

## Example scenes

You can find more example scenes written with SDK7 here:

- [Scene examples](https://studios.decentraland.org/resources)


## Reporting issues

If you encounter a problem, please see [Report a bug]({{< ref "/content/creator/sdk7/debugging/report-bug.md">}}).

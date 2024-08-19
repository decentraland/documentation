---
date: 2023-01-04
title: Version support agreement
description: Version support agreement
categories:
  - development-guide
type: Document
url: /creator/releases/version-agreement
weight: 2
---

This document describes the versioning policy applied to both the Scene Editor (in the Creator Hub) and the scripting framework (the `@dcl/sdk` package).

The goal of this versioning policy is to forge a contract between the Decentraland Foundation's SDK team and content creators, to establish clear expectations and allow content creators to plan their work accordingly.

<!-- TODO: What about support from other teams? Do we have a commitment for content with older versions to keep working too? -->

## Definitions

- _Version number_ -- a unique identifier for a publicly available version of software. This identifier consists of a _major version_ number and a _minor version_ number, separated dots (for example, 7.2).

- _Version family_ -- all versions that have identical major version form a family. We call version A a _successor_ of version B if A and B belong to same family and A minor number is higher than B's (for example, 7.11 is a successor of 7.10).

- _Breaking change_ -- a change that forces a user to change their code or assets to keep them in functioning state. For example, a property changes name, and forces the user to change that property name every time it's used throughout their code.

- _Non-breaking change_ -- a change that does not require any action by a user, the behavior and properties of the user's code and assets are unchanged if they migrate their scene.

- _Stable version_ -- a version that forbids breaking changes in all its successors (which are all considered as stable too). Any breaking change must be introduced only through creation of a new version family by incrementing the major version number, however see caveat in the [breaking changes](#breaking-changes) section. Non-breaking changes are reflected through incrementing the minor version number.

- _Unstable version_ -- a version that allows breaking changes in its successors. Breaking changes may be introduced by incrementing the minor version number.

## Support policy

In every stable version family, the Decentraland Foundation supports only the latest minor version. At any given time there should be at most two supported families.

For example, if the latest minor version of the 6.x family is 6.11, and the latest minor version of the 7.x family is 7.3, content creators are expected to develop their scenes on either 6.11 or 7.3. Scenes that were developed and published with version 6.10 or older will most likely keep working and players will be able to enjoy them. However, if these older scenes experience any issue, they must first be updated to a supported version, and the issue will only be investigated if it still occurs in a supported version.

The Scene Editor offers to automatically update the scripting package of all scenes within a same version family, so that all developers are using the latest supported version when they develop their scenes.

## Feature development

New features will only be released into the latest version in development. As soon as the development team starts work in a new version family, older version families that remain in support will only receive major bugs fixes, and no additional features will be implemented.

## Breaking changes

Breaking changes should only occur in major releases. There should be no breaking changes within the stable minor releases of a same version family, except in case of an emergency and absence of any other means to address it. Breaking changes within a minor release are a drastic measure that the developers will avoid at all costs. New minor releases will extend the capabilities of the existing syntax, but should never change what the established syntax produces, except when fixing bugs.

### Isolated changes

On very rare occasions, it could be preferable to make a small, isolated breaking change, if this will only cause inconvenience to a small subset of users. (Creating a new major version is an inconvenience to all users.) In this case, the SDK might deprecate a feature, but must continue to support the feature for a reasonable amount of time.

### Emergency changes

In certain exceptional cases, such as security concerns or regulatory requirements, any feature may be changed in a breaking manner regardless of its stability level, and a deprecation is not promised in these situations.

## Stable and unstable releases

### Alpha

Whenever a new major release is introduced, a few initial minor releases may be labeled as unstable **alpha** versions. Breaking changes must be allowed and expected in alpha releases, and users must have no expectation of stability.

Developers are free to experiment with these alpha versions, but they're not encouraged to publish content built with unstable alpha versions, as there is no guarantee that the content will keep working after subsequent changes. It's also not recommended to begin large complicated migrations at this point, since more changes may be required before the next stable release.

### Beta

Once a version family reaches a certain level of maturity, a **beta** release is made available. A beta release is be considered complete and ready to be declared stable, subject to public testing.

Beta version families should be as stable as possible; however, they are permitted to change over time. These changes should be minimal but may include breaking changes. Breaking changes must be made only after a reasonable deprecation period to give content creators the opportunity to migrate their scenes. This deprecation period must be defined at the time of introducing a breaking change.

Beta version families should only be in beta for a limited period of time, specified at the time of being marked beta. They should be promoted to stable if no issues are found in that period. The length of this time period may vary case by case, but a good rule of thumb is 90 days.

Content written with the syntax of a beta version should be effortless to migrate to the next versions within that family tree. It's still not advisable to develop content for major events with a beta version, as testing is still in progress and bugs are still likely.

### Stable

Once the beta time period is over without major issues, the version family is considered **stable** and there should be no further changes to the syntax, other than addition of new features. From this point onwards, the version is considered the recommended and encouraged option for all developers to use.

A stable version family must be fully-supported over its lifetime. There must be no breaking changes, subject to the caveats described below.

## Unstable features in stable releases

Specific features in an release may have different stability levels from the release as a whole. This can be either because the feature has recently been introduced, and requires more testing, or because it's destined to be replaced soon.

For example, a new type of component could be introduced as alpha in an already stable release of the SDK framework, as this particular component may still require its own testing cycle. It can then undergo the versioning flow described above, going from alpha, to beta, to stable.

Any feature from a stable release that is not considered stable should be clearly labeled as such in the documentation. Creators who make use of unstable features must be aware that the feature could potentially undergo breaking changes. Any breaking changes will be communicated clearly, including migration guides, and there will be a transition period for creators to adjust their scene's code.

<!-- In exceptional cases, a stable (beta or GA) version may include specific features grouped into a legacy namespace that is not considered to be part of the supported release and is meant to be deprecated in the future. This namespace will be labeled as unstable, and the documentation will make it clear when this is the case. The purpose of leaving these legacy features is to aid in the transition between major versions, without losing any functionality. This can happen when a proper re-implementation of certain features is required, but it would delay releasing the stable version too much.  -->

## How long do we support a stable version family?

Once a new version family becomes stable (7.x), the team commits to support (major bugfixes) on the previous version (6.x) for several months, to give creators plenty of time to migrate. The amount of months is determined in a case-by-case basis, depending on the migration effort required by creators to migrate.

## Pre-released versions

It's always possible to access the most recent additions to the scripting framework by installing the `@next` version of the `@dcl/sdk` package into a scene.

The features in this branch may be unstable or undocumented, as they're not pushed as part as an officially supported version of the SDK.

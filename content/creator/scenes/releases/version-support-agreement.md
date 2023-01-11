---
date: 2023-01-04
title: Version support agreement
description: Version support agreement
categories:
  - development-guide
type: Document
url: /creator/releases/releases
weight: 2
---


This document describes the versioning policy applied to both the Decentraland Editor and the scripting framework (the `@dcl/sdk` package).

The goal of this versioning policy is to forge a contract between the Decentraland Foundation's SDK team and content creators, to establish clear expectations and allow content creators to plan their work acoordingly.

<!-- TODO: What about support from other teams? Do we have a commitment for content with older versions to keep working too? -->

## Definitions

* *Version number* -- a unique identifier for a publicly available version of software. This identifier consists of a *major version* number and a *minor version* number, separated dots (for example, 7.2).

* *Version family* -- all versions that have identical major version form a family. We call version A a *successor* of version B if A and B belong to same family and A minor number is higher than B's (for example, 7.11 is a successor of 7.10).

* *Breaking change* -- a change that forces a user to change their code or assets to keep them in functioning state. For example, a property changes name, and forces the user to change that property name every time it's used throughout their code.

* *Non-breaking change* -- a change that does not require any action by a user, the behavior and properties of the user's code and assets are unchanged if they migrate their scene.

* *Stable version* -- a version that forbids breaking changes in all its successors (which are all considered as stable too). Any breaking change must be introduced only through creation of a new version family by incrementing the major version number. Non-breaking changes are reflected through incrementing the minor version number.

* *Unstable version* -- a version that allows breaking changes in its successors. Breaking changes may be introduced by incrementing the minor version number.

## Support policy

In every stable version family, the Decentraland Fountation supports only the latest minor version. At any given time there should be at most two supported families. 

For example, if the latest minor version of the 6.x family is 6.11, and the latest minor version of the 7.x family is 7.3, content creators are expected to develop their scenes on either 6.11 or 7.3. Scenes that were developed and published with version 6.10 or older will most likely keep working and players will be able to enjoy them. However, if these older scenes experience any issue, they must first be updated to a supported version, and the issue will only be investigated if it still occurs in a supported version.

The Decentraland Editor automatically updates the scripting package of all scenes within a same version family, so that all developers are using the latest supported version when they develop their scenes.

## Feature development

New features will only be released into the latest version in development. As soon as the development team starts work in a new version family, older version families that remain in support will only receive major bugs fixes, and no additional features will be implemented.

## Breaking changes

Breaking changes should only occur in major releases. There should be no breaking changes within the stable minor releases of a same version family, except in case of an emergency and absence of any other means to address it. Breaking changes within a minor release are a drastic measure that the developers will avoid at all costs. New minor releases will extend the capabilities of the existing syntax, but should never change what the established syntax produces, except when fixing bugs.

## Stable and unstable releases

Whenever a new major release is introduced, a few initial minor releases may be labeled as unstable **alpha** versions.  These versions may suffer from breaking changes going forward.

Developers are free to experiment with these alpha versions, but they're not encouraged to publish content built with unstable alpha versions, as there is no guarantee that the content will keep working after subsequent changes. It's also not recommended to begin large complicated migrations at this point, since more changes may be required before the next stable release.

Once a major release reaches a certain level of maturity, a **beta** release can be made available. As of the release of the first beta version in a version family, the version family is considered **stable** and there should be no further changes to the syntax, other than addition of new features. Content written with the syntax of a beta version should be effortless to migrate to the next versions within that family tree. It's still not adviseable to develop content for major events with a beta version, as testing is still in progress and bugs are still likely.

Once the development of the version family is considered to be ready for production, a **GA** (general availability) release can be made available. From this point onwards, the version is considered the recommended and encouraged option for all developers to use.


## How long do we support a stable version family?

Once a new version family becomes stable (7.x), the team commits to support (major bugfixes) on the previous version (6.x) for several months, to give creators plenty of time to migrate. The amount of months is determined in a case-by-case basis, depending on the migration effort required by creators to migrate.


## Pre-released versions

It's always possible to access the most recent additions to the scripting framework by installing the `@next` version of the `@dcl/sdk` package into a scene.

The features in this branch may be unstable or undocumented, as they're not pushed as part as an officially supported version of the SDK.
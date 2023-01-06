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

The goal of this versioning policy is to forge a contract between the Decentraland Foundation's SDK team and content creators: which versions of the SDK are supported and how long the support lasts.

<!-- TODO: What about support from other teams? Do we have a commitment for content with older versions to keep working too? -->

## Definitions

* *Version number* -- a unique identifier of publicly available version of software which consists of *major version* number and *minor version* number separated by a dot (for example, 7.11).

* *Version family* -- all versions that have identical major version form a family. We call version A a *successor* of version B if A and B belong to same family and A minor number is higher than B's (for example, 7.11 is a successor of 7.10).

* *Breaking change* -- a change that forces a user to change their code or assets to keep them in functioning state. TODO: compile a list of common breaking changes.

* *Non-breaking change* -- a change that does not require any action by a user, the behavior and properties of user's code and assets are unchanged.

* *Stable version* -- a version that forbids breaking changes in all its successors (which all considered as stable too). Any breaking change must be introduced only through creation of new version family by incrementing major version number. Non-breaking changes are reflected through incrementing minor version number.

* *Unstable version* -- a version that allows breaking changes in its successors. Breaking changes may be introduced by incrementing minor version number.

## Support policy

In every stable version family we support only the latest minor version. At any given time there should be at most two supported families.

New features are only going to be added to the latest major version. Any older major versions that remain in support will only receive fixes for major bugs.

## Stable and unstable releases



## How long do we support a stable version family?

Let's assume we start with a stable version 7.1 released publicly. We continue the development of 7.x version family for as long as possible, adding new features and bugfixes while avoiding breaking changes.

```
7.1-stable -> 7.2 -> ... -> 7.15
```

Once further development becomes unbearably hindered or impossible by stability requirement, we create a new version family (in our example, 8.x) that initially could be declared unstable. Starting from this moment, previous family (7.x) should not receive any new features and receive only major bugfixes.

```
7.1-stable -> 7.2 -> ... -> 7.15
                             |
                             |-> 8.0-unstable
```

Once a new version family becomes stable (8.x), a team commits to support (major bugfixes) previous version (7.x) for N months (case-by-case basis), thus giving creators plenty of time to migrate.

```
7.1-stable -> 7.2 -> ... -> 7.15 -> ... -> 7.21 (major bugfixes)
                             |
                             |-> 8.0-unstable -> ... -> 8.7-stable
```

## Pre-released versions

It's always possible to access the most recent additions to the repository by installing the `@next` version of the `@dcl/sdk` package into a scene.

The features in this branch may be unstable or undocumented, as they're not pushed as part as an officially supported version of the SDK.
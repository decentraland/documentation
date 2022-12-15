---
title: "Overview"
sidebartitle: Overview
url: "/contributor/content/overview"
weight: 1
---

Everything you can find inside the virtual world of Decentraland is hosted in a distributed network of servers known as [[Catalysts]], that can be used (among other things) to upload and download content.

The complete API of the Catalyst is available in [[its own reference]]. Here, we'll focus on understanding how content is organized, and how it can be discovered and downloaded. 

All of the important concepts mentioned below are further described in their own pages.

## Files, Entities, Pointers

There are three layers in Decentraland's content system: [[files]] are packaged inside [[entities]], and entities are discovered using [[pointers]].

!!diagram showing relation

Files are stored in a decentralised file-system resembling IPFS, and automatically synchronized across content servers. They are identified by a unique string ID that is computed from the file's content, and both the identifier and the content are **immutable**. There is no such thing as updating a file. Instead, replacement files are uploaded and stale files are deleted.

Entities are atomic packages of files and metadata, and represent actual content found in the world, such as scenes and wearable items. Just like the individual files they contain, they are immutable and identified by a unique string ID computed their from content. All entities have an owner, who possesses the private keys required to manage them.

Pointers are stable references that can be resolved to the ID of an entity. When the entity is replaced (i.e. the owner uploads a new package, an the old one is deleted), the contained files and metadata are different and so are their identifiers, but pointers stay the same and are redirected to the new version.


## Snapshots

Content servers also host large line-separated-JSON files with summaries of all active entities (i.e. those currently referenced by pointers) at a certain point in time. These are called [[snapshots]], and can be used to explore all available content.

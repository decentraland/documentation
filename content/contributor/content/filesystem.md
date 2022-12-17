---
title: "File System"
sidebartitle: File System
url: "/contributor/content/filesystem"
weight: 2
---

Underlying the different content APIs in the Decentraland protocol is an implementation of a distributed file system. Each [[Catalyst]] server holds a copy of the entire storage, and synchronizes the updates it receives with other instances.

> !!INFO
> When a change is made in the distributed file-system, it takes about 4 seconds for the updated metadata to propagate through the Catalyst network. 
>
> _!!Verify this, I only heard it without thinking, what about the entity's files? Is it atomic?_

Files uploaded to the system are **immutable**. Once created and indexed, neither their identifier
nor their contents change. They can be updated only in the sense that a new version is uploaded and
applications choose to use it, while the old one can be discarded.

## File identifiers

Decentraland's file system is organized into a flat index (i.e. there is no natural hierarchy
of directories), where each file is identified by a unique string.

Identifier strings are [[base32]] encodings of a !!37-byte handle, calculated using the [[IPFS CID v1]] algorithm, which depends on the file's contents. They look like this:

```
bafybeicgclohdfaccu2sqqkzrzuenjxzcry3m5vcb4mpxgucjl3oheq5tq
```

The first few bytes contain information about the encoding and version of the identifier itself, and the rest is a SHA-256 hash.

> !!NOTE
> For historical reasons, some APIs call the file identifier _hash_ rather than _id_. They refer to the same thing.

In practice, these details are not necessary to discover and download content. Most clients of the protocol can treat identifiers like opaque strings without losing capabilities.

## Ownership and Persistence

Most of the files stored in the network are associated to an [[entity]] owned by an Ethereum account. The owner is the only one allowed to update the entity, indirectly enforcing permissions for the related files.

[[Catalyst]] servers are required by protocol to always store the latest version of an entity, and thus all the associated files, but may choose whether to retain old versions according to their individual configuration.

## Downloading Files

The [[`/contents/<fileId>` endpoint]] of the content server can be used to download any file.

## Uploading Files

Files are uploaded to content servers during the deployment of an [[entity]]. Only a few special files, such as [[snapshots]], are independent from any particular entity.
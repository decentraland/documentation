---
title: "File System"
sidebartitle: File System
url: "/contributor/content/filesystem"
weight: 2
---

Underlying the different content APIs in the Decentraland protocol is an implementation of a distributed file system. Each content server holds a copy of the entire storage, and synchronizes the updates it receives with other instances.

Files uploaded to the system are **immutable**. Once deployed, neither their identifier
nor their contents change. They can be updated only in the sense that a new version is uploaded and
applications choose to use it, while the old one can be discarded.

You can experiment with files in the [practice]({{< relref "practice" >}}) section.

## File identifiers {#identifiers}

Decentraland's file system is organized into a flat index (i.e. there is no natural hierarchy
of directories), where each file is identified by a unique string.

Identifier strings are prefixed [base32](https://en.wikipedia.org/wiki/Base32) encodings of the file content's SHA-256 hash, using the [IPFS CID v1](https://docs.ipfs.tech/concepts/content-addressing/) algorithm. They look like this:

```
bafybeicgclohdfaccu2sqqkzrzuenjxzcry3m5vcb4mpxgucjl3oheq5tq
```

The prefix in the first few bytes indicates the encoding, version and hash type of the identifier itself.

{{< info >}}
For historical reasons, some APIs call the file identifier _hash_ rather than _id_, but they refer to the same thing. You may also find legacy identifiers in old content that look a little different.
{{< /info >}}

In practice, these details are not necessary to discover and download content. Most clients of the protocol can treat identifiers like opaque strings without losing capabilities.

Note that modern CIDv1 identifiers are compatible with IPFS, yielding the same CID for the same file, so IPFS can be used as the file provider.

## Ownership and Persistence

Except for [snapshots]({{< relref "snapshots" >}}), files stored in the network are associated to an [entity]({{< relref "entities" >}}) owned by an Ethereum account. The owner is the only one allowed to update the entity and related files.

Content servers are required by protocol to always store the latest version of an entity and its files, but may choose whether to retain old versions according to their individual configuration.

## Downloading Files {#downloading}

The [`/contents/<fileId>`](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getContentFile) endpoint of the content server can be used to download any file. Their identifiers are found in the parent [entity's]({{< relref "entities" >}})'s manifest.

## Uploading Files

Files are not independently uploaded. Instead, they are packaged inside entities, and uploaded during the deployment of the entity to the content server.

See the [content creator documentation]({{< ref "/creator" >}}) for more details.
---
title: "Snapshots"
sidebartitle: "Snapshots"
url: "/contributor/content/snapshots"
weight: 5
---

Content servers will periodically compile summaries of the active entities they are hosting, called _snapshots_. They are regular [files]({{< relref "filesystem" >}}) and can be downloaded using their identifier.

Separate snapshots are created for each entity type, as well as a global one for all content. Clients that want to systematically discover content can use these files as the starting point.

You can play around with snapshots in the [practice]({{< relref "practice" >}}) section.

## Format

Snapshot files begin with this exact line:

```
### Decentraland json snapshot
```

After that, each line is a JSON document describing an [entity]({{< relref "entities" >}}) with the following fields:

| Field | Value |
| ----- | --- |
| `entityId` | The immutable identifier for this [entity]({{< relref "entities" >}}).
| `entityType` | One of `scene`, `profile`, `wearable`, `emote`, `store` or `outfits`.
| `pointers` | An array of [pointers]({{< relref "pointers" >}}) that resolve (or used to resolve) to this entity.
| `localTimestamp` | The Unix UTC timestamp when this entity was uploaded.
| `authChain` | The [authentication chain]({{< relref "entities#ownership" >}}) for this entity.

A typical entry looks like this:

```json
{
  "entityId": "bafkreigrvaqynmiglpvewwhn2yd63q5dvagrrt5jbhimzvbrn5kimj5zne",
  "entityType": "wearable",
  "pointers": ["urn:decentraland:matic:collections-v2:0x11a6879861f36cbad632a4e7226816a16139fb33:0"],
  "localTimestamp": 1671117456129,
  "authChain": [
    // ... authentication chain payloads and signatures
  ]
}
```

{{< info >}}
If you intend to parse a snapshot line by line, remember to skip the first one with the header, and be ready to handle an empty line at the end of the file.
{{< /info >}}

## Dowloading Snapshots

To locate the current set of snapshots, use the [`/snapshot`](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getActiveEntities) endpoint. The response contains a reference to a global snapshot file for all entities, as well as individual ones for every entity type. Each entry lists the Unix UTC timestamp at the time of creation. For example:

```json
{
  "hash": "bafybeiasjraajptih2ffc64hwnie2a7fbysalij7modahswdd54zrnsr4u",
  "lastIncludedDeploymentTimestamp": 1671294282247,

  "entities": {
    "wearable": {
      "hash": "bafybeihfpwdtow7qickcnryunu3smb4twrqlrmhbvzj5f25xvaxudiayyy",
      "lastIncludedDeploymentTimestamp": 1671294282247
    },
    // ... same for emote, profile, etc
  },
}
```

{{< info >}}
The global and profile snapshot files are enormous. You probably don't want to download and save them locally.
{{< /info >}}



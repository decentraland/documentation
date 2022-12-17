---
title: "Snapshots"
sidebartitle: "Snapshots"
url: "/contributor/content/snapshots"
weight: 5
---

Content servers will periodically compile summaries of the active entities they are hosting, called _snapshots_. They are regular [[files]] and can be downloaded using their ID.

Clients that want to systematically discover content can use these files as the starting point.

## Format

Snapshot files begin with this exact line:

```
### Decentraland json snapshot
```

After that, each line is a JSON document describing an [[entity]] with the following fields:

| Field | Value |
| ----- | --- |
| `entityId` | The immutable [[identifier]] for this entity
| `entityType` | One of `scene`, `profile`, `wearable`, `emote` or `store`
| `pointers` | An array of [[pointers]] that resolve (or used to resolve) to this entity. !!mmm
| `localTimestamp` | The Unix UTC timestamp when this entity was uploaded.!!why local
| `authChain` | The [[authentication chain]] for this entity.

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

> !!INFO
> If you intend to parse a snapshot line by line, remember to skip the first one.

## Dowloading Snapshots

To locate the current set of snapshots, use the [[`/snapshot` endpoint]]. The response contains referecenes to snapshot files for each entity type, as well as the Unix UTC timestamp of their creation. For example:

```json
{
  "entities": {
    "profile": {
      "hash": "bafybeihfpwdtow7qickcnryunu3smb4twrqlrmhbvzj5f25xvaxudiayyy",
      "lastIncludedDeploymentTimestamp": 1671294282247
    },
    // ... same for emote, wearable, etc
  },
  "hash": "bafybeiasjraajptih2ffc64hwnie2a7fbysalij7modahswdd54zrnsr4u",
  "lastIncludedDeploymentTimestamp": 1671294282247
}
```



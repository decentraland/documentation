---
title: "Snapshots"
sidebartitle: "Snapshots"
url: "/contributor/content/snapshots"
weight: 5
---

Content servers will periodically compile summaries of the active entities they are hosting, called _snapshots_. They are regular [files]({{< relref "filesystem" >}}) and can be downloaded using their identifier.

Snapshots are created on a daily, weekly, monthly and yearly basis. Each contains the set of active entities that changed since the prior snapshot for that range.

Snapshots will contain conflicting versions of the same entities (i.e. different [manifest files]({{< relref "entities#properties" >}}) associated to the same pointer) as they are updated. When scanning them, clients should keep the version in the most recent snapshot. Since content servers are allowed to delete inactive files, stale entity versions are not guaranteed to be available for download.

When a new snapshot _replaces_ older ones (e.g. a weekly snapshot that combines a series of daily ones), its metadata indicates which prior files are replaced so clients don't need to download them. 

The full set of active entities can be discovered by combining all the available snapshots (more on this below), keeping the most recent entity referenced by each [pointer]({{< relref "pointers" >}}) discovered along the way.

You can experiment with snapshots using working code in the [practice]({{< relref "practice" >}}) section.


## Discovering Snapshots {#discover}

To locate the current set of snapshots, use the [`snapshots` endpoint](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getSnapshots). The response contains an array of items with these fields:

| Field | Value |
| ----- | --- |
| `generationTimestamp` | The Unix UTC timestamp when this snapshot was created. 
| `hash` | The snapshot [file]({{< relref "filesystem" >}}).
| `numberOfEntities` | The number of entries in the snapshot file.
| `replacedSnapshotHashes` | An array with the `hash` of any snapshots replaced by this one.
| `timeRange.initTimestamp` | The Unix UTC timestamp (in milliseconds) for the beginning of the snapshot range.
| `timerange.endTimestamp` | The Unix UTC timestamp (in milliseconds) for the end of the snapshot range.

For example:

```json
{
  "generationTimestamp": 1684979298844,
  "hash": "bafybeiflmm46nr4vv2h3wuzbx3pukcz7ju4fhbfzt6yxmoo533uktlgru4",
  "numberOfEntities": 12345,
  "replacedSnapshotHashes": [ "bafybeicw6x75ieaxfwynekbyhpcsgctpjkt6cb4j6oa7s57qjj6e4b5phd" ],
  "timeRange": {
     "initTimestamp": 1684281600000,
     "endTimestamp": 1684886400000
  }
}
```

## Downloading Snapshots {#download}

Using the `hash` field of a snapshot, clients can download the associated  containing entities created or updated in that time range.

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
| `entityTimestamp` | The Unix UTC timestamp (in milliseconds) when this entity was uploaded.
| `authChain` | The [authentication chain]({{< relref "entities#ownership" >}}) for this entity.

A typical entry looks like this:

```json
{
  "entityId": "bafkreigrvaqynmiglpvewwhn2yd63q5dvagrrt5jbhimzvbrn5kimj5zne",
  "entityType": "wearable",
  "pointers": ["urn:decentraland:matic:collections-v2:0x11a6879861f36cbad632a4e7226816a16139fb33:0"],
  "entityTimestamp": 1671117456129,
  "authChain": [
    // ... authentication chain payloads and signatures
  ]
}
```

{{< info >}}
If you intend to parse a snapshot line by line, remember to skip (or better still, validate) the first one with the header, and be ready to handle an empty line at the end of the file.
{{< /info >}}


### Starting an Entity Index {#index-start}

Clients that want to index the entire set of active entities should process all currently available snapshots, and keep the most recent [entity]({{< relref "entities" >}}) for each [pointer]({{< relref "pointers" >}}).

The simplest strategy is to process snapshots in reverse-chronological order (i.e. most recent first), ignoring pointers that have already been discovered, in order to keep the reference to the latest entity.

In pseudo-code:

```py
# Download the current set of snapshots, and sort them from newest to oldest:
snapshots = get_snapshots()
snapshots.sort('timeRange.initTimestamp', DESCENDING)

seen_pointers = set()

# Process snapshots, keeping the newest entity for each pointer:
for snapshot in snapshots:
    items = get_snapshot_items(snapshot) 

    for item in items:
        if any(pointer in seen_pointers for pointer in item.pointers):
            discard(item)
        else:
            keep(item)
            seen_pointers.update(item.pointers)
```

Since individual entities can be referenced by multiple pointers (as is commonly the case with [scenes]({{< relref "entity-types/scenes" >}})), all of them must be checked before choosing to keep or discard the item.

{{< info >}}
Snapshot files for the longer time ranges can be very large. For development and experimentation purposes that don't require indexing the entire entity set, using the smaller snapshots is recommended. The resulting set of entities will be incomplete but valid.
{{< /info >}}


### Updating an Entity Index {#index-update}

Clients maintaining an up-to-date entity index can make periodic calls to the [`snapshots`](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getSnapshots) endpoint, and determine whether to download each file by considering:

* Was the snapshot identified by `hash` already downloaded?
* Is `hash` in the `replacedSnapshotHashes` list of another snapshot that was already downloaded?
* Is the `timeRange` relevant for current purposes?

If any new snapshots must be processed, the same strategy as above can be used to update an existing dataset.


## Examples

In the [practice]({{< relref "practice" >}}) section, you'll find code examples that work with the snapshot system.

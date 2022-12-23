---
title: Wearables
url: /contributor/content/entity-types/wearables
weight: 3
---

Wearables are the [entities]({{< relref "../entities" >}}) that contain items for players to wear and customize their avatars.

The `wearables` field in a player's [profile]({{< relref "profiles" >}}) contains a list of pointers to the items they are currently wearing.

Every wearable belongs to a _category_, indicating the spot it takes on the avatar's body, and can hide or replace other categories (for example, a long dress may be worn as top clothing but entirely cover the legs).

There are 16 wearable categories, referenced in various metadata fields: `hair`, `head`, `eyes`, `eyebrows`, `facial_hair`, `mouth`, `upper_body`, `lower_body`, `feet`, `hat`, `helmet`, `mask`, `tiara`, `top_head`, `earring`, `eyewear`, `skin`.

Wearable entities include files in GLB format for different body shapes.

## Pointers {#pointers}

Wearables have exactly one associated [pointer]({{< relref "../pointers" >}}), which indicates the collection they belong to and their index inside of it. They are URNs of this form:

```
urn:decentraland:matic:collections-v2:<collection address>:<item index>
```

To illustrate, the `pointers` array for a wearable looks like this:

```json
{
  "pointers": [
    "urn:decentraland:matic:collections-v2:0x2d9560df9dd8ba8b2dc3746bc1d217698d258fb5:0"
  ],
  // ... other entity properties
}
```

## Metadata Fields

Wearables share most of their basic fields with [emotes]({{< relref "emotes" >}}). The `data` property is where the wearable-specific information is located.

| Field | Value |
| ----- | --- |
| `id` | The [pointer]({{< relref "../pointers" >}}) that resolves (or used to resolve) to this wearable.
| `name` | The display title for this wearable in a [collection]({{< relref "../collections" >}}).
| `description` | An extended description for this wearable.
| `image` | The [internal filename]({{< relref "../entities#files" >}}) of a picture for this wearable.
| `thumbnail` | The [internal filename]({{< relref "../entities#files" >}}) of a 256x256 version of the `image`.
| `rarity` | One of `common`, `uncommon`, `rare`, `epic`, `legendary`, `mythic` or `unique`.
| `i18n` | An array of translations for the `name` field.
| `collectionAddress` | The Ethereum address for the collection that contains this wearable.
| `metrics` | Some useful measurements about the animations (see below).
| `data` | The extended metadata for this wearable (see below).

In typical JSON form:

```json
{
  "id": "urn:decentraland:matic:collections-v2:0x11a6879861f36cbad632b4e7226816a16139fb33:0",
  "name": "Pretty Dress",
  "description": "Very nice to wear",
  "image": "image.png",
  "thumbnail": "thumbnail.png",
  "rarity": "uncommon",
  "i18n": [
    { "code": "es", "text": "Vestido Lindo" }
  ],
  "collectionAddress": "0x11a6879861f36cbad632b4e7226816a16139fb33",
  "metrics": {
    // Measurements object (see below).
  },
  "data": {
    // Extended metadata (see below).
  }
}
```

## Metrics

In the `metadata.metrics` object, you'll find some simple measurements for the models packaged with this wearable. An example:

```json
{
{
  "entities": 1,
  "bodies": 12,
  "materials": 2,
  "meshes": 12,
  "textures": 2,
  "triangles": 3321
}
```

## Data

The `metadata.data` object is where the wearable-specific properties are located.

| Field | Value |
| ----- | --- |
| `category` | One of the wearable categories listed above.
| `representations` | An array of files associated to different body shapes.
| `hides` | An array of categories this wearable hides.
| `replaces` | An array of categories this wearable replaces entirely.
| `tags` | An array of string labels descriptive of this wearable.

_!!Talk to platform or dapps team regarding these fields, they have non-obvious behavior_

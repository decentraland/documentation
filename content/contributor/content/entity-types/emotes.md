---
title: Emotes
url: /contributor/content/entity-types/emotes
weight: 4
---

Emotes are the [entities]({{< relref "../entities" >}}) that hold animations for player's avatars.

They include files in GLB format for different body shapes.

## Pointers {#pointers}

Emotes have exactly one associated [pointer]({{< relref "../pointers" >}}), which indicates the collection they belong to and their index inside of it. They are URNs of this form:

```
urn:decentraland:matic:collections-v2:<collection address>:<item index>
```

To illustrate, the `pointers` array for an emote looks like this:

```json
{
  "pointers": [
    "urn:decentraland:matic:collections-v2:0x2d9560df9dd8ba8b2dc3746bc1d217698d258fb5:0"
  ],
  // ... other entity properties
}
```

## Metadata Fields

Emotes share most of their basic fields with [wearables]({{< relref "wearables" >}}). The `emoteDataADR74` property is where the emote-specific information is located.

| Field | Value |
| ----- | --- |
| `id` | The [pointer]({{< relref "../pointers" >}}) that resolves (or used to resolve) to this emote.
| `name` | The display title for this emote in a [collection]({{< relref "../collections" >}}).
| `description` | An extended description for this emote.
| `image` | The [internal filename]({{< relref "../entities#files" >}}) with a picture for this emote.
| `thumbnail` | The [internal filename]({{< relref "../entities#files" >}}) for a 256x256 version of the `image`.
| `rarity` | One of `common`, `uncommon`, `rare`, `epic`, `legendary`, `mythic` or `unique`.
| `i18n` | An array of translations for the `name` field.
| `collectionAddress` | The Ethereum address for the collection that contains this emote.
| `metrics` | Some useful measurements about the animations (see below).
| `emoteDataADR74` | The extended metadata for this emote, as defined in [ADR-74](https://adr.decentraland.org/adr/ADR-74) (see below).


This is how a typical JSON looks like:

```json
{
  "id": "urn:decentraland:matic:collections-v2:0x2d9560df9dd8ba8b2dc3746bc1d217698d258fb5:0",
  "name": "Funny Dance",
  "description": "Move around like a champ",
  "image": "image.png",
  "thumbnail": "thumbnail.png",
  "rarity": "rare",
  "i18n": [
    { "code": "es", "text": "Danza Graciosa" }
  ],
  "collectionAddress": "0x2d9560df9dd8ba8b2dc3746bc1d217698d258fb5",
  "metrics": {
    // Measurements object (see below).
  },
  "emoteDataADR74": {
    // Extended metadata defined in ADR-74 (see below).
  }
}
```

## Metrics

In the `metadata.metrics` object, you'll find some simple measurements for the animation packaged with this emote. An example:

```json
{
  "triangles": 0,
  "materials": 0,
  "textures": 0,
  "meshes": 0,
  "bodies": 0,
  "entities": 1
}
```

## Emote Data ADR-74

This object contains the fields that World Explorers (or other graphical applications) need to animate models with this emote.

| Field | Value |
| ----- | --- |
| `category` | One of `dance`, `stunt`, `greetings`, `fun`, `poses`, `reactions`, `horror` or `miscellaneous`.
| `representations` | An array of animation files associated to different body shapes.
| `tags` | An array of string tags descriptive of this emote. !!?
| `loop` | `true` if the animation should repeat itself once it ends.

Some JSON for clarity:

```json
{
  "category": "dance",
  "representations": [
    // Information about the animation for different body shapes (see below).
  ],
  "tags": [ "carnaval", "dance" ],
  "loop": true
}
```

### Representations

Each item in the `metadata.emoteDataADR74.representations` field defines the animation files appropriate for each body shape.

| Field | Value |
| ----- | --- |
| `bodyShapes` | An array of applicable [[body shape URNs]].
| `mainFile` | The [internal filename]({{< relref "../entities#files" >}}) for the main GLB file.
| `contents` | All files, including `mainFile` and any additional ones that it can reference.

For example, a `representation` item:

```json
{
  "bodyShapes": [ "urn:decentraland:off-chain:base-avatars:BaseMale" ],
  "mainFile": "male/funnydance.glb",
  "contents": [
    "male/funnydance.glb"
  ]
}
```

You will commonly find two representation entries, one for `BaseMale` and one for `BaseFemale`. !!?
---
title: Outfits
url: /contributor/content/entities-types/outfits
weight: 2
---

Outfits are the saved outfits of a player. An outfit is composed of body shape, skin, hair, eyes and wearables configurations. 

## Pointers {#pointers}

Outfits [pointers]({{< relref "../pointers" >}}) are the Ethereum address of the owner with a "`:outfits`" suffix. For example:

```
0x210c4415d6a71195af76beef9b85dd0eb43f35df:outfits
```

## Metadata Fields

| Field | Value |
| ----- | --- |
|`outfits`| An array of descriptions for each outfit (see below).
|`namesForExtraSlots`| An array of owned names used for validating extra slots. For each owned name, it is granted an extra slot up to 5. 

## Outfits

Each outfit in `metadata.outfts[]` represents an outfit of the user, and has a number of properties:

| Field | Value |
| ----- | --- |
| `slot` | Slot number of the saved outfit.
| `outfit` | The saved outfit (see below).

An example:

```json
{
  "slot": 1,
  "outfit": {
    // See below
  }
}
```

### Outfit Field

The `metadata.outfits[].outfit` field has all the information to save a player's outfit and render it.

| Field | Value |
| ----- | --- |
| `bodyShape` | The [pointer]({{< relref "../pointers" >}}) to the avatar's body shape entity.
| `eyes` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's eyes.
| `hair` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's hair.
| `skin` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's skin.
| `wearables` | An array of [wearable pointers]({{< relref "wearables#pointers" >}}) in use by the avatar.

To illustrate:

```json
{
  "bodyShape": "urn:decentraland:off-chain:base-avatars:BaseMale",
  "eyes": {
    "color": { "r": 0.37109375, "g": 0.22265625, "b": 0.1953125 }
  },
  "hair": {
    "color": { "r": 0.234375, "g": 0.12890625, "b": 0.04296875 }
  },
  "skin": {
    "color": { "r": 0.80078125, "g": 0.609375, "b": 0.46484375 }
  },
  "wearables": [
    "urn:decentraland:off-chain:base-avatars:eyes_00",
    "urn:decentraland:off-chain:base-avatars:eyebrows_00",
    "urn:decentraland:off-chain:base-avatars:mouth_00",
    "urn:decentraland:off-chain:base-avatars:m_mountainshoes.glb",
    "urn:decentraland:off-chain:base-avatars:sport_jacket",
    "urn:decentraland:off-chain:base-avatars:brown_pants",
    "urn:decentraland:off-chain:base-avatars:aviatorstyle",
    "urn:decentraland:off-chain:base-avatars:casual_hair_03",
    "urn:decentraland:off-chain:base-avatars:Mustache_Short_Beard"
  ]
}
```

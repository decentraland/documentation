---
title: Profiles
url: /contributor/content/entities-types/profiles
weight: 2
---

Profiles are the basic description of a player, with information such as their in-world name and avatar.

They are available in content servers as regular [entities]({{< relref "../entities" >}}), though World Explorers usually leverage the comms system to get up-to-date versions on the fly.

The system is prepared to allow for multiple identities with the same owner, all included as avatars in the entity manifest. In practice though, the vast majority of players have only one.

## Pointers {#pointers}

Profile [pointers]({{< relref "../pointers" >}}) are the Ethereum address of the owner, without any prefix or suffix. For example:

```
0x210c4415d6a71195af76beef9b85dd0eb43f35df
```

## Metadata Fields

| Field | Value |
| ----- | --- |
|`avatars`| An array of descriptions for each of the owner's avatars (see below).

## Avatars

Each avatar in `metadata.avatars[]` represents an identity with the same owner, and has a number of properties that allow clients to display profiles, render avatars in-world and contact the owner.

| Field | Value |
| ----- | --- |
| `userId` | The [pointer]({{< relref "../pointers" >}}) that resolves (or used to resolve) to this profile.
| `name` | The display name of this player.
| `email` | (Optional) An email address for this player.
| `description` | (Optional) Text chosen by the player to describe themselves.
| `ethAddress` | The ethereum address of this player (currently equal to their `userId`).
| `hasClaimedName` | Whether the `name` field is a claimed ENS name.
| `unclaimedName` | A temporary name for users without an ENS name (e.g. guests).
| `tutorialStep` | The progress of the tutorial for this player.
| `avatar` | Properties of the player's in-world avatar (see below).

An example:

```json
{
  "userId": "0x210c4415d6a71195af76beef9b84dd0eb43f35da",
  "name": "Bob",
  "email": "",
  "hasClaimedName": false,
  "description": "",
  "ethAddress": "0x210c4415d6a71195af76beef9b84dd0eb43f35da",
  "avatar": {
    // See below
  }
}
```

### Avatar Field

The `metadata.avatars[].avatar` field has all the information a World Explorer (or other clients, such as a standalone avatar editor) require to render a player.

| Field | Value |
| ----- | --- |
| `bodyShape` | The [pointer]({{< relref "../pointers" >}}) to the avatar's body shape entity.
| `snapshots` | An object with images for this avatar (see below).
| `eyes` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's eyes.
| `hair` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's hair.
| `skin` | An object with a `color` in the form of an `{ r, g, b }` object for the avatar's skin.
| `wearables` | An array of [wearable pointers]({{< relref "wearables#pointers" >}}) in use by the avatar.

To illustrate:

```json
{
  "bodyShape": "urn:decentraland:off-chain:base-avatars:BaseMale",
  "snapshots": {
    // See below
  },
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

### Snapshots

The `metadata.avatars[].avatar.snapshots` field contains [file identifiers]({{< relref "../filesystem#identifiers" >}}) for images (included in the [`content` top-level field]({{< relref "../entities#properties" >}})). Each property is an image kind, and there are currently two: `face256` (a thumbnail) and `body` (a full-sized version).

For example:

```json
{
  "face256": "bafkreidvjwc3gqqdqk646rqnxnqzpsyjsjafqfc76zenfgjnm2ahbvrtsd",
  "body": "bafkreigclygt6vzzu7myzg3weifapb3a5uec245lzndg4f53y4vfb3cmwm"
}
```

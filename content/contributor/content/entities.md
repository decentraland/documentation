---
title: Entities
url: /contributor/content/entities
weight: 3
---

Each individual piece of content in the world (such as a scene or a wearable item) is called an _entity_.

Entities are immutable packages of [files]({{< relref "filesystem" >}}) with a unique string identifier, deterministically derived from the contained data, which can be used to discover and download the related files from the content server.

The main file of an entity is the _manifest_, a JSON document describing the entity's general properties, as well as special attributes for each [type](#types). The identifier for an entity is actually the [file identifier]({{< relref "filesystem#identifiers" >}}) of this manifest.

Since they are immutable, entities can't be updated in the traditional sense. Instead, they are replaced by new entities discoverable using the same stable [pointer]({{< relref "pointers" >}}). The newest version of an entity is said to be _active_.

Every entity is signed by an owner (who is associated to an Ethereum account). The owner can later use the same signing keys to upload a new version of the entity and indicate that it replaces the old one. Content servers validate these signatures before accepting new entities, whether they come straight from a client or were relayed by another server.

You can look at actually deployed entities in the [practice]({{< relref "practice" >}}) section.

## Entity Types {#types}

There are five types of entities:

- [**Scenes**]({{< relref "entity-types/scenes" >}}): virtual spaces in the world with their own objects and behavior.
- [**Profiles**]({{< relref "entity-types/profiles" >}}): information about a specific player, such as their name and avatar.
- [**Wearables**]({{< relref "entity-types/wearables" >}}): clothing and items that players can add to their avatars.
- [**Emotes**]({{< relref "entity-types/emotes" >}}): animations that a player's avatar can perform.
- [**Stores**]({{< relref "entity-types/stores" >}}): marketplace sites for wearables and emotes that players can purchase.
- [**Outfits**]({{< relref "entity-types/outfits" >}}): saved outfits for a specific player.

All types follow the same procedures for creation, identification, ownership and hosting.

## Common Properties {#properties}

Every entity has certain common properties in its manifest, applicable to all types. These top-level fields will always be present:

| Field | Value |
| ----- | --- |
| `type` | One of `scene`, `profile`, `wearable`, `emote`, `store` or `outfits`.
| `pointers` | An array of [pointers]({{< relref "pointers" >}}) associated to this entity.
| `timestamp` | The Unix UTC timestamp when this entity was uploaded.
| `content` | An array of references to additional [files]({{< relref "filesystem" >}}) in the entity's package.
| `metadata` | An object with information specific to this entity type.

The structure and values of the `metadata` field for each type are detailed in their specific pages. The `pointers` array also has different contents dependent on the type.

{{< info >}}
Old entity manifests may contain the `version` field, deprecated in [ADR-45](https://adr.decentraland.org/adr/ADR-45). You may safely ignore it, since the `timestamp` field is now used for versioning.
{{< /info >}}

This is a typical JSON manifest describing an entity:

```json
{
  "type": "wearable",
  "pointers": ["urn:decentraland:matic:collections-v2:0xbdf21eaf54ebf4a6cadc2dcb371df7afce98bc1d:0"],
  "timestamp": 1628181913506,
  "content": [
    // ...file references, see below
  ],
  "metadata": {
    // ...specific fields for this entity type, see the relevant page
  }
}
```

You can find the schemas for these JSON structures, along with other objects in Decentraland protocol, in the [Common Schemas](https://github.com/decentraland/common-schemas) repository.


{{< info >}}
When looking at entity manifests, you may find undocumented fields. This is because the entity schema allows for additional custom properties, freely set by the owner.
{{< /info >}}

## Files {#files}

As mentioned above, all entities have at least one associated file: the JSON manifest describing the entity itself. The entity identifier is actually the [file identifier]({{< relref "filesystem#identifiers" >}}) of this special file.

The `content` field inside each manifest is an array of references to additional files. These are typically assets, such as 3D models and animations, or scripts for scenes.

All files are stored in Decentraland's [distributed file system]({{< relref "filesystem" >}}), and each item in the array has two properties:

| Field | Value |
| --- | --- |
| `file` | The internal name used by files in this entity to reference each other.
| `hash` | The global [identifier for this file]({{< relref "filesystem#identifiers" >}}), unique across all content.

This is how it typically looks inside the `content` field:

```json
[
  {
    "file": "thumbnail.png",
    "hash": "bafkreiglecvpnqibvf6pltcnid5nhbx3caj77lu4ia4xitpmp3lrcouuhm",
  },
  {
    "file": "model.glb",
    "hash": "bafkreic2i3awiu7srhatf3k47l3c5lmadisznjigppor2a35saosjfbo25",
  },
  // ...more files
]
```

{{< info >}}
The `file` field value is always in lower-case, to prevent issues when building entities in different operating systems, where filename casing may be important.
{{< /info >}}

The lifespan of a file is tied to the entity that contains it. For active entities (i.e. not yet replaced by their owner), content servers are required by protocol to preserve all associated files. If the entity is deleted, the files can be kept or discarded at the server's discretion.

## Ownership and Authentication {#ownership}

To prove ownership and authorize actions around entities, the [authentication chain]({{< relref "../auth/authchain" >}}) mechanism is used.

The [`decentraland-crypto`](https://github.com/decentraland/decentraland-crypto) repository contains the implementation of all cryptographic procedures.


## Discovering and Downloading Entities

Content servers can be used to locate entities using [pointers]({{< relref "pointers" >}}), and to download their manifests and any additional files. 

- To resolve a pointer into an entity ID, you can use the [`/entities/active`](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getListOfEntities) endpoint.

- Using the entity ID, you can download the manifest with the [`/contents/<id>`](https://decentraland.github.io/catalyst-api-specs/#tag/Content-Server/operation/getContentFile) endpoint.

- To get all active entities of a certain type, start by downloading a [snapshot]({{< relref "snapshots" >}}).

Check out the [practice]({{< relref "practice" >}}) section for examples and guides.
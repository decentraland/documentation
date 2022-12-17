---
title: Entities
url: /contributor/content/entities
weight: 3
---

Each individual piece of content in the world (such as a scene or a wearable item) is called an _entity_.

Entities are immutable packages of [files]({{< relref "filesystem" >}}) identified by an `entityId`. This identifier is deterministically derived from the contained data, and can be used to download the package from the content server.

Since they are immutable, entities can't be updated in the traditional sense. Instead, they are replaced by new entities discoverable using the same stable [pointer]({{< relref "pointers" >}}). The newest version of an entity is said to be _active_.

Every entitiy is signed by an owner (who is associated to an Ethereum account). The owner can later use the same signing keys to upload a new version of the entity and indicate that it replaces the old one. Content servers validate these signatures before accepting new entities, whether they come straight from a client or were relayed by another server. !!mmmmm


## Entity Types

There are five types of entities:

- [**Scenes**]({{< relref "entity-types/scenes" >}}): virtual spaces in the world with their own objects and behavior.
- [**Profiles**]({{< relref "entity-types/profiles" >}}): information about a specific player, such as their avatar.
- [**Wearables**]({{< relref "entity-types/wearables" >}}): clothing and items that players can add to their avatars.
- [**Emotes**]({{< relref "entity-types/emotes" >}}): animations that a player's avatar can perform.
- [**Stores**]({{< relref "entity-types/stores" >}}): collections of wearables and emotes that players can explore and purchase. !!mmmmNO

All types follow the same procedures for creation, identification, ownership and hosting. !!mmm

## Common Properties {#properties}

Every entity has certain common properties, applicable to all types. When [[requesting an entity]] from a content server, these fields will always be present:

| Field | Value |
| ----- | --- |
| `type` | One of `scene`, `profile`, `wearable`, `emote` or `store`.
| `pointers` | An array of [pointers]({{< relref "pointers" >}}) associated to this entity.
| `timestamp` | The Unix UTC timestamp when this entity was uploaded.
| `content` | An array of references to additional [files]({{< relref "filesystem" >}}) in the entity's package.
| `metadata` | An object with information specific to this entity type.

The structure and values of the `metadata` field for each type are detailed in their specific pages. The `pointers` array also has different use-cases for some types.

{{< info >}}
Old entity documents may contain the `version` field, deprecated in [ADR-45](https://adr.decentraland.org/adr/ADR-45). You may safely ignore it, since the `timestamp` field is now used vor versioning.
{{< /info >}}

This is a typical JSON document describing an entity:

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

## Files

All entities have at least one associated file: the JSON document describing the entity itself. The entity ID is the [file-system identifier]({{< relref "filesystem#identifiers" >}}) of this special file.

Contained inside each entity is an array of references to additional files, under the `content` field. These are typically assets, such as 3d models and animations, or scripts for scenes.

Entity files are stored in Decentraland's [distributed file system]({{< relref "filesystem" >}}). Each item in the array has two properties:

| Field | Value |
| --- | --- |
| `file` | The internal name used by files in this entity version to reference each other.
| `hash` | The global [identifier for this file]({{< relref "filesystem#identifiers" >}}), unique across all content.

This is how it typically looks inside the `content` field showcased above:

```json
[
  {
    "file": "thumbnail.png",
    "hash": "QmbktMUXMm5yUfk9zwdsf9dMMeoUCMDxa1Bxi4XaRu67Sy",
  },
  {
    "file": "model.glb",
    "hash": "QmS6HmXWb3k5xzvxsPpkeddh5U8sLARGVUfjbzy9eh6gkZ",
  },
  // ...more files
]
```

The JSON document with the entity's description is a file itself, uploaded by the owner and stored in the distributed file-system just like any other. The entity ID is actually the JSON file's ID.

> !!NOTE
> The `file` field is always in lower-case, to prevent issues when building entities in different operating systems, where filename casing may be important.

The lifespan of a file is tied to the entity that contains it. For entities currently in use (i.e. not yet replaced by their owner), [[Catalyst]] servers are required by protocol to preserve all associated files. If the entity is deleted, the files can be kept or discarded at the server's discretion.

## Ownership

## Discovering and Downloading Entities
---
title: "Pointers"
sidebartitle: "Pointers"
url: "/contributor/content/pointers"
weight: 4
---

Pointers are unique, case-insensitive strings that reference an active [entity]({{< relref "entities" >}}). Content servers can resolve these pointers to obtain the entity's identifier.

Remember that both [entities]({{< relref "entities" >}}) and their [files]({{< relref "filesystem" >}}) are immutable in the Decentraland content system, and their identifiers change when replacement versions are uploaded. Pointers, on the other hand, are stable references that persist across replacements. This is achieved by automatically redirecting the pointer to a new entity when the owner uploads a replacement.

Multiple pointers can resolve to the same [entity]({{< relref "entities" >}}), as is often the case with [scenes]({{< relref "entity-types/scenes" >}}).

As you may gather, the most common use of pointers is obtaining the ID for the active version (i.e. latest replacement) of an [entity]({{< relref "entities" >}}), in order to download it.

## Pointer Types

There are 4 types of pointers that content servers can resolve to entities, each with its own syntax:

- [Scene pointers]({{< relref "entity-types/scenes#pointers" >}}) are parcel coordinates, such as `"0,0"`.
- [Profile pointers]({{< relref "entity-types/profiles#pointers" >}}) are the Ethereum address of the owner.
- [Wearable pointers]({{< relref "entity-types/wearables#pointers" >}}) and [emote pointers]({{< relref "entity-types/emotes#pointers" >}}) are either [collection]({{< relref "collections" >}}) item or off-chain URNs.
- [Store pointers]({{< relref "entity-types/stores#pointers" >}}) are off-chain URNs with the Ethereum address of the owner.
- [Outfits pointers]({{< relref "entity-types/outfits#pointers" >}}) are the Ethereum address of the owner suffixed by `:outfits`.

You can find more details in their specific sections.

## Resolving Pointers

Content servers have an endpoint that can resolve pointers into their active entity's manifest, by making a `GET` request to:

```
https://<content-base-url>/entities/<entity-type>?pointer=<pointer>
```

{{< info >}}
For historical reasons, the response from this endpoint is an array containing one element.
{{< /info >}}

Some useful examples, using the Foundation's content server:

```bash
# An on-chain collection pointer to a wearable:
curl "https://peer.decentraland.org/content/entities/wearables/?pointer=urn:decentraland:matic:collections-v2:0x30517529cb5c16f686c6d0b48faae5d250d43005:0"

# An off-chain collection pointer to a default asset:
curl https://peer.decentraland.org/content/entities/wearables/?pointer=urn:decentraland:off-chain:base-avatars:BaseFemale

# A parcel pointer:
curl https://peer.decentraland.org/content/entities/wearables/?pointer=0,0

# A profile pointer:
curl https://peer.decentraland.org/content/entities/profiles/?pointer=0xe2c2b80ca5ad868f4b30fa83cca2bf12cc95b4fe
```

Note that, if you already know the entity's ID, you can [download the manifest]({{< relref "filesystem#downloading" >}}) file directly.
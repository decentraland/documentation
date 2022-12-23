---
title: "Pointers"
sidebartitle: "Pointers"
url: "/contributor/content/pointers"
weight: 4
---

Pointers are unique, case-insensitive strings that reference an active [entity]({{< relref "entities" >}}). Content servers can resolve these pointers to obtain its ID.

Remember that both [entities]({{< relref "entities" >}}) and their [files]({{< relref "filesystem" >}}) are immutable in the Decentraland content system, and their identifiers change when replacement versions are uploaded. Pointers, on the other hand, are stable references that persist across replacements. This is achieved by automatically redirecting the pointer to a new entity when the owner uploads a replacement.

Multiple pointers can resolve to the same [entity]({{< relref "entities" >}}), as is often the case with [scenes]({{< relref "entity-types/scenes" >}}).

As you may gather, the most common use of pointers is obtaining the ID for the active version (i.e. latest replacement) of an [entity]({{< relref "entities" >}}), in order to download it.

## Pointer Types

There are 3 types of pointers that content servers can resolve, each with its own syntax:

- [Scene pointers]({{< relref "entity-types/scenes#pointers" >}}) are parcel coordinates, such as `"0,0"`.
- [Profile pointers]({{< relref "entity-types/profiles#pointers" >}}) are the Ethereum address of the owner
- [Wearable pointers]({{< relref "entity-types/wearables#pointers" >}}) and [emote pointers]({{< relref "entity-types/emotes#pointers" >}}) are [collection]({{< relref "collections" >}}) URNs with an index suffix

You can find more details in their specific sections.


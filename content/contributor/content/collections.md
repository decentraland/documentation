---
title: Collections
url: /contributor/content/collections
weight: 6
---

Collections are groups of [wearables]({{< relref "entity-types/wearables" >}}) and [emotes]({{< relref "entity-types/emotes" >}}) defined in the same off-chain namespace or on-chain contract.

They are not [entities]({{< relref "entities" >}}) in and of themselves, but their individual items can be obtained from content servers normally using [pointers]({{< relref "pointers" >}}).

## URNs and Pointers {#pointers}

Collections are identified using URNs, which are prefixes to their item URNs. There are 4 general types of URNs:

* `v1` collections with Foundation-approved content (deprecated).
* `v2` collections with community-approved content.
* `thirdparty` collections with items associated to NFTs outside Decentraland.
* `off-chain` collections, containing mostly default items for new avatars.

{{< info >}}
Despite the fact that `v1` collections are deprecated and will not be created or updated anymore, they are still valid and their items can be used.
{{< /info >}}

### Version 1 and 2 Collections

Both the old `v1` and the current `v2` collection namespaces have URNs of the same form:

```
urn:decentraland:<blockchain>:<collections-version>:<contract-address>
```

For example:

```
# A collection in the deprecated v1 space:
urn:decentraland:mainnet:collections-v1:DCL Test Masks

# A collection in the v2 community-approved space:
urn:decentraland:matic:collections-v2:0x25a1d66891d44cdf7b8c45802489c1dea7aadf8b
```

If the `:<id>` segment is appended at the end, the URN becomes a [pointer]({{< relref "pointers" >}}) to an item inside the collection. See [wearable pointers]({{< relref "entity-types/wearables#pointers" >}}) and [emote pointers]({{< relref "entity-types/emotes#pointers" >}}) for information on these.

### Third-party Collections

Third-party collections, also known as [linked wearables]({{< ref "/content/creator/wearables-and-emotes/wearables/linked-wearables.md" >}}), are different from regular wearables in that they are tied to existing NFTs outside Decentraland. They allow players to display NFTs from their personal set on their in-world avatars.

Their URNs look like this:

```
urn:decentraland:<blockchain>:collections-thirdparty:<third-party-id>:<collection-id>
```

You can find ample information about these in the [linked wearables]({{< ref "/content/creator/wearables-and-emotes/wearables/linked-wearables.md" >}}) documentation for creators.

## Discovering Collections

Content servers can give you a list of all known collections, using the [`/lambdas/collections`](https://decentraland.github.io/catalyst-api-specs/#tag/Lambdas/operation/getCollections) endpoint.

The response will be an object with a `collections` property, containing an array of URNs and names. For example:

```json
{
  "collections": [
    {
      "id": "urn:decentraland:amoy:collections-v2:0xff5d4ebc6bc1ff7262cab42d3c693d953f4614d2",
      "name": "Winter clothes collection"
    },
    // ... many more
  ]
}
```

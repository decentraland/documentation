---
title: Stores
url: /contributor/content/entity-types/stores
weight: 5
---

Stores are off-chain [entities]({{< relref "../entities" >}}) that represent user-managed marketplace sites. They contain a description and a picture to show buyers, plus information about the store owner.

## Pointers {#pointers}

Store pointers are URNs in the `off-chain` namespace, with the following form:

```
urn:decentraland:off-chain:marketplace-stores:<owner-address>
```

The address segment is the Ethereum address of the store's owner. For example:

```
urn:decentraland:off-chain:marketplace-stores:0xa2a1dc503be6fdb7878f58f053ded40564e3b9b2
```

## Metadata Fields

| Field | Value |
| ----- | --- |
| `id` | The [pointer]({{< relref "../pointers" >}}) that resolves (or used to resolve) to this store.
| `description` | The display title for this store.
| `owner` | The Ethereum address of the owner.
| `images` | An array of `{ file, name }` objects referencing images (see below).
| `links` | An array of `{ name, url }` objects with social media or website links (see below).


### Images

Stores have a picture to show buyers in the marketplace, each with a name identifying the role. The typical `images` array has a single element with the name `cover`, like this:

```json
[
  {
    "name": "cover",
    "file": "imgs/store-logo.png"
  }
]
```

### Links

Owners can add external links to stores, such as social media profiles and external websites. Facebook and Discord URLs are commonly included. An example:

```json
[
  {
    "name": "facebook",
    "url": "https://www.facebook.com/mydclstore"
  },
  {
    "name": "website",
    "url": "https://mydclstore.com"
  }
]
```
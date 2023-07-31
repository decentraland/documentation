---
title: "Content API from the CLI"
bookhidden: true
url: "/contributor/content/practice/cli"
---

This practice demonstrates how to play with the content API in a terminal. We'll be using the Decentraland Foundation's instance at `peer.decentraland.org`, and all you need is the `curl` command-line tool.

{{< info >}}
You can use [`httpie`](https://github.com/httpie/httpie) or format responses with [`jq`](https://github.com/stedolan/jq) to get more readable JSONs with each request. In this guide, we'll show formatted documents for clarity.
{{< /info >}}

This is what we'll do:

1. Query the status of the content server.
2. Locate and download a daily [snapshot]({{< relref "snapshots" >}}) with a list of entities.
3. Obtain the manifest for an entity.
4. Download one of the entity's files.

Let's begin by querying the server status using `/about`:

```bash
curl "https://peer.decentraland.org/about"
```

```js
{
  "healthy": true,
  "content": {
    "healthy": true,
    "version": "6.5.0",
  },
  // ... more server information (feature flags, versions, paths, etc.)
}
```

Looks like the server is up and running normally (`"healthy": true`), and is giving us information about the version it implements for each feature set, plus some configuration options of the instance.

We're interested in downloading some content, so let's explore the available [snapshots]({{< relref "snapshots" >}}) to get our hands on some identifiers via `/content/snapshots`.

```bash
curl "https://peer.decentraland.org/content/snapshots"
```
```js
[
  {
    "hash": "bafybeia6qoum64psaooiqo3f45i6hykfwx723uc236waub3gng2naof224",
    "timeRange": {
      "initTimestamp": 1689120000000,
      "endTimestamp": 1689206400000
    },
    "replacedSnapshotHashes": [],
    "numberOfEntities": 981,
    "generationTimestamp": 1689219353866
  },
  // ...more snapshot files
]
```

Each item in the array describes a [snapshot]({{< relref "snapshots" >}}). Let's grab a `hash` and download the file from the `/content/contents` endpoint.

```bash
curl "https://peer.decentraland.org/content/contents/bafybeia6qoum64psaooiqo3f45i6hykfwx723uc236waub3gng2naof224" > snapshot
```

{{< info >}}
You can experiment with larger snapshots, as in the [advanced python example](https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots.py). To try this out interactively, you probably want one of the smaller ones.
{{< /info >}}

We can check that we downloaded the right file in a format we know, by looking at the first line:

```bash
head -n1 snapshot
```
```
### Decentraland json snapshot
```

Great! Now we have a local summary of all entities that were captured in that snapshot. Let's take the first one listed (the second line in the file), a `profile`:

```bash
tail -n+2 snapshot | head -n1 
```
```js
{
  "entityId": "bafkreif7hjremkxlvixyxoxnoo7bdcnf7qqp245sjb2pag2nk3n6o6yc4c",
  "entityType": "profile",
  "pointers": [
    "0x271cdb3b1c792c336c4b2bdc52c4f415d0046b92"
  ],
  "authChain": [
    // See https://docs.decentraland.org/contributor/auth/authchain/
  ],
  "entityTimestamp": 1689120135624
}
```

{{< info >}}
Since snapshots expire and entities are replaced, the identifiers in this article won't work. Follow along in your command line to get real, active file IDs.
{{< /info >}}

This is information we could save. We'll use the `entityId` to download the entity's JSON manifest, but persisting the listed [pointer]({{< relref "pointers" >}}) is a good idea if we want to locate this entity and any updated versions in the future.

We also have the [authentication chain]({{< relref "../entities#ownership" >}}) used to sign this entity, and we could validate the listed signatures to verify the authenticity of any related files we download.

Let's get our hands on the entity manifest. Remember, the `entityId` is the [file identifier](({{< relref "filesystem#identifiers" >}})) we need, and we can use the `/content/contents` endpoint again:

```bash
curl "https://peer.decentraland.org/content/contents/bafkreigcreq7rv6b2wf4zc4fsnif43ziwb4q46v4qhsewpf7gbsyxew3om"
```
```js
{
  "version": "v3",
  "type": "profile",
  "pointers": [
    "0x273cdb3b1c791c336c4b2bcc52c4f415d0046b91"
  ],
  "timestamp": 1689120135624,
  "content": [
    {
      "file": "body.png",
      "hash": "bafybeibzaqkirz7fk474xvyhurho5xviphs7anawaceb6gscuigia4x33u"
    },
    // ...more files
  ],
  "metadata": {
    // ...avatars and other information
  }
}
```

This `profile` entity has all the information World Explorers use to render and animate a player. If we're interested in getting one of the packaged files, we can continue to use the `/content/contents` endpoint.

If we look at the `content` field, we can see the `hash` of the file internally called `body.png`. Let's get it:

```bash
curl "https://peer.decentraland.org/content/contents/bafybeibzaqkirz7fk474xvyhurho5xviphs7anawaceb6gscuigia4x33u" > body.png
```

We can open this `png` file in an image viewer or web browser, and check out the author's work. Nice!
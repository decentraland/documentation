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
2. Locate and download the [snapshot]({{< relref "snapshots" >}}) for a list of entities.
3. Obtain the manifest for an entity.
4. Download some of the entity's files.

Let's begin by querying the server status using `/about`:

```bash
curl "https://peer.decentraland.org/about"
```

```json
{
  "healthy": true,
  "acceptingUsers": true,
  "bff": {
    "commitHash": "1a2ff915a216191ecc6ef85f3822f0809fe16f3c",
    "healthy": true,
    "protocolVersion": "1.0_0",
    "publicUrl": "/bff",
    "userCount": 12
  },
  "comms": {
    "commitHash": "ad06af3339484411eb639e402462fd2715ce80f6",
    "healthy": true,
    "protocol": "v3"
  },
  "content": {
    "commitHash": "d6e5d094ef81e2d5630eba9f3eaba2bdc21f5b13",
    "healthy": true,
    "publicUrl": "https://peer-ec1.decentraland.org/content/",
    "version": "5.1.9"
  },
  "lambdas": {
    "commitHash": "b80be3b95e0e8d5b4c9295e7f89fc6f17f7d8a8d",
    "healthy": true,
    "publicUrl": "https://peer-ec1.decentraland.org/lambdas/",
    "version": "5.1.10"
  },
  "configurations": {
    "globalScenesUrn": [],
    "networkId": 1,
    "realmName": "hephaestus",
    "scenesUrn": []
  },
}
```

Looks like the server is up and running normally (`"healthy": true`), and is giving us information about the version it implements for each feature set, plus some configuration options of the instance.

We're interested in downloading some content, so let's explore the available [snapshots]({{< relref "snapshots" >}}) to get our hands on some identifiers via `/content/snapshots`.

```bash
curl "https://peer.decentraland.org/content/snapshots"
```

```json
{
  "hash": "bafybeibtfyox4mho6nfxtfibvol3h6mvnsduslofnwuej33eag2yqgw5bi",
  "lastIncludedDeploymentTimestamp": 1671631795620,
  "entities": {
    "scene": {
      "hash": "bafybeiadxlvdmgmzhvhrgbgzumfdp52i7ubzmhq5sxfyfiivcjuxyddl54",
      "lastIncludedDeploymentTimestamp": 1671631464866
    },
    "profile": {
      "hash": "bafybeib6mk6p2ymod7lmsw6ttsacbmkgmvwpn23jmdkpkfdzvgvp7lzaeu",
      "lastIncludedDeploymentTimestamp": 1671631795620
    },
    "wearable": {
      "hash": "bafybeidcl3kmsnufkvl7tlmeussajiqiqqzsq3uto7m5wrzhstnix5f6vu",
      "lastIncludedDeploymentTimestamp": 1671630538830
    },
    "store": {
      "hash": "bafybeidq2yivbl5wlozds4okldqlb6uesqeflb7k6hyygyr7xjx63h5eta",
      "lastIncludedDeploymentTimestamp": 1671604715626
    },
    "emote": {
      "hash": "bafkreialb5j2vhhes3dorynuyvkbvh3nxddjtadmupaukr4da7peyvlfny",
      "lastIncludedDeploymentTimestamp": 1671621566675
    }
  }
}
```

There we have the [file identifiers](({{< relref "filesystem#identifiers" >}})) for each [snapshot]({{< relref "snapshots" >}}) file. Say we want to look at some of the available emotes, and let's take the `entities.emote.hash` field to download the file from the `/content/contents` endpoint.

```bash
curl "https://peer.decentraland.org/content/contents/bafkreialb5j2vhhes3dorynuyvkbvh3nxddjtadmupaukr4da7peyvlfny" > emotes.snapshot
```

{{< info >}}
You can experiment with the `profile` or global snapshots, but bear in mind that those are very large files.
{{< /info >}}

We can check that we downloaded the right file in a format we know, by looking at the first line:

```bash
head -n1 emotes.snapshot
```
```
### Decentraland json snapshot
```

Great! Now we have a local copy of the current set of `emote` entities. Let's take the first one listed (the second line in the file):

```bash
# You can omit jq and get the raw unformatted JSON:
head -n+2 emotes.snapshot | jq 
```
```json
{
  "entityType": "emote",
  "entityId": "bafkreigcreq7rv6b2wf4zc4fsnif43ziwb4q46v4qhsewpf7gbsyxew3om",
  "pointers": [
    "urn:decentraland:matic:collections-v2:0xc304f10579a499c967291c014365304207c59a62:0"
  ],
  "localTimestamp": 1667798266960,
  "authChain": [
    {
      "type": "SIGNER",
      "payload": "0xa8c7d5818a255a1856b31177e5c96e1d61c83991",
      "signature": ""
    },
    {
      "type": "ECDSA_EPHEMERAL",
      "payload": "Decentraland Login\r\nEphemeral address: 0x8cbbCC5B597981cf0c2B254089cf2d7c90943961\r\nExpiration: 2022-11-16T07:18:01.235Z",
      "signature": "0x97d38594dad0388eb20cfc3ef2e2a692858f1a809594ba43b7bca9171aecff09218adeb949a72b60f8b2d4281f85f348dae5224a2f750b4b22fe7b6bf392f6941c"
    },
    {
      "type": "ECDSA_SIGNED_ENTITY",
      "payload": "bafkreigcreq7rv6b2wf4zc4fsnif43ziwb4q46v4qhsewpf7gbsyxew3om",
      "signature": "0xe0037fc5ddb00d0befae6b29214ed3a846fbd2982c70edf6d556ef813efe78cc7a64b3f0669a50d6aa1d12cbc3b5cc75adc833c6b3ee2c444d34de48227726321b"
    }
  ]
}
```

This is information we could save. We'll use the `entityId` to download the entity's JSON manifest, but persisting the listed [pointer]({{< relref "pointers" >}}) is a good idea if we want to locate this entity and any updated versions in the future.

We also have the [authentication chain]({{< relref "../entities#ownership" >}}) used to sign this entity, and we could validate the listed signatures to verify the authenticity of any related files we download.

Let's get our hands on the entity manifest. Remember, the `entityId` is the [file identifier](({{< relref "filesystem#identifiers" >}})) we need, and we can use the `/content/contents` endpoint again:

```bash
curl "https://peer.decentraland.org/content/contents/bafkreigcreq7rv6b2wf4zc4fsnif43ziwb4q46v4qhsewpf7gbsyxew3om"
```
```json
{
  "version": "v3",
  "type": "emote",
  "image": "image.png",
  "thumbnail": "thumbnail.png",
  "pointers": [ "urn:decentraland:matic:collections-v2:0xc304f10579a499c967291c014365304207c59a62:0" ],
  "timestamp": 1667798235182,
  "content": [
    {
      "file": "thumbnail.png",
      "hash": "bafkreiajc6gwp4ldcnah7jrv4ligmuokb2ssn2yq3rmlx3erzvak42vjoe"
    },
    {
      "file": "male/PassedOut.glb",
      "hash": "bafkreigdc2ytkyfqvdggodgkh4u4wae7x6b2q45mxqv3vfzh4xt6k772y4"
    },
    {
      "file": "female/PassedOut.glb",
      "hash": "bafkreigdc2ytkyfqvdggodgkh4u4wae7x6b2q45mxqv3vfzh4xt6k772y4"
    },
    {
      "file": "image.png",
      "hash": "bafkreihxvd736yotitatwqyhl7fmrpzjprsah32kwf63djwdr5xepak54y"
    }
  ],
  "metadata": {
    "id": "urn:decentraland:matic:collections-v2:0xc304f10579a499c967291c014365304207c59a62:0",
    "name": "Passed Out",
    "description": "Sometimes you need to sleep it off",
    "collectionAddress": "0xc304f10579a499c967291c014365304207c59a62",
    "rarity": "legendary",
    "i18n": [
      { "code": "en", "text": "Passed Out" }
    ],
    "emoteDataADR74": {
      "category": "poses",
      "representations": [
        {
          "bodyShapes": [ "urn:decentraland:off-chain:base-avatars:BaseMale" ],
          "mainFile": "male/PassedOut.glb",
          "contents": [ "male/PassedOut.glb" ]
        },
        {
          "bodyShapes": [ "urn:decentraland:off-chain:base-avatars:BaseFemale" ],
          "mainFile": "female/PassedOut.glb",
          "contents": [ "female/PassedOut.glb" ]
        }
      ],
      "tags": [ "sleep", "mvmf22", "emote", "canessa", "passed", "out", "beer" ],
      "loop": true
    },
    "metrics": {
      "triangles": 0,
      "materials": 0,
      "textures": 0,
      "meshes": 0,
      "bodies": 0,
      "entities": 1
    }
  }
}
```

This is all the information World Explorers use to animate avatars with this emote. If we're interested in getting one of the packaged files, we can continue to use the `/content/contents` endpoint.

If we look at the `thumbnail` field, we can see that the internal file name is `thumbnail.png`. This is listed in `content` array of files, where we can match the `name` to a `hash` that identifies the file. Let's get it:

```bash
curl "https://peer.decentraland.org/content/contents/bafkreiajc6gwp4ldcnah7jrv4ligmuokb2ssn2yq3rmlx3erzvak42vjoe" > thumbnail.png
```

We can open this `png` file in an image viewer or web browser, and check out the author's work. Nice!
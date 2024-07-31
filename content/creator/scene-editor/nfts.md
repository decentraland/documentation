---
date: 2024-07-25
title: NFTs
description: Adding NFT Portraits to your scenes
categories:
  - scene-editor
type: Document
aliases:
  - /builder/nfts/
url: /creator/editor/nfts
weight: 6
---

You can add NFTs (Non-Fungible Tokens) into your scene, displayed as picture frames.

All image and gif formats that are supported in OpenSea are also supported by Decentraland by picture frames. NFTs in video or audio format are currently not supported. NFTs that also have 3D representations, like Decentraland wearables, are displayed in picture frames as 2D images.

## Adding an NFTs

Use the NFT smart item, that you can find in the **Smart Items** asset pack, or by simply searching _NFT_ in the search bar above. Once you drag a copy of the NFT item to your scene and select it, there are a few fields that your can configure.

<img src="/images/editor/nft-item.jpg" width="300"/>

The main fields to configure determine what NFT to display:

- **Network**: The blockchain network that your NFT is in. It uses Ethereum mainnet by default, but you can also pick Polygon (matic), Solana, etc.
- **NFT Collection Contract**: The contract address of the collection that this NFT belongs to (ie: Cryptokitties, SuperRare, Decentraland Halloween Wearables 2019, etc)
- **Token ID**: The unique id of this specific NFT

To obtain these, the simplest way is to look them up in the Decentraland Marketplace and then check the URL. For example, from the URL of the following item:

_https://market.decentraland.org/contracts/0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0/tokens/20175_

You can infer that the contract is _0xb932a70a57673d89f4acffbe830e8ed7f75fb9e0_ (referring to SuperRare) and the ID is _20175_.

Similarly, you can also obtain these from the OpenSea URL of the token. For example, from the URL of the following item:

_https://opensea.io/assets/0x31385d3520bced94f77aae104b406994d8f2168c/2614_

Yon can infer that the contract is _0x31385d3520bced94f77aae104b406994d8f2168c_ (referring to CryptoPunks) and the ID is _2614_.

Other optional fields that can be configured in the NFT smart item are:

- **Frame Type**: The default frame style has a glowing margin that might not match the style of the artwork or your scene. There are several other options to pick from with varying styles, from barroque to minimalist, or even tape on the painting's corners.
- **Background Color**: NFTs with transparent background are given a background color, violet by default. You can choose any other color. Note that some frame styles, like _None_, don't include a background color at all.

{{< hint warning >}}
**📔 Note**: You can only see these changes take effect when entering the scene in Preview mode. None of these changes modify the representation of the smart item that you drag around in edit mode.
{{< /hint >}}

See [Display an NFT]({{< ref "/content/creator/sdk7/media/display-a-certified-nft.md#">}}) for more details on how Decentraland handles NFT portraits.

---
date: 2022-02-17
title: Buying NFTs
description: Different contracts and functions that can be used to buy NFTs from the Decentraland Marketplace
categories:
  - blockchain-integration
type: Document
url: /player/blockchain-integration/buying-nfts
weight: 15
---

## Buying NFTs directly through Decentraland's Smart Contracts

Users can easily buy Land, Estates, Names, Wearables and Emotes using the [Marketplace](https://market.decentraland.org/). As easy as it seems to do it on the website, various Smart Contracts on the Ethereum Network and the Polygon Network make this possible.

Lands, Estates, and Names are commercialized in the marketplace using a different contract than the ones used for Wearables and Emotes, and Wearables that you buy from the store listed as primary sales use a different one as well. Users can also place bids for different NFTs, which are also handled by other smart contracts.

Hopefully, this guide will let you understand the different Smart Contracts used behind the scenes to make the marketplace possible and the ways one can interact with these contracts directly to execute a purchase without the need or relying on a UI.

## Smart Contracts

This is a list of smart contracts accessible to users through the marketplace application.

**Mainnet**

|Contract|Mainnet|Polygon|
|:-|:-|:-|
|Marketplace|[0x8e5660b4ab70168b5a6feea0e0315cb49c8cd539](https://etherscan.io/address/0x8e5660b4ab70168b5a6feea0e0315cb49c8cd539)|[0x480a0f4e360E8964e68858Dd231c2922f1df45Ef](https://polygonscan.com/address/0x480a0f4e360E8964e68858Dd231c2922f1df45Ef)|
|Bids|[0xe479dfd9664c693b2e2992300930b00bfde08233](https://etherscan.io/address/0xe479dfd9664c693b2e2992300930b00bfde08233)|[0xb96697FA4A3361Ba35B774a42c58dACcaAd1B8E1](https://polygonscan.com/address/0xb96697FA4A3361Ba35B774a42c58dACcaAd1B8E1)|
|CollectionStore|-|[0x214ffC0f0103735728dc66b61A22e4F163e275ae](https://polygonscan.com/address/0x214ffC0f0103735728dc66b61A22e4F163e275ae)|

**Testnet**

|Contract|Sepolia|Amoy|
|:-|:-|:-|
|Marketplace|[0xccf0c17da6cd68041b1bf0f7e015767242077d8c](https://sepolia.etherscan.io/address/0xccf0c17da6cd68041b1bf0f7e015767242077d8c)|[0x0c8ad1f6aadf89d2eb19f01a100a6143108fe2b0](https://amoy.polygonscan.com/address/0x0c8ad1f6aadf89d2eb19f01a100a6143108fe2b0)|
|Bids|[0x2c2835b95852fd975e087b3b25297322728792e2](https://sepolia.etherscan.io/address/0x2c2835b95852fd975e087b3b25297322728792e2)|[0x4b66eab79cc03a96fb6275cfcdf23c0db431606d](https://amoy.polygonscan.com/address/0x4b66eab79cc03a96fb6275cfcdf23c0db431606d)|
|CollectionStore|-|[0xe36abc9ec616c83caaa386541380829106149d68](https://amoy.polygonscan.com/address/0xe36abc9ec616c83caaa386541380829106149d68)|

As you can see, there are contracts both in the Ethereum and the Polygon networks. This is because different kinds of assets can be found in one network and the rest in the other. For example, LANDs, Estates, and Names are all in the Ethereum Network, while Wearables and Emotes are in the Polygon Network.

**Networks are not interoperable, meaning that you cannot buy Wearables in the Ethereum network or place bids for LANDs in Polygon. Contracts can only interact with the assets found in their same networks. But still, users can get Wearables or Emotes in Polygon while connected to the Ethereum network thanks to [Meta-Transactions](https://docs.decentraland.org/player/blockchain-integration/transactions-in-polygon/) which are automatically used in the Marketplace for a better UX**

## Marketplace

The Marketplace Smart Contract in Ethereum allows users to create an Order to sell LANDs, Estates, Names and Legacy Wearables, while the one in Polygon only allows the creation of Orders for Wearables and Emotes.

Orders can be created using the `createOrder` function with the following signature.

```sol
/// @param nftAddress The address of the NFT contract (The LandRegistry, EstateRegistry or Wearable/Emote Collection address).
/// @param assetId The token id of the NFT.
/// @param priceInWei The price (in MANA) the sender wants the NFT to be sold for.
/// @param expiresAt The duration the order will last until it cannot be executed anymore.
function createOrder(
  address nftAddress,
  uint256 assetId,
  uint256 priceInWei,
  uint256 expiresAt
)
```

Once an Order has been created on-chain, the asset will be listed for sale so that any user can buy it.

When a user wants to buy an asset listed in the Marketplace, they have to allow the Marketplace Smart Contract to operate with their MANA first. This is done by sending a transaction. Users can set an allowance for the amount of the asset they want to buy or a higher cap to continue using the Marketplace without changing it every time. We recommend using the Allowance cap by default.

Once the MetaMask pop up opens, you will see something like this:

![](/images/blockchain-integration/spending-cap-1.png)

Choose the default option to interact with the Marketplace without having to sign this message again.

![](/images/blockchain-integration/spending-cap-2.png)

Any user with enough MANA can purchase the NFT if the value of the asset to be bought is lower than the allowance cap. An order is executed by calling the `executeOrder` function in the Marketplace Smart Contract.

```sol
/// @param nftAddress The address of the NFT contract (The LandRegistry, EstateRegistry or Wearable/Emote/etc Collection address).
/// @param assetId The token id of the NFT.
/// @param price The price (in MANA) the caller wants to purchase the NFT for.
///        Has to match the price of the Order for that NFT.
function executeOrder(
  address nftAddress,
  uint256 assetId,
  uint256 price
)
```

When the transaction to execute an Order is successful. The buyer will pay the price in MANA to the owner of the NFT, and the NFT will be transferred from the owner to the buyer, which becomes the new owner.

Another way to execute Orders is by calling 'safeExecuteOrder'.

```sol
/// @param nftAddress The address of the NFT contract (The LandRegistry, EstateRegistry or Wearable/Emote Collection address).
/// @param assetId The token id of the NFT.
/// @param price The price (in MANA) the caller wants to purchase the NFT for.
///        Has to match the price of the Order for that NFT.
/// @param fingerprint Data that determines how the NFT has to be composed of for the Order to be executed.
function safeExecuteOrder(
  address nftAddress,
  uint256 assetId,
  uint256 price,
  bytes memory fingerprint
)
```

Composable NFTs (NFTs made up of other NFTs such as Estates composed of many LANDs) have a fingerprint that determines what they are composed of.

By executing an Order providing a fingerprint, you are telling the contract that you want that NFT to be composed in a certain way. If it is different, the Order will fail to be executed.

This a safe mechanism to prevent bad actors from removing all LAND from an Estate before an interested buyer purchase it.

More information about it can be found in [Integrating Decentraland's Estate in your Marketplace](/player/blockchain-integration/estates-marketplace-integrations)

**IMPORTANT: The asset owner has to approve the Marketplace contract to operate the NFT on its behalf. The buyer also has to approve the Marketplace contract to operate MANA. If these conditions are not met, the transaction will revert when the Marketplace contract transfers the NFT from the previous owner to the buyer or when the contract tries to transfer MANA from the buyer to the owner.**

## Bids

Maybe the NFT you like is too expensive or is not even on sale. This is where the Bids contract comes in handy.

Users can create a Bid for an NFT using this contract by determining the price they are willing to pay. If the owner finds that price fair, they can accept the Bid and the bidder will become the owner of the NFT while the previous owner will receive the payment in MANA.

Bids can be created by calling the `placeBid` function on the Bids contract.

```sol
/// @param _tokenAddress The address of the NFT contract (The LandRegistry, EstateRegistry or Wearable/Emote/etc Collection address).
/// @param _tokenId The token id of the NFT.
/// @param _price The price (in MANA) the caller wants to purchase the NFT for.
/// @param _duration How long the Bid will be valid until it expires.
function placeBid(
    address _tokenAddress,
    uint256 _tokenId,
    uint256 _price,
    uint256 _duration
)
```

There is another `placeBid` function in the contract that, along with the arguments received by the previous examples, receives a `fingerprint` argument.

```sol
/// @param _tokenAddress The address of the NFT contract (The LandRegistry, EstateRegistry or Wearable/Emote/etc Collection address).
/// @param _tokenId The token id of the NFT.
/// @param _price The price (in MANA) the caller wants to purchase the NFT for.
/// @param _duration How long the Bid will be valid until it expires.
/// @param _fingerprint Data that determines how the NFT has to be composed of for the Bid to be executed.
function placeBid(
    address _tokenAddress,
    uint256 _tokenId,
    uint256 _price,
    uint256 _duration,
    bytes memory _fingerprint
)
```

More information about the `fingerprint` argument can be found in [Integrating Decentraland's Estate in your Marketplace](/player/blockchain-integration/estates-marketplace-integrations)

As the owner of the NFT. You can accept any Bids made for it as long as it has not expired and the bidder still has enough MANA to pay for it.

To accept a Bid, the asset owner has to transfer the NFT to the Bids contract using the `safeTransferFrom` function of the NFT contract with some extra data containing the accepted Bid information.

For example, to accept a Bid for one of my LANDs, I would have to call the LAND contract `safeTransferFrom` function to transfer my LAND to the Bids contract, which will then execute the bid.

```sol
/// @param from The current owner (or operator) of the NFT.
/// @param to The address that will receive the NFT.
/// @param assetId The token id of the NFT to be transferred.
/// @param userData Arbitrary data used by the recipient of the NFT to handle the transfer.
function safeTransferFrom(
  address from,
  address to,
  uint256 assetId,
  bytes memory userData
)
```

Let's say I want to accept a Bid with id "0xBidId" for one of the LANDs I own that has token id "100".

I would have to call the `safeTransferFrom` function on the LAND contract with the following input.

```js
safeTransferFrom(
  "0xMyAddress", // My address as I am the owner of the LAND.
  "0xBidsContractAddress", // The address of the Bids contract in the same network.
  "100", // The token id of my LAND.
  "0xBidId" // The id of the Bid I want to accept.
);
```

When the Bids contract receives the NFT, it will check in its `onERC721Received` function that the bid is not expired and the bidder has enough funds to pay for it. If everything is correct, the NFT will be transferred to the bidder and the caller of the `safeTransferFrom` function will be paid the amount of MANA declared in the Bid.

**IMPORTANT: The bidder must have approved the Bids Smart Contract to operate MANA on its behalf or the bid execution will revert when the Bids contract tries to transfer the bidders MANA to the previous owner.**

## CollectionStore

This smart contract can only be found on the Polygon Network. This is because collections like Wearables, Emotes, etc, only exist on that chain, meaning there is no purpose for them to be on Ethereum unless Collections were published there.

When a creator publishes a collection approved by the curation committee, the creator can then put the collection on sale in the marketplace, allowing other users to buy the items of that collection for the price determined by the creator.

When you buy items from a collection this way, you are minting a new NFT that can be commercialized with the Polygon Marketplace or Bids smart contract.

If a collection is on sale, any user with a sufficient amount of MANA can buy an item from it as long as there is stock left to be minted.

The CollectionStore smart contract exposes the `buy` function to do so.

```sol
/// @param _itemsToBuy A list of items from different collections that the caller want to buy.
function buy(ItemToBuy[] memory _itemsToBuy)
```

```sol
struct ItemToBuy {
  // The address of the collection the items in the ids array belong to.
  IERC721CollectionV2 collection;
  // The id of the particular items in the collection that the caller want to buy.
  uint256[] ids;
  // The price that the buyer wants to pay for the item in the same index.
  // Must be equal to the price set by the creator.
  uint256[] prices;
  // The addresses that will receive the minted items in the same index.
  address[] beneficiaries;
}
```

To make this easier to understand. Imagine that I want to buy item "Spooky Hat" with item id 0 from the collection called "Halloween Madness".

The hat has been determined by the creator to have a price of 20 MANA.

To buy the item, I would have to call the `buy` function with the following data:

```js
buy([
  [
    "0xHalloweenMadnessAddress",
    ["0"], // The item id of the Spooky Hat. Other items in the collection will have different incrementing ids.
    ["20000000000000000000"], // Which is the equivalent in wei to 20
    ["My own address"],
  ],
]);
```

When the transaction to buy the item is successful. 20 MANA will be transferred from my address to the creator (or a beneficiary defined by the creator), the hat will be minted as an NFT and transferred to me.

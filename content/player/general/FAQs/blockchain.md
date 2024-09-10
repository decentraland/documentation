---
date: 2020-02-17
title: Blockchain
description: Decentraland uses the Ethereum blockchain to record the ownership of all digital assets and tradable items.
aliases:
  - /get-a-wallet/
  - /blockchain-integration/get-a-wallet/
  - /examples/get-a-wallet/
categories:
  - examples
type: Document
url: player/blockchain-integration/get-a-wallet
weight: 10
---

## What is a wallet?

Decentraland uses the Ethereum blockchain to record the ownership of all digital assets and tradable items.

<img src="/images/media/get-a-wallet-account.png" style="margin: 2rem auto; display: block;width: 90%; max-width: 600px;" />

Digital wallets are tools that work as a bridge between the blockchain and the dApp (decentralized applications). This means that with a wallet you will be able to monitor your available funds, transaction history and security options.

## Do I need a wallet to play in Decentraland?

<img src="/images/media/get-a-wallet-wallet.png" style="max-width: 400px;margin: 2rem auto;display: block;" />

If you want to fully enjoy the Decentraland experience, we highly recommend you get yourself a digital wallet. Why? Because it will work as your personal account, allowing you to connect from different devices, keeping all your digital assets (such as names, collectibles, LANDs) and progress safe.

If you choose to experience Decentraland without a wallet, the information will be only be locally stored: you will be able to walk around, customize your avatar and chat with others in-world, but you won’t have the chance to receive daily rewards, participate in events or log in with a different device using the same Guest ID and Avatar.

## How do I get a digital wallet?

To enter Decentraland, you must use a wallet that is integrated to your web browser, so we recommend you [MetaMask](https://metamask.io/)

<img src="/images/media/get-a-wallet-metamask-logo.png" style="max-width: 60%;margin: 2rem auto;display: block;" />

<span style="text-align:center;display:block">Once you install it, you will see an icon like this:</span>

<img src="/images/media/get-a-wallet-metamask-extension.png" style="margin: 2rem auto;display: block; width: 70%;" />

## Wallet address

All wallets have a public and private key. A public key Is a unique identifier for your wallet and it looks like this: **0xcba113f589805095a892ecefdb4eb83eff45d98**. It is basically a name that you can share freely with others and it’s used to direct assets to your wallet.

<span style="text-align:center;display:block">You can localize your wallet address clicking on the extension icon in your browser, and then clicking on your wallet name with the public key to copy it to clipboard:</span>

<img src="/images/media/get-a-wallet-public-key-1.png" style="max-width: 50%;margin: 2rem auto;display: block;" />

<span style="text-align:center;display:block">Or by clicking on your account details:</span>

<img src="/images/media/get-a-wallet-public-key-2.png" style="margin: 2rem auto;display: block; width: 90%;" />

The private key is used by your wallet to sign each transaction and certify that it was truly sent by you. It is also used to restore your wallet in case you forget your password.

Keep in mind that a digital wallet is like a bank account, so make sure you **don’t forget your password, or backup phrase. Keep them in a safe place and don’t share them with anyone.**

## What is Ether (ETH), and how do I send it to my wallet?

<img src="/images/media/get-a-wallet-ether.png" style="max-width: 20%;margin: 2rem auto;display: block;" />

For executing transactions, you’ll need to put money in your wallet. dApps based on Ethereum, like Decentraland, use Ether: a digital currency that powers the Ethereum network. It acts like any other currency, in that its value fluctuates with the market.

- You need to convert your currency (e.g. USD, CAD, GBP) into Ether to pay for things such as a collectibles.

## How do I get Ether?

_For US citizens only:_

You can purchase ETH for the MetaMask Browser Extension with the Coinbase service.

- Click the `Buy` button.
- Select the `Coinbase` option.
- Click the `Continue to Coinbase` button to purchase Ethereum.

_For the rest of the World:_

You need to buy ETH from Coinbase or another exchange using normal fiat currency.

- Copy your MetaMask address by clicking on your name account and address.
- Select `Copy Address to clipboard`.
- Go to Coinbase or another exchange.
- Click `Accounts` in your top navigation.
- Select your ETH wallet and click `buy`.
- Follow the steps to `Add payment method` and paste your MetaMask address with the amount you'd like to transfer.

## What is MANA and how do I get it?

<img src="/images/media/get-a-wallet-mana.png" style="margin: 2rem auto; display: block;width: 90%; max-width: 400px;" />

[MANA](https://etherscan.io/token/decentraland) is Decentraland’s fungible (reproducible or interchangeable) cryptocurrency token. It is burned, or spent in exchange for LAND parcels, wearables and names.

Steps to buy MANA:

- First, you need to register with an exchange that lists MANA (such as [Coinbase](https://www.coinbase.com/), [Huobi](https://www.huobi.io/), [Binance](https://www.binance.com/)).
- Secondly, you will need to deposit funds into your account. While things change rapidly in the crypto world, it’s not likely that there’s an exchange available to convert your USD directly for MANA. If that’s the case, you’ll first need to obtain a cryptocurrency listed in a currency pair with MANA, such as Ether (ETH), and then exchange it for Decentraland’s native token.
- Third, once logged into your exchange account, click on the “Markets” or “Exchange” link and search for your desired currency pairing. For example, MANA/ETH. In the “Buy” field, you can then specify the amount of MANA you want to buy or the amount of ETH you want to spend. Make sure you take a moment to review the full details of the transaction including any fees that apply and the total cost of completing your purchase.

## What is ‘gas’?

‘Gas’ is a shorthand term used to describe the cost of powering a transaction or contract in Ethereum. Because blockchain is decentralized, every transaction is distributed through multiple computers, not a central server. This ensures each token – in this case, each collectible – is secure and one-of-a-kind. It also takes a lot of computational power, which is covered by the cost of gas.

- _‘Gas’ is composed of two parts: Gas Price and Gas Limit. Gas Price is what you offer to pay the miners (in a tiny measurement of ether called ‘gwei’) for each operation to execute the smart contract. Gas Limit is how many operations you let them do before they run out of gas and drop the transaction._
- _1 gwei = 1/1,000,000,000th of an Ether._

<img src="/images/media/get-a-wallet-gas.png" style="margin: 2rem auto;display: block; width:90%" />

To summarize, Gas Price (gwei) is the amount of Ether offered per gas unit to pay miners to process your transaction. The higher the gas price you set, the faster your transaction will get processed. So, for more important transactions – such as a collectible that you really like ;D – think about increasing the suggested gas price.

**For extra technical information, visit**
**[this link]({{< ref "/player/blockchain-integration/ethereum-essentials.md" >}})**

# Polygon

## What is Polygon?

As stated in the the official Polygon website, [Polygon](https://polygon.technology/) is a protocol and a framework for building and connecting Ethereum-compatible blockchain networks. Aggregating scalable solutions on Ethereum supporting a multi-chain Ethereum ecosystem.”

## What is Matic?

MATIC is Polygon’s native token. It is a cryptocurrency used to cover gas fees in the Polygon network, among other use cases. MATIC is to Polygon as ETH is to Ethereum.
You can buy MATIC in most cryptocurrency exchanges.

## Polygon in Decentraland’s Marketplace and Builder

By using the Polygon network, and thanks to Decentraland’s DAO, users can list, sell and buy wearables in the Marketplace or publish their collections in the Builder without paying for the transaction gas using the meta-transactions services.

**Transactions in Polygon are not free**. The Decentraland DAO covers the cost of the transactions in Polygon so that users can enjoy many costless transactions in the Marketplace.

In order to enjoy costless transactions there are three conditions that need to be met:

- You need to be connected to Ethereum Mainnet.
- The item you are intending to buy needs to have a price of 1 MANA or higher.
- You didn’t reach your free transaction limit.

The Decentraland DAO reserves itself the rights to consume or pause the meta-transactions services when the network’s gas fees are high to prevent the consumption of the gas tanks so they can last longer and be used by as many people as possible.

## Why do I have to cover the transaction fees for items that cost less than 1 MANA?

In order to avoid exploitation and protect the free gas service, items that cost less than 1 MANA are not included in the costless transactions. You can buy these items by connecting to the Polygon network with MATIC in your wallet.

Gas fees are variable.

## What can I do if network fees are higher than 300 gwei?

Network fees are variable, so the best you can do is wait and try again at another moment.

Alternatively, you can buy these items by connecting to the Polygon network to use the MATIC in your wallet to pay for the fees. The MATIC fee will be deducted automatically as part of the transaction fee of the Polygon network. You only need to be connected to the Polygon network and have MATIC in your wallet.

Gas fees are variable.

## What happens if the free transaction limit is reached?

The free transaction limit renews every day, so you can try the day after. Alternatively, you can cover the cost of your transaction with MATIC while being connected to the Polygon network.

The MATIC fee will be deducted automatically as part of the transaction fee of the Polygon network. You only need to be connected to the Polygon network and have MATIC in your wallet.

Gas fees are variable.

## Where can I get MATIC to pay for transaction fees?

One way to obtain MATIC is buying it through [the Account dapp](https://account.decentraland.org/).

Simply click on the BUY button in the Polygon MANA section, and exchange the crypto you want to purchase from MANA to MATIC.

Another way is through Decentralized or Centralized exchanges. You can check [https://polygon.technology/matic-token/](https://polygon.technology/matic-token/) to see which exchanges operate with MATIC. If you want to use a Centralized exchange, make sure that it allows withdrawals through the Polygon network.

If you have MATIC in the Ethereum network, you can always use the [Polygon Bridge](https://wallet.polygon.technology/bridge/) to deposit that MATIC to the Polygon network.

> **Warning:**
> After completing a transaction in Polygon, remember to switch back to Ethereum Mainnet to enjoy all the features in the Marketplace and the Builder that are not supported in the Polygon network.

# Ethereum essentials

---

date: 2018-01-01
title: About the blockchain
description: How Decentraland uses the Ethereum blockchain.
categories:

- blockchain-integration
  type: Document
  aliases:
- /blockchain-interactions/ethereum-essentials
- /blockchain-integration/ethereum-essentials/
  url: /player/blockchain-integration/ethereum-essentials
  weight: 2

---

All blockchains are in essence decentralized databases that are distributed among the machines of a network. Transactions are grouped into “blocks” and processed sequentially to form a _chain_ of events.

Ethereum is one of the most popular blockchains. What sets it apart from others, such as Bitcoin, is that it uses the blockchain as storage for more than just a record of currency transactions. Ethereum can store more complex information to distinguish different kinds of tokens or even handle unique tokens with specific characteristics. The Ethereum blockchain also runs smart contracts, these allow to execute more complex transactions that can also depend on agreed upon events.

Decentraland uses the Ethereum blockchain to record the ownership of the digital assets, and other tradable items that can be read and reacted to by a 3D scene.

The blockchain isn’t used to store the scene state, player position or anything that needs to change in real time as a player interacts with a scene, all of that is either stored locally on each player's machine, or on a private server owned by the scene owner. The developers of each scene must choose what information is worth storing on the blockchain, and what to store in a private server.

## Wallets

Ethereum tokens are held by wallets. An Ethereum wallet can hold various tokens, including Ether, MANA, LAND, and other tokens that may be used by games or experiences in Decentraland.

There are many wallet providers where you can hold Decentraland tokens. To use the Marketplace, or to enter Decentraland, you must use a wallet that is integrated to your web browser, so we recommend that you use:

- [Metamask](https://metamask.io/)
- [Trezor](https://trezor.io/)/[Ledger](https://www.ledger.com/) hardware wallets

Every wallet has a public and a private key. The hash of your public key is your wallet’s unique address, used to route transactions and identify a player. Your private key is used by your wallet to sign each transaction that you send to the network and certify that it was truly sent by you. Your private key is also used to restore your wallet in case you forget your password, so keep it in a safe place and don’t share it with anyone.

In Decentraland, player identities are built around wallets. Since wallet public keys are unique, your scene can use them to identify a Decentraland user in a persistent way. Wallets can also hold different tokens that can give a player a unique avatar, a wearable item, permissions to enter scenes that choose to restrict access, a special weapon to use in a game, etc.

## Transactions

Transactions make changes to the information that’s stored in the blockchain. Typical transactions involve tokens changing owners, for example user A giving his LAND token to user B in exchange for an amount of MANA tokens. In the Ethereum network, however, a transaction can also mean changing the information that’s stored about a token without changing its owner. For example, changing the description of a parcel, or merging several parcels into an Estate.

All transactions that occur in Ethereum’s main chain have a cost that is paid in Ether tokens. This fee is referred to as the ‘gas’ fee, and it’s paid to the network user that ‘mines’ the transaction.

When you request a transaction to take place, you set the gas price that you’re willing to pay for the transaction to be mined. Transactions that offer higher prices get mined faster, since miners give these priority. Market prices for these transactions oscillate regularly, they tend to be more expensive when there is a higher usage of the network. Make sure that what you offer isn’t below the market price, otherwise your transaction could remain in an unprocessed pool indefinitely.

All transactions must be signed by an Ethereum address, using the addresse’s private key. This is what certifies that the transaction was carried out by that address.

### Transaction validation

Blockchain transactions aren’t immediate, they require time to be “mined” by one of the nodes in the network, and then to be propagated throughout the rest of the machines. The more transactions that are being requested by the network, the more time they take to be validated.

In brief terms, this is how a transaction is validated:

1. A new transaction occurs, it goes into a pool of unconfirmed transactions.
2. One of the machines in the network successfully solves an algorithm to mine a new “block” containing a handful of transactions from this pool, including this one. It attaches this new block to the end of the chain.
3. The block is shared with other machines of the network. Each machine verifies that each transaction in a block is valid and checks the block’s hash to ensure it’s legitimate, then it adds it to its own version of the chain.
4. The new block is propagated throughout the whole network. There’s a universally shared understanding that this transaction has taken place.

#### Sidechains

Decentraland is partnering with [Matic](https://matic.network/) to create a _sidechain_ (a special kind of blockchain) that will be able to handle transactions faster and cheaper than the main Ethereum network. This sidechain will be ideal for in-game transactions, as changes can occur closer to real time and at a very low cost. For transactions that involve valuable items, we’ll still recommend the main Ethereum chain, as it will be more secure.

Each developer working on a scene will be able to choose whether to use the mainchain, the sidechain or a combination of both for different transactions.

The sidechain will be kept interoperable with the Ethereum’s mainchain. You’ll be able to load tokens from the main chain into the side chain and vice versa. Transactions that take place in the sidechain are eventually reflected in the mainchain when the tokens “exit” back into the mainchain.

Read more about this in [Second layer]({{< ref "/content/creator/scenes/blockchain/second-layer.md" >}}).

#### Trigger transactions from a scene

Your scene’s code can trigger transactions, both on the Ethereum mainchain and on Decentraland’s sidechain. You could have a store in your scene that sells tokens (like NFTs), or have a game that rewards game items to players that achieve certain goals.
The user must always approve these transactions explicitly on their Ethereum client. For example, when using Metamask, Metamask prompts the user to accept each transaction before it’s processed.
Read [game design doc] for more ideas about how to integrate a scene to the blockchain. See [blockchain operations] for instructions on how to implement these integrations.

## Types of tokens

Different types of tokens can be handled in the Ethereum network. A few standards have emerged that group tokens that share the same characteristics.

In Decentraland, you can use tokens to represent items that relate to your game or experience, such as a weapon or a trophy. As tokens are held in a player’s wallet, they accompany a player from scene to scene, so each scene can choose if and how they want to react to every existing kind of token.

Read [What are NFTs](https://decentraland.org/blog/technology/what-are-nfts/) on our blog for a more in-depth look at the emergence and evolution of non-fungible tokens.

#### Fungible tokens

If an item is fungible, then it can be substituted or exchanged for any similar item. Fiat currencies, like the US dollar, are fungible. One dollar bill can be exchanged for any other dollar bill.

Cryptocurrency tokens like Bitcoin, Ethereum, and MANA are all fungible because one token unit can be exchanged for any other token unit.

You could also create custom fungible tokens to use in Decentraland scenes and use them to depict items that are all equal and have no distinctive or customizable properties between them. You could, for example, create a game that revolves around collecting a large quantity of identical items, and represent these through a fungible token . You could also use a fungible token to represent a golden ticket that gives players who hold it access to a specific region or service.

_ERC20_ is the most accepted standard for fungible tokens in the Ethereum Network. MANA is built upon this standard.

#### Non-Fungible tokens

Non-fungible tokens (or NFTs) have characteristics that make each unit objectively different from others. Parcels of LAND in Decentraland are NFTs, as the location of each parcel is unique. The adjacency to other parcels, roads, or districts make these locations relevant to token owners.

In Decentraland, you can use NFTs to represent in-game items such as avatars, wearables, weapons, and other inventory items. You could, for example, use a single type of NFT to represent all weapons in your game, and differentiate them by setting different properties in these NFT.

NFTs can be used to provide provably scarce digital goods. Because of the legitimate scarcity made possible by the blockchain, buyers can rest assured that the art they purchase is, in fact, rare. This gives digital art real value that we’ve never seen before.

Game items will have a history that’s stored in the blockchain. This history could deem an item more valuable, for example if it was used to accomplish great achievements or used by someone who’s admired.

Depending on the contract describing the token, each NFT could either be immutable, or you could allow players to customize and change certain characteristics about them if they choose to.

_ERC721_ is the most accepted standard for non-fungible tokens in the Ethereum Network. LAND tokens follow the ERC721 standard.

## Smart Contracts

A contract consists of a both code (its methods) and data (its state) that resides at a specific address on the Ethereum blockchain.

The methods in a contract are always called via a transaction that has the _to_ field set to the contract’s address. The code that’s executed by the contract’s method can include calls to other contracts, these trigger more transactions that have the _from_ field set to the contract’s address.

A contract can’t trigger any actions on its own or based on a time event. All actions performed by a smart contract always arise from a transaction that calls one of the contract’s functions.
You can use smart contracts to condition transactions based on custom conditions. For example, players could stake a bet on the outcome of a game, and the corresponding payments would occur as soon as the outcome of the game is informed to the contract.
The entire code for a smart contract is public to whoever wants to read it. This allows developers to create publicly verifiable rules.
All Tokens are defined by a smart contract that specifies its characteristics and what can be done with it. Decentraland has written and maintains a number of smart contracts. LAND and MANA tokens themselves are defined by the _LANDregistry_ and _MANAtoken_ contracts respectively.

You can find the address of every contract created by Decentraland in [Decentraland smart contracts](https://contracts.decentraland.org/addresses.json).

You can read the full code of each of those contracts, as it's public information on the blockchain. You can find the contract by name on [Etherscan](https://etherscan.io/contractsVerified) and read its content there.

## dApps

_dApps_ (decentralized applications) are applications that are built upon smart contracts and the blockchain.

A dApp can be as simple as something that validates that your wallet holds a certain token and lets you use a service. Or it can be a fully fledged application with its own UI, such as the Decentraland Marketplace.

If you want to build your own dApp around Decentrlanad, see [Create a dApp]({{< ref "/content/creator/sdk7/blockchain/create-a-dapp.md" >}}).

## Sepolia test network

Before you deploy a smart contract, create a new type of token, or a Decentraland scene that relies on transactions on the Ethereum network, you need to make sure that it has no bugs or gaps that malicious users could exploit.

The Sepolia test network is an alternative version of Ethereum that’s specifically made for running tests.

Tokens in the Sepolia network have no real value, so you can afford to make mistakes without running any real risk. You can replenish any lost tokens for free by using a faucet:

- Sepolia Ether faucet (<https://www.alchemy.com/faucets/ethereum-sepolia/>)
<!-- - Sepolia MANA faucet (https://faucet.decentraland.today/) -->

If you’re developing a scene that triggers transactions, testing these transactions in the Sepolia network is free, as the tokens you send don’t have a value. In mainnet you would otherwise have to pay at the very least a real gas fee in Ether for each test transaction you carry out.

Once you’re confident that your code works as expected and can’t be exploited, you can deploy to the Ethereum mainnet.

## Blockchain reorgs

Occasionally, multiple machines will create alternative new blocks at roughly the same time. This is a problem, because this forks the chain into two diverging versions that could potentially contradict each other. When a fork occurs, Ethereum solves this by always giving priority to the longest chain and discarding any shorter chains. Even though it’s possible for two rivaling chains to exist at the same time, soon one of the two chains will add another block and outgrow the other. Due to the time it takes to solve the mining algorithms, it becomes increasingly difficult for rivaling chains to keep growing in perfect sync with each other. Sooner or later one will prevail over the other.

When one chain outgrows the other and the dispute is resolved, machines that had adopted the shorter chain need to make adjustments. This is what’s known as a “reorg”. They need to roll back on all of the transactions included in the blocks from the branch they’re in until they reach the point at which the fork occurred. Then they need to add the new blocks from the longer branch that’s considered legitimate.

Rolled back transactions may return to the pool of pending transactions until they’re picked up again by a miner (or are discarded). Any gas fees paid for these transactions are also rolled back.

Blocks that were just added to the end of a chain have a substantial chance of being rolled back because of the mechanisms explained above. As subsequent blocks are added to the end of the chain, it becomes less and less likely that the blocks that are further back in the blockchain could be rolled back, because that would require a larger reorg. Due to this, each new block that’s added to the end of the chain after a transaction is called a confirmation for that transaction.

When creating applications (or scenes) that use information from off the blockchain, you should be aware of the occurrence of reorgs. You might want to only consider transactions as verified when a certain number of confirmations have occurred, and the transaction is no longer at the very end of the chain.

Using several confirmations will make the information very stable, but transactions will take a long time to be reflected.
Using few confirmations, changes will be reflected faster, but there will sometimes be hiccups that appear to undo transactions when reorgs occur. If these transactions have off-chain consequences in your scene, then you might need to somehow reverse these consequences as well.

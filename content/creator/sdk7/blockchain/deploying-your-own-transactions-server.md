---
date: 2024-12-16
title: Deploying your own transactions server
description: Provide users with costless transactions
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/deploying-your-own-transactions-server/
  - /creator/development-guide/deploying-your-own-transactions-server
url: /creator/development-guide/sdk7/deploying-your-own-transactions-server/
weight: 5
---

The [transactions-server](https://github.com/decentraland/transactions-server/tree/1.8.0) is a proxy server that relays transactions to [Gelato](https://www.gelato.network/relay). It receives a signed transaction from the client that it's in turn sent to the appropiate network behind the scenes. This allows the server's owner to facilitate it's users with costless transactions

The transaction server is used to help with the UX of using multiple networks and to prevent them from switching network providers on the fly. The users can stay connected to [Ethereum](https://ethereum.org/en/) and interact with [Polygon](https://polygon.technology/) [by only signing transactions](https://docs.decentraland.org/blockchain-integration/transactions-in-polygon/)

The Decentraland DAO has set up a server used by our dapps, covering the cost up to a certain limit with a few [restrictions](#restrictions). This document explains how you can [deploy this server](#running-the-server) to enable your users to relay transactions with the restrictions you need, if any.

## Restrictions

All restrictions are per-transaction the user tries to send. Which, in practice, translates into a POST request to the server.

The configurable restrictions the server has are:

- Checks for a quota of max transactions per day. See [the collections section](#collections) for more info.
- Checks for whitelisted contracts, so if a transaction is trying to interact with a contract that's not recognized it'll fail. To do this it uses
  - The deployed contracts and collections. See [the contracts and collections section](#contracts-and-collections) for more info
- The price of sales, restricting it if it's below a threshold. See [min sale value section](#min-sale-value) for more info

## Configuring Gelato

[Gelato](https://www.gelato.network/relay) is a Multichain Relayer Protocol. We use it's infrastructure to enable costless transactions. This effectively means that, when you go to send a transaction, you're instead signing a message and sending that to Gelato. The service will take care of sending the transaction for you and giving you a response (transaction hash) back.

It needs a contract to forward the transactions, but luckily we can reuse the one that's being used by Decentraland (see below)

[Gelato](https://www.gelato.network/relay) works as an API to the server. [To configure](#configuring-the-server) it you'll first need an API KEY which we [we'll use later](#gelato). To get these:

- [Register](https://app.gelato.network/relay) in the service
- Create new dapp for the network you intent to target. To mimic what Decentraland setup:
  - Select the `Mainnets` options
  - Set an appropiate `App name` for your dApp
  - choose `Polygon` as the network for the `Smart Contract`
  - Enable the `Any Contract` toggle option
- Copy the API KEY from the `API Key` section

Lastly, you'll need to fund your newly created dapp. You can do this by connecting your wallet in the [1Balance](https://app.gelato.network/1balance) section at the left sidebar. Once connected, it'll enable you to deposit your [USDC](https://polygonscan.com/token/0x3c499c542cef5e3811e1192ce70d8cc03d5c3359) to fund the transactions your users will send. If you need to get MATIC, check this [post](https://docs.decentraland.org/blockchain-integration/transactions-in-polygon/#where-can-i-get-matic-to-pay-for-transaction-fees).

### Testnet

If you want to test your app before going live and you're using Polygon you can do so in `Polygon Amoy`, the Polygon testnet.

To do this simply repeat [the process](#configuring-gelato) but picking `Matic Testnet (Amoy)` on the network field.

You'll need to fund your dapp, but you can do so easily by getting Sepolia ETH tokens from the [faucet](https://sepoliafaucet.com/).

## Downloading the transactions server

First off, you'll need a copy of the Decentraland's transactions-server code. You can find it [on github](https://github.com/decentraland/transactions-server/tree/v1). From there, you have two options:

1. **Downloading the code**: To download the code, you have to first click on the green `Code` button and then either

- Click on `Download ZIP`
- Copy the URL under the `Clone` title and then run `$ git clone THE_URL_HERE`

2. **Forking the code**: You can click the `fork` button on the top right of the page. Once the process is complete, you'll be able to download you code the same way you'd do it on the first option. You'll need a Github account for this, for more information on forking repositories see [here](https://docs.github.com/en/enterprise-server@3.5/get-started/quickstart/fork-a-repo)

## Configuring the server

The transactions server is written in [NodeJS](https://nodejs.org/en/) using [Typescript](https://www.typescriptlang.org/). Before running it you'll need to configure a few environment variables.

To do this:

- Copy the `.env.example` file and paste it renamed to `.env`
- Open the `.env` file. You'll see some variables have a default value, like `HTTP_SERVER_PORT=5000` (in which port to run the server)
- You can leave most values as they are, but there're a few important values to consider:
  - [Gelato](#gelato)
  - [Transactions](#transactions)
  - [Contracts and collections](#contracts-and-collections)
  - [Min sale value](#min-sale-value)

### Gelato

Use the API KEY we got when [configuring gelato](#configuring-gelato).

```
GELATO_API_KEY=p_qXAlcVwWyU__Fjbn_qwr0rTy14asDf_Z2XCVBnmZX_
```

### Transactions

When a new transaction request arrives it'll check the amount **an address** has sent that day. If it's over the set value the transaction will fail.

```
MAX_TRANSACTIONS_PER_DAY=10
```

To completely remove this check, you can go into the code and remove the

```ts
await checkQuota(components, transactionData)
```

method from `async function checkData(transactionData: TransactionData): Promise<void> {` in `src/ports/transactions/component.ts`

### Contracts and collections

The server will fetch the Contract addresses URL and store them locally and query the subgraph. When a new transaction request arrives it'll then check if the contract the transaction is interacting with belongs to either the deployed contracts in the URL or the deployed collections in the subgraph.

If you want to supply your own contracts change the URL and keep the same structure the current <https://contracts.decentraland.org/addresses.json> has. The network used is determined by COLLECTIONS_CHAIN_ID, and the interval with which the cache is re-fetched is COLLECTIONS_CHAIN_ID

If you have your own collections you can also change the subgraph URL.

To completely remove this checks, you can go into the code and remove the

```ts
await checkContractAddress(components, transactionData)
```

method from `async function checkData(transactionData: TransactionData): Promise<void> {` in `src/ports/transactions/component.ts`

```
CONTRACT_ADDRESSES_URL=https://contracts.decentraland.org/addresses.json
COLLECTIONS_FETCH_INTERVAL_MS=3600000
COLLECTIONS_CHAIN_ID=80002

COLLECTIONS_SUBGRAPH_URL=https://subgraph.decentraland.org/decentraland/collections-matic-amoy
```

### Min sale value

When a new transaction request arrives it'll first parse the data it's trying to relay. If it detects a sale (marketplace buy, bid, etc), it'll check the value against MIN_SALE_VALUE_IN_WEI. If it's lower, the transaction will fail.

```
MIN_SALE_VALUE_IN_WEI=1000000000000000000
```

To check the relevant sale methods, you can see `src/ports/transaction/validation/checkSalePrice.ts` and to completely remove this check, you can go into the code and remove the

```ts
await checkSalePrice(components, transactionData)
```

method from `async function checkData(transactionData: TransactionData): Promise<void> {` in `src/ports/transactions/component.ts`

## Running the server

Now all configuration is set, what's left is actually running the server. You can follow [it's README]() but in a nutshell, you'll have to:

- Have [NodeJS](https://nodejs.org/en/) installed
- Open your terminal of choice
- Run the following commands:

```bash
npm install
npm run migrate # only the first run
npm run start
```

Of course, you'll probably want to deploy this to your service of choice, like [AWS](https://aws.amazon.com/) for example. You can use the Project's [Dockerfile](https://github.com/decentraland/transactions-server/tree/v1/blob/master/Dockerfile) to do so.

## Using the server

Now everthing's set up and running, it's time to actually use the server.

To actually send a transaction, you need to POST to `/transactions`. The schema required for the request is defined by `transactionSchema` on `src/ports/transaction/types.ts`.

If, instead, you want to use our pre-made libs to make your life easier you can try [decentraland-transactions](https://github.com/decentraland/decentraland-transactions). It's used via [decentraland-dapps](https://github.com/decentraland/decentraland-dapps) in our dapps like the [Marketplace](https://market.decentraland.org), with the utils [`sendTransaction`](https://github.com/decentraland/decentraland-dapps/blob/master/src/modules/wallet/utils.ts#L104). Check [this code](https://github.com/decentraland/marketplace/blob/a2191515c6ae7ede54a685cc2dd9f9fafa35366b/webapp/src/modules/vendor/decentraland/OrderService.ts#L33) for an example.

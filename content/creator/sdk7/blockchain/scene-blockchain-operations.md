---
date: 2018-01-07
title: Scene blockchain operations
description: Learn what the SDK offers for performing operations with the Ethereum blockchain
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/scene-blockchain-operations/
weight: 1
---

A Decentraland scene can interface with the Ethereum blockchain. This can serve to obtain data about the user's wallet and the tokens in it, or to trigger transactions that could involve any Ethereum token, fungible or non-fungible. This can be used in many ways, for example to sell tokens, to reward tokens as part of a game-mechanic, to change how a player interacts with a scene if they own certain tokens, etc.

You use the **Ethers.js** library in Decentraland scenes, this is a popular 3rd party library to interact with the Ethereum blockchain.

Note that all transactions in the Ethereum mainnet that are triggered by a scene will require a player to approve and pay a gas fee.

All blockchain operations also need to be carried out as [asynchronous functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}}), since the timing depends on external events.




<!--
## Download and import the ethers.js library

To use ethers.js library, you must manually install the package in your scene's project. To do so, follow the steps in [Manage dependencies]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md" >}}), typing the library name `ethers`.

Once installed, you can import whatever you need from `ethers` to the scene's code:

```ts
import { ethers } from 'ethers'
``` -->

<!--

## Ethereum controller library

The simplest way to perform operations on the Ethereum blockchain is through the _ethereum controller_ library. This controller is packaged with the SDK, so you don't need to run any manual installations.

To import the Ethereum controller into your scene file:

```ts
import * as EthereumController from "~system/EthereumController"
```

Below we explain some of the things you can do with this controller. -->

## Get a player's ethereum account

To get a player's Ethereum account, use the `getPlayer()` function.

```ts
import { getPlayer } from '@dcl/sdk/src/players'

export function main() {
	let userData = getPlayer()
	if (!userData.isGuest) {
		console.log(userData.userId)
	} else {
		log('Player is not connected with Web3')
	}
}
```

Note that if a player has entered Decentraland as a guest, they will not have a connected ethereum wallet. If they are connected as guests, the `isGuest` field in the response from `getPlayer()` will be true. If `hasConnectedWeb3` is true, then you can obtain the player's address from the field `publicKey`. Learn more about the data you can obtain from a player in [get player data]({{< ref "/content/creator/sdk7/interactivity/user-data.md#get-player-data" >}})

You should wrap the function in an `async()` function, learn more about this in [async functions]({{< ref "/content/creator/sdk7/programming-patterns/async-functions.md" >}})

{{< hint warning >}}
**📔 Note**: Even though the eth address may contain upper case characters, some browsers convert the returned string to lower case automatically. If you wish compare address values and have it work on all browsers, use the `.toLowerCase()` method to convert the value into lower case.
{{< /hint >}}

<!--
## Sign messages

A player can sign a message using their Ethereum private key. This signature is a secure way to give consent or to register an accomplishment or action that is registered with the block chain. The message can be verified with the player's public key.

The signing of a message isn't a transaction, so it doesn't imply paying any gas fees on the Ethereum network, it does however open a pop-up to ask the player for consent.

Messages that can be signed need to follow a specific format to match safety requirements. They must include the “Decentraland signed header” at the top, this prevents the possibility of any mismanagement of the player’s wallet.

Signable messages should follow this format:

```
# DCL Signed message
<key 1>: <value 1>
<key 2>: <value 2>
<key n>: <value n>
Timestamp: <time stamp>
```

For example, a signable message for a game might look like this:

```ts
# DCL Signed message
Attacker: 10
Defender: 123
Timestamp: 1512345678
```

Before a player can sign a message, you must first convert it from a string into an object using the `convertMessageToObject()` function, then it can be signed with the `signMessage()` function.

```ts
import { signMessage, convertMessageToObject } from "~system/EthereumController"

const messageToSign = `# DCL Signed message
Attacker: 10
Defender: 123
Timestamp: 1512345678`

executeTask(async () => {
  const convertedMessage = await convertMessageToObject({message: messageToSign})
  const { message, hexEncodedMessage, signature } = await signMessage({message:convertedMessage.dict})
  console.log({ message, signature })
})
```

## Check if a message is correct

To verify that the message that the player signed is in fact the one that you want to send, you can use the `toHex()` function from `eth-connect` library, to convert it and easily compare it. See further below for instructions on how to import the `eth-connect` library. -->
<!--
```ts
import { toHex } from "eth-connect"
import { signMessage, convertMessageToObject } from "~system/EthereumController"

const messageToSign = `# DCL Signed message
Attacker: 10
Defender: 123
Timestamp: 1512345678`

function signAndVerifyMessage(msg: string) {
  executeTask(async () => {
    const convertedMessage = await convertMessageToObject({message:msg})
    const { message, hexEncodedMessage, signature } = signMessage({message:convertedMessage.dict})
    console.log({ message, hexEncodedMessage, signature })

    const originalMessageHex = await toHex(msg)
    const isEqual = hexEncodedMessage === originalMessageHex
    console.log("Is the message correct?", isEqual)
  })
}

signAndVerifyMessage(messageToSign)
```

### Require a payment

The `requirePayment()` function prompts the player to accept paying a sum to an Ethereum wallet of your choice.

Players must always accept payments manually, a payment can never be implied directly from the player's actions in the scene.

```ts
import { requirePayment } from "~system/EthereumController"

requirePayment({toAddress:myWallet, amount:enterPrice, currency:'ETH' })
```

The function requires that you specify an Ethereum wallet address to receive the payment, an amount for the transaction and a specific currency to use (for now only `ETH` is supported).

If accepted by the player, the function returns the hash number of the transaction.

{{< hint danger >}}
**❗Warning**
This function informs you that a transaction was requested, but not that it was confirmed. If the gas price is too low, or it doesn't get mined for any reason, the transaction won't be completed.
{{< /hint >}}

```ts
import { requirePayment } from "~system/EthereumController"

const myWallet:string = '0x0123456789...'
const enterPrice = 0.05

function payment(){
  executeTask(async () => {
    try {
      await requirePayment({toAddress:myWallet, amount:enterPrice, currency:'ETH' })
      // openDoor()
    } catch {
      console.log("failed process payment")
    }
  })
}

const myEntity = engine.addEntity()
MeshRenderer.setBox(myEntity)
MeshCollider.setBox(myEntity)

pointerEventsSystem.onPointerDown(
	myEntity,
  function () {
     payment()
  },
  {
    button: InputAction.IA_POINTER,
    hoverText: 'Click'
  }
)
```

The example above listens for clicks on a _button_ entity. When clicked, the player is prompted to make a payment in ETH to a specific wallet for a given amount. Once the player accepts this payment, the rest of the function can be executed. If the player doesn't accept the payment, the rest of the function won't be executed.

![](/images/media/metamask_confirm.png)

{{< hint info >}}
**💡 Tip**:  We recommend defining the wallet address and the amount to pay as global constants at the start of the _.ts_ file. These are values you might need to change in the future, setting them as constants makes it easier to update the code.
{{< /hint >}} -->

## Check gas price

After importing the `eth-connect` library, you must instance a web3 provider and a request manager, which will will allow you to connect via web3 to Metamask in the player's browser.

The function below fetches the current gas price in the Ethereum main network and prints it.

```ts
import { RequestManager } from 'eth-connect'
import { createEthereumProvider } from '@dcl/sdk/ethereum-provider'

executeTask(async function () {
	// create an instance of the web3 provider to interface with Metamask
	const provider = createEthereumProvider()
	// Create the object that will handle the sending and receiving of RPC messages
	const requestManager = new RequestManager(provider)
	// Check the current gas price on the Ethereum network
	const gasPrice = await requestManager.eth_gasPrice()
	// log response
	console.log({ gasPrice })
})
```

{{< hint info >}}
**💡 Tip**: Note that the functions handled by the `requestManager` must be called using `await`, since they rely on fetching external data and can take some time to be completed.
{{< /hint >}}

## Import a contract ABI

An ABI (Application Binary Interface) describes how to interact with an Ethereum contract, determining what functions are available, what inputs they take and what they output. Each Ethereum contract has its own ABI, you should import the ABIs of all the contracts you wish to use in your project.

For example, here's an example of one function in the MANA ABI:

```ts
{
  anonymous: false,
  inputs: [
    {
      indexed: true,
      name: 'burner',
      type: 'address'
    },
    {
      indexed: false,
      name: 'value',
      type: 'uint256'
    }
  ],
  name: 'Burn',
  type: 'event'
}
```

ABI definitions can be quite lengthy, as they often include a lot of functions, so we recommend pasting the JSON contents of an ABI file into a separate `.ts` file and importing it into other scene files from there. We also recommend holding all ABI files in a separate folder of your scene, named `/contracts`.

```ts
import { abi } from '../contracts/mana'
```

Here are links to different Decentraland contracts. Obtain the ABI for each contract by clicking _Export ABI_ and choosing _JSON Format_.

- [MANA Token ABI](https://etherscan.io/address/0x0f5d2fb29fb7d3cfee444a200298f468908cc942#code)
- [Decentraland Marketplace](https://etherscan.io/address/0x19a8ed4860007a66805782ed7e0bed4e44fc6717#code)
- [LAND ABI](https://etherscan.io/address/0xf87e31492faf9a91b02ee0deaad50d51d56d5d4d#code)
- [Estate ABI](https://etherscan.io/address/0x959e104e1a4db6317fa58f8295f586e1a978c297#code)
- [AvatarNameRegistry ABI](https://etherscan.io/address/0x894b883905bfEe2CC448880F1b59f4A762E67566)
- [Catalyst ABI](https://etherscan.io/address/0xcc054fab08127c19f621ab83ade5962cd10584ec)

These are the contracts for the various wearable collections: (each collection was emitted as a separate contract)

- [ExclusiveMasksCollection ABI](https://etherscan.io/address/0xc04528c14c8ffd84c7c1fb6719b4a89853035cdd)
- [Halloween2019Collection ABI](https://etherscan.io/address/0xc1f4b0eea2bd6690930e6c66efd3e197d620b9c2)
- [Halloween2019CollectionFactory ABI](https://etherscan.io/address/0x07ccfd0fbada4ac3c22ecd38037ca5e5c0ad8cfa)
- [Xmas2019Collection ABI](https://etherscan.io/address/0xc3af02c0fd486c8e9da5788b915d6fff3f049866)
- [MCHCollection ABI](https://etherscan.io/address/0xf64dc33a192e056bb5f0e5049356a0498b502d50)
- [CommunityContestCollection ABI](https://etherscan.io/address/0x32b7495895264ac9d0b12d32afd435453458b1c6)
- [DCLLaunchCollection ABI](https://etherscan.io/address/0xd35147be6401dcb20811f2104c33de8e97ed6818)
- [DCGCollection ABI](https://etherscan.io/address/0x3163d2cfee3183f9874e2869942cc62649eeb004)

{{< hint info >}}
**💡 Tip**: To clearly see the functions exposed by a contract, open it in [abitopic.io](https://abitopic.io). Just paste the contract address there and open the _functions_ tab to see the full list of supported functions and their arguments. You can even test calling the functions with different parameters via the webpage.
{{< /hint >}}

Configuring TypeScript to be able to import from a JSON file has its difficulties. The recommended easier workaround is to change the `ABI.JSON` file's extension to `.ts` and modifying it slightly so that it its content starts with `export default`.

For example, if the ABI file's contents starts with `[{"constant":true,"inputs":[{"internalType":"bytes4" ...etc`, modify it so that it starts with `export default [{"constant":true,"inputs":[{"internalType":"bytes4" ...etc`.

### Instance a contract

After importing the `eth-connect` library and a contract's _abi_, you must instance several objects that will allow you to use the functions in the contract and connect to Metamask in the player's browser.

You must also import the web3 provider. This is because Metamask in the player's browser uses web3, so we need a way to interact with that.

```ts
import { RequestManager, ContractFactory } from 'eth-connect'
import { createEthereumProvider } from '@dcl/sdk/ethereum-provider'
import { abi } from '../contracts/mana'

executeTask(async () => {
	// create an instance of the web3 provider to interface with Metamask
	const provider = createEthereumProvider()
	// Create the object that will handle the sending and receiving of RPC messages
	const requestManager = new RequestManager(provider)
	// Create a factory object based on the abi
	const factory = new ContractFactory(requestManager, abi)
	// Use the factory object to instance a `contract` object, referencing a specific contract
	const contract = (await factory.at(
		'0x2a8fd99c19271f4f04b1b7b9c4f7cf264b626edb'
	)) as any
})
```

{{< hint info >}}
**💡 Tip**: For contracts that follow a same standard, such as ERC20 or ERC721, you can import a single generic ABI for all. You then generate a single `ContractFactory` object with that ABI and use that same factory to instance interfaces for each contract.
{{< /hint >}}

### Call the methods in a contract

Once you've created a `contract` object, you can easily call the functions that are defined in its ABI, passing it the specified input parameters.

```ts
import { getPlayer } from '@dcl/sdk/src/players'
import { createEthereumProvider } from '@dcl/sdk/ethereum-provider'
import { RequestManager, ContractFactory } from 'eth-connect'
import { abi } from '../contracts/mana'

executeTask(async () => {
	try {
		// Setup steps explained in the section above
		const provider = createEthereumProvider()
		const requestManager = new RequestManager(provider)
		const factory = new ContractFactory(requestManager, abi)
		const contract = (await factory.at(
			'0x2a8fd99c19271f4f04b1b7b9c4f7cf264b626edb'
		)) as any
		let userData = getPlayer()
		if (userData.isGuest) {
			return
		}

		// Perform a function from the contract
		const res = await contract.setBalance(
			'0xaFA48Fad27C7cAB28dC6E970E4BFda7F7c8D60Fb',
			100,
			{
				from: userData.userId,
			}
		)
		// Log response
		console.log(res)
	} catch (error: any) {
		console.log(error.toString())
	}
})
```

The example above uses the abi for the Ropsten MANA contract and transfers 100 _fake MANA_ to your account in the Ropsten test network.

### Other functions

The eth-connect library includes a number of other helpers you can use. For example to:

- Get an estimated gas price
- Get the balance of a given address
- Get a transaction receipt
- Get the number of transactions sent from an address
- Convert between various formats including hexadecimal, binary, utf8, etc.

## Using the Ethereum test network

While testing your scene, to avoid transferring real MANA or other currencies, you can use the _Ethereum Sepolia test network_ and transfer fake testnet MANA instead.

To use the test network you must set your Metamask Chrome extension to use the _Sepolia test network_ instead of _Main network_.

You must acquire Sepolia Ether, which you can obtain for free from various external faucets like [this one](https://www.alchemy.com/faucets/ethereum-sepolia/).

<!-- If your transactions also involve MANA, you can also obtain free Sepolia MANA from our [Sepolia MANA faucet](https://faucet-goerli.decentraland.io/). -->

{{< hint info >}}
**💡 Tip**: To run the transaction of transferring Sepolia MANA to your wallet, you will need to pay a gas fee in Sepolia Ether.
{{< /hint >}}

To preview your scene using the test network, open Decentraland with the following command:

`npm run start -- --explorer-alpha --realm https://peer.decentraland.zone --dclenv zone --position 0,0`

{{< hint info >}}
**💡 Tip**: Change the position parameter to the coordinates of your scene, to load directly into your scene..
{{< /hint >}}

When running a preview on the web client, of a scene that uses one of the ethereum libraries, you must open the preview in a separate browser window, have Metamask open in your browser, and manually include the string `&ENABLE_WEB3`.

Any transactions that you accept while viewing the scene in this mode will only occur in the test network and not affect the MANA balance in your real wallet.

If you need to test transactions in the Polygon Testnet and need to have MANA on that testnet, you'll need to swap MANA to that network after acquiring it in Sepolia. To bridge Sepolia MANA to the Polygon Testnet, visit your [Decentraland account page in Sepolia](https://account.decentraland.zone/) and click on ‘swap’ on the Ethereum MANA side.

## Send custom RPC messages

Use the function `sendAsync()` to send messages over [RPC protocol](https://en.wikipedia.org/wiki/Remote_procedure_call).

```ts
import { sendAsync } from '~system/EthereumController'

// send a message
await sendAsync({
	id: 1,
	method: 'myMethod',
	jsonParams: '{ myParam: myValue }',
})
```

## Decentraland smart contracts

In the following link you can find a list of Etherum smart contracts relevant to the Decentraland ecosystem. The list includes the contracts in mainnet as well as in other Ethereum test networks.

[contracts.decentraland.org](https://contracts.decentraland.org/links)

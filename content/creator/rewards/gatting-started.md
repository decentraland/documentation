---
title: 'Rewards - Getting Starting'
url: /creator/rewards/getting-started
weight: 2
---

## Pre-Requirements

Before starting to use the Rewards Service, make sure you have a collection [approved and ready to mint]({{< ref "/creator/wearables-and-emotes/publishing/publishing-collections.md" >}}).

## Create your first campaign

A campaign refers to an incentive initiative designed to boost user engagement through reward offerings. In this section, you'll discover the campaign configuration details, along with the prerequisites for initiating the distribution of rewards.

1. Access the [Rewards Service](https://rewards.decentraland.org/)
2. Connect your wallet
3. Click on the **Campaigns** tab
4. Click on the **Create Campaign** button. You will be redirected to the campaign creation page.

<img src="/images/rewards/create-campaign-page.png" alt="Creating new campaign" style="width:100%; max-width: 600px; margin: 0 auto;display: block;" width="1480" hegiht="1532" />

5. Complete the following fields

   - Campaign name: identify your campaign. The name is shown to users on they rewards page.
   - Campaign network: the network where your wearables will be minted, it can't be changed once the campaign is created.
   - Max gas price: the maximum gas price you are willing to pay for each transaction. If the gas price of a transaction exceeds the maximum gas price, the transaction will be deferred until the gas price is lower. The UI displays an estimation of how much it will cost to mint each item.

6. Click on the **Create Campaign** button. You will be redirected to the campaign page.

<img src="/images/rewards/new-campaign.png" alt="New campaign" style="width:100%; margin: 0 auto;display: block;" width="2454" hegiht="1362" />

Once your campaign is created, you still need to do the following to start delivering rewards:

- Add a supply of MATIC tokens to pay for transaction fees
- Add items to the campaign stock
- Create a dispenser to deliver the rewards
- Activate your campaign

### Add MATIC to pay for transaction fees

In order to mint items, you need to pay for the transaction fees. For this, you need to add a supply of MATIC tokens to the campaign address. You can find this address below its name.

To send MATIC from your wallet, make sure you are connected to the same network as the campaign, then copy the campaign address and send MATIC to it. If you don't have any MATIC on your wallet, you can follow [this guide]({{< ref "/content/player/blockchain-integration/transactions-in-polygon.md" >}}#where-can-i-get-matic-to-pay-for-transaction-fees) to get some.

{{< hint info >}}
**💡 Tip**: For campaigns running on the test **AMOY** network, you can get some MATIC from [this faucet](https://faucet.polygon.technology/).
{{< /hint >}}

To send MATIC from an exchange you just need to withdraw MATIC token to the Polygon Network (usually Amoy Network is not available on exchanges).

### Add items to the campaign stock

When you create a new campaign, it doesn't contain any items. You'll need to add some items to it before you can start delivering rewards.

<img src="/images/rewards/without-supply.png" alt="without supply" style="width:100%; margin: 0 auto;display: block;" width="2296" hegiht="1012" />

1. Grant minting permissions to the campaign. Follow [this guide]({{< ref "/content/creator/wearables-and-emotes/publishing/publishing-collections.md" >}}#adding-minters-to-the-collection) using the campaign address (which you can find below the campaign name) as the minter's address. Then wait for the transaction to be confirmed.
2. Add items to the campaign stock.

    a) Click on the **Add supply** button to see all collections the campaign has minting permissions on.

        <img src="/images/rewards/collection-available.png" alt="Collection available" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1808" hegiht="1494" />

    b) Select the collection item you want to add to the stock, and click on the **Add supply** button.

        <img src="/images/rewards/add-supply.png" alt="add supply" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1816" hegiht="772" />

    c) Select the amount of items you want to add to the campaign stock and click on the **Add supply** button.

<img src="/images/rewards/with-supply.png" alt="supply added" style="width:100%; margin: 0 auto;display: block;" width="2290" hegiht="360" />

{{< hint info >}}
Priority and Group fields are advance features that will be covered in a dedicated section.
{{< /hint >}}

### Create a dispenser to deliver the rewards

Dispensers are the way to send or claim rewards from the stock, each one has a key that you need to authenticate against the HTTP API. The key is not visible on the UI, but you can copy it by clicking on the **Copy** button.

Upon creating a new campaign, a default dispenser with a "master key" is provided for testing purposes only. To establish a new dispenser, simply click the **Add dispenser** button.

<img src="/images/rewards/create-dispenser.png" alt="create dispenser" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1714" hegiht="584" />

Select the item group where you want take items from, and click on the **Save** button.

{{< hint info >}}
Dispenser have some configuration options that will be covered in a dedicated section.
{{< /hint >}}

### Activate your campaign

By default your campaign is inactive. This prevents the rewards service from assigning any new rewards. To activate your campaign, click on the **Activate campaign** button.

{{< hint warning >}}
**📔 Note**: If an active campaign is set back to inactive, any rewards that were pending will still be sent. Only new claims are prevented.
{{< /hint >}}

**Now you are ready to start minting wearables/emotes using the [API]({{< ref "/content/creator/rewards/api.md">}})**

### Manage funds
Once the campaign is done, the owner can choose to either reclaim the funds allocated to it or reassign them to a different campaign. To claim funds, click on the **Manage funds** button in the campaign detail page.

{{< hint warning >}}
**📔 Note**: If all funds are removed from a campaign, any pending or new transactions related to that campaign will be blocked until more funds are assigned.
{{< /hint >}}

---
title: 'Getting Starting'
url: /creator/rewards/getting-started
weight: 2
---

## Pre-Requirement

Before starting to use the Rewards Service, make sure you have a collection [approved and ready to mint]({{< ref "/creator/wearables-and-emotes/publishing/publishing-collections.md" >}}).

## Create your first campaign

Enter to the [Rewards Service](https://rewards.decentraland.org/), connect your wallet, click on the **Campaigns** tab, and finally click on the **Create Campaign** button. You will be redirected to the campaign creation page.

<img src="/images/rewards/create-campaign-page.png" alt="Creating new campaign" style="width:100%; max-width: 600px; margin: 0 auto;display: block;" width="1480" hegiht="1532" />

- Campaign name will help you to identify your campaign on the list of campaigns and will be shown to the users on they rewards page.
- Campaign network is the network where your wearables will be minted, it can't be changed once the campaign is created.
- Max gas price is the maximum gas price you are willing to pay for each transaction. If the gas price exceeds the maximum gas price, the transaction will be deferred until the gas price is lower. You will also see an estimation of how much it will cost to mint each item.

Once you have filled the form, click on the **Create Campaign** button. You will be redirected to the campaign page.

<img src="/images/rewards/new-campaign.png" alt="New campaign" style="width:100%; margin: 0 auto;display: block;" width="2454" hegiht="1362" />

In order to start delivering rewards, you need:

- Add MATIC to pay for transaction fees
- Add items to the campaign stock
- Create a dispenser to deliver the rewards
- Activate your campaign

### Add MATIC to pay for transaction fees

In order to mint items, you need to pay for the transaction fees and to do it, you need to add MATIC to the campaign address which you can find below its name.

To send MATIC from your wallet, make sure you are connected to the same network as the campaign, then copy the campaign address and send MATIC to it. If you don't have any MATIC on your wallet, you can follow [this guide]({{< ref "/content/player/blockchain-integration/transactions-in-polygon.md" >}}#where-can-i-get-matic-to-pay-for-transaction-fees) to get some. In case your campaign is running on **MUMBAI** network you can get some MATIC from [this faucet](https://mumbaifaucet.com/).

To send MATIC from an exchange you just need to withdraw MATIC token to the Polygon Network (usually Mumbai Network is not available on exchanges)

## Add items to the campaign stock

When you create a new campaign it doesn't have any item on its stock, so you need to add some items to it before you can start delivering rewards.

<img src="/images/rewards/without-supply.png" alt="without supply" style="width:100%; margin: 0 auto;display: block;" width="2296" hegiht="1012" />

Any campaign can't deliver rewards if you don't grant minting permissions first, to do it, follow [this guide]({{< ref "/content/creator/wearables-and-emotes/publishing/publishing-collections.md" >}}#adding-minters-to-the-collection) using the campaign address (which you can find below its name) as the minters address.

Once you have granted minting permissions, and the transaction is confirmed, you can add items to the campaign stock. To do it, click on the **Add supply** button to see all collections the campaign has minting permissions on.

<img src="/images/rewards/collection-available.png" alt="Collection available" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1808" hegiht="1494" />

Select the collection item you want to add stock, and click on the **Add supply** button.

<img src="/images/rewards/add-supply.png" alt="add supply" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1816" hegiht="772" />

Select the amount of items you want to add to the campaign stock and click on the **Add supply** button.

{{< hint info >}}
Priority and Group fields are advance features that will be covered in a dedicated section.
{{< /hint >}}

<img src="/images/rewards/with-supply.png" alt="supply added" style="width:100%; margin: 0 auto;display: block;" width="2290" hegiht="360" />

## Create a dispenser to deliver the rewards

Dispensers are the way to send or claim rewards from the stock, each one have a key that you need to authenticate against the HTTP API. UI doesn't show any key, but you can get it by clicking on the **Copy** button.

When you create a new campaign it comes with a default dispenser with a "master key" that is intended to be used for testing purposes only, so you need to create a new dispenser, to do it click on the **Add dispenser** button.

<img src="/images/rewards/create-dispenser.png" alt="create dispenser" style="width:100%; margin: 0 auto;display: block; max-with: 600px" width="1714" hegiht="584" />

Select the item group where you want take items from, and click on the **Save** button.

{{< hint info >}}
Dispenser have some configuration options that will be covered in a dedicated section.
{{< /hint >}}

## Activate your campaign

By default your campaign is inactive, this prevents that the service assign rewards to users but is still sending rewards if there are any pending. To activate your campaign, click on the **Activate campaign** button.

**Now you are ready to start minting wearable/emotes using the [API]({{< ref "/content/creator/rewards/api.md">}})**

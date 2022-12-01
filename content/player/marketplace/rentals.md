---
date: 2022-11-29
title: Rentals
description: LAND Rentals
categories:
  - market
type: Document
url: /player/market/rentals
weight: 25
---
# Glossary

**Land Owner:** Account (address) that owns LAND, it could be a Parcel, an Estate, or both.

**Tenant:** Account (address) that rents LAND from a LAND Owner. This is also the only Account that can change the Address that has Operator Permissions.

**Operator Permission:** The address with this permission is the only one that can deploy scenes in that LAND.

**Transactions:** Ethereum Blockchain transactions that cost gas.

# Intro

The new Renting System allows LAND Owners and Tenants to **Rent LAND in a secure and trustless way** by using a combination of signatures that are stored in a server handled by the Decentraland Foundation (off-chain) and Ethereum transactions (on-chain). 

For instance, a DJ could find a cool plot of LAND, rent it and deploy a nightclub to play every Saturday. A University could rent an Estate and build a campus for its students. 

Below you will find all the steps you need to follow to Rent a LAND, and the transactions involved for both parties. 

# For LAND Owners

## List LAND for Rent

As a LAND Owner, you can list your LAND (Parcels or Estates) for Rent in the [Marketplace](https://market.decentraland.org/) > My Assets > LAND. 

In order to do this on-chain, the LAND Owner has to approve the Rent Smart Contract to use the LAND on their behalf. Then every listing would need a signature from the Owner as well.

![](/images/Rentals/Image1.png)

You can set a rental price per day in MANA and the amount of days you want to allow people to rent it. The price per day times the number of days in the period is what the tenant will pay **upfront, and in total** for that rent.

![](/images/Rentals/Image2.png)

After defining the Price per Day, you need to select the number of days that Users can rent your LAND. For example, if you select 7 and 30 days only, the Tenant can only choose between those 2 options. In case 30 days option is selected by the Tenant, that would be the duration of the rent from the day it is confirmed.

![](/images/Rentals/Image3.png)

You can also set an expiration date for the listing. This means that, if the LAND wasn’t rented until the selected date, the listing will be removed from the Marketplace. Also, the smart contract will reject the expired signature so that no one can rent it for the listing price and duration previously selected. This is a security measure to prevent it to be rented for an undesired price or duration. 

![](/images/Rentals/Image4.png)

After the price, rent period and listing expiration date are set, your LAND will appear as available for rent in the Marketplace.

<aside>
💡 When LAND is rented by a Tenant, it can not be sold until it’s claimed back. Bids from potential buyers can not be received either.

</aside>

<aside>
💡 Voting Power is kept by the LAND Owner, even if it is rented.

</aside>

## Edit or Cancel a Listing

After the LAND is Listed for Rent in the Marketplace, and before anybody rents it, you can edit the conditions of the Listing by clicking on the pencil icon in the LAND detail. You can also remove the Listing from the Marketplace and the blockchain.

![](/images/Rentals/Image5.png)

<aside>
💡 Edit and cancel actions may require a transaction, which costs gas. See Transactions section below for more details.

</aside>

## After the Rent is over

After the Rent is over, you can either **Claim your LAND Back, or List it for Rent Again**.

**Operator Permissions are not transferred automatically back to the LAND Owner**. In order to get them back, the LAND Owner has to Claim the LAND back by sending that transaction and paying for the gas fee. Confirming the transaction will take out Operator Permissions from the Tenant and give them back to the LAND Owner.

![](/images/Rentals/Image6.png)

The other possibility is to List the LAND for Rent Again, instead of claiming it back. This will not require paying for another transaction, but **Operator Permissions will be kept by the previous Tenant until a new Tenant confirms a new Rent.** 

The LAND Owner can edit the price, rent period, and listing expiration date for the new listing. 

![](/images/Rentals/Image7.png)

Both actions can be done from the LAND detail page in the Marketpalce.

![](/images/Rentals/Image8.png)

## Renting Status

You can check the Status of any rented LAND in My Store > My Assets. The possible status are:

- Listed for Rent - The listing was confirmed and it’s available for users to rent in the Marketplace
- Rented Period Over - At this stage, the LAND is available to Claim Back or List Again for Rent by the LAND Owner
- Rented until *“date”* - The LAND is already rented and the Tenant has Operator Permissions until it’s claimed back or rented by another user

![](/images/Rentals/Image9.png)

# For Tenants

## Rent LAND

All users can find LAND listed for rent in the Marketplace under the LAND section.

![](/images/Rentals/Image10.png)

There are LANDs that are available for Sale or Rent. In case both options are available, you can see the conditions available for each one by clicking on the toggle Sale/Rent. 

![](/images/Rentals/Image11.png)

Once you find the LAND you want to rent, you need to select the Rent Period, this is the days you will have the LAND. After selecting the Rent Period, you will see the total price to be paid for the Rent. 

![](/images/Rentals/Image12.png)

You’ll need to approve the Rent Smart Contract to take the MANA from your account before you proceed.

Before you confirm the Rent, you can decide who will manage the LAND (Operator Permission). It can be yourself or any other address you choose. 

![](/images/Rentals/Image13.png)

Operator Permission can be changed later by the Tenant (the address who rented the LAND in the first place) from the [Builder](https://builder.decentraland.org/). 

![](/images/Rentals/Image14.png)

After selecting all the details and approving the Rent Smart Contract to handle your MANA, you can confirm the Rent by sending a transaction. 

And you are all set! you can start working on your LAND, and deploy a scene using the Builder or the SDK. 

![](/images/Rentals/Image15.png)

Note: after the Rent ends, the Tenant will still have Operator Permissions until the LAND Owner Claims it back, or somebody else rents it. **Make sure you save your content before the end of the rent, otherwise it could be lost.**

<aside>
💡 Renting LAND does not transfer Voting Power to the Tenant. Voting Power is kept by the LAND Owner

</aside>

# Transactions

For the sake of **security and decentralization**, the Renting system relies on the Ethereum blockchain as a source of truth.

But, not every action involved requires an entry in the blockchain. If that was the case, it would be too expensive for both parties. 

Transactions in the blockchain are minimum in order to provide a **robust and trustless system for LAND renting while keeping it affordable.** These are all the transactions to consider:

## For Land Owners

### List for Rent

Before Listing the first Parcel or Estate for rent, LAND Owners need to allow the Rents Smart Contract to operate LAND on their behalf. This has to be done only once for Parcels and only once for Estates. 

![](/images/Rentals/Image16.png)

### Claim LAND Back or List for Rent Again

After the renting period ends, **Operator Permissions are not transferred automatically back to the LAND Owner**. In order to get them back, the LAND Owner has to Claim the LAND back by sending that transaction and paying for the gas fee.

![](/images/Rentals/Image17.png)

Another possibility is to List the LAND for Rent Again, instead of claiming it back. This will not require paying for another transaction, but Operator Permissions will be kept by the previous Tenant until a new Tenant confirms a new Rent. 

### Edit Listing

If either the Price, Rent Period, or Expiration Date is changed, a transaction has to be sent by the LAND Owner in order to protect themselves from somebody hitting the Smart Contract directly (not from the Marketplace UI) and getting it from a lower price than desired or for an undesired duration. 

![](/images/Rentals/Image18.png)

## For Tenants

### Allow Rent Contract to operate your MANA

Whether it’s a Parcel or an Estate, every user that wants to Rent LAND has to send one transaction to allow the Rent Smart Contract to operate MANA on their behalf. This is needed because the Smart Contract has to pull the MANA and transfer it to the LAND Owner when the rent is activated. This is done only once for all LAND to be rented from that moment onwards.

### Rent LAND

After approving the Rent Smart Contract to operate your MANA, you are ready to confirm your first Rent. Once you find the LAND you want, choose the rent period, and confirm the Rent transaction, Operator Permissions are transferred to the selected address. 

If you want to rent another Parcel or Estate, you only need to send one transaction to confirm it, there is no need to approve the Smart Contract to operate your MANA again. 

![](/images/Rentals/Image19.png)

### Change Operator

At the moment of renting the LAND, the user can choose which address will have Operator Permissions for that LAND. If that address wants to be changed, a transaction has to be sent.

![](/images/Rentals/Image20.png)

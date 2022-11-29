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

As a LAND Owner, you can list your LAND (Parcels or Estates) for Rent in the [Marketplace](https://market.decentraland.org/) > My Assets > [LAND](https://market.decentraland.org/account?assetType=nft&section=land&vendor=decentraland&page=1&sortBy=newest&onlyOnSale=false&viewAsGuest=false). 

In order to do this on-chain, the LAND Owner has to approve the Rent Smart Contract to use the LAND on their behalf. Then every listing would need a signature from the Owner as well.

![](static/images/Rentals/Image1.png)

You can set a rental price per day in MANA and the amount of days you want to allow people to rent it. The price per day times the number of days in the period is what the tenant will pay **upfront, and in total** for that rent.

![](static/images/Rentals/Image2.png)

After defining the Price per Day, you need to select the number of days that Users can rent your LAND. For example, if you select 7 and 30 days only, the Tenant can only choose between those 2 options. In case 30 days option is selected by the Tenant, that would be the duration of the rent from the day it is confirmed.

![](static/images/Rentals/Image3.png)

You can also set an expiration date for the listing. This means that, if the LAND wasn’t rented until the selected date, the listing will be removed from the Marketplace. Also, the smart contract will reject the expired signature so that no one can rent it for the listing price and duration previously selected. This is a security measure to prevent it to be rented for an undesired price or duration. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/967379db-3a93-4d36-8fde-2cc298220747/Untitled.png)

After the price, rent period and listing expiration date are set, your LAND will appear as available for rent in the Marketplace.

<aside>
💡 When LAND is rented by a Tenant, it can not be sold until it’s claimed back. Bids from potential buyers can not be received either.

</aside>

<aside>
💡 Voting Power is kept by the LAND Owner, even if it is rented.

</aside>

## Edit or Cancel a Listing

After the LAND is Listed for Rent in the Marketplace, and before anybody rents it, you can edit the conditions of the Listing by clicking on the pencil icon in the LAND detail. You can also remove the Listing from the Marketplace and the blockchain.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ef30382-6177-4454-92d1-decb1bb61576/Untitled.png)

<aside>
💡 Edit and cancel actions may require a transaction, which costs gas. See Transactions section below for more details.

</aside>

## After the Rent is over

After the Rent is over, you can either **Claim your LAND Back, or List it for Rent Again**.

**Operator Permissions are not transferred automatically back to the LAND Owner**. In order to get them back, the LAND Owner has to Claim the LAND back by sending that transaction and paying for the gas fee. Confirming the transaction will take out Operator Permissions from the Tenant and give them back to the LAND Owner.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de1fb895-04b9-43f8-9ab8-5e854d9ae9c0/Untitled.png)

The other possibility is to List the LAND for Rent Again, instead of claiming it back. This will not require paying for another transaction, but **Operator Permissions will be kept by the previous Tenant until a new Tenant confirms a new Rent.** 

The LAND Owner can edit the price, rent period, and listing expiration date for the new listing. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c600c48e-2ee2-4666-9283-b1a112562bd3/Untitled.png)

Both actions can be done from the LAND detail page in the Marketpalce.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d71cd93d-3462-4693-be4a-dc548d2cc68a/Untitled.png)

## Renting Status

You can check the Status of any rented LAND in My Store > My Assets. The possible status are:

- Listed for Rent - The listing was confirmed and it’s available for users to rent in the Marketplace
- Rented Period Over - At this stage, the LAND is available to Claim Back or List Again for Rent by the LAND Owner
- Rented until *“date”* - The LAND is already rented and the Tenant has Operator Permissions until it’s claimed back or rented by another user

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/00ce683c-7a9d-4e40-b2d8-4e05370a016f/Untitled.png)

# For Tenants

## Rent LAND

All users can find LAND listed for rent in the Marketplace under the LAND section.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a5b0d04-2aac-4b52-9ee6-a60b89ccf8f4/Untitled.png)

There are LANDs that are available for Sale or Rent. In case both options are available, you can see the conditions available for each one by clicking on the toggle Sale/Rent. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4f38bd8c-36fa-4a38-acf2-9276ed479ea4/Untitled.png)

Once you find the LAND you want to rent, you need to select the Rent Period, this is the days you will have the LAND. After selecting the Rent Period, you will see the total price to be paid for the Rent. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/737e3a67-8ea5-42f8-b30e-e02e409b4a5a/Untitled.png)

You’ll need to approve the Rent Smart Contract to take the MANA from your account before you proceed.

Before you confirm the Rent, you can decide who will manage the LAND (Operator Permission). It can be yourself or any other address you choose. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/75131e13-9637-4732-bebc-bff5703dba6b/Untitled.png)

Operator Permission can be changed later by the Tenant (the address who rented the LAND in the first place) from the [Builder](https://builder.decentraland.org/). 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/08ef8997-5fdd-4820-9347-2de953caa793/Untitled.png)

After selecting all the details and approving the Rent Smart Contract to handle your MANA, you can confirm the Rent by sending a transaction. 

And you are all set! you can start working on your LAND, and deploy a scene using the Builder or the SDK. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e74e5dcd-1496-41f1-92f8-4dedffa016cd/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b1fdd32-53d6-4bef-b0cb-3c40a9ba1428/Untitled.png)

### Claim LAND Back or List for Rent Again

After the renting period ends, **Operator Permissions are not transferred automatically back to the LAND Owner**. In order to get them back, the LAND Owner has to Claim the LAND back by sending that transaction and paying for the gas fee.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3df2a497-5f8f-4e2f-91f7-f4b21d522297/Untitled.png)

Another possibility is to List the LAND for Rent Again, instead of claiming it back. This will not require paying for another transaction, but Operator Permissions will be kept by the previous Tenant until a new Tenant confirms a new Rent. 

### Edit Listing

If either the Price, Rent Period, or Expiration Date is changed, a transaction has to be sent by the LAND Owner in order to protect themselves from somebody hitting the Smart Contract directly (not from the Marketplace UI) and getting it from a lower price than desired or for an undesired duration. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f03e1655-75c9-48b2-9130-59e6410d876f/Untitled.png)

## For Tenants

### Allow Rent Contract to operate your MANA

Whether it’s a Parcel or an Estate, every user that wants to Rent LAND has to send one transaction to allow the Rent Smart Contract to operate MANA on their behalf. This is needed because the Smart Contract has to pull the MANA and transfer it to the LAND Owner when the rent is activated. This is done only once for all LAND to be rented from that moment onwards.

### Rent LAND

After approving the Rent Smart Contract to operate your MANA, you are ready to confirm your first Rent. Once you find the LAND you want, choose the rent period, and confirm the Rent transaction, Operator Permissions are transferred to the selected address. 

If you want to rent another Parcel or Estate, you only need to send one transaction to confirm it, there is no need to approve the Smart Contract to operate your MANA again. 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/714412a9-eeae-4bb5-9202-62c81ab8484b/Untitled.png)

### Change Operator

At the moment of renting the LAND, the user can choose which address will have Operator Permissions for that LAND. If that address wants to be changed, a transaction has to be sent.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/981dfe34-d990-434e-9307-d7470710fcdf/Untitled.png)
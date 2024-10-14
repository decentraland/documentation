---
title: 'Overview'
url: /creator/rewards/overview
weight: 1
---

The [Rewards dApp](https://decentraland.org/rewards/) is a powerful tool that enables creators to reward users with Decentraland Wearables or Emotes via HTTP requests. It can be used to motivate users, promote scenes, or increase retention. Rewards can be granted directly from a scene, a server, or in a [quests]({{< ref "/content/creator/quests/overview.md" >}}).

The Rewards system manages most of the complexities involved in minting items on the blockchain, including:

- Batching multiple minted items into a single transaction to reduce waiting time and fees
- Handling the payment of transaction fees
- Managing retries in case of blockchain failures or reorders
- Limiting the number of items minted per user address
- Minimizing automation exploits through a captcha system
- Verifying user presence in the scene via Catalyst nodes
- Monitoring transaction status
- Informing users about the item they will receive before the transaction is confirmed
- Emits Notifications when rewards are granted and received 

- <img src="/images/rewards/overview.png" alt="Rewards Service Overview" width="1716" hegiht="687" />

## Limitations

Although the service offers some automation protections to prevent one person from minting wearables massively, it is impossible to be 100% secure from exploits. **It is NOT recommended to use Rewards to mint Wearables/Emotes with a rarity level that is more scarce than [EPIC]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}#rarity) (100 or less copies)**.

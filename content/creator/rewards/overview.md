---
title: 'Rewards Overview'
url: /creator/rewards/overview
weight: 1
---

The **Rewards service** is a powerful tool that allows creators to reward users with Decetraland's Wearables or Emotes by HTTP Request, it can be use to motivate users, promote your scene, or increase retention. Rewards can be used directly on your scene, server, or in [quests]({{< ref "/content/creator/quests/overview.md" >}}).

The rewards service handles most of the logic involved in minting items on the blockchain, including:

- Batching multiple minted items into a single transaction to minimize waiting time and fees
- Handling the payment of the transaction fees
- Handling retries in case of blockchain failure or reorders
- Limiting the number of items minted per user address
- Minimize minting automation exploits by using a captcha system
- Checking user presence in the scene by Catalyst
- Monitoring transaction status
- Letting users know which item they are going to receive before the transaction is confirmed

<img src="/images/rewards/overview.png" alt="Rewards Service Overview" width="1716" hegiht="687" />

## Limitations

Although the service offers some automation protections to prevent one person from minting wearables massively, it is impossible to be 100% secure from exploits. **It is NOT recommended to use Rewards to mint Wearables/Emotes with a rarity level that is more scarce than [EPIC]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}#rarity) (100 or less copies)**.

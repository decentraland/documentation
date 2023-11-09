---
title: 'Overview'
url: /creator/rewards/overview
weight: 1
---


**Rewards** is a powerful service  that allows creators to reward users with Decetraland's Wearables or Emotes by HTTP Request, it can be use to motivate users, promote your scene, or increase retention. Rewards can be use directly on your scene, server, or quests.

It handle most of the logic involve on minting items on the blockchain, including:

- Batching multiple minted item in a single transaction to minimize waiting time and fees
- Handling the payment of the transaction fees
- Handling retries in case of blockchain failure or reorders
- Limiting the number of items minted per user address
- Minimize minting automation by using a captcha system
- Checking user presence in the scene by Catalyst
- Monitoring transaction status
- Letting users know which items is going to receive before transaction is confirmed

<img src="/images/rewards/overview.png" alt="Rewards Service Overview" width="1716" hegiht="687" />

## Limitations

Although the service offers some automation protections to prevent minting wearable massively to one person, it is impossible to be 100% accurate. **We do not recommended to use Rewards to mint Wearable/Emotes with a rarity lower than [EPIC]({{< ref "/content/creator/wearables-and-emotes/manage-collections/creating-a-collection.md" >}}#rarity)**.

---
title: 'Users and Roles'
url: /creator/rewards/users
weight: 3
---

To perform any actions on a campaign within the Rewards service, you must be logged in with a wallet that has the necessary permissions.

When you create a campaign, you are automatically assigned as its owner and granted all permissions. As the owner, you can add other users to the campaign and assign them roles with specific permissions. However, each campaign can have only one owner—the creator—who is the only user with the authority to manage the funds.

To add a user to the campaign.

1. Click on the **User Roles** tab to view the list of users who have access to the campaign.
2. At the end of this list, you'll find a form to add a new user. Note: This form will only be visible if you have the necessary permissions to add users.
4. Complete the form by entering the user's wallet address (or ENS name) and selecting their role.
5. Click the **Add User** button to finalize the addition.

<img src="/images/rewards/users.png" alt="Users" width="2284" hegiht="689" />

## Permissions for roles

These are the actions allowed for each role:

| Permission                               | viewer | developer | collaborator | owner |
| ---------------------------------------- | :----: | :-------: | :----------: | :---: |
| View campaign name, network, and max gas |   ✅   |    ✅     |      ✅      |  ✅   |
| Edit campaign name, and max gas          |   ❌   |    ❌     |      ✅      |  ✅   |
| Activate and deactivate campaign         |   ❌   |    ❌     |      ✅      |  ✅   |
| View supply                              |   ✅   |    ✅     |      ✅      |  ✅   |
| Add/remove Supply                        |   ❌   |    ✅     |      ✅      |  ✅   |
| View dispensers                          |   ✅   |    ✅     |      ✅      |  ✅   |
| View dispenser key                       |   ❌   |    ✅     |      ✅      |  ✅   |
| Add/remove dispenser                     |   ❌   |    ✅     |      ✅      |  ✅   |
| View campaign transactions               |   ✅   |    ✅     |      ✅      |  ✅   |
| View users                               |   ✅   |    ✅     |      ✅      |  ✅   |
| Add/Remove users                         |   ❌   |    ❌     |      ✅      |  ✅   |
| Remove owner users                       |   ❌   |    ❌     |      ❌      |  ✅   |
| Manage funds                             |   ❌   |    ❌     |      ❌      |  ✅   |

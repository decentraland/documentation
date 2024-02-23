---
title: 'Rewards Users and Roles'
url: /creator/rewards/users
weight: 3
---

To perform any action on a campaign in the Rewards service, you need to be logged in with a wallet that has the required permissions.

When you create a campaign, you are automatically assigned as its owner and have all permissions. You can add other users to the campaign and grant them permissions according to their role.

To add a user to the campaign.

1. Click on the **Users** tab to see the list of users that have access to that campaign.
2. At the end of this list you should see the form to add a new user. Note: you'll only see this if you have permissions to add users.
3. Complete the form address wallet (or ens name), select the role of the new user
4. Click on the **Add user** button.

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

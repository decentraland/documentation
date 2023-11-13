---
title: 'Users and Roles'
url: /creator/rewards/users
weight: 3
---

To perform any action on a campaign, you need to be logged in with a wallet that has the required permissions.

When you create a campaign, you are the owner of it and you have all the permissions, but you can add other users to the campaign and grant them permissions according to their role.

To add a user to the campaign, click on the **Users** tab to see the list of users that have access to that campaign, if you have permissions to add users at the end of the user list you will see the form to add a new user. Complete the form address wallet (or ens name), select the role of the new user and then click on the **Add user** button.

<img src="/images/rewards/users.png" alt="Users" width="2284" hegiht="689" />

## Permissions for roles

| Permission | viewer | developer | collaborator | owner |
|------------|:------:|:---------:|:------------:|:-----:|
| View campaign name, network, and max gas | ✅ | ✅ | ✅ | ✅ |
| Edit campaign name, and max gas          | ❌ | ❌ | ✅ | ✅ |
| Activate and deactivate campaign         | ❌ | ❌ | ✅ | ✅ |
| View supply                              | ✅ | ✅ | ✅ | ✅ |
| Add/remove Supply                        | ❌ | ✅ | ✅ | ✅ |
| View dispensers                          | ✅ | ✅ | ✅ | ✅ |
| View dispenser key                       | ❌ | ✅ | ✅ | ✅ |
| Add/remove dispenser                     | ❌ | ✅ | ✅ | ✅ |
| View campaign transactions               | ✅ | ✅ | ✅ | ✅ |
| View users                               | ✅ | ✅ | ✅ | ✅ |
| Add/Remove users                         | ❌ | ❌ | ✅ | ✅ |
| Remove owner users                       | ❌ | ❌ | ❌ | ✅ |

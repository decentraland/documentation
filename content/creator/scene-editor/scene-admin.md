---
date: 2025-02-14
title: Scene Admin
description: Scene administrators have special control over what happens in the scene in real time.
categories:
  - scene-editor
type: Document
url: /creator/editor/scene-admin
weight: 8
---

Grant certain players the special role of **admin** on your scene. When a scene admin visits your scene, they see a special UI on the top-right corner that only they are able to see. Through this UI they can play videos or live streams, send announcements, or activate any smart item in the scene. These actions are seen by all other players in the scene that are connected to the same island as the admin.

{{< youtube JDH0Sf6O_30 >}}


During a live event, an admin can spontaneously control what happens in the scene from inside Decentraland, without needing to pre-schedule actions or relying on a 3rd party service. Start playing the music when enough of a crowd gathered, drop confetti or make a spaceship appear when the time feels right.

  <img src="/images/editor/admin/admin-console.png" alt="Scene name" width="500"/>


## Setting up admins

To assign admins, you need to add the **Scene Admin** smart item to your scene.

  <img src="/images/editor/admin/admin-smart-item.png" alt="Scene name" width="500"/>


{{< hint warning >}}
**📔 Note**: Update your scene to use the latest dependencies. The Scene Admin Smart item won't work if the scene is outdated. 

 <img src="/images/editor/admin/update-dependencies.png" alt="Scene name" width="500"/>

{{< /hint >}}

While you're developing the scene and trying it locally, you are always an admin. Once the scene is published, anyone with publish permissions to the scene is also automatically an admin. This includes the scene owner, operators or renters.

You can assign additional people to the admin list once your scene is published by visiting your scene as an admin and opening the **Moderation Tools** tab.

  <img src="/images/editor/admin/moderation-tools.png" alt="Scene name" width="500"/>

Write the wallet address of the person you want to add to the admin list and click **Add**.

You can see who is an admin in the scene by clicking the **Admin List** button. From this screen you can also **Remove** people from the admin list.

  <img src="/images/editor/admin/admin-list.png" alt="Scene name" width="500"/>

{{< hint warning >}}
**📔 Note**: It's only possible to remove the admin role from players that were added manually to the list via the **Moderation Tools** tab. Players who are owners, operators, or renters of the scene are displayed on this list but can't be removed from their admin roles.
{{< /hint >}}

Whenever an admin player is in the scene, they will see a special UI on the top-right corner. Non-admin players don't see this UI.

  <img src="/images/editor/admin/admin-console.png" alt="Scene name" width="500"/>

## Video playing

One of the most common actions for admins to do is to play videos. The admin panel includes a video player section where they can control anything related to videos.

To enable this, you need to add a **Video Player** smart item to your scene and link it to the Scene Admin smart item.

1. Add a **Video Player** smart item to your scene

    <img src="/images/editor/admin/video-player-item.png" alt="Scene name" width="500"/>


  {{< hint warning >}}
  **📔 Note**: An admin can only play videos from URLs on video screens that are added as Smart Items in the Creator Hub, not on screens added via SDK code.

  You can include as many video screens as you want. In general, avoid having more than one different video playing at the same time, as that hurts performance a lot.
  {{< /hint >}}

2. On the Scene Admin Smart Item, make sure the **Video Control** section is enabled. Then select the screen from a dropdown list and give it a name.

Once the above is configured, admin users in your scene can open the admin panel and select the video section to control these video screens.

  <img src="/images/editor/admin/video-player.png" alt="Scene name" width="500"/>


If your scene has multiple video screens, a dropdown list allows you to select which one you want to control. The list displays the names you gave to each video screen on the Admin Tools smart item configuration.

### Video playing modes

There are two different modes for playing videos:

- **Video**: Play a video file from your local filesystem or from an URL.
  Paste a video URL into the **Video URL** field and click the green **Activate** button. The video will start playing on the selected screen for all players. You can also stop, pause, restart, mute, or change the volume of the video.

  <img src="/images/editor/admin/video-from-url.png" alt="Scene name" width="500"/>

  {{< hint warning >}}
  **📔 Note**: Not any video URL will work. Videos from sites like Youtube for example have strict policies about their content and will block access to them from Decentraland. See [Streaming Videos]({{< ref "/content/creator/scene-editor/smart-items/play-videos.md#streaming-videos" >}}) for more information on what you can and can't play in Decentraland.
  {{< /hint >}}

- **Live stream**: Play a live stream using a streaming software like OBS.

  <img src="/images/editor/admin/live-stream.png" alt="Scene name" width="500"/>

  See [Live Streaming]({{< ref "/content/creator/scene-editor/live-streaming.md" >}}) for more information on how to set up a live stream.

Each screen in your scene will have one of these modes set as **Active**. You can click the **Video** or **Live** buttons to explore the settings on each section, they won't interrupt what's currently playing until you click the **Activate** button on either section.

<img src="/images/editor/admin/activate.png" alt="Scene name" width="200"/>


## Announcements

In the **Announcements** tab of the admin panel, admins can write messages that get seen by all players in the scene. Messages like this can only be sent by admins, so other players will perceive them as more legitimate than a message on the chat by someone claiming to be an admin.

Select the Message section of the admin UI. Write a message and click **Share**. The message can be up to 90 characters long.

  <img src="/images/editor/admin/announcement.png" alt="Scene name" width="500"/>

<!-- TODO: Waiting for rewards to be released
## Airdrops

To create an airdrop, you need to:

1. Create an airdop in the [Rewards server]({{< ref "/content/creator/rewards/gatting-started.md" >}})

2. Add a **Collectible dispenser** Smart Item to your scene. Configure it with your **Campaign ID** and **Dispenser Key**

    <img src="/images/editor/admin/airdrop-item.png" alt="Scene name" width="500"/>


3. Open the settings for the **Scene Admin** Smart Item. In the **Airdrops** section, select the **Collectible dispenser** smart item you just added from the dropdown list and give it a name.

Once the above is configured, admins can release the airdrop by selecting the **Airdrop** section of the admin UI and clicking **Release**. Players will then see the airdrop drone descend to the ground, where they can click on the item to claim it. If the Rewards campagin is configured to require a captcha, players will have to complete this captcha before they're allowed to claim the item.

  <img src="/images/editor/admin/airdrops.png" alt="Scene name" width="500"/>


{{< hint info >}}
**💡 Tip**: Configure the Rewards Campaign to require a captcha to claim the item. This will make the airdrop more secure and prevent bots from claiming the item. You can also configure the campaign to only allow claiming the item once per player, and to only allow claims coming from the coordinates of your scene on Decentraland. See [Securing the Rewards Dispenser]({{< ref "/content/creator/rewards/api.md#securing-the-rewards-dispenser" >}}) for more information.

{{< /hint >}}
 -->

## Trigger smart items

To Trigger an action from any smart item in the scene:

- Add a smart item to your scene
- Open the settings for the **Scene Admin** Smart Item in the Creator Hub
- In the **Smart item actions** section, add the smart item from the dropdown, give it a custom name and select a default action


Once the above is configured, admins can trigger the action by opening the **Smart Item Actions** section of the admin UI and then selecting an item from the dropdown list. They can then either click the **Default** button to trigger the default action of that item, or select any other of the item's actions from the list.

  <img src="/images/editor/admin/smart-item-actions.png" alt="Scene name" width="500"/>

You can also show or hide any smart item in this list, even if it doesn't include an action to do that.

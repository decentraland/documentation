---
date: 2024-09-11
title: Video Screen
description: Play Videos in your scene
categories:
  - scene-editor
type: Document
url: /creator/editor/videos
weight: 3
---

To play pre-recorded or streamed videos on a screen on your scene, use the Video Player [Smart Item]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}).

<img src="/images/editor/admin/video-player-item.png" alt="Scene name" width="200"/>

## General settings

These settings are relevant for all scenarios, either if you're playing videos or streaming.

 <img src="/images/editor/admin/video-automatic.png" width="300"/>

You can configure the volume of the video's audio. Note that the audio from the stream is not positional, it is heard at an even volume through all your scene.

<!--
The Video Screen smart item includes an **Image Placeholder** field, that lets you point to a local image or URL. This image will be displayed as a texture on the screen whenever there is no video or stream to show.

It's a good practice to set an image as a placeholder for whenever your sceen is not playing any videos, to avoid a simple black screen before a video starts or after it ends, of if technical difficulties arise.

{{< hint info >}}
**💡 Tip**: 
Take advantage of this space to display instructions for how to play the video, the time of the next event, or a simple "We'll be back soon", depending on the scenario.
{{< /hint >}}

-->

The **Default Media Source** dropdown lets you pick between two different kinds of sources:

- **Video URL**: Fetch a video or a stream from a URL or local video file
- **Live Stream**: Use Decentraland's free streaming infrastructure to display a stream. To use this, you must also include an [Admin tools]({{< ref "/creator/scene-editor/scene-admin.md">}}) smart item iin your scene.

## Play Videos

You can Play pre-recorded videos from either:

- **Local files**: Upload a video file as part of the scene, then point the _URL_ field to the path to that file.
- **Stream from a URL**: Point to a live or pre-recorded stream on the web, for example from Vimeo. See [streaming videos](#streaming-videos)

The timing of when the Video Player smart item plays a video can depend on different things:

- **Automatic**: The video starts playing as soon as the scene loads. For this, set the default media source dropdown to **Video URL** and paste a URL directly into the **Default Video URL** field.

  <img src="/images/editor/admin/video-automatic.png" width="400"/>

- **Triggered by an admin**: A [Scene admin]({{< ref "/content/creator/scene-editor/scene-admin.md" >}}) who's currently in the scene can use the Admin UI to paste a video URL and play it for all players who are currently in the scene.

- **Based on player actions**: Define an Action of type **Play Video Stream**. This lets you trigger the playing of the video as the result of interacting with some other smart item, like walking into a room, or pushing a button. See [Smart Items - Advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md" >}}).

  <img src="/images/editor/video-from-action.png" width="400"/>

In all cases you configure the video to either loop or play once.

{{< hint warning >}}
**📔 Note**: If too many videos are playing at the same time in your scene, some will be paused by the engine. The priority is determined based on proximity to the player, direction of the camera and size of the screen. The maximum amount of simultaneous videos depends on the player's quality settings.

- Low: 1
- Medium: 5
- High: 10

We also recommend starting to play the video when the player is near or performs an action to do that. Starting to play a video when your scene is loaded far in the horizon will unnecessarily affect performance while players visit neighboring scenes.
{{< /hint >}}

### About Video Files

The following file formats are supported:

- _.mp4_
- _.ogg_
- _.webm_

Keep in mind that a video file adds to the total size of the scene, which makes the scene take longer to download for players walking into your scene. The video size might also make you go over the [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}), as you have a maximum of 15 MB per parcel to use. We recommend compressing the video as much as possible, so that it's less of a problem.


## Live streaming

You can stream your webcam or desktop into Decentraland. This is useful for live events, tutorials, or any other content that you want to share with others.

To do this, you need a streaming software that can output to an URL. Some popular choices are [OBS](https://obsproject.com/), [XSplit](https://www.xsplit.com/), or [StreamYard](https://streamyard.com/).


1. Besides the Video Screen smart item, aslo add a an [Admin Tools smart item]({{< ref "/content/creator/scene-editor/scene-admin.md" >}}).

    <img src="/images/editor/admin/admin-smart-item.png" alt="Scene name" width="200"/>

2. Open the Scene Admin Smart Item, make sure the **Video Screens** checkbox is enabled for this section to show. Then select the screen from a dropdown list and give it a friendly name to display on the Admin UI. You can add as many Video Screens as you want, each screen is controlled independently.

      <img src="/images/editor/admin/multi-video-setup.png" alt="Scene name" width="400"/>

3. Publish your scene, either to a World or to Genesis City.

    <img src="/images/editor/publish-button.png" alt="Scene name" width="200"/>

3. Enter the scene as a player with the permission to use the Admin tools. You should be able to see the Admin tools UI on the top-right corner of the screen.

    <img src="/images/editor/admin/admin-icon.png" alt="Scene name" width="74"/>

4. Open the Amin console, select the **Video** tab, then select the **Live** functionality and click the **Get Stream Key** button.

    <img src="/images/editor/admin/get-key.png" alt="Scene name" width="400"/>

5. Copy the **RMTP Server** and **Stream key** to your streaming software. For example for OBS, open **Settings**, then the **Stream** tab, and paste these values into the **Server** and **Stream Key** fields. Then press **Start Streaming**.

    <img src="/images/editor/admin/OBS-configuration.png" alt="Scene name" width="600"/>

  {{< hint danger >}}
  **❗Warning**: Only one person can stream to a scene at a time, even if the scene has multiple screens. When done streaming, streamers must click **Stop Streaming** on OBS to free the channel for others to start.
  {{< /hint >}}

6. Back in the scene's Amdin Tools console, press the **Activate** button to start showing your stream in the scene.

    <img src="/images/editor/admin/activate.png" alt="Scene name" width="200"/>


Streaming works on all Decentraland scenes, including Worlds and LAND in Genesis City. There are no limits to how many players can be in the scene watching the stream, they should all be able to see it.

A single scene can include as many Video screens showing the same stream without a significant impact on performance.

{{< hint warning >}}
**📔 Note**: If you add multiple **Video Screen** smart items to your scene, make sure you mute all except one. Otherwise the sound might be glitchy and have artifacts resulting from multiple copies of the same audio.
{{< /hint >}}



### Stream Keys

Stream keys are used to only allow authenticated users to stream content into your stream. They are generated per scene, and are valid for 4 days (96 hours), then they expire and you must obtain a new key.

Although the keys are valid for 4 days, you can stream continuosly for up to 4 hours at a time. After that, you will need to end the stream session and start streaming again. This is to prevent usused streams from being left open indefinitely and using up unnecessary server capacity.

<img src="/images/editor/admin/live-stream-settings.png" alt="Scene name" width="400"/>

Click **Reset Stream Key** to revoke the current key and generate a new key. Any stream that's taking place at the time will be interrupted. To keep on streaming after that, you will need to copy the new stream key into your streaming software. 

Each scene has its own streaming address and key, only the scene admins have access to the key, but they can share it with other users. Users who are streaming don't need to be in Decentraland, they could even be using a mobile app.

Only one stream can be active at a time in your scene, even if your scene has multiple screens. If you try to start a new stream while another is active, the new stream will stop and overwrite the current one, so if there are multiple streamers make sure they're well coordinated.

{{< hint danger >}}
**❗Warning**: Be careful who you share your stream key with, once they have the key you won't be able to stop them from streaming into your scene.

If you host an event with multiple different presenters, make sure that when finished they click **stop their stream** to make room for the next presenter.

As a last resort you can click **Reset Stream Key** to end all current streams. You must then share a new key with whoever needs to stream next.
{{< /hint >}}

### Streaming from other sources

You can also stream videos using other streaming infrastructures. To do this, simply configure the Video Player smart item to use the **Video URL** media source, and paste the stream URL into the **Default Video URL** field.

The source of the streaming must be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. This means you can't stream a video from YouTube or similar sites, as these only allow displaying their content in their branded HTML widget. See See [About External Streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#about-external-streaming" >}}) for options and tips.

There are a number of options for streaming video. The simplest option is to use a managed hosting provider like [Vimeo](https://vimeo.com/), [Livepeer Studio](https://livepeer.studio/) or [Serraform](https://serraform.gitbook.io/streaming-docs/guides/decentraland-playback) where you pay a fee to the provider to manage all the streaming infrastructure.

Read [Setting up OBS for successful streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#setting-up-obs-for-successful-streaming" >}}) for tips on how to best stream content into Decentraland.





 

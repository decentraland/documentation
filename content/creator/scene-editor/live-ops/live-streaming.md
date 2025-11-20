---
date: 2025-11-04
title: Live Streaming
description: Stream live video into your scene using the Video Screen and Admin Tools.
categories:
  - scene-editor
type: Document
url: /creator/scene-editor/live-ops/live-streaming
weight: 2
---

Use the **Video Screen** smart item together with the **Scene Admin** smart item to stream live video into your scene.

Decentraland offers different ways to stream live video into your scene:

- **DCL Cast** _(Easy Mode)_: Use Decentraland's free streaming web app to easily share your camera or screen with other players in the scene, no need to set up a streaming software. This mode has the lowest latency and is the easiest to set up.
- **Stream** _(Advanced Mode)_: Use a streaming software like [OBS](https://obsproject.com/) to stream through Decentraland's streaming infrastructure. This mode allows you to have more control over the stream, like screen layout and audio sources.
- **Video URL** _(Advanced Mode)_: Point to your own streaming infrastructure, by pasting the URL into the **Video URL** field.

<img src="/images/editor/admin/stream-modes.png" alt="Stream methods" width="400"/>



Streaming works in Worlds and Genesis City, with no audience limits on the scene side.

## Configure the scene

The following steps are common to both DCL Cast and Stream methods:

1. Add a **Video Screen** smart item to your scene.

   <img src="/images/editor/admin/video-player-item.png" alt="Video Screen item" width="200"/>

2. Add a **Scene Admin** smart item and enable the **Video Screens** section. Select each screen from the dropdown and give it a friendly name for the admin UI.

   <img src="/images/editor/admin/multi-video-setup.png" alt="Link screens to Admin" width="400"/>

3. Publish your scene (World or Genesis City) and enter as a user with admin permissions.

   <img src="/images/editor/publish-button.png" alt="Publish" width="200"/>

Once your scene is published, you can enter as a user with admin permissions and configure the streaming settings.


{{< hint info >}}
**💡 Tip**: If you add multiple Video Screens, configure all but one's source to point to the same video player, see [Multiple Video Screens]({{< ref "/content/creator/scene-editor/interactivity/video-screen.md#multiple-video-screens" >}}) for more details.
{{< /hint >}}



## DCL Cast

### Sharing access to the app

Enter your published scene as an admin user, and open the admin panel. Select the **Video** tab, then select the **DCL Cast** functionality.

   <img src="/images/editor/admin/dcl-cast.png" alt="DCL Cast" width="400"/>

You'll see two links that you can copy and share with others.

- **Cast Speakers**: This link is for the speakers to use to cast their video to the scene.

   {{< hint danger >}}
   **❗Warning**: Treat the steaming link as a secret, only share it with people you trust. Reset the link between presenters if needed.

   Only one person can stream to a scene at a time. When finished streaming, close the DCL Cast browser tab to free the channel.
   {{< /hint >}}

- **Viewers**: This link is for the audience to use to watch the video from a browser. This is useful for players who are currently not inside Decentraland, or even on a mobile device.

Click the **Copy link** button to copy the links to the clipboard.

When ready to stream, click the **Activate** button to make the stream visible to the audience in the scene.

   <img src="/images/editor/admin/activate.png" alt="Activate stream" width="200"/>



If for any reason you need to reset the room, click the **Reset Room** button to generate a new one. Anyone who's currently streaming will be disconnected.

 <img src="/images/editor/admin/reset-room.png" alt="Reset room" width="400"/>


### Using the DCL Cast app

When someone pastes the speaker link into a browser, they'll see a screen like this:

 <img src="/images/editor/admin/dcl-cast-landing.png" alt="DCL Cast app" width="400"/>

The browser will ask for permission to share your camera and microphone. You can also configure the different input devices to use for the stream.

{{< hint info >}}
**📔 Tip**: Use Google Chrome or a browser built on the Chrome engine. These browsers offer the functionality to easily share both video and audio directly from a browser tab.
{{< /hint >}}


Users can input a name (doesn't need to match their Decentraland username) and click the **Join Now** button to start streaming.

Once streaming, the app is similar to various familiar video conferencing apps, with buttons to mute/unmute, share camera and screen, and a chat interface.

The chat is read-only, and listens to all messages sent by players inside the scene in Decentraland. This is great to keep in touch with the audience, even if you're streaming from a different device.

 <img src="/images/editor/admin/dcl-cast-app.png" alt="DCL Cast app" width="400"/>

On the **Participants** tab you can see three lists:

- **Speakers**: The people who are currently streaming to the scene.
- **Viewers**: The people who are currently watching the stream from a browser.
- **In-world participants**: The players who are currently inside the scene, watching the stream in-world.

 <img src="/images/editor/admin/participants.png" alt="Participants tab" width="400"/>


## Stream method

To use the Live Streaming feature on your scene you'll need to install a streaming software that can output to an RTMP endpoint (e.g. [OBS](https://obsproject.com/), [XSplit](https://www.xsplit.com/), [StreamYard](https://streamyard.com/)).

### Get stream credentials

1. Open the Admin UI in the scene (top‑right icon).

   <img src="/images/editor/admin/admin-icon.png" alt="Admin icon" width="74"/>

2. In the **Video** tab, switch to **Live** and click **Get Stream Key**.

   <img src="/images/editor/admin/get-key.png" alt="Get stream key" width="400"/>

3. Copy the **RTMP Server** and **Stream Key** into your streaming software.

   <img src="/images/editor/admin/OBS-configuration.png" alt="OBS configuration" width="600"/>

{{< hint danger >}}
**❗Warning**: Only one person can stream to a scene at a time. When finished streaming, click **Stop Streaming** in your software to free the channel.
{{< /hint >}}

### Start and control the stream

1. Start streaming from your software.
2. In the Admin UI, click **Activate** to show the stream in the scene.

   <img src="/images/editor/admin/activate.png" alt="Activate stream" width="200"/>


### Stream keys

Stream keys are generated per scene and are valid for 4 days (96 hours). A single live session can run up to 4 hours continuously.

<img src="/images/editor/admin/live-stream-settings.png" alt="Stream settings" width="400"/>

- Click **Reset Stream Key** to revoke the current key and issue a new one. Ongoing streams will stop.
- Each scene has its own streaming address and key. Admins can share the key with external streamers.
- Only one stream can be active per scene at a time; starting a new one will overwrite the current stream.

{{< hint danger >}}
**❗Warning**: Treat stream keys as secrets. Reset the key between presenters if needed.
{{< /hint >}}

## Streaming from URL method

You can also stream using third‑party infrastructure by configuring the Video Screen to **Video URL** and pasting a stream URL.

- The URL must be `https` and CORS‑enabled by the provider (YouTube and similar sites won’t allow direct playback). See [About External Streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#about-external-streaming" >}}).
- Managed providers include [Vimeo](https://vimeo.com/), [Livepeer Studio](https://livepeer.studio/) and [Serraform](https://serraform.gitbook.io/streaming-docs/guides/decentraland-playback).
- Tips for encoder setup: [Setting up OBS for successful streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#setting-up-obs-for-successful-streaming" >}}).



description: Live streaming
categories:
  - scene-editor
type: Document
url: /creator/editor/live-streaming
weight: 9
---


You can stream your webcam or desktop to Decentraland. This is useful for live events, tutorials, or any other content that you want to share with others.

To do this, you need a streaming software that can output to an URL. Some popular choices are [OBS](https://obsproject.com/) and [XSplit](https://www.xsplit.com/).

On your scene, you will need to add an [Admin Tools smart item]({{< ref "/content/creator/scene-editor/scene-admin.md" >}}) and a [Video Screen smart item]({{< ref "/content/creator/scene-editor/smart-items/video-screen.md" >}}).

IMAGE

1. Add an [Admin tools]({{< ref "/creator/scene-editor/scene-admin.md">}}) smart item to your scene, as well as a [Video player]({{< ref "/creator/scene-editor/smart-items/play-videos.md">}}) smart item.

IMAGE

2. Publish your scene, either to a World or to Genesis City.

IMAGE

3. Enter the scene as a player with the permission to use the Admin tools. You should be able to see the Admin tools UI on the top-right corner of the screen.

IMAGE

4. Open the Amin console, select the **Video** tab, then select the **Live** functionality and click the **Get Stream Key** button.

IMAGE

5. Copy the **Server URL** and *Streaming key** to your streaming software (for example OBS).

IMAGE

6. Press the **Activate** button to start streaming.

IMAGE


## Streaming Keys

Streaming keys are used to authenticate your stream. They are valid for 72 hours and can be used on multiple scenes.

Although the keys are valid for 72 hours, you can stream continuosly for up to 4 hours. After that, you will need to end the stream and start streaming again.

IMAGE

Click **Reset Streaming Key** to revoke the current key and stop streaming. This will generate a new key and you will need to update your streaming software with the new credentials.


Each scene has its own streaming address and key, only the scene admins have access to the key, but they can share it with others.

Only one stream can be active at a time. If you try to start a new stream while another is active, the new stream will stop the current one.


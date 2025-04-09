description: Live streaming
categories:
  - scene-editor
type: Document
url: /creator/editor/live-streaming
weight: 9
---


You can stream your webcam or desktop into Decentraland. This is useful for live events, tutorials, or any other content that you want to share with others.

To do this, you need a streaming software that can output to an URL. Some popular choices are [OBS](https://obsproject.com/) and [XSplit](https://www.xsplit.com/).

On your scene, you will need to add an [Admin Tools smart item]({{< ref "/content/creator/scene-editor/scene-admin.md" >}}) and a [Video Screen smart item]({{< ref "/content/creator/scene-editor/smart-items/play-videos.md" >}}).


1. Add an [Admin tools]({{< ref "/creator/scene-editor/scene-admin.md">}}) smart item to your scene, as well as a [Video player]({{< ref "/creator/scene-editor/smart-items/play-videos.md">}}) smart item.

<img src="/images/editor/admin/admin-smart-item.png" alt="Scene name" width="500"/>
<img src="/images/editor/admin/video-player-item.png" alt="Scene name" width="500"/>

2. Reference the Video Player smart item from inside the Admin Tools smart item.

IMAGE

3. Publish your scene, either to a World or to Genesis City.

<img src="/images/editor/publish-button.png" alt="Scene name" width="500"/>

3. Enter the scene as a player with the permission to use the Admin tools. You should be able to see the Admin tools UI on the top-right corner of the screen.

<img src="/images/editor/admin/admin-icon.png" alt="Scene name" width="100"/>

4. Open the Amin console, select the **Video** tab, then select the **Live** functionality and click the **Get Stream Key** button.

IMAGE

5. Copy the **RMTP Server** and **Stream key** to your streaming software. For example for OBS, open **Settings**, then the **Stream** tab, and paste these values into the **Server** and **Stream Key** fields. Then press **Start Streaming**.

<img src="/images/editor/admin/OBS-configuration.png" alt="Scene name" width="100"/>

6. Back in the scene's Amdin Tools console, press the **Activate** button to start showing your stream in the scene.

<img src="/images/editor/admin/activate.png" alt="Scene name" width="100"/>


## Streaming Keys

Streaming keys are used to only allow authenticated users to stream content into your stream. They are generated per scene, and are valid for 72 hours, then they expire and you must obtain a new key.

Although the keys are valid for 72 hours, you can stream continuosly for up to 4 hours. After that, you will need to end the stream session and start streaming again. This is to prevent usused streams from staying open and use up unnecessary server time.

<img src="/images/editor/admin/live-stream-settings.png" alt="Scene name" width="100"/>

Click **Reset Stream Key** to revoke the current key and generate a new key. Any stream that's taking place at the time will be interrupted. To keep streaming after that, you will need to update your streaming software with the new credentials.

Each scene has its own streaming address and key, only the scene admins have access to the key, but they can share it with other users, who don't need to be connected to Decentraland, they could even be using a mobile app.

Only one stream can be active at a time in your scene, even if your scene has multiple screens. If you try to start a new stream while another is active, the new stream will stop the current one.


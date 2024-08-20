---
title: "Decentraland Cast"
url: /creator/worlds/cast
weight: 22
---

Decentraland Cast is a specialized tool tailored for world owners and other authorized individuals. It offers the capability to stream camera footage or share screens seamlessly within their world, all without the need to host a server. With low-latency streaming, the experience is smooth and immediate, enhancing the virtual connection.

## Streaming

Streaming through Decentraland Cast is an exclusive feature available only to World owners or those with streaming rights for a World scene. For more details on these rights, refer to the [Access Contol Lists]({{< ref "/creator/worlds/about.md#access-control-lists-acl" >}}) section.

1. Visit [Decentraland Cast](https://cast.decentraland.org/)
2. Select Your World: Log in and select the world to stream to.
<br/><img src="/images/worlds/world-selector.png" width="400"  style="display: block; margin: 0 auto;" /><br/>
1. Join the Session: Once the world is selected, a session will be joined. 
<br/><img src="/images/worlds/cast-ui.png" width="400"  style="display: block; margin: 0 auto;" /><br/>
1. Share Screen or Camera Footage: If authorized, users have the option to either activate their cameras or share their screens directly within the app.
{{< hint warning >}}
**📔 Note**: If you intend to stream a video along with its audio, it's advisable to utilize Google Chrome or a browser built on the Chrome engine. These browsers offer the functionality to easily share both video and audio directly from a browser tab.
{{< /hint >}}
<div style="text-align: center;">
    <img src="/images/worlds/screen-sharing-host.png" width="600"  style="display: block; margin: 0 auto;"/>
    <img src="/images/worlds/screen-sharing-viewer.png" width="600"  style="display: block; margin: 0 auto;"/>
</div>
5. Flawless Integration: Decentraland Cast’s integration with the world ensures uninterrupted communication, allowing users to effortlessly send, receive, and listen to chat and voice messages.
<!-- <image showing the screen and chat Decentraland Cast UI>
<image showing the screen and chat in the World>-->

## Showcasing the stream in a world

1. You must first deploy a scene in the world with the ability to handle video streams. To delve deeper into the specifics of this integration, please consult the [Play Videos]({{< ref "/content/creator/sdk7/media/video-playing.md#streaming-using-decentraland-cast" >}}) SDK documentation.
{{< hint warning >}}
**💡 Note**: To get started quickly, download the Decentraland Cast example scene and modify the world URL in the scene.json file to match your specific world.
{{< /hint >}}
3. Ensure that there is an open session in Decentraland Cast.
4. Join the world and test the streaming being showcased.

{{< hint danger >}}
**❗Warning**  
Since the session in Decentraland Cast is the same LiveKit session within the world, one address can be presented in either the World or the Decentraland Cast session, but not in both simultaneously. If this occurs, the whole casting session will be disconnected for all users. For testing purposes, it is recommended to enter the world as a guest so the Decentraland Cast session remains live.
{{< /hint >}}

## Spectating

It’s recommended for spectators to join the world (not the Decentraland Cast application) unless accessing via mobile phones. In Decentraland Cast, all users will be able to watch what is being streamed, the chat, and other people in the session but those lacking authorization will find their capabilities restricted. Specifically, they will not have permissions to broadcast any data, whether it be video, voice chat, or text messaging.

<img src="/images/worlds/cast-mobile.png" width="300"  style="display: block; margin: 0 auto;" />


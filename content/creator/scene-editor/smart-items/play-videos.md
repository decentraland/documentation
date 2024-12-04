---
date: 2024-09-11
title: Play videos
description: Play Videos in your scene
categories:
  - scene-editor
type: Document
url: /creator/editor/videos
weight: 3
---

To play videos on a screen on your scene, use the Video Player [Smart Item]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}).

You can Play videos from either:

- **Local files**: Upload a video file as part of the scene, then point the _URL_ field to the path to that file.
- **Stream from a URL**: Point to a live or pre-recorded stream on the web, for example from Vimeo. See [streaming videos](#streaming-videos)
- **Stream live from DCL Cast**: This simplified service lets you easily set up a live stream as a scene owner. See [Decentraland Cast]({{< ref "/creator/worlds/cast.md">}}).

There are two options for when to play a video:

- Configure the **Video Player** component of the item directly. This makes the video start playing as soon as the scene loads.
  <img src="/images/editor/video-from-start.png" width="300"/>

- Define an Action of type **Play Video Stream**. This lets you trigger the playing of the video as the result of a player interaction, like walking into a room, or pushing a button. See [Smart Items - Advanced]({{< ref "/content/creator/scene-editor/smart-items/smart-items-advanced.md" >}}).

  <img src="/images/editor/video-from-action.png" width="300"/>

You can configure the volume of the video's sounds. Note that the audio from the stream is not positional, it is heard at an even volume through all your scene.

You can also configure the video to either loop or play once.

{{< hint warning >}}
**📔 Note**: If too many videos are playing at the same time in your scene, some will be paused by the engine. The priority is determined based on proximity to the player, direction of the camera and size of the screen. The maximum amount of simultaneous videos depends on the player's quality settings.

- Low: 1
- Medium: 5
- High: 10

We also recommend starting to play the video when the player is near or performs an action to do that. Starting to play a video when your scene is loaded far in the horizon will unnecessarily affect performance while players visit neighboring scenes.
{{< /hint >}}

## Streaming videos

The source of the streaming must be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. This means you can't stream a video from YouTube or similar sites, as these only allow displaying their content in their branded HTML widget. See See [About External Streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#about-external-streaming" >}}) for options and tips.

There are a number of options for streaming video. The simplest option is to use a managed hosting provider like [Vimeo](https://vimeo.com/), [Livepeer Studio](https://livepeer.studio/) or [Serraform](https://serraform.gitbook.io/streaming-docs/guides/decentraland-playback) where you pay a fee to the provider to manage all the streaming infrastructure.

Read [Setting up OBS for successful streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#setting-up-obs-for-successful-streaming" >}}) for tips on how to best stream content into Decentraland.

## About Video Files

The following file formats are supported:

- _.mp4_
- _.ogg_
- _.webm_

Keep in mind that a video file adds to the total size of the scene, which makes the scene take longer to download for players walking into your scene. The video size might also make you go over the [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}), as you have a maximum of 15 MB per parcel to use. We recommend compressing the video as much as possible, so that it's less of a problem.

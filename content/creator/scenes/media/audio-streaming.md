---
date: 2022-07-11
title: Audio Streaming
description: Play live audio streams in your scene.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/audio-streaming
url: /creator/development-guide/audio-streaming
---


You can stream audio from a URL. This is useful to play music directly from an internet radio, or stream a conference into your scene.

The audio in the source must be in one of the following formats: `.mp3`, `ogg`, or `aac`. The source must also be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. If this is not the case, you might need to set up a server to act as a proxy and expose the stream in a valid way.

> Note: To instead play a pre-recorded sound in your scene, see [Sounds]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}).


To add an audio stream into your scene, simply add an entity with an `AudioStream` component:

```ts
const streamSource = new Entity()
streamSource.addComponent(
  new AudioStream(
    "https://icecast.ravepartyradio.org/ravepartyradio-192.mp3"
  )
)
engine.addEntity(streamSource)

streamSource.getComponent(AudioStream).playing = true
```

> Note: The streamed sound isn't positional, it will be heard at a consistent volume throughout your entire scene. If a player steps out of the scene, they will not hear the streaming at all.

Set the volume of the `AudioStream` component by changing its `volume` property.

Switch the `AudioStream` component on or off by setting its `playing` property to _true_ or _false_.

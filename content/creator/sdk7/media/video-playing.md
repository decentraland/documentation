---
date: 2020-05-04
title: Play videos
description: Stream video into a scene
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/video-playing/
weight: 2
---

There are two different ways you can show a video in a scene. One is to stream the video from an external source, the other is to pack the video file with the scene and play it from there.

In both cases, you use a `VideoPlayer` component to control the state of the video. You also need to create a `VideoTexture`, which can be used on a [material]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}) and then applied to any [primitive shape]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md" >}}) like a plane, cube, or even a cone.

{{< hint warning >}}
**📔 Note**: Keep in mind that streaming video demands a significant effort from the player's machine. For this reason, we recommend never having more than one video stream displayed at a time per scene. Videos are also not played if the player is standing on a different scene. Also avoid streaming videos that are in very high resolution, don't use anything above _HD_.
{{< /hint >}}

## Show a video

The following instructions apply both to streaming and to showing a video from a file:

1. Create an entity to serve as the video screen. Give this entity a `MeshRenderer` component so that it has a visible shape.

2. Create a `VideoPlayer` component, either referencing a streaming URL or a path to a video file. Here you can also set the video's `playing` state, and its volume. This component can be assigned to the video screen entity, or to any other entity in the scene.

3. Create a `VideoTexture` object, and in its `videoPlayerEntity` property assign the entity that owns the `VideoPlayer` component.

4. Create a `Material`, assign it to the screen entity, and set its `texture` to the `VideoTexture` you created.

This example uses a video that's locally stored in a `/videos` folder in the scene project:

```ts
// #1
const screen = engine.addEntity()
MeshRenderer.setPlane(screen)
Transform.create(screen, { position: { x: 4, y: 1, z: 4 } })

// #2
VideoPlayer.create(screen, {
  src: 'videos/myVideo.mp3',
  playing: true,
})

// #3
const videoTexture = Material.Texture.Video({ videoPlayerEntity: screen })

// #4
Material.setPbrMaterial(screen, {
  texture: videoTexture,
  roughness: 1.0,
  specularIntensity: 0,
  metallic: 0,
})
```

To use a video from an external streaming URL, just change step 2 so that the `src` property in the `VideoPlayer` component references the path to the file.

{{< hint warning >}}
**📔 Note**: For a video stream to work in your scene, you must also edit the `scene.json` to allow streaming, and add the domains you want to stream from to the allowlist. See [About streaming](#about-streaming).
{{< /hint >}}

```ts
// #2
VideoPlayer.create(screen, {
  src: 'https://player.vimeo.com/external/552481870.m3u8?s=c312c8533f97e808fccc92b0510b085c8122a875',
  playing: true,
})
```

## About Streaming

The source of the streaming must be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. If this is not the case, you might need to set up a server to act as a proxy and expose the stream in a valid way.

To stream videos from an external URL, you must add the `ALLOW_MEDIA_HOSTNAMES` permission to the `requiredPermissions` list in the `scene.json` file. You must also include the list of high-level domains where you'll be streaming from under `allowedMediaHostnames`.

```json
"requiredPermissions": [
    "ALLOW_MEDIA_HOSTNAMES"
  ],
   "allowedMediaHostnames": [
    "somehost.com",
    "otherhost.xyz"
  ]
```

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.

To launch your own video streaming server, we recommend using a [Node Media Server](https://github.com/illuspas/Node-Media-Server), which provides most of what you need out of the box. See

## Video Materials

The default properties of a material make the video look rather opaque for a screen, but you can enhance that by altering other properties of the material.

Here are some recommended settings for the video to stand out more:

```ts
Material.setPbrMaterial(screen, {
  texture: videoTexture,
  roughness: 1.0,
  specularIntensity: 0,
  metallic: 0,
})
```

If you want the screen to glow a little, more like a LED screen, you can also add some emissive properties. You can even set the `emissiveTexture` of the material to the same `VideoTexture` as the `texture`.

```ts
Material.setPbrMaterial(screen, {
  texture: videoTexture,
  roughness: 1.0,
  specularIntensity: 0,
  metallic: 0,
  emissiveTexture: videoTexture,
  emissiveIntensity: 0.6,
  emissiveColor: Color3.White(),
})
```

See [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md">}}) for more details.

{{< hint info >}}
**💡 Tip**: Since the video is a texture that's added to a material, you can also experiment with other properties of materials, like tinting it with a color, of adding other texture layers. for example to produce a dirty screen effect.
{{< /hint >}}

## About Video Files

The following file formats are supported:

- _.mp4_
- _.ogg_
- _.webm_

Keep in mind that a video file adds to the total size of the scene, which makes the scene take longer to download for players walking into your scene. The video size might also make you go over the [scene limitations]({{< ref "/content/creator/sdk7/optimizing/scene-limitations.md" >}}), as you have a maximum of 15 MB per parcel to use. We recommend compressing the video as much as possible, so that it's less of a problem.

We also recommend starting to play the video when the player is near or performs an action to do that. Starting to play a video when your scene is loaded far in the horizon will unnecessarily affect performance while players visit neighboring scenes.

## Start pause and stop a video

To start playing the video or pause it, set the `playing` property to _true_ or _false_. If `playing` is set to false, the video is paused at the last frame shown.

You can make a screen toggleable by adding a pointer event to it as shown below:

```ts
pointerEventsSystem.onPointerDown(
  screen,
  () => {
    const videoPlayer = VideoPlayer.getMutable(screen)
    videoPlayer.playing = !videoPlayer.playing
  },
  {
    button: InputAction.IA_POINTER,
    hoverText: 'Play/pause',
  }
)
```

To stop the video and send it back to the first frame, set the `position` property to 0. in the following example, clicking on the video stops it.

```ts
pointerEventsSystem.onPointerDown(
  screen,
  () => {
    const videoPlayer = VideoPlayer.getMutable(screen)
    videoPlayer.playing = false
    videoPlayer.position = 0
  },
  {
    button: InputAction.IA_POINTER,
    hoverText: 'STOP',
  }
)
```

## Configure the video player

The following optional properties are available to set on the `VideoPlayer` component:

- `playing`: Determines if the video is currently playing. If false, the video is paused.

{{< hint warning >}}
**📔 Note**: There can only be one `VideoPlayer` component active at a time in each scene.
{{< /hint >}}

- `playbackRate`: Changes the speed at which the video is played. _1_ by default.
- `volume`: Lets you change the volume of the audio. _1_ by default.
- `position`: Allows you to set a different starting position on the video. It's expressed in seconds after the video's original beginning. _-1_ by default, which makes it start at the actual start of the video.
- `loop`: Boolean that determines if the video is played continuously in a loop, or if it stops after playing once. _false_ by default.
- `playbackRate`: The speed at which the video is played

<!-- TODO: check if exposed and how it works -->

## Play multiple videos

To avoid running into performance problems, each scene is only allowed to play one single video texture at a time. However, a scene can play multiple copies of one same video texture in several different screens. That action is not restricted as it impacts performance considerably less than playing separate videos. To play a same video on multiple entities, simply assign the same instance of the video texture object to the `Material` components of each screen entity.

```ts
// #1
const screen1 = engine.addEntity()
MeshRenderer.setPlane(screen1)
Transform.create(screen1, { position: { x: 4, y: 1, z: 4 } })

const screen2 = engine.addEntity()
MeshRenderer.setPlane(screen2)
Transform.create(screen2, { position: { x: 6, y: 1, z: 4 } })

// #2
VideoPlayer.create(screen1, {
  src: 'https://player.vimeo.com/external/552481870.m3u8?s=c312c8533f97e808fccc92b0510b085c8122a875',
  playing: true,
})

// #3
const videoTexture = Material.Texture.Video({ videoPlayerEntity: screen1 })

// #4
Material.setPbrMaterial(screen1, {
  texture: videoTexture,
  emissiveTexture: videoTexture,
  emissiveIntensity: 0.6,
  roughness: 1.0,
})

Material.setPbrMaterial(screen2, {
  texture: videoTexture,
  emissiveTexture: videoTexture,
  emissiveIntensity: 0.6,
  roughness: 1.0,
})
```

Note that in the example above, it's only necessary to create one `VideoPlayer` component, which controls the state of both video screens. In this case this component is assigned to belong to the `screen1` entity, but it could also be assigned to belong to any other entity on the scene, not necessarily one of the screens.

## Video events

Easily handle state changes in a video, to respond to when a video starts playing, is paused, etc. This can be used for example to play animations in perfect sync with a video, ensuring they start at the same time as the video.

Use ‘videoEventsSystem.registerVideoEventsEntity‘ to define a function that runs every time the state of the video assigned to an entity. Every time the state changes, your function can check the new state and respond accordingly.

```ts
import {
  engine,
  Entity,
  VideoPlayer,
  videoEventsSystem,
  VideoState,
} from '@dcl/sdk/ecs'

// ... Create videoPlayerEntity with VideoPlayer component, Transform, MeshRenderer.setPlane(), etc. ...

videoEventsSystem.registerVideoEventsEntity(
  { entity: videoPlayerEntity },
  function (videoEvent) {
    console.log(
      'video event - state: ' +
        videoEvent.state +
        '\ncurrent offset:' +
        videoEvent.currentOffset +
        '\nvideo length:' +
        videoEvent.videoLength
    )

    switch (videoEvent.state) {
      case VideoState.VS_READY:
        console.log('video event - video is READY')
        break
      case VideoState.VS_NONE:
        console.log('video event - video is in NO STATE')
        break
      case VideoState.VS_ERROR:
        console.log('video event - video ERROR')
        break
      case VideoState.VS_SEEKING:
        console.log('video event - video is SEEKING')
        break
      case VideoState.VS_LOADING:
        console.log('video event - video is LOADING')
        break
      case VideoState.VS_BUFFERING:
        console.log('video event - video is BUFFERING')
        break
      case VideoState.VS_PLAYING:
        console.log('video event - video started PLAYING')
        break
      case VideoState.VS_PAUSED:
        console.log('video event - video is PAUSED')
        break
    }
  }
)
```

The videoEvent object passed as an input for the function contains the following properties:

- `currentOffset` (_number_): The current value of the `seek` property on the video. This value shows seconds after the video's original beginning. _-1_ by default, if the video hasn't started playing.
- `state`: The value for the new video status of the video, expressed as a value from the `VideoState` enum. This enum can hold the following possible values:
  - `VideoState.VS_READY`
  - `VideoState.VS_NONE`
  - `VideoState.VS_ERROR`
  - `VideoState.VS_SEEKING`
  - `VideoState.VS_LOADING`
  - `VideoState.VS_BUFFERING`
  - `VideoState.VS_PLAYING`
  - `VideoState.VS_PAUSED`
- `videoLength` (_number_ ): The length in seconds of the entire video. _-1_ if length is unknown.
- `timeStamp` ( _number_): A _lamport_ timestamp that is incremented every time that the video changes state.
- `tickNumber` (_number_): The time at which the event occurred, expressed as counting ticks since the scene started running.

### Latest video event

Query a video for its last state change by using `getLatestVideoEvent`. This function returns an object with a `currentState` property, with one of the following values from the `VideoState` enum, indicating the current state of the video:

- `VideoState.VS_READY`
- `VideoState.VS_NONE`
- `VideoState.VS_ERROR`
- `VideoState.VS_SEEKING`
- `VideoState.VS_LOADING`
- `VideoState.VS_BUFFERING`
- `VideoState.VS_PLAYING`
- `VideoState.VS_PAUSED`

```ts
function mySystem() {
  const latestVideoEvent = getLatestVideoEvent(videoPlayerEntity)
  console.log(latestVideoEvent.currentState)
}
```

<!--
## Map a video texture

TODO
in video texture...
filterMode?: TextureFilterMode | undefined;
wrapMode?: TextureWrapMode | undefined;

if using a plane or cube...
use uvs to map parts of the video

-->

<!-- 
## Handle a video file

When playing a video from a file, you can perform the following actions:

- `play()`: Plays the video. It will start from where the `seek` property indicates.

- `pause()`: Stops the video playing, but leaves its `seek` property where the video last was. The last played frame remains visible.

- `reset()`: Stops the video playing and sends its `seek` property back to the begining of the video. The first frame of the video is displayed.

- `seekTime()`: Sets the `seek` property to a specific value, so that the video plays from that point on. It's expressed in seconds after the video's original beginning.

You can also change the following properties:

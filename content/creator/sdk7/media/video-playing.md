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

There are tree different ways you can show a video in a scene:

- Upload a video file as part of the scene contents
- Stream the video from an external source
- Stream live via Decentraland cast

{{< hint info >}}
**💡 Tip**: In the [Scene Editor]({{< ref "/content/creator/scene-editor/about-editor.md" >}}), you can use an **Video Player** [Smart Item]({{< ref "/content/creator/scene-editor/smart-items/smart-items.md" >}}) for a no-code way to achieve this.
{{< /hint >}}

In all cases, you'll need:

- An entity with a [primitive shape]({{< ref "/content/creator/sdk7/3d-essentials/shape-components.md" >}}) like a plane, cube, or even a cone.
- A [material]({{< ref "/content/creator/sdk7/3d-essentials/materials.md" >}}) with a A `VideoTexture` assigned to its texture
- A `VideoPlayer` component to control the state of the video.

## Performance considerations

Keep in mind that streaming video demands a significant effort from the player's machine. It's recommended to avoid playing more than one video at a time.

If too many videos are playing at the same time in your scene, some will be paused by the engine. The priority for pausing a screen is determined based on several factors that include proximity to the player, size, and if the screen is in field of fiew of the player. The maximum amount of simultaneous videos depends on the player's quality settings.

- Low: 1
- Medium: 5
- High: 10

We also recommend starting to play the video when the player is near or performs an action to do that. Starting to play a video when your scene is loaded far in the horizon will unnecessarily affect performance while players visit neighboring scenes.

Also avoid streaming videos that are in very high resolution, don't use anything above _HD_.

It's also ideal to play videos on Basic (unlit) materials, to reduce the performance load, as is the case on all of the example snippets below.

## Show a video

The following instructions apply to all three video showing options:

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
	src: 'videos/myVideo.mp4',
	playing: true,
})

// #3
const videoTexture = Material.Texture.Video({ videoPlayerEntity: screen })

// #4
Material.setBasicMaterial(screen, {
	texture: videoTexture,
})
```

To use a video from an external streaming URL, just change step 2 so that the `src` property in the `VideoPlayer` component references the path to the file.

```ts
// #2
VideoPlayer.create(screen, {
	src: 'https://player.vimeo.com/external/552481870.m3u8?s=c312c8533f97e808fccc92b0510b085c8122a875',
	playing: true,
})
```

See [Streaming using Decentraland cast](#streaming-using-decentraland-cast) for details on how to use this third alternative method.

## About External Streaming

The source of the streaming must be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. If this is not the case, you might need to set up a server to act as a proxy and expose the stream in a valid way.

There are a number of options for streaming video. The simplest option is to use a managed hosting provider like [Vimeo](https://vimeo.com/) ,  [Livepeer Studio](https://livepeer.studio/) or [Serraform](https://serraform.gitbook.io/streaming-docs/guides/decentraland-playback) where you pay a fee to the provider to manage all the streaming infrastructure.

The other recommended alternative is to set up your own server, using free software but paying for hosting on a platform like [Digital Ocean](https://try.digitalocean.com/developerbrand/?_campaign=emea_brand_kw_en_cpc&_adgroup=digitalocean_exact_exact&_keyword=digitalocean&_device=c&_adposition=&_content=conversion&_medium=cpc&_source=bing&msclkid=160bfc160a2a1bab9bbf9933594bd9c5&utm_source=bing&utm_medium=cpc&utm_campaign=emea_brand_kw_en_cpc&utm_term=digitalocean&utm_content=DigitalOcean%20Exact_Exact) or [Cloudflare](https://www.cloudflare.com/products/cloudflare-stream/). You can deploy something like a [Node Media Server](https://github.com/illuspas/Node-Media-Server), which provides most of what you need out of the box.

All these options have pros and cons for different scenarios. You should evaluate what's best for you taking into account your needs, technical skills and budget.

## Setting up OBS for successful streaming

[OBS](https://obsproject.com/) is a popular and free tool for managing your streams.

Whether you are using a venue’s stream key or your own RTMP server, your settings in OBS are important for the success of your stream. You should aim for a solid, consistent connection.

### Simple OBS set-up

The following simple set-up is recommended:

- Bitrate 2500kbps (which will work with all Decentraland venues)
- Audio bitrate 160kbps
- Video encoder preset: Hardware NVENC
- Audio Encoder AAC
- Broadest Resolution: 720 (any greater causes issues in DCL)
- Frame rate 30fps

### Advice for new streamers

- Early sound checks are essential to test your set up with the venue.
- Small errors like a digit wrong in the stream key are the most likely to mess up the stream.
- Do not go above 720 resolution or a bitrate of 2500 kbps.

## Live streaming

You can livestream from your camera or share your screen using the [Live streaming]({{< ref "/creator/scene-editor/smart-items/play-videos.md#live-streaming">}}) feature of the [Admin tools]({{< ref "/creator/scene-editor/scene-admin.md">}}) smart item.

This streaming method uses the same comms architecture used for live communications between players, and is easy to set up and has a lot less delay than streaming from external sources.

1. Add an [Admin tools]({{< ref "/creator/scene-editor/scene-admin.md">}}) smart item to your scene, as well as a [Video player]({{< ref "/creator/scene-editor/smart-items/play-videos.md">}}) smart item.
2. Publish your scene, either to a World or to Genesis City.
3. Enter the scene as a player with the permission to use the Admin tools.
4. Open the Amin console, select the **Video** tab, then select the **Live** functionality and click the **Get Stream Key** button.
5. Copy the **Server URL** and *Streaming key** to your streaming software (for example OBS).
6. Press the **Activate** button to start streaming.

Instead of adding a Video player smart item to your scene, you can also use the URL `livekit-video://current-stream` as the video source, to play the stream in your scene. You will still need the Admin tools to get the stream key.

```ts
// #1
const screen = engine.addEntity()
MeshRenderer.setPlane(screen)
Transform.create(screen, { position: { x: 4, y: 1, z: 4 } })

// #2
VideoPlayer.create(screen, {
	src: `livekit-video://current-stream`,
	playing: true,
})

// #3
const videoTexture = Material.Texture.Video({ videoPlayerEntity: screen })

// #4
Material.setBasicMaterial(screen, {
	texture: videoTexture,
})
```

## Video Materials

Most of the times, you'll want to play videos on an unlit [Basic material]({{< ref "/content/creator/sdk7/3d-essentials/materials.md#unlit-materials" >}}), rather than a PBR material. This results in a much brighter and crisper image, and is better for performance.

```ts
Material.setBasicMaterial(screen, {
	texture: videoTexture,
})
```

It's usually recommended to play videos on Basic unlit materials, as this is better for performance, but if you instead want to project a video onto a PBR material, keep in mind that the default properties make the video look rather opaque. You can enhance that by altering other properties of the material. Here are some recommended settings for the video to stand out more:

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

{{< hint info >}}
**💡 Tip**: Since the video is a texture that's added to a material, you can also experiment with other properties of materials, like tinting it with a color, of adding other texture layers. for example to produce a dirty screen effect.

See [materials]({{< ref "/content/creator/sdk7/3d-essentials/materials.md">}}) for more details.
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
	{
		entity: screen,
		opts: { button: InputAction.IA_POINTER, hoverText: 'Play/Pause' },
	},
	function () {
		const videoPlayer = VideoPlayer.getMutable(screen)
		videoPlayer.playing = !videoPlayer.playing
	}
)
```

To stop the video and send it back to the first frame, set the `position` property to 0. in the following example, clicking on the video stops it.

```ts
pointerEventsSystem.onPointerDown(
	{
		entity: screen,
		opts: { button: InputAction.IA_POINTER, hoverText: 'STOP' },
	},
	function () {
		const videoPlayer = VideoPlayer.getMutable(screen)
		videoPlayer.playing = false
		videoPlayer.position = 0
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
Material.setBasicMaterial(screen1, {
	texture: videoTexture,
})

Material.setBasicMaterial(screen2, {
	texture: videoTexture,
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
	videoPlayerEntity,
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

Query a video for its last state change by using `videoEventsSystem.getVideoState()`. This function always returns the latest `VideoEvent` value for the video.

```ts
function mySystem() {
    const latestVideoEvent = videoEventsSystem.getVideoState(videoPlayerEntity)
    if(!latestVideoEvent) return
    
    console.log(`state: ${latestVideoEvent.state}
    \ncurrentOffset: ${latestVideoEvent.currentOffset}
    \nvideoLength: ${latestVideoEvent.videoLength}`)
}
```

## Alpha masks on videos

A neat trick to have non-rectangular video screens is to apply an alpha texture on top of a plane. You can cut away part of the plane into whatever shape you want.

Use the following image to cut your video into a circular shape, with transparent corners.

<img src="/images/circle_mask.png" width="250" height="140" />

```ts
const videoTexture = Material.Texture.Video({
	videoPlayerEntity: screen,
})
const alphaMask = Material.Texture.Common({
	src: 'assets/scene/circle_mask.png',
	wrapMode: TextureWrapMode.TWM_MIRROR,
})

Material.setBasicMaterial(screen, {
	texture: videoTexture,
	alphaTexture: alphaMask,
})
```

<img src="/images/circular-video-screen.png" width="500" />

{{< hint warning >}}
**📔 Note**: In previous versions, the `alphaTexture` property was only present in PRB materials, currently it only works in basic materials.
{{< /hint >}}

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


TODO
When playing a video from a file, you can perform the following actions:

- `play()`: Plays the video. It will start from where the `seek` property indicates.

- `pause()`: Stops the video playing, but leaves its `seek` property where the video last was. The last played frame remains visible.

- `reset()`: Stops the video playing and sends its `seek` property back to the begining of the video. The first frame of the video is displayed.

- `seekTime()`: Sets the `seek` property to a specific value, so that the video plays from that point on. It's expressed in seconds after the video's original beginning.

You can also change the following properties:
-->

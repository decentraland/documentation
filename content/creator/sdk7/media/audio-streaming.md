---
date: 2022-07-11
title: Audio streaming
description: Play live audio streams in your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/audio-streaming/
weight: 1
---

You can stream audio from a URL. This is useful to play music directly from an internet radio, or stream a conference into your scene.

{{< hint info >}}
**💡 Tip**: In the [Scene Editor]({{< ref "/content/creator/scene-editor/get-started/about-editor.md" >}}), you can use an **Audio Stream** [Smart Item]({{< ref "/content/creator/scene-editor/interactivity/smart-items.md" >}}) for a no-code way to achieve this.
{{< /hint >}}

The audio in the source must be in one of the following formats: `.mp3`, `ogg`, or `aac`. The source must also be an _https_ URL (_http_ URLs aren't supported), and the source should have [CORS policies (Cross Origin Resource Sharing)](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) that permit externally accessing it. If this is not the case, you might need to set up a server to act as a proxy and expose the stream in a valid way.

{{< hint warning >}}
**📔 Note**: To instead play a pre-recorded sound in your scene, see [Sounds]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}).
{{< /hint >}}
To add an audio stream into your scene, simply add an `AudioStream` component to an entity:

```ts
const streamEntity = engine.addEntity()

AudioStream.create(streamEntity, {
	url: 'https://icecast.ravepartyradio.org/ravepartyradio-192.mp3',
	playing: true,
	volume: 0.8,
})
```

{{< hint warning >}}
**📔 Note**: The streamed sound isn't positional, it will be heard at a consistent volume throughout your entire scene. If a player steps out of the scene, they will not hear the streaming at all.
{{< /hint >}}

Set the volume of the `AudioStream` component by changing its `volume` property.

Switch the `AudioStream` component on or off by setting its `playing` property to _true_ or _false_.

{{< hint info >}}
**📔 Note**:
Not all streaming services allow you to play their audio outside their site. The following are some examples that work in Decentraland:

```ts
DELTA = "https://cdn.instream.audio/:9069/stream?_=171cd6c2b6e"
GRAFFITI = "https://n07.radiojar.com/2qm1fc5kb.m4a?1617129761=&rj-tok=AAABeIR7VqwAilDFeUM39SDjmw&rj-ttl=5"
ISLA NEGRA = "https://radioislanegra.org/listen/up/basic.aac"
```

{{< /hint >}}

## Stream state

Query the state of an audio stream using the function `AudioStream.getAudioState()`, passing the entity that owns the `AudioStream` component.

The returned state is a value of the `MediaState` enum. This enum has the following possible values:

- `MS_BUFFERING`
- `MS_ERROR`
- `MS_LOADING`
- `MS_NONE`
- `MS_PAUSED`
- `MS_PLAYING`
- `MS_READY`
- `MS_SEEKING`

The following example checks on the state of a stream, and logs when there's a change.

```ts
export function main() {
	const entity = engine.addEntity()

	AudioStream.create(entity, {
		playing: true,
		volume: 1,
		url: 'https://audio-edge-es6pf.mia.g.radiomast.io/ref-128k-mp3-stereo',
	})

	let lastState: ReturnType<typeof AudioStream.getAudioState> = undefined
	engine.addSystem(() => {
		const currentState = AudioStream.getAudioState(entity)
		if (lastState !== currentState) {
			console.log('Stream state: ', currentState)

			if (currentState == MediaState.MS_ERROR) {
				// Attempt reconnection
			}
		}
	})
}
```

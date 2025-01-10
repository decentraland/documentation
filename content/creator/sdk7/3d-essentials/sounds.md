---
date: 2018-02-10
title: Sounds
description: Learn how to add sounds to your scene.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/sounds/
weight: 4
---

Sound is a great way to provide feedback to player actions and events, background sounds can also give your scene more context and improve the player's immersion into it.

{{< hint warning >}}
**📔 Note**: Keep in mind that sounds are only heard by players who are standing within the parcels that make up the scene where the sound was generated, even if they would otherwise be in hearing range. Players can also chose to turn off all sounds on their settings.
{{< /hint >}}

Supported sound formats vary depending on the browser, but it's recommended to use _.mp3_.

_.wav_ files are also supported but not generally recommended as they are significantly heavier.

## Play sounds

The easiest way to play a sound is to add an **Audio Source** component visually on the [Scene Editor]({{< ref "/content/creator/scene-editor/about-editor.md" >}}) and set it to **Start Playing** and **Loop**. See [Add Components]({{< ref "/content/creator/scene-editor/components.md#add-components" >}}).

<img src="/images/editor/AudioSource-component.png" alt="Scene name" width="200"/>

You can also trigger the playing of a sound in a no-code way via **Actions**, see [Make any item smart]({{< ref "/content/creator/scene-editor/smart-items/make-any-item-smart.md" >}}).

To play a sound via code, use the `AudioSource.playSound` function.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Play sound
AudioSource.playSound(sourceEntity, 'assets/sounds/sound-effect.mp3')
```

The sound file must be inside the project folder. In the example above, the audio file is located in an `assets/sounds` folder, which is located at root level of the scene project folder.

{{< hint warning >}}
**📔 Note**: The `AudioSource` component must be imported via

> `import { AudioSource } from "@dcl/sdk/ecs"`

See [Imports]({{< ref "/content/creator/sdk7/getting-started/coding-scenes.md#imports" >}}) for how to handle these easily.
{{< /hint >}}

The `AudioSource.playSound()` function takes the following arguments:

- `entity`: On what entity to apply the sound. The sound will be heard from this entity's position, meaning it gets louder as the player approaches it.
- `src`: The location of the sound file within your project.
  {{< hint info >}}
  **💡 Tip**: For more clarity, we recommend keeping your sound files separate in a `assets/sounds` folder inside your scene.
  {{< /hint >}}
- `resetCursor`: _(optional)_ If true, the sound always starts from the beginning. Otherwise it continues from the current cursor position. Useful for pausing and resuming.

Another way to play sounds is to manually create an `AudioSource` component on an entity. Use this approach to have more control over the sound, for example to make it loop or set the volume.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/sound-effect.mp3',
	loop: true,
	playing: true,
})
```

The following properties can be set:

- `audioClipUrl`: The location of the sound file within your project.
- `playing`: If true, the sound starts playing. You can create a sound with `playing` set to false, and then set it to true at a later time.
- `volume`: _(optional)_ The volume of the sound file. 1 by default, which is full volume.
- `pitch`: _(optional)_ Modify the pitch of a sound. 1 is the default, make it lower for a deeper sound and higher for a higher pitch sound.
  {{< hint info >}}
  **💡 Tip**: To prevent a sound effect from becoming too repetitive during a game, it's useful to randomize some slight variations to the sound's pitch every time it plays.
  {{< /hint >}}
- `currentTime`: _(optional)_ The current playback time of the sound file, in seconds. 0 by default. Set this value to avoid starting from the beginning of the sound file. You can also query this value at any time to check the sound's progress.

Each entity can only have a single `AudioSource` component, that can only play a single clip at a time. This limitation can be easily overcome by modifying the audio source at the time of playing a new sound, or by including multiple invisible child entities, each with their own sound.

{{< hint warning >}}
**📔 Note**: Sounds are played on each player's local instance. Other nearby players won't hear the same sounds unless their local scene explicitly plays them too.
{{< /hint >}}

## Stopping sounds

To stop an entity from playing its sound, use the `AudioSource.stopSound()` function. You only need to specify the entity, since each entity has a single `AudioSource` component, and each `AudioSource` component plays a single file at a time.

```ts
AudioSource.stopSound(sourceEntity)
```

Another way to stop a sound is to set the `playing` property to false.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/explosion.mp3',
	playing: true,
})

// Define a simple function
function stopSound(entity: Entity) {
	// fetch mutable version of audio source component
	const audioSource = AudioSource.getMutable(entity)

	// modify its playing value
	audioSource.playing = false
}

// call function
stopSound(sourceEntity)
```

## Looping

To keep a sound playing in a continuous loop, set the `loop` field of the `AudioSource` component to _true_ before you start playing it.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/sound-effect.mp3',
	playing: true,
	loop: true,
})
```

Looping sounds is especially useful for adding background music or other background sounds.

## Set volume

You can set the `volume` property of the `AudioSource` component to change the volume of a sound.

The volume is expressed as a number from _0_ to _1_.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/sound-effect.mp3',
	playing: true,
	volume: 0.5,
})
```

{{< hint warning >}}
**📔 Note**: Of course, the volume of a sound is also affected by the distance of the player from the audio source. As the player walks away, the volume will be lower.
{{< /hint >}}

## Global sounds

By default, all sounds from an `AudioSource` are positional. This means they appear to generate from the position of the `Transform` component, and will sound louder as the player walks closer. But you can also configure a sound to be global, so that the volume is constant, no matter where the player is standing. This is ideal for using on background music, notification sounds, and other non-positional sound.

{{< hint warning >}}
**📔 Note**: Global Sounds are a feature that's only supported in the DCL 2.0 desktop client.
{{< /hint >}}

To make a sound global, set the `global` property to _true_.

```ts
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/music.mp3',
	playing: true,
	global: true,
})
```

## Play a segment of a sound

To play a segment of a longer sound file, use the `playSoundSegment()` in the SDK Utils library. See [SDK7 Utils](https://github.com/decentraland/sdk7-utils).

You can also achieve this by explicitly set the `currentTime` property on an `AudioSource` component, and then stopping it after waiting for a period of time.

## Audio streaming

See [Audio streaming]({{< ref "/content/creator/sdk7/media/audio-streaming.md" >}}) to learn how you can play a live audio stream from an external source.

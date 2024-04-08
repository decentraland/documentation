---
date: 2018-02-10
title: Sounds
description: Learn how to add sounds to your scene.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/sounds/
url: /creator/development-guide/sounds
weight: 4
---

{{< hint warning >}}
**📔 Note**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}).
{{< /hint >}}

Sound is a great way to provide feedback to player actions and events, background sounds can also give your scene more context and improve the player's immersion into it.

{{< hint warning >}}
**📔 Note**: Keep in mind that sounds are only heard by players who are standing within the parcels that make up the scene where the sound was generated, even if they would otherwise be in hearing range. Players can also chose to turn off all sounds on their settings.
{{< /hint >}}

Supported sound formats vary depending on the browser, but it's recommended to use _.mp3_.

_.wav_ files are also supported but not generally recommended as they are significantly larger.

## Play sounds

To play a sound, you need the following:

- An `Entity` to use for the sound location.
- An `AudioSource` component, added to that entity.
- An `AudioClip` object, referenced by that component.

```ts
// Create entity
const cube = new Entity()

// Create AudioClip object, holding audio file
const clip = new AudioClip('sounds/carnivalrides.mp3')

// Create AudioSource component, referencing `clip`
const source = new AudioSource(clip)

// Add AudioSource component to entity
cube.addComponent(source)

// Play sound
source.playing = true
```

When creating an `AudioClip` object, you need to provide the path to the location of the sound file.

The sound file must be inside the project folder. In the example above, the audio file is located in a `sounds` folder, which is located at root level of the scene project folder.

{{< hint info >}}
**💡 Tip**: We recommend keeping your sound files separate in a `/sounds` folder inside your scene.
{{< /hint >}}

Each entity can only have a single `AudioSource` component, that can only have a single `AudioClip`. This limitation can be easily overcome by including multiple invisible entities, each with their own sound.

If you set the `playing` property of an `AudioSource` component to _false_, the file is stopped. This means that if you later set `playing` to _true_ again, the sound file will begin from the start again.

{{< hint warning >}}
**📔 Note**: Sounds are played on each player's local instance. Other nearby players won't hear the same sounds unless their local scene explicitly plays them too.
{{< /hint >}}

## Looping

To keep a sound playing in a continuous loop, set the `loop` field of the `AudioSource` component to _true_ before you start playing it.

```ts
source.loop = true
source.playing = true
```

Looping sounds is especially useful for adding background music or other background sounds.

You can use the `playOnce()` function to play a sound once from start to finish.

```ts
source.playOnce()
```

## Set volume

You can set the `volume` property of the `AudioSource` component to change the volume of a sound.

The volume can be a number from _0_ to _1_.

```ts
source.volume = 0.5
```

{{< hint warning >}}
**📔 Note**: Of course, the volume of a sound is also affected by the distance from the audio source.
{{< /hint >}}

## Reuse sound objects

A great way to save processing power is to use a same `AudioClip` object on many `AudioSource` components.

Suppose you have a large amount of balls bouncing around in your scene, and you want to hear a _thump_ sound every time two of them collide. You can add an `AudioSource` component to each ball, and use a single `AudioClip` object on all of these.

<!--
```ts
```
-->

## Audio streaming

See [Audio streaming]({{< ref "/content/creator/scenes/media/audio-streaming.md" >}}) to learn how you can play a live audio stream from an external source.

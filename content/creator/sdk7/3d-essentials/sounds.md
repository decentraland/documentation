---
date: 2018-02-10
title: Sounds
description: Learn how to add sounds to your scene.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/sounds/
url: /creator/development-guide/sounds/
weight: 4
---

Sound is a great way to provide feedback to player actions and events, background sounds can also give your scene more context and improve the player's immersion into it.

> Note: Keep in mind that sounds are only heard by players who are standing within the parcels that make up the scene where the sound was generated, even if they would otherwise be in hearing range. Players can also chose to turn off all sounds on their settings.

Supported sound formats vary depending on the browser, but it's recommended to use _.mp3_.

_.wav_ files are also supported but not generally recommended as they are significantly heavier.

## Play sounds

To play a sound, you need to add an `AudioSource` component to an entity.

```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
	audioClipUrl: 'sounds/sound-effect.mp3',
	loop: true,
	playing: true
})

```


When creating an `AudioSource` component, you need to provide the path to the location of the sound file in the `audioClipUrl` field.

The sound file must be inside the project folder. In the example above, the audio file is located in a `sounds` folder, which is located at root level of the scene project folder.

> Tip: For more clarity, we recommend keeping your sound files separate in a `/sounds` folder inside your scene.

Each entity can only have a single `AudioSource` component, that can only play a single clip at a time. This limitation can be easily overcome by modifying the audio source at the time of playing a new sound, or by including multiple invisible child entities, each with their own sound.

## Playing and stopping

To make an `AudioSource` play its file, set the `playing` property to true.


```ts
// Create entity
const sourceEntity = engine.addEntity()

// Create AudioSource component
AudioSource.create(sourceEntity, {
    audioClipUrl: 'sounds/explosion.mp3',
    playing: false
})

// Define a simple function
function playSound(entity: Entity){

    // fetch mutable version of audio source component
    const audioSource = AudioSource.getMutable(entity)
    
    // modify its playing value
    audioSource.playing = true
}

// call function
playSound(sourceEntity)
```

If you set the `playing` property of an `AudioSource` component to _false_, the file is stopped. This means that if you later set `playing` to _true_ again, the sound file will begin from the start again.

> Note: Sounds are played on each player's local instance. Other nearby players won't hear the same sounds unless their local scene explicitly plays them too.

## Looping

To keep a sound playing in a continuous loop, set the `loop` field of the `AudioSource` component to _true_ before you start playing it.

```ts
const audioSource = AudioSource.getMutable(entity)

audioSource.loop = true
audioSource.playing = true
```

Looping sounds is especially useful for adding background music or other background sounds.

## Set volume

You can set the `volume` property of the `AudioSource` component to change the volume of a sound.

The volume is expressed as a number from _0_ to _1_.

```ts
const audioSource = AudioSource.getMutable(entity)

source.volume = 0.5
```

> Note: Of course, the volume of a sound is also affected by the distance of the player from the audio source. As the player walks away, the volume will be lower.


## Audio streaming

See [Audio streaming]({{< ref "/content/creator/sdk7/media/audio-streaming.md" >}}) to learn how you can play a live audio stream from an external source.
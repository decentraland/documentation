---
date: 2023-09-19
title: Smart Items
description: Using smart items in your scene to add interactivity.
categories:
  - web-editor
type: Document
url: /creator/smart-items
weight: 2
---

Some of the items in the catalog of the Decentraland Editor are **Smart Items**. Players can interact with these, they have configurable properties, and they can trigger actions on other smart items. For example: doors that can be opened and closed, platforms that move up and down, or buttons and levers that can activate other items.

You can recognize these items because they have a lightning icon and a different colored background.

<img src="/images/editor/smart-items.jpg" width="300"/>

{{< hint info >}}
**📔 Note**:
Smart items are available on both the web editor, and the desktop VS Studio Code extension. See [using smart items on VS Studio](#using-smart-items-on-vs-studio) if you encounter issues.
{{< /hint >}}

## Using items

To use a smart item, drag it into the scene like any other item. All items include a default behavior, run a scene preview try it out.

Here are some common items and their default behaviors:

- **Doors**: Doors are opened or closed when clicked. You can change this behavior so they're opened by buttons, trigger areas, etc.
- **Buttons**: When clicked, they play sound and an animation as feedback. Add more actions to their trigger events to activate other smart items.
- **Levers**: When clicked, they switch between two states. Make each position of the lever perform different actions on other smart items.
- **Chests**: They behave like doors, by default are opened or closed when clicking. You can place smaller items inside them.
- **Platforms**: They move between two positions. Use their tween actions to control where they move to, their speed, etc.
- **Trigger area**: An [invisible item](#invisible-items) that can trigger other smart items when the player walks into its area. See [About trigger areas](#about-trigger-areas).
- **Video Player**: A screen for showing videos or live streams. See [Playing Videos](#playing-videos).
- **Audio Stream**: Play audio from a live stream. See [Playing Audio Streams](#playing-audio-streams)
- **NFT**: Display an NFT image as a portrait. See [Displaying NFTs](#displaying-nfts)

All smart items can be configured to behave in custom ways. For example, change what sounds a door plays when opened, how far a platform moves, etc.

## Configure an item

Select an item in the Editor to view all of its properties on the right. Properties are grouped into [**components**]({{< ref "/content/creator/sdk7/architecture/entities-components.md" >}}). Different smart items may have different components, depending on their functionality.

The behavior of most items is controlled by:

- [**Actions**](#actions): The Actions component defines things that the item can do. For example play a sound, play an animation, move up, or become invisible.
- [**Triggers**](#triggers): The Triggers component assigns what events make those actions happen. For example when the player clicks on the item, when the player walks into an area, or when the scene first loads.

For example, in a door smart item, the **Actions** component includes "Open" and "Close" actions. The **Triggers** component in that item includes an **On Click** trigger that activates the "Open" action when the door is clicked by the player.

The triggers of a smart item can activate actions on any smart item in the scene, not just on that same smart item. For example, a button smart item can have a **Triggers** component that activates the "move up" action defined on the **Actions** component of a floating platform.

Triggers can also happen conditionally. For example, door smart items include two **On Click** triggers in its Triggers component: one opens the door if that door was closed, the other closes the door if it was open. For more details see [States and conditional logic](#states-and-conditional-logic).

## Interactions between items

To make items interact with each other:

- One item needs to have at least one action defined in an [Actions](#actions) component.
- The other item needs a trigger in the [Triggers](#triggers) component that points to that action.

For example, to make a button open a door:

1. Add any button smart item, open its **Triggers** component. It has a default trigger event that plays a sound and an animation for the button itself.
2. Click the **+** sign next to **Assigned Actions**, to add a third action on that same trigger event.
3. Select the smart item for the door on the first dropdown.
4. On the second dropdown, select the "Open" action.

<img src="/images/editor/button-to-door.png" width="300"/>

{{< hint info >}}
**💡 Tip**: You can instead create a new Trigger event that only handles the door's action. Both trigger events are called every time the button is clicked.

<img src="/images/editor/button-to-door2.png" width="300"/>
{{< /hint >}}

Any item can trigger any action from any other item, as long as the action is defined. See [Triggers](#triggers) for more ways in which an action can be triggered.

You can use [states and conditional logic](#states-and-conditional-logic) to only trigger an action if a condition is met. The condition can even check the state of a third smart item. For example, a button only opens the door if the a custom "power generator" smart item has its state set to "On".

## Actions

The **Actions** component lists actions that the item can carry out. Each smart item includes a set of pre-defined actions. You can customize existing actions or add new ones. The following types of actions are available:

- **Play Animation**: Plays an animation in the 3D model of the item. See [About playing animations](#about-playing-animations)
- **Stop Animation**: Stops all animations being played by the 3D model of the item.
- **Play Sound**: Plays a sound from a file, at the location of the item. See [About playing sounds](#about-playing-sounds)
- **Stop Sound**: Stops all sounds playing from the item.
- **Start Tween**: Makes a gradual change in position, rotation or scale over a given period. See [Moving, rotating or scaling](#moving-rotating-or-scaling).
- **Set Visibility**: Makes the item visible or invisible.
- **Attach To Player**: Sets the item as a child of the player's avatar. For example to carry it on their hand or above their head.
- **Detach From Player**: Detaches the item from the player's avatar.
- **Open Link**: Opens a link to an external website.
  {{< hint info >}}
  **📔 Note**:
  This action can only happen as a result of clicking on an item. It can't be triggered by walking into a trigger area.
  {{< /hint >}}
- **Teleport Player**: Teleport a player to the coordinates of another scene in Decentraland. Players will appear in the spawn-point of the destination scene.
- **Play Emote**: Make the player's avatar perform an animation.
- **Show Text**: Display text on the screen's UI, to be hidden after a few seconds. Ideal hints, dialog lines, notifications, etc.
- **Hide Text**: Hides any UI text that might be currently displayed.
- **Start Delay**: Delays another action of the same item by as many seconds as you need.
- **Stop Delay**: Cancels any delayed actions on the item.
- **Start Loop**: Replays an action from the same item recurrently at a given interval.
- **Stop Loop**: Cancels any looped actions on the item.
- **Play Video Stream**: See [Playing Videos](#playing-videos).
- **Stop Video Stream**: Stop any videos currently played.
- **Play Audio Stream**: [Playing Audio Streams](#playing-audio-streams)
- **Stop Audio Stream**: Stop any audio streams currently playing.

See [states and conditional logic](#states-and-conditional-logic) to learn about other actions related to logic conditions.

The **Actions** component defines possible actions, but these don't do anything in the scene unless they are triggered. Actions are activated by a [trigger](#triggers), either from the same smart item, or from a different one.

To add a new action to an item, click the **Add New Action** button at the bottom of the Action component. Then give the action a name, select a type, and complete any additional fields specific to the type of action.

<img src="/images/editor/new-action.png" width="300"/>

## Triggers

The **Triggers** component defines trigger events, these activate actions when a certain event happens. The following types of trigger events exist:

- **On Click**: When the player clicks on the item. See [About click triggers](#about-click-triggers)
- **Player Enters Area**: When the player enters an area. See [About trigger areas](#about-trigger-areas)
- **Player Leaves Area**: When the player leaves an area. See [About trigger areas](#about-trigger-areas)
- **On Spawn**: When the scene starts, or the item is spawned in the scene. See [Trigger on spawn](#trigger-on-spawn)

See [states and conditional logic](#states-and-conditional-logic) to learn about other triggers related to logic conditions.

To add a new trigger, click the **Add New Trigger Event** at the bottom of the Trigger component. Then select the type of trigger, the entity you want to activate and an action from that entity.

<img src="/images/editor/new-trigger.png" width="300"/>

{{< hint info >}}
**📔 Note**:
An action needs to be defined in the [Actions](#actions) component of the entity before you can trigger it. Triggers can only affect entities that have an Actions component.
{{< /hint >}}

## About Playing Animations

Use an action of type **Play Animation** to run an animation on the 3D model of the smart item. The animation needs to already exist as part of the 3D model file. The **Select Animation** dropdown displays a list of all of the available animations in the 3D mode.

The **Play Mode** field lets you select if an animation should play just once, or if it should keep looping.

<img src="/images/editor/play-animation.png" width="300"/>

Once the action is created, you can activate it via the [Triggers](#triggers) component of that same item or of any other item.

Use the **Stop Animation** action to stop all animations by the item, both looping and non-looping.

{{< hint info >}}
**💡 Tip**: To easily check the contents of a 3D model, to see what animations it includes and what they look like, a good tool is the [Babylon Sandbox](https://sandbox.babylonjs.com/). Just drag the 3D model file into the window. A dropdown with a list of its animations should appear on the bottom.
{{< /hint >}}

To learn more about animations and how you can create your own as part of a 3D model, see [Animations]({{< ref "/content/creator/3d-modeling/animations.md" >}}).

## About Playing sounds

Use an action of type **Play Sound** to play a sound file. You can play any sound file as long as it's imported into the scene project. The sound is heard positionally, from the location of the item, meaning they sound louder if the player is closer.

{{< hint info >}}
**💡 Tip**: Instead of typing in the path to the sound file, you can drag it into the **Path** field from the file navigation menu on the bottom of the editor.
{{< /hint >}}

Use the **Play Mode** field to chose if playing the sound once, or looping it continuously.

<img src="/images/editor/play-sound.png" width="300"/>

Once the action is created, you can activate it via the [Triggers](#triggers) component of that same item or of any other item.

Use the **Stop Sound** action to stop all sounds by the item, both looping and non-looping. This also stops sounds from the **AudioSource** component.

To make an item play a looping sound always, for example for ambience or music, it's easier to use the **AudioSource** component, instead of using Actions and Triggers. This component only requires that you provide a path to a file, and check the boxes **Start Playing** and **Loop**.

<img src="/images/editor/audiosource.png" width="300"/>

{{< hint info >}}
**📔 Note**:
A smart item can only play one sound at a time. Calling a second sound will interrupt any other sounds currently sounding. This also applies to sounds of the **AudioSource** component.
If you need two sounds to sound together, consider adding an invisible entity in the same location to hold a **Play Sound** action.
{{< /hint >}}

See [sounds]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}) for more about playing sounds in Decentraland.

## Moving, rotating, or scaling

Use a **Start Tween** action to change the **position**, **scale**, or **rotation**, of the item over a period of time. All **Start Tween** actions start from the original state of the item, and change to an ending state over a period of time.

Tweens in position can be relative or absolute. An absolute tween in position moves the item to a fixed position in relation to the scene. The item will move from wherever it is to that position. If it's already there, it won't appear to move. A relative tween in position moves the item a certain distance from where it is now, for example a tween to a relative position of `1, 0, 0` moves the item 1 meter forward, in the direction it's currently facing. If you run the tween action a second time, the item will move another meter forward.

Tweens in rotation can also be relative or absolute. A relative rotation is added to the item's current rotation. An absolute tween in rotation will make the item face a specific direction, relative to the scene.

Use the **Duration** field to set how long the whole movement should take, in seconds. Note that the slider goes up to 100 seconds, but you can also write a larger number manually if you need to.

<img src="/images/editor/tweens.png" width="300"/>

Once the action is created, you can activate it via the [Triggers](#triggers) component of that same item or of any other item.

Tweens can follow different **Curve Types** that affect the rate of change over time. A **linear** curve (default), means that the speed of the change is constant from start to finish. There are plenty of options to chose, that draw differently shaped curves depending on if the beginning and/or end start slow, and how much. An **easeinexpo** curve starts slow and ends fast, increasing speed exponentially, on the contrary an **easeoutexpo** curve starts fast and ends slow.

<img src="/images/editor/easing-functions.jpeg" width="600"/>

{{< hint info >}}
**💡 Tip**: Experiment with different movement curves. The differences are often subtle, but we subconsciously interpret information from how things move, like weight, friction, or even personality.
{{< /hint >}}

Use **On Tween End** trigger events in the **Triggers** component to activate an action after a tween has finished. Use [states and conditional logic](#states-and-conditional-logic) to describe a looping path for a floating platform, so that it constantly moves between two locations.

When an item performs a tween, this affects everything about the item. For example, if it changes scale, it changes the scale of its visible 3D model and also invisible collider geometry, the size of text, etc. If the item has any children (nested in the entity tree on the left), these child entities are also affected by the tween.

{{< hint info >}}
**📔 Note**:
Each entity can only perform one tween at a time. For example, you can´t make an item move sideways and also rotate at the same time. As a workaround, you can use parented entities. For example, you can have an invisible parent entity that moves sideways, with a visible child that rotates.
{{< /hint >}}

## About click triggers

To trigger an action by clicking on an item, create an **On Click** trigger. The action will be activated every time that the player clicks on the entity.

<img src="/images/editor/on_click.png" width="300"/>

{{< hint info >}}
**📔 Note**:
When using custom 3D models, the model must have an invisible collider geometry for it to be clickable. See [colliders]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#pointer-blocking" >}}).

As an alternative, you can configure the **GLTF** component of the item, so that its **Visible Layer** of collision is set to **Pointer**.

Another alternative is to add a **Click Area** smart item, to draw a cube that overlaps the item you want to click. The Click Area smart item is an [invisible item](#invisible-items).
{{< /hint >}}

## About Trigger areas

To trigger an action when the player walks into or out of an area, use the Trigger Area smart item. The is is an [invisible item](#invisible-items), the orange cube is only visible in the editor, it becomes invisible when running a preview of the scene. You can easily adjust and scale the orange cube to cover exactly the area you need.

<img src="/images/editor/trigger.png" width="150"/>

Use the **On Player Enters Area** and **On Player Leaves Area** trigger types on the item's **Triggers** components. The actions on these trigger events are activated every time that the player enters or leaves the area.

<img src="/images/editor/on_player_enters.png" width="300"/>

{{< hint info >}}
**📔 Note**:
You can also use **On Player Enters Area** and **On Player Leaves Area** trigger events on any other smart item, but keep in mind that it can be challenging to know the area covered by the trigger.

The size of the triggerable area doesn't relate to the item's visible shape or its colliders, it's always a cube of 1m on each side, affected by the scale of the item.
{{< /hint >}}

## Trigger on spawn

Triggers of type **On Spawn** activate an action when the scene is loaded. Instead of waiting for the player to interact with an item, the action runs right away.

For example, use this to make a platform move continually. Use an **On Spawn** trigger to activate a tween action. Then use **On State Change** triggers to keep it moving between two or more positions.

<img src="/images/editor/on_spawn.png" width="300"/>

## Playing videos

Play videos from either:

- **Local files**: Upload a video file as part of the scene, then point the _URL_ field to the path to that file.
- **Stream from a URL**: Point to a live or pre-recorded stream on the web, for example from Vimeo.
  {{< hint info >}}
  **📔 Note**:
  You can't stream a video from YouTube or similar sites, as these only allow displaying their content in their branded HTML widget. See See [About External Streaming]({{< ref "/content/creator/sdk7/media/video-playing.md#about-external-streaming" >}}) for options and tips.
  {{< /hint >}}
- **Stream live from DCL Cast**: This simplified service lets you easily set up a live stream as a scene owner. See [Decentraland Cast]({{< ref "/creator/worlds/cast.md">}}).

There are two options for when to play a video:

- Configure the **Video Player** component of the item directly. This makes the video start playing as soon as the scene loads.
  <img src="/images/editor/video-from-start.png" width="300"/>
- Define an Action of type **Play Video Stream**. This lets you trigger the playing of the video as the result of a player interaction, like walking into a room, or pushing a button.
  <img src="/images/editor/video-from-action.png" width="300"/>

You can configure the volume of the video's sounds. Note that the audio from the stream is not positional, it is heard at an even volume through all your scene.

You can also configure the video to either loop or play once.

{{< hint warning >}}
**📔 Note**: Avoid playing more than one video at any given time in your scene, because it can severely impact performance for players. Always stop other videos before playing a second video.
{{< /hint >}}

## Playing audio streams

Play an audio stream from a URL.

{{< hint info >}}
**📔 Note**:
Not all streaming services allow you to play their audio outside their site. The following are some examples that work in Decentraland:

```ts
RAVE = ‘https://icecast.ravepartyradio.org/ravepartyradio-192.mp3’
DELTA = ‘https://cdn.instream.audio/:9069/stream?_=171cd6c2b6e’
GRAFFITI = ‘https://n07.radiojar.com/2qm1fc5kb.m4a?1617129761=&rj-tok=AAABeIR7VqwAilDFeUM39SDjmw&rj-ttl=5’
SIGNS = ‘https://edge.singsingmusic.net/MC2.mp3’
JAZZ = ‘https://live.vegascity.fm/radio/8010/the_flamingos.mp3’
```

{{< /hint >}}

You can adjust the volume of your stream. Note that the audio from the stream is not positional, it is heard at an even volume through all your scene.

## Displaying NFTs

To display an NFT on Ethereum mainnet on a picture frame, you must configure the **NFTShape** component. You must provide the following fields:

- Network
  {{< hint info >}}
  **📔 Note**:
  Currently **ethereum** is the only supported network.
  {{< /hint >}}
- Contract: The smart contract for the NFT collection.
- Token: The token ID of this particular NFT collectible.

<img src="/images/editor/nft-shape.png" width="300"/>

You can obtain this information from [OpenSea](https://opensea.io), by checking the **Details** tab under the NFT image.

<img src="/images/editor/opensea.png" width="300"/>

{{< hint info >}}
**📔 Note**:
You can also obtain this information from the opensea URL. For example, if the NFT's URL is the following:

> `https://opensea.io/assets/ethereum/0x32b7495895264ac9d0b12d32afd435453458b1c6/1956`

You can complete the fields with the following:

- Network: ethereum
- Contract: 0x32b7495895264ac9d0b12d32afd435453458b1c6
- Token: 1956
  {{< /hint >}}

You can also configure a background color, this is particularly useful for NFTs with a transparent background.

You can also chose a **Frame style**, to frame the NFT in a variety of different styles, classic and modern.

See [Display an NFT]({{< ref "/content/creator/sdk7/media/display-a-certified-nft.md#">}}) for more details.

## Invisible items

Some items are not meant to be seen by the player, but are visible while editing your scene to make them easier to manage. This is the case for items like **Ambience**, **Trigger Area**, **Click Area**, etc.

These items have a **Visibility** component set to invisible. This component doesn't affect the visibility of the items on the editor, but any item set to invisible isn't seen by players when running a preview.

## Multiplayer

All smart items are multiplayer by default. This means that if multiple players are in the scene, the changes that one player does are seen by all other players. For example, if one player opens a door, all other players see it open too.

Note that the state of the item is only kept as long as there are players in the scene. If all players go away, the door will revert back to its default closed state.

By default, all items share their updates on only the components that are relevant to their normal behavior. You can change this list by looking for the item's **Multiplayer** component and checking the boxes for the components you want to share.

For example, a door shares its `Animator` so all see the opening animations, its `AudioSource` so all hear its sound, and its `State` so all keep track of if it's currently open or closed. The door doesn't share its `Visibility` component, because the door is usually always visible. If you include actions to trigger its visibility on and off, you might want to have this component ticked too, so that changes are synced between all players.

## Making any item smart

Smart items are just regular items with an **Action** and/or **Trigger** component. You can add these components to any item in your scene. You can also import your own custom 3D models and add the same to those.

To add components to an item click the **Plus Icon** next to the item name, and select what component to add from the dropdown list.

<img src="/images/editor/add-component.png" width="300"/>

This allows for a huge amount of creative possibilities. Turn a candle into a lever that opens up a secret passage behind a book shelf, play mysterious sounds from inside a well, make diamonds into collectable items that shrink to 0 when clicked. There are tons of imaginative ways to combine these mechanics!

{{< hint info >}}
**💡 Tip**: When a player interacts with an item, you should show some kind of feedback to make that interaction clear. If the model doesn't have any animations, consider at least playing a sound. In some cases it might work to make the item do a slight tween in scale and then return to its original scale, as a form of feedback.
{{< /hint >}}

## States and conditional logic

Add conditions on a trigger, so that the action only occurs if those conditions are met. For example, clicking on a door only activates the "Open" action if it wasn't already open.

To add a condition, click the three dots icon next to **Trigger event** and select **Add Trigger Condition**.

A single trigger can include multiple conditions. Click the **+** icon to add more conditions. When more than one condition exist, you can select one of these options:

- **All Conditions should be met (AND)**: The trigger only happens if every one of the conditions is true.
- **Any Condition can be met (OR)** The trigger happens if at least one of the conditions is true.

### States

The **States** component is included on several smart items. It lists possible states that the smart item can be in. At any given time, the smart item is in one of these states. For example, a door can be _Open_ or _Closed_. The Open action sets the state to _Open_, the Close action sets the state to _Closed_.

You can do the following things with states:

1. Use a condition on a trigger to check the state of an entity. In that way the action is only carried out if a specific state is active.

<img src="/images/editor/condition.png" width="300"/>

2. Change a state via the **Set State** action.

<img src="/images/editor/set-state.png" width="300"/>

3. React to changes in state via the **On State Change** trigger event.

To toggle between two actions, define two triggers, each with a condition that checks a state. For example, doors have one trigger that activates the Open action, with a condition that first checks that the door's state is _Closed_, and another trigger that activates the Close action, with a condition that checks that the door's state is _Open_. Only one of the two is activated each time the player clicks on the door.

<img src="/images/editor/door_conditions.png" width="300"/>

You can add as many states as you want to a smart item. Just click the **Add New State** button to add another one to the list.

<img src="/images/editor/new_state.png" width="300"/>

One of the states is selected as the default, the item will always start in this state when the scene runs. You can assign a different state to be the default by clicking the three dots next to another one of the states and selecting **Set as Default**.

{{< hint info >}}
**💡 Tip**: Keep interactions between items simple. For example, avoid scenarios like having a button that opens a door by triggering three actions: play the door's animation, play the door's sound and change the door's state. Instead, make the button change the door's state. Then use an **On State Change** trigger so that the door itself handles playing the animation and sound whenever the state changes.
{{< /hint >}}

### Counter

Use the **Counter** component to keep track of a number, which can change as the player performs actions in the scene. You can use the values of the counter in conditional logic.

When an entity has a Counter component, you can run the following actions on it:

- **Increment Counter**: Increment the value of the counter by 1.
- **Decrease Counter**: Decrease the value of the counter by 1.
- **Set Counter**: Set the value of the counter to a specific number, for example to set it back to 0.

Use the **On Counter Change** trigger to perform an action every time the counter's value changes. Add a condition to this trigger so that it only activates after passing a certain threshold.

<img src="/images/editor/on_counter_change.png" width="300"/>

On a condition, you can check if the value of the counter is

- Greater than a given value
- Lower than a given value
- Equal to a given value

{{< hint info >}}
**💡 Tip**: To check for greater or equal, you can add two conditions to the trigger event, using the AND option.

To make an action occur only once when passing a threshold, and not repeat on every increment after that, combine the counter with a **State** component. Set the State to "Done" whenever you reach the desired value, and add a condition to check this state on the trigger event.
{{< /hint >}}

## Using smart items on VS Studio

Smart items work out of the box on the [Web Editor]({{< ref "/content/creator/sdk7/web-editor/web-editor.md" >}}). They also work out of the box with fresh new scenes in the Desktop [Decentraland Editor]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}).

If using smart items on an older scene in the Desktop Decentraland Editor, or a scene built based on an older example, you may need to do the following adjustments:

1. Install the library `@dcl/asset-packs`. See [Manage Dependencies]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md" >}}) for how to install libraries in a project.

2. Paste the following lines on your scene's `index.ts` file:

```ts
import { initAssetPacks } from '@dcl/asset-packs/dist/scene-entrypoint'

// You can remove this if you don't use any asset packs
initAssetPacks(engine, pointerEventsSystem, {
	Animator,
	AudioSource,
	AvatarAttach,
	Transform,
	VisibilityComponent,
	GltfContainer,
	Material,
	VideoPlayer,
  	UiTransform,
  	UiText,
  	UiBackground
})
```

{{< hint warning >}}
**📔 Note**: The smart items asset pack is not displayed at all on scenes that don't have this dependency installed.
{{< /hint >}}

When using the desktop editor, you can combine smart items with behavior from custom code. See [Combine with code]({{< ref "/content/creator/sdk7/web-editor/combine-with-code.md" >}}).

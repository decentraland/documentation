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

Some of the items in the catalog of the Decentraland Editor are **Smart Items**. Players can interact with these,they also have configurable properties, and they can trigger actions on other smart items. For example, you can find doors that can be opened and closed, platforms that move up and down, or buttons and levers that can activate other items.

You can recognize these items because they have a lightning icon and a different colored background.

<!--<screenshot>-->

## Using items

To use a smart item, simply drag it into your scene. Run a preview of your scene to interact with the item in its default way.

You can configure smart items to behave in custom ways. For example you can change what sounds a door plays when opened, how far a platform moves, etc. Select an item in the Editor to view all of its properties on the right.

Some items you can find include:

- **Doors**: By default doors are opened or closed when clicked. You can change this behavior to be triggered by buttons, trigger areas, etc.
- **Buttons**: When clicked, they play sound and an animation as feedback. Add triggers to make them activate other smart items.
- **Levers**: When clicked, they switch between two states. Make each position of the lever perform different triggers on other smart items.
- **Chests**: Behave similar to doors, by default are opened or closed. You can place smaller items inside them.
- **Platforms**: Move between two positions. Use their tween actions to control where they move to, their speed, etc.
- **Trigger area**: This is an invisible item that can trigger other smart items when the player walks into its area.

## Configure an item

When a smart item is selected, note that there are several fields, grouped into **components** on the right panel. Different smart items may have different components, depending on their functionality.

The behavior of most items is controlled by the **Actions** and **Triggers** components. Actions are things that the item can do, for example play a sound, play an animation, move up, or become invisible. Triggers define what events make those actions happen, for example when the player clicks on the item, or walks into an area.

For example, in a door smart item, the **Actions** component includes "open" and "close" actions. The **Triggers** component in that item includes an "on_click" trigger that activates the "open" action when the door is clicked by the player.

The **Triggers** component of a smart item can activate actions on any smart item in the scene, not just on that same smart item. For example, a button smart item can have a **Triggers** component that activates the "move up" action on a floating platform.

Triggers can also happen conditionally. For example, door smart items include two on_click triggers in its Triggers component: one opens the door if that door was closed, the other closes the door if it was open. For more details see [States and conditional logic](#states-and-conditional-logic).

## Actions

The **Actions** component lists actions that the item can carry out. Each smart item includes a set of pre-defined actions. You can customize existing actions or add new ones. The following types of actions are available:

- **play_animation**: Plays an animation in the 3D model of the item. See [About playing animations](#about-playing-animations)
- **stop_animation**: Stops all animations being played by the 3D model of the item.
- **play_sound**: Plays a sound from a file, at the location of the item. See [About playing sounds](#about-playing-sounds)
- **stop_sound**: Stops all sounds playing from the item.
- **start_tween**: Makes a gradual change in position, rotation or scale over a given period. See [Moving, rotating or scaling](#moving-rotating-or-scaling).
- **change_visibility**: Makes the item visible or invisible.
- **attach_to_player**: Sets the item as a child of the player's avatar. For example to carry it on their hand or above their head.
- **detach_from_player**: Detaches the item from the player's avatar.

See [states and conditional logic](#states-and-conditional-logic) to learn about other actions related to logic conditions.

The **Actions** component defines possible actions, but these don't do anything in the scene unless they are triggered. Actions are activated by a [trigger](#triggers), either from the same smart item, or from a different one.

To add a new action to an item, click the **Add New Action** button at the bottom of the Action component. Then give the action a name, select a type, and complete any additional fields specific to the type of action.

<img src="/images/editor/new-action.png" width="300"/>

## Triggers

The **Triggers** component defines triggers, these activate actions when a certain thing happens. The following types of triggers exist:

- **on_click**: When the player clicks on the item. See [About click triggers](#about-click-triggers)
- **on_player_enters_area**: When the player enters an area. See [About trigger areas](#about-trigger-areas)
- **on_player_leaves_area**: When the player leaves an area. See [About trigger areas](#about-trigger-areas)
- **on_spawn**: When the scene starts, or the item is spawned in the scene. See [Trigger on spawn](#trigger-on-spawn)

See [states and conditional logic](#states-and-conditional-logic) to learn about other triggers related to logic conditions.

To add a new trigger, click the **Add New Trigger Event** at the bottom of the Trigger component. Then select the type of trigger, the entity you want to activate and an action from that entity.

<img src="/images/editor/new-trigger.png" width="300"/>

{{< hint info >}}
**📔 Note**:
An action needs to be defined in the Actions component of the entity before you can trigger it. Triggers can only affect entities that have an Actions component.
{{< /hint >}}

## About Playing Animations

Use an action of type **play_animation** to run an animation on the 3D model of the smart item. The animation needs to already exist as part of the 3D model file. The **Select Animation** dropdown displays a list of all of the available animations in the 3D mode.

The **Play Mode** field lets you select if an animation should play just once, or if it should keep looping.

<img src="/images/editor/play-animation.png" width="300"/>

Use the **stop_animation** action to stop all animations by the item, both looping and non-looping.

To learn more about animations and how you can create your own as part of a 3D model, see [Animations]({{< ref "/content/creator/3d-modeling/animations.md" >}}).

## About Playing sounds

Use an actions of type **play_sound** to play a sound file. You can play any sound file as long as it's imported into the scene project. The sound is heard positionally, from the location of the item, meaning they sound louder if the player is closer.

{{< hint info >}}
**💡 Tip**: Instead of typing in the path to the sound file, you can drag it into the **Path** field from the file navigation menu on the bottom of the editor.
{{< /hint >}}

Use the **Play Mode** field to chose if playing the sound once, or looping it continuously.

<img src="/images/editor/play-sound.png" width="300"/>

Use the **stop_sound** action to stop all sounds by the item, both looping and non-looping. This also stops sounds from the **AudioSource** component.

To make an item play a looping sound always, for example for ambience or music, it's easier to use the **AudioSource** component, instead of using Actions and Triggers. This component only requires that you provide a path to a file, and check the boxes **Start Playing** and **Loop**.

<img src="/images/editor/audiosource.png" width="300"/>

{{< hint info >}}
**📔 Note**:
A smart item can only play one sound at a time. Calling a second sound will interrupt any other sounds currently sounding. This also applies to sounds of the **AudioSource** component.
If you need two sounds to sound together, consider adding an invisible entity in the same location to hold a **play_sound** action.
{{< /hint >}}

See [sounds]({{< ref "/content/creator/sdk7/3d-essentials/sounds.md" >}}) for more about playing sounds in Decentraland.

## Moving, rotating, or scaling

Use a **start_tween** action to change the position, scale, or rotation, of the item over a period of time. All **start_tween** actions start from the original state of the item, and change into to an ending state over a period of time.

Tweens in position can be relative or absolute. An absolute tween in position moves the item to a fixed position in relation to the scene. The item will move from wherever it is to that position. If it's already there, it won't appear to move. A relative tween in position moves the item a given amount from where it is now, for example a tween to a relative position of `1, 0, 0` moves the item 1 meter forward, in the direction it's currently facing. If you run the tween action a second time, the item will move another meter forward.

Tweens in rotation can also be relative or absolute. A relative rotation is added to the item's current rotation. An absolute tween in rotation will make the item face a specific direction, relative to the scene.

Use the **Duration** field to set how long the whole movement should take, in seconds. Note that the slider goes up to 100 seconds, but you can also write a larger number manually if you need to.

Tweens can follow different **Curve Types** that affect the rate of change over time. A **linear** curve (default), means that the speed of the change is constant from start to finish. There are plenty of options to chose, that draw differently shaped curves depending on if the beginning and/or end start slow, and how much. An **easeinexpo** curve starts slow and ends fast, increasing speed exponentially, on the contrary an **easeoutexpo** curve starts fast and ends slow.

{{< hint info >}}
**💡 Tip**: Experiment with different movement curves. The differences are often subtle, but we subconsciously interpret information from how things move, like weight, friction, or even personality.
{{< /hint >}}

Use **on_finish_tween** triggers in the **Triggers** component to activate an action after a tween has finished. Use [states and conditional logic](#states-and-conditional-logic) to describe a looping path for a floating platform, so that it constantly moves between two locations.

When an item performs a tween, this affects everything about the item. For example, if it changes scale, it changes the scale of its visible 3D model and also invisible collider geometry, the size of text, etc. If the item has any children (nested in the entity tree on the left), these child entities are also affected by the tween.

{{< hint info >}}
**📔 Note**:
Each entity can only perform one tween at a time. For example, you can´t make an item move sideways and also rotate at the same time. As a workaround, you can use parented entities. For example, you can have an invisible parent entity that moves sideways, with a visible child that rotates.
{{< /hint >}}

## About click triggers

To trigger an action by clicking on an item, create an **on_click** trigger. The action will be activated every time that the player clicks on the entity.

<img src="/images/editor/on_click.png" width="300"/>

{{< hint info >}}
**📔 Note**:
When using custom 3D models, the model must have an invisible collider geometry for it to be clickable. See [colliders]({{< ref "/content/creator/sdk7/3d-essentials/colliders.md#pointer-blocking" >}}).

As an alternative, you can configure the **GLTF** component of the item, so that its **Visible Layer** of collision is set to **Pointer**.
{{< /hint >}}

## About Trigger areas

To trigger an action when the player walks into or out of an area, use the **on_player_enters_area** and **on_player_leaves_area** trigger. The action will be activated every time that the player enters or leaves the area.

<img src="/images/editor/on_player_enters.png" width="300"/>

The triggerable area of an item always is shaped like a cube of 1m on each side, it doesn't relate to the item's visible shape or its colliders. This triggerable shape can be stretched by changing the scale of the item.

{{< hint info >}}
**💡 Tip**: The best way to use trigger areas is through the Trigger Area smart item. This item comes with a visible shape that matches the triggerable area, and that you can easily adjust and scale to cover exactly the area you need. the item is only visible in the editor, it becomes invisible when running a preview of the scene.

<img src="/images/editor/trigger.png" width="150"/>
{{< /hint >}}

## Trigger on spawn

Triggers of type **on_spawn** activate an action when the scene is loaded. Instead of waiting for the player to interact with an item, the action runs right away.

For example, use this to make a platform move continually. Use an on*spawn trigger to activate a tween action. Then use \_on_state_change* triggers to keep it moving between two or more positions.

<img src="/images/editor/on_spawn.png" width="300"/>

## Invisible items

Some items are not meant to be seen by the player, but are visible while editing your scene to make them easier to manage. This is the case for items like **Ambience**, **Trigger Area**, **Click Area**, etc.

These items have a **Visibility** component set to invisible. This component doesn't affect the visibility of the items on the editor, but any item set to invisible isn't seen by players when running a preview.

## Making any item smart

Smart items are just regular items with an **Action** and/or **Trigger** component. You can add these components to any item in your scene. You can also import your own custom 3D models and add the same to those.

This allows for a huge amount of creative possibilities. Turn a candle into a lever that opens up a secret passage behind a book shelf, play mysterious sounds from inside a well, make diamonds into collectable items that shrink to 0 when clicked. There are tons of imaginative ways to combine these mechanics!

{{< hint info >}}
**💡 Tip**: When a player interacts with an item, you should show some kind of feedback to make that interaction clear. If the model doesn't have any animations, consider at least playing a sound. In some cases it might work to make the item do a slight tween in scale and then return to its original scale, as a form of feedback.
{{< /hint >}}

## States and conditional logic

Add conditions on a trigger, so that it only occurs if those conditions are met. For example, clicking on a door only activates the "open" action if it wasn't already open.

To add a condition, click the three dots icon next to **Trigger event** and select **Add Trigger Condition**.

A single trigger can include multiple conditions. Click the **+** icon to add more conditions. When more than one condition exist, you can select one of these options:

- **All Conditions should be met (AND)**: The trigger only happens if every one of the conditions is true.
- **Any Condition can be met (OR)** The trigger happens if at least one of the conditions is true.

### States

The **States** component is present on several smart items. It lists possible states that the smart item can be in. At any given time, the smart item is in one of these states. For example, a door can be "open" or "closed". The Open action sets the state to "open", the Close action sets the state to "closed".

You can do the following things with states:

1. Use a condition on a trigger to check the state of an entity. In that way the action is only carried out if a specific state is active.

<img src="/images/editor/condition.png" width="300"/>

2. Change a state via the **set_state** action.

<img src="/images/editor/set-state.png" width="300"/>

3. React to changes in state via the **on_state_change** trigger.

To toggle between two actions, define two triggers, each with a condition that checks a state. For example, doors have one trigger that activates the Open action, with a condition that first checks that the door's state is "closed", and another trigger that activates the Close action, with a condition that checks that the door's state is "open". Only one of the two is activated each time the player clicks on the door.

<img src="/images/editor/door_conditions.png" width="300"/>

{{< hint info >}}
**💡 Tip**: Keep interactions between items simple. For example, avoid scenarios like having a button that opens a door by triggering three actions: play the door's animation, play the door's sound and change the door's state. Instead, make the button change the door's state. Then use an **on_state_change** trigger so that the door reacts with playing the animation and sound.
{{< /hint >}}

### Counter

Use the **Counter** component to keep track of a number, which can change as the player performs actions in the scene. You can use the values of the counter in conditional logic.

When an entity has a Counter component, you can run the following actions on it:

- **increment_counter**: Increment the value of the counter by 1.
- **decrease_counter**: Decrease the value of the counter by 1.
- **set_counter**: Set the value of the counter to a specific number, for example to set it back to 0.

Use the **on_counter_change** trigger to perform an action every time the counter's value changes. Add a condition to this trigger so that it only activates after passing a certain threshold.

<img src="/images/editor/on_counter_change.png" width="300"/>

## Using smart items on VS Studio

Smart items work out of the box on the [Web Editor]({{< ref "/content/creator/sdk7/web-editor/web-editor.md" >}}).

To use them on the Desktop [Decentraland Editor]({{< ref "/content/creator/sdk7/getting-started/installation-guide.md" >}}), you may need to make a couple of adjustments. New scenes built from a fresh template already include everything necessary, also scenes exported from the Web Editor. Older scenes, or scenes built based on an older example may need the following:

1. Install the library `@dcl/asset-packs`. See [Manage Dependencies]({{< ref "/content/creator/sdk7/libraries/manage-dependencies.md" >}}) for how to install libraries in a project.

2. Paste the following lines on `index.ts`:

```ts
import { createComponents, initComponents } from '@dcl/asset-packs'
import { actionsSystem } from '@dcl/asset-packs/dist/src/actions'
import { triggersSystem } from '@dcl/asset-packs/dist/src/triggers'

// This is only necessary if you are using items from asset packs
createComponents(engine as any)
initComponents(engine as any)
engine.addSystem(actionsSystem)
engine.addSystem(triggersSystem)
```

---
date: 2023-21-09
title: Adding Props and Sounds to your Emotes
description: Guidelines to add props and sounds to the emotes.
categories:
  - emotes
type: Document
aliases:
  - /emotes/props-and-sounds/
url: /creator/emotes/props-and-sounds
weight: 5
---

<img src="/images/wearables-and-emotes/props-and-sound/01-props-and-sound-banner.png" width="900" />

In order to take your Decentraland Emotes to the next level you can add props (3d geometry) and/or sounds to them, doing the emotes much more fun and engaging! In this guideline you will find everything you need to know to export them correctly!

# **The Basics and Limitations**

To start adding the props to your emotes it's important to use the [Decentraland Template File](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/BaseMale_Rig_1.0.blend) which will have the rig for the avatar and also the Ground Reference to keep your work inside the allowed space boundaries.

**Currently, the props animations only work with **Armature/Bones Animations** meaning that _transform animations_ are not allowed.**

The emote with their props must be exported all together in one single _.glb_ file (Avatar_Armature + Props_Armature with its animations).

- No more than 3 MB in total.

- No more than 3k tris for props in total.

- No more than 2 materials and 2 textures for props.

- No more than 62 bones for the prop armature.

- The emote must have one animation for the avatar and one animation for the prop. *Currently multiple animations are not allowed.*

- Both animations (Avatar and Prop) must have the same keyframe length.

- Animations cannot exceed 300 frames or 10 seconds.

- Space boundaries are 4 square meters. Props and particles should stay within the reference cube provided in the Avatar File. For avatar movement, check [Ground Reference and Animation Area](/creator/wearables-and-emotes/emotes/creating-emotes.md#ground-reference-and-animation-area). section.

# **Naming Conventions:**

Naming conventions must be strictly followed for the emotes to work! Otherwise they will not play correctly neither in the builder nor in world.

### Armatures Name Conventions:

**For Avatar:**

`Armature`

**For Props:**

`Armature_Prop`

### Animations Name Conventions:

**For Avatar:**

`AnimationName_Avatar`

- Example: `TennisServe_Avatar`, `GunShoot_Avatar`

**For Props:**

`AnimationName_Prop`

- Example: `TennisServe_Prop`, `GunShoot_Prop`

# **Getting Started**

Before starting you animation, you will have to create a rig for the prop. If you’re not familiar with the process, check [Create a Rig](/creator/3d-modeling/create-a-rig) for more information on how to do it.


Ensure that the prop object and armature have their origins located at the 0,0 location within Blender. Additionally, apply transformations to the prop object and armature, ensuring they are frozen at a scale of 1,1,1. This is crucial to prevent any potential issues with the prop's behavior when being utilized within the world or during animations.

<img src="/images/wearables-and-emotes/props-and-sound/18-freeze-transforms.png" width="600" />

### Making the Prop Follow the Avatar Rig

Some props might have to be attached to certain body parts, like a tennis racket to the hand. That can be done by simply adding a constraint. To do so, in **_Pose Mode_**, select the prop bone (the tennis racket one, for example), press **_CTRL + Shift + C_** on your keyborad and select **_Child of_** or just click on the **_Bone Constraint Properties_** tab and, in the drop down menu, select **_Child of_**.

<img src="/images/wearables-and-emotes/props-and-sound/14-add-constrain.png" width="400" />

_Add a constraint by pressing `Ctrl + Shift + C` on your keyboard._

<img src="/images/wearables-and-emotes/props-and-sound/15-add-constrain-02.png" width="400" />

Then, in **_Target_**, select the avatar armature and in **_Bone_** select the bone you want the prop to follow. To maintain the prop’s original position, click on **_Set Inverse_** once you add the constraint. If the influence is 1, the prop will fully follow the selected bone, if it’s 0, the constraint will be disabled. You can set keyframes on the influence to turn it on and off throughout the animation. To do that, just press I while the cursor is on top of **_Influence_**.

<img src="/images/wearables-and-emotes/props-and-sound/16-target.png" width="600" />

_***Chlid of*** constraint menu. Keyframe the influence to turn it on and off._

{{< hint info >}}
**💡Animation Tip!**
If you use the slide to turn off the Influence, the prop will not maintain its previous position, making it hard to keep the animation fluid. To avoid having to manually fix the position, instead of using the slide, click on the X next to Influence, set a keyframe on it and another one on all the transform attributes. This way the prop will keep the same poistion as when the Influence was on!
{{< /hint >}}

<img src="/images/wearables-and-emotes/props-and-sound/17-influence.gif" width="600" />


## Animation Slots

Belnder 4.4 introduced a new feature: animation slots. According to Blender documentation, “the purpose of slots is to allow an action to store distinct animation data for multiple data-blocks”. In a nutshell, slots make it possible to store the animation of multiple things in the same Action. How does it affect emotes 2.0?

<img src="/images/wearables-and-emotes/props-and-sound/animationslots.png" width="600" />

Blender 4.4 new feature: animation slots.

Even though it’s possible to have both the avatar and prop sharing the same action clip, because of the naming convention and number of animation clips involved in Emotes 2.0, it won’t work. So the pipeline for this would be: 

1. Create an animation clip for the avatar, or rename the one provided (***Starting_Pose***). It already has an animation slot, but feel free to use it (***Avatar_Animation***) or create a new one.
2. Rename the animation clip ***AnimationName_Avatar***
3. Create an animation clip for the prop and rename it ***AnimationName_Prop***
4. Click on ***New*** button to create an animation slot for it (it will receive an automatic name: ***Armature_Prop***)
5. Animate as you would do in previous Blender versions.

<img src="/images/wearables-and-emotes/props-and-sound/animation-slot-prop.gif" width="600" />

Creating and action clip and a slot for the prop animation.

# **NLA Tracks**

In order for all the animations to be exported, the clips should be added to the NLA Tracks. Make sure there’s only one animation clip for the avatar and another one for the prop, **they must have the exact same number of frames.**

{{< hint info >}}
**💡Animation Tip**

Don’t leave the prop visible from the start! To avoid spoiling what’s about to happen and an abrupt transition, start the animation with the prop scaled down to 0.001 and only turn it to 1 when you want it to appear. Remember to scale back down to 0 by the end of the action. This will make the transitions much more fluid and cool!
{{< /hint >}}

In ***Object Mode***, select the avatar armature, got to ***Pose Mode***, select the respective animation clip in the Browse Action menu, click on ***Action*** and then the ***Push Down*** option.

Then, change back to ***Object Mode***, select the prop armature, go to ***Pose mode***, select the respective animation clip in the Browse Action menu, click on ***Action*** and then the ***Push Down*** option.

<img src="/images/wearables-and-emotes/props-and-sound/nla-tracks.gif" width="600" />

Pushing actions down to the NLA tracks.

{{< hint info >}}
**🔥 Optimization Tip**

**Before this step make sure to do a backup of your project.**

If you have different objects for your props you can merge them together in one single mesh. This would help to reduce the draw calls in game making the emote more performant.

<img src="/images/wearables-and-emotes/props-and-sound/03-merge-mesh.png" width="400" />

_Select objects and press `Ctrl+J` to merge them together._

<img src="/images/wearables-and-emotes/props-and-sound/04-merge-mesh-02.png" width="400" />

{{< /hint >}}

To export **be sure to select only both Avatar and Prop Armatures with its animations and the Prop mesh**. Then go to the export glb settings and be sure to export only selected objects and untoggle unnecessary features like _Shapekeys Animation_. Always remember to enable Export Deformation Bones Only, so you don’t end up exporting unnecessary bones, like controls.

<img src="/images/wearables-and-emotes/props-and-sound/05-export-props.png" width="600" />

<img src="/images/wearables-and-emotes/props-and-sound/06-export-settings.png" width="600" />

<img src="/images/wearables-and-emotes/props-and-sound/13-export-deformation-bones.png" width="600" />

_Under *Data>Armature* make sure to toggle **Export Deformation Bones Only**_

{{< hint info >}}
**💡 Attention!**
You should **NOT** export the avatar mesh into the .glb.
{{< /hint >}}

# **Add Audio to the Emotes**

## Format and Limitations for Audio Clips

- The correct format to export sounds for your emotes are `.mp3` and `.ogg`.

- The audio clip must have the same duration as the emote.

- While there is no limitation for size in the audio, the emote with props and sounds cannot be bigger than 3mb.

{{< hint info >}}
**📔 Note**: If the emote has sound (mp3 or ogg), it must be zipped with the .glb. After that, just drag and drop the .zip to the builder. More details can be found here: [Uploading emote with sound](https://docs.decentraland.org/creator/wearables-and-emotes/manage-collections/uploading-emotes/#uploading-emotes-using-a-zip-file)
{{< /hint >}}

{{< hint info >}}
**💡 Attention!**
Take into consideration that audio clips used in the emote must be original IP (Intellectual Property), having the rights for reproducing and follows the [Content Policy](https://decentraland.org/content/)criteria.
{{< /hint >}}


## Editing Sounds

To add sounds to your emotes you can do it in different ways:

1. **Edit your sounds directly on Blender**

One way to add sounds to your emotes is using the video sequencer editor that Blender provides.

To start adding sounds go to _Editor Type> Video Sequencer._

<img src="/images/wearables-and-emotes/props-and-sound/07-video-sequencer.png" width="400" />

Drag and Drop you sounds to the channels interface.

<img src="/images/wearables-and-emotes/props-and-sound/08-drag-sound.png" width="600" />

Press the shortcut `N` to see more options to handle your sounds like displaying waveform, make your sounds Mono or changing the volume.

<img src="/images/wearables-and-emotes/props-and-sound/09-sound-properties.png" width="400" />

{{< hint info >}}
If you want to fade in and out you can simply do it by adding keyframes from 0 to 1 and viceversa to the volume property.
{{< /hint >}}

Once you finished to edit your sounds you can export it going to _Render> Render Audio_. In the exporting option you need to select `.mp3` or `.ogg` format in the _Container_ section and then _Mixdown_. **Only the audio within the frame range will be exported.**

<img src="/images/wearables-and-emotes/props-and-sound/10-export-sound.png" width="600" />

2. **Render animation and add sound with a sound edit software**

While editing sounds directly in Blender can be convenient, it is not very flexible because the software is not primarily focused on sound editing. The available tools are very basic. If you want to add a more professional touch to your sounds, we recommend using dedicated sound editing software of your choice.

There are several software options you can use, such as [Audacity](https://www.audacityteam.org/) (Free and OpenSource), Adobe Audition, Ableton Live, or ProTools. Using dedicated sound editing software will provide you with a wider range of tools, functionalities, and sound effects, allowing you to enhance your sounds and give them a more professional feel.

To render your emote you can simply add a camera to your Blender scene and position it in a way you can see all the elements as clearly as possible to later have a good reference to add sounds.

<img src="/images/wearables-and-emotes/props-and-sound/11-setting-render.png" width="600" />

When rendering an emote, it is important to only include the frame range of your emote and not more. Choose an aspect ratio that suits your needs and select the output folder where you want the video or image sequence to be saved.

{{< hint info >}}
**Hint!**

<img src="/images/wearables-and-emotes/props-and-sound/12-sampling-render.png" width="400" />

_Before rendering make sure you do a low sampling rendering to save time in your render!_

{{< /hint >}}

Once this step is completed, use your video as a reference to create the corresponding sounds using your preferred sound editing software. **Ensure that the video sequence matches the animation's framerate of 30 frames per second (fps)**

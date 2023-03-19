---
date: 2022-09-01
title: Creating Emotes
description: Tips and guidelines for creating Decentraland Emotes.
categories:
  - emotes
type: Document
aliases:
  - /emotes/creating-and-exporting-emotes/
url: /creator/emotes/creating-and-exporting-emotes
weight: 2
---

# **Creating Emotes**

This documentation will cover the file specifications, the basics of animation in Blender, the proper way to export an Emote, and how to import one into the Builder.

### Animation Specs Chart

| Frame Rate | 30 fps |
| --- | --- |
| Max Length | 10 seconds (300 frames) |
| Animations per File | 1 |
| Export Format | .glb |
| Sampling Rate | 2 or 3 (if needed) |
| Max File Size | 1 MB |
| Max Animation Distance | 1 meter (in any direction) |
| Max Animation Height | 1 meter |

You can find a more detailed explanation of the animation specifications [**below**](#the-animation-specifications).

# Getting Started

## **Resources**
This documentation explains the set up for Rig 1.0, its controls, and features.

### Blend File for Rig 1.0

[BaseMale_Rig_1.0.blend](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/BaseMale_Rig_1.0.blend)

## **Frame Rate**

To getstarted, it’s important to check the frame rate. Decentraland’s animations must have a frame rate of **30 fps**. The rig file provided probably has that set up, but since Blender’s default value is 24 fps, it is best to double check before starting (a wrong frame rate will affect the speed of the animation). That option can be found in _Output Properties_ (the printer icon) under _Format_, as shown below:

![Make sure the framerate is set to 30 fps before starting.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/framerate.png)

Make sure the framerate is set to 30 fps before starting.

## **Pose Mode**

In Blender, a rig can be viewed in three different modes: _Object Mode_, _Edit Mode,_ and _Pose Mode_. Animations can only be done in _**Pose Mode**_ (in that mode, controls have colors). With the rig selected, you’ll find that option in a dropdown menu, at the top right.

![Changing to Pose Mode.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/changing_pose_mode.gif)

Changing to Pose Mode.

### **Starting Pose**

In the rig file provided, there’s already an action, the _**Starting_Pose**_. Considering that all avatar actions start from the idle pose, **we really encourage starting your animation from that pose and also using it again in the last frame**. This will make for a better transition from Idle to Emote and a more fluid animation.

{{< hint info >}}
**💡 Hint!**

If you want to do a loop animation, you don’t have to start the animation from the Starting Pose. Feel free to use the pose that makes more sense in your animation!**
{{< /hint >}}

## **Blender Interface for Animations**

In the rig file, other than the two windows for the viewport (front and side view), there are three more at the bottom: a _**Graph Editor**_, _**a Dope Sheet**_, and a _**Timeline**_.

-   _**Graph Editor**_: In this editor, it is possible to edit the animation curves of each transform property of the selected controls. Those curves show how the interpolation is being calculated and they can be edited to achieve the wanted effect in the animation. Both in here and in the dope sheet the _**Only Show Selected**_ tool is toggled, which means it’ll only include channels related to the selected control. This can be turned on and off by simply clicking on the arrow icon.
-   _**Dope Sheet**_: Here you can edit the keyframes. This is also where you can create new animations or go through the multiple ones created. Keep in mind that in order to have access to the animation, the _**Action Editor**_ must be selected. This option is right next to the _Dope Sheet_ icon, in a dropdown menu.
-   _**Timeline**_: This is where the timeline and playback controls are found. In here, the _**Auto Keying**_ is on, which means that every time a control is manipulated it automatically creates a keyframe. You can always disable that function by clicking on the dot next to the playback controls.

With this workspace, you have everything needed to start animating!

![These are the bottom windows. The top one is in the Graph Editor, the middle one in the Dope Sheet, and the bottom one is the Timeline. The top red arrow shows the Only Show Selected tool and the bottom one shows the Auto Keying.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/workspace.png)

These are the bottom windows. The top one is in the _**Graph Editor,**_ the middle one in the _**Dope Sheet,**_ and the bottom one is the _**Timeline.**_ The top red arrow shows the _**Only Show Selected**_ tool and the bottom one shows the _**Auto Keying**_.

{{< hint info >}}
**💡 Hint!**

Since Blender is highly customizable, this is also a good time to set up the layout that best suits you, adding, adjusting, or removing windows. Each animator has their own preferences, so feel free to edit the layout however you want!
{{< /hint >}}

# **Creating an Animation**

To create a new animation, simply click on _**Create A New Action**_ button (this will duplicate the current animation with all the keyframes) or press the X next to it, the _**Unlink Action,**_ and press the _**New**_ button. This way you’ll start with no keyframes at all. Make sure to always toggle _**Fake User**_ (the shield icon) so your animation is saved!

![Create a new animation by duplicating the existing one or by clicking on Unlink Action and then New.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/new_anim.gif)

Create a new animation by duplicating the existing one or by clicking on _**Unlink Action**_ and then _**New**_.

**Browsing and Deleting Animations**

In Blender, you can have multiple animation tracks in the same file. It is possible to browse them by clicking on the _**Browse Action**_ dropdown menu. All animation with and F (_**Fake User**_) will be saved. To delete an animation, press _**Shift**_ on the keyboard and click on the _**X**_. After doing that, the animation will show a 0 next to it, which means that it will be deleted the next time you close Blender or reopen the file.

![Browsing animations: The ones with an F will be saved, and the ones with 0 will be deleted.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/anim_list.gif)

Browsing animations: The ones with an F will be saved, and the ones with 0 will be deleted.

{{< hint info >}}
**💡 Hint!**

Do not always edit the same animation track. Before making major changes, just duplicate the animation. That way you have a back up version in case you regret deleting or changing something. This is also a nice way to keep track of the progress made so far!
{{< /hint >}}


**Naming**

**An animation’s name should start with a capital letter and if the name is more than one word long, the words should be separated by _.** Do not use spaces or special characters. Here are some examples of naming:

-   Snowfall
-   Rainbow_Dance
-   Throw_Money
-   Talk_To_Hand

# The Animation Specifications

## **Ground Reference and Animation Area**

In order to avoid ground penetration during animation, a plane has been added to the file as a ground reference. Along with the animation area reference, it also helps identify the area that can be used for the animation. For reference, the samller circle on the plane has a radius of 2 meters and the larger one, 4 meters.

![Ground and animation area reference.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_area_reference.png)

Ground and animation area reference.

The avatar center of gravity is the CTRL_Avatar_UpperBody. The limit to move it around is 1 meter (left, right, front, back), so try to keep it inside the smaller circle during animation. Arms and legs can exceed the small circle up to the larger one. As for the height, the limit is also 1 meter. The avatar cannot move over a meter up from its original position.

![Avatar centered.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_area_center.png)

Avatar centered.

![Max distance right.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_area_ok_right.png)

Max distance right.

![Max distance left.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_area_ok_left.png)

Max distance left.

![Max distance up.](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_area_ok_up.png)

Max distance up.

Here are some examples of emotes that are within the boundaries.

![Spotlight](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/spotlight.gif)

Spotlight

![Thalia Dance](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/thalia_dance.gif)

Thalia Dance


{{< hint info >}}
**💡 Attention!**

Watch out for these boundaries because crossing them might cause gameplay issues.
{{< /hint >}}

## **Animation Length**

The max length of an animation is **10 seconds** or **300 frames**. Remember to keyframe every control’s properties on the first and last frames.

{{< hint warning >}}
⚠️ Channels with visibility turned off in the Graph Editor won’t be keyframed, deleted, or even shown in the Action Editor. Unless it was intentionally done that way, pay extra attention to the visibility.
{{< /hint >}}

![Make channels visible before keyframing!](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/channels_visibility_graph_editor.gif)

Make channels visible before keyframing!

## **Number of Animations**

The exported file can only have **one animation**. If animations were duplicated during the process, make sure you delete all of them before exporting. Keep only the final version. Sequence emotes that need many animations to work (action start, action loop, and action end) are not supported right now.

## **Format**

Animations should be exported as .**GLB**. The file can only contain the deforming skeleton and the animation. **Mesh, controls, and any other object should not be exported**. More details on how to export can be found [**below**](#exporting).

## **Sampling**

Since constraints can’t be exported, the only way to export the animation clip is by baking it, which means that all the deforming bones’ positions, rotation, and scale will be keyframed in every single frame of the animation. If the clip is too long, like up to 300 frames, it’ll have 300 keyframes after exporting and the more keyframes it has, the heavier the file gets.

Sampling is a good way to optimize the animation. The sampling rate will define how often a keyframe will be baked in the animation. For example, if the sampling rate is set to 2, that means a keyframe will be created at every two frames. A sampling rate of 3 will bake a keyframe every three frames and so on. The higher the sampling rate, the lighter the file.

The drawback, however, is that the animation will start getting less and less fluid since it loses some important keyframes (they are distributed through the animation in an uneven way). It’s also important to notice that **sampling is NOT dividing the number of the animation’s frames by the sampling rate**.

Usually, a **sampling rate of 2 or 3** will do the trick. Those numbers can optimize the animation without compromising the quality.

{{< hint info >}}
**💡 Hint!**

If the number of frames of the animation can be divided by the sampling rate, that’s a good thing! It means that the final frame will be baked, preserving the transition from end to start of the animation.
{{< /hint >}}


## **File Size**

The max file size is **1 MB**. If the file is over that after exporting, try checking if the mesh wasn’t exported by accident or if the animation isn’t over 10 seconds. If it is still over 1 MB, try experimenting with the Sampling Rate, as higher values will improve the optimization.

# Exporting

Since we only want the armature and the animation to be exported, turn off the mesh visibility and any object other than the armature before exporting, as shown below:

![Turn off the mesh visibility before exporting!](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/mesh_visibility.gif)

Turn off the mesh visibility before exporting!

To export, go to _File_ > _Export_ > _glTF2.0 (.glb, .gltf)_

![export.gif](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/export.gif)

For the export settings, expand _**Include**_ and in _**Limit to**_ toggle _**Visible Objects**_. For _Transform_ and _Geometry_, leave it as it is.

![visible_objects2.gif](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/visible_objects2.gif)

Next, expand the _**Animation**_ tab, expand the second _**Animation**_ tab and toggle _**Export Deformation Bones Only.**_ This is also where the _**Sampling Rate**_ is defined.

![animation_export.gif](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/animation_export.gif)

That’s it for exporting the animation! 

# References

If you’re still not sure where to start or need some reference or inspiration, here are some animation clips to help you with that. These can be some nice studying material!

[Idle.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/idle.glb)

[Jump.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/jump.glb)

[Walk.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/walk.glb)

[Run.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/run.glb)

[Pose_Jump.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/pose_jump.glb)

[Pose_Spin.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/pose_spin.glb)

[Spotlight.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/spotlight.glb)

[Fashionista.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/fashionista.glb)

[Chic.glb](https://raw.githubusercontent.com/decentraland/documentation-creators/main/images/emotes/chic.glb)
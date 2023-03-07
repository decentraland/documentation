---
date: 2023-01-07
title: Creating wearables
description: Tips and guidelines for creating Decentraland wearables
categories:
  - Decentraland
type: Document
aliases:
  - /wearables/creating-wearables/
  - /decentraland/creating-wearables/
url: /creator/wearables/creating-wearables
weight: 2
---

# **How To Create Wearables**

## **Intro**

This guide introduces the basics of creating custom 3D models for Decentraland wearables. It explains how the Decentraland avatar system works, and it illustrates how to properly model your own wearables.

*Note: this guide assumes that you already have some basic to intermediate knowledge of 3D modeling. If you’re new to 3D modeling, [start here](https://docs.decentraland.org/creator/3d-modeling/3d-models/).*

Before you get started, download the example files for reference meshes and textures: **[Wearables Reference Models](https://drive.google.com/drive/u/1/folders/12hOVgZsLriBuutoqGkIYEByJF8bA-rAU)**


## **The Decentraland Avatar System**

The Decentraland “avatar system” is the broad collection of different body components and subcomponents that can be decorated with custom wearables. These components are:

- Body shape
- Head
    - Head shape
    - Eyebrows
    - Eyes
    - Mouth
- Upper body
- Lower body
- Feet
- Accessories

### **Body Shape**

The basic form of an avatar. Wearables can be assigned to one, or both, body shapes. Currently, there are two body shapes: A or B.

[]({{< ref “/images/wearables/1_creating_wearables.png”>}})

### **Head** 

The head includes several different meshes:

**Head Shape:** This is the base mesh of the head on which all other head features can be attach.

**Eyebrow Mesh:** The Eyebrow mesh works as a transparency mask. It is used to create different eyebrow styles.

**Eye Mesh:** The Eye mesh works as a transparency mask, and is used to create different eye styles.

**Mouth Mesh:** The mouth mesh works as a transparency mask, and is used to create different mouth styles.

[Head]({{< ref “/images/wearables/2_avatar_head.jpeg”>}})

### **Upper Body**

The upper body, or torso, of an avatar includes the arms and hands. All upper body wearables are applied to the entire torso.

[UpperBody]({{< ref “/images/wearables/3_upper_body.jpeg”>}})

### **Lower Body**

The lower body includes the pelvis, legs, and ankles of an avatar.

[LowerBody]({{< ref “/images/wearables/4_lower_body.jpeg”>}})

### **Feet**

Boots, shoes, sandals, etc. are applied to this slot.

[Feet]({{< ref “/images/wearables/5_feet.jpeg”>}})

## **Wearable Categories [#](https://docs.decentraland.org/creator/wearables/creating-wearables/#wearable-categories)**

Each wearable has a specific category that determines which body part in the avatar system (e.g. head, upper body, etc.) the wearable will be applied to. Certain wearables will impact whether or not other wearables are rendered, depending on the specific category. Some wearables will entirely replace others with sometimes unexpected and surprising results. See the list below for details.

The different categories are:

- **Skin:** Replaces the entire avatar (head, upper body, lower body and feet except accessories)
- **Head:**
    - **Mouth**
    - **Eyes**
    - **Eyebrows**
    - **Facial Hair:** facial hair won’t replace or override any other wearables.
    - **Hair:** Replaces an avatar’s hair.
- **Upper Body**
- **Lower Body**
- **Feet**

There are also accessories that can be applied to different areas of an avatar. Some of these accessories can impact other wearables. The accessories are:

- **Mask**
- **Eyewear**
- **Earring**
- **Tiara**
- **Top Head** 
- **Hat** 
- **Helmet** 

## **Building 3D models for wearables [#](https://docs.decentraland.org/creator/wearables/creating-wearables/#building-3d-models-for-wearables)**

Let’s start to create some wearables!

### **Limitations**

#### **Tris, materials and texture limitations**

To ensure that Decentraland runs smoothly for all users, it is important to create wearable models without using too many triangles. The goal is to keep models as simple as possible so that they can easily be rendered, without sacrificing too much detail.

The same goes for textures. It’s critical that we use as few textures as possible.

There are limits for the number of triangles and textures that can be used for each wearable or accessory:

- No more than 1.5K triangles per wearable slot: upper body, lower body, feet and hair.
- No more than 500 triangles per these accessories slots: mask, eyewear, earring, tiara, top_head and facial hair.
- No more than 1k triangles per these accessories slots: hat, helmet.
- No more than 2 textures (at a resolution of 512x512px or lower) per wearable. All textures must be square.
- No more than 2 materials (without counting the AvatarSkin_MAT)
- In the case of skin wearable, the amount of tris allowed are 5k and 5 textures.

{{< hint warning >}} **Wearable Tris Combiner:**

*If the wearable hide other wearables the creator is allowed to combine the tris per slot. For example: if you want to do a jumpsuit you could create it using the upper body category hiding lower body; in that case you could have 1.5K*2= 3K triangles.*

In the case of the helmet, if you hide all the wearables from the head (head, earrings, eyewear, tiara, hat, facial_hair, hair and top_head you can reach the 4k tris and 2 materials and 2 textures) 
{{< /hint >}}

#### **Max width, height and depth dimension of the wearables**

There is a distance limit for wearables to ensure that they do not obstruct the visibility of other players screens or invading the scene space in an excessive way. 

The dimension for the wearables cannot exceed:

**`Height: 2.42 m`**

**`Width: 2,42 m`**

**`Depth: 1,4 m`**

[MaxWidth&Height]({{< ref “/images/wearables/12_max_width_height.png”>}}) 
[MaxDepth]({{< ref “/images/wearables/13_max_depth.png”>}})

### **Maps**

Decentraland supports 3 types of maps to texture your **Avatars/Wearables** Which are:

[Maps]({{< ref “/images/wearables/6_maps.png”>}})

1. **Base Color**: This is the main texture with the colors and details of your model.
2. **Emission**: This map is for the parts that are glowing in your model. The emission map goes in a separated material specifically for emission.
3. **Alpha**: This map is to handle transparency. It uses the opacity channel of the texture.

[Maps]({{< ref “/images/wearables/7_alpha.png”>}})

Since Image textures in blender have a Color and Alpha output you can use the color texture and the opacity texture in the same material.

#### **Don’t allowed maps**

Because Decentraland reference client uses of a Toon shader for the avatar materials, some maps are **not necessary** like:

- **Normal maps:** Normal maps are maps used to simulate height on a surface.
- **Roughness maps:** Roughness is used to determine which part of the surface will receive more or less roughness based on the amount of darkness on the map**.**

To use these maps in Decentraland the workaround is to bake them in one texture. You can find more info about baking textures here: [https://docs.blender.org/manual/en/latest/render/cycles/baking.html](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)

### **Normals**

Decentraland engine render only one side normals. (That means that a plane only will be visible from one side, the other side won’t be rendered) So, to ensure that your 3D is absolutely correct with the normals we can check that in two different ways.

The first one is to toggle the “Backface culling” on the Material properties settings, this is a good practice for spot inverted normals, like in this image:

[Normals]({{< ref “/images/wearables/8_normals.gif”>}}) 
[BackfaceCulling]({{< ref “/images/wearables/9_backface_culling.png”>}}) 

The second way to check if the normals are right is by toggling “Face orientation” on the viewport overlay options. It will turn your model blue, but don’t worry. The blue faces are the correct ones and the red ones are the ones that needs to be corrected, you can find this option here:

[NormalsFace]({{< ref “/images/wearables/10_normals_face.png”>}}) 


### **Base Body Structure**

After downloading the base avatar example file, load the model into your 3D editor, like Blender.

You’ll notice that each model contains 7 different meshes related to an armature. These meshes represent the head, eyebrows, eyes, mouth, upper body, lower body and feet. You can use these example models as a reference and starting point for your own custom wearable.

{{< hint warning >}} **Important: Do not modify the “cuts” or the “stitches” between categories (unless you want to create an unusual “floating head” effect or similar).**
{{< /hint >}}

Each part of the body has caps, making them “water tight”. These caps exist to prevent unsightly glitches if there are any animation clipping problems due to bad skin weighting. It’s best to not remove these caps when editing the mesh.

[BodyParts]({{< ref “/images/wearables/14_body_parts.png”>}})

### **Eyebrows, Eyes and Mouth**

These meshes work with a transparent shader so you don’t have to do anything aside from creating your own png texture for the new eyebrow, eye, or mouth style you want and placing it correctly into the UV map. These textures should be 256x256px and need to have an alpha channel for transparency.

Here are some example png textures:

[Eyes]({{< ref “/static/images/wearables/21_eyes.png”>}})
[Eyebrows]({{< ref “/static/images/wearables/22_eyebrows.png”>}})
[EyesMask]({{< ref “/static/images/wearables/23_eyes_mask_uv.png”>}})

Eyes and Eyewbrows use the same mesh and UV map.

[Mouth]({{< ref “/static/images/wearables/24_mouth.png”>}})
[MouthMask]({{< ref “/static/images/wearables/25_mouth_mask_uv.png”>}})

Mouth mesh and UV map.

Nodes:To visualize the final result you’ll need to use these nodes (in Blender):

[EyesNodes]({{< ref “/static/images/wearables/26_eyes_nodes.png”>}})
[EyesAlpha]({{< ref “/static/images/wearables/27_eyes_alpha.png”>}})

Masks: The Avatar Editor has different color options where users can choose from when selecting eyes.

[EyesEditor]({{< ref “/static/images/wearables/28_eyes_tone.png”>}})

These color choices are applied to a specific mask in the wearable.

[EyesMask]({{< ref “/static/images/wearables/29_eyes_mask.png”>}})
[EyesBase]({{< ref “/static/images/wearables/30_eyes_base.png”>}})

The black area in the image on the left (Eyes Mask) indicates the area of the texture on the right (Eyes Base) that will be colored. It’s important to remember that irises always need to have a grey scale (if the iris is pure black, the tint isn’t going to work. By the contrary, if the iris is pure white it would be fully tinted by the selected color using the editor).

### **Hair and Facial Hair**

There are two important things to remember when creating custom hair wearables.

First, try to follow the shape of the head. You can always refer to the head mesh provided in the example files if you need a place to start.

[HairBase]({{< ref “/static/images/wearables/31_hair_base.png”>}})

Second, if you want users to be able to change the color of your custom hair or facial hair using the avatars editor, then you must paint the hair in grayscale and use "Hair” in the naming (example “M_Hair_Short”). If you want to include other object which doesn't is influenced by tint just don't add the that naming convention. 

[HairMat]({{< ref “/static/images/wearables/32_hair_mat.png”>}})
[HairTX]({{< ref “/static/images/wearables/33_hair_tx.png”>}})

Lower shades of gray will appear darker and higher shades of gray will appear brighter, but always in the color selected by the user in the avatar editor.


## **Base Materials and Textures**

There are two basic materials for avatar models. One is the material used for the wearable itself and the other one is used for the skin.

[Materials]({{< ref “/images/wearables/15_avatar_skin_mat.png”>}})

Each base mesh comes with its own skin texture.

[SkinAvatarShapeA]({{< ref “/images/wearables/16_Avatar_MaleSkinBase.png”>}})

[SkinAvatarShapeB]({{< ref “/images/wearables/17_Avatar_FemaleSkinBase.png”>}})

The skin texture is made in grayscale so it allows the render engine to tint the skin of the avatar using the editor according to the user’s preference.

[SkinTone]({{< ref “/images/wearables/18_skin_tone.png”>}})

{{< hint warning >}}
Important: always preserve the UV mapping for any body part that is exposed by a wearable, like the legs exposed by the shorts or skirts.
{{< /hint >}}

[SkinUV]({{< ref “/images/wearables/19_skin_uv.png”>}})

You can create custom textures for your wearables! However, it’s always best to use a single, very small, texture file for each wearable. Using the default AvatarWearable_MAT texture provided in the example files will guarantee that your wearables are performant!

[WearablesUV]({{< ref “/static/images/wearables/20_wearables_uv.png”>}})

{{< hint warning >}}
✨ In the case you want to do your own textures for the model we recommend the following addons for better UV Unwrapping:

**UVPacker**

UvPacker is a free addon that helps you to pack and organize your uvs with just a few clicks. As Decentraland works with 512x for the wearables this tool is a great assist to create better and more organized textures. 

You can download directly from the website here: 

[**https://www.uv-packer.com/download/**](https://www.uv-packer.com/download/)

**UVToolKit**

UvToolKit is a addon that helps you to expand your UV settings and options to create great UVs in blender. 

Here is the link for the download:
[**https://alexbel.gumroad.com/l/NbMya**](https://alexbel.gumroad.com/l/NbMya)

{{< /hint >}}

## **Skin Weighting**

Skin weighting is the process of determining which bones in the avatar’s rigging affect which wearables during an animation.

When skin weighting our new wearables, there are several considerations we need to keep in mind.

Each asset must be weighted to the full skeleton. For example, an upper body asset will look like this when applying skin weights:

[Rig]({{< ref “/static/images/wearables/34_rig.png”>}})

Wearables that meet at intersections between body parts must be fully weighted to the same bone. For example, in these two green zones, the vertices in the neck need to be fully weighted to the “Neck” bone only.

[HeadCuts]({{< ref “/static/images/wearables/35_head_cuts.png”>}})

### **Key Bones**

The “key” bones to use when skin weighting are:

**Head Bone:** for the hair, earrings, tiaras, eyes, eyebrows, mouth and any accessory that needs to follow the head’s movement.

**Neck Bone:** for the main head and upper body’s intersecting vertices.

**Hips Bone:** for the upper body and lower body’s intersecting vertices.

**Right Leg and Left Leg Bones:** for the lower body and feet intersecting vertices.

{{< hint warning >}}
⚠️ **Hint**

- Remember, you can use any bone to influence any mesh’s vertices! For example, you could create a new foot mesh for a tall pair of boots, and skin weight the top of the boot to the “Leg Bones”. Or, you could create some long hair and use the “Shoulder” or “Spine” bones to influence the hair when the avatar moves around.
- It's always recommendable to keep a symmetry from both sides of the rig, left and right should have similar bone influences.
- As a common advice, a vertex cannot be influenced by more than 4 bones or joints.
{{< /hint >}}

## **Good practices for modeling**

### **Change your mesh from T-pose to A-pose**

When you’re making wearables, the best way to visualize the final result, and to facilitate how you handle topology and position of the wearable is to work with the model in A-Pose. In order to do that you have to follow this simple steps:

1. First select the upper body, then you have to toggle “**Edit mode**” and “**On cage**” in the armature modifier.

[APose]({{< ref “/static/images/wearables/36_60_1.gif”>}})

2. Now, in pose mode you can rotate the arms 60°.

[APose]({{< ref “/static/images/wearables/37_60_2.gif”>}})

3. You can edit your mesh in A-Pose instead of T-pose.

[APose]({{< ref “/static/images/wearables/38_60_3.gif”>}})

4. But it is also good to keep in mind that you can easily alternate from A-Pose to T-Pose just toggling back the “Edit mode” and “On cage” in the armature modifier.

[APose]({{< ref “/static/images/wearables/39_60_4.gif”>}})

## **Joint deformation:**

In order to get the best results on the wearable topology when it comes to joints (arms or legs, for example) it's important to have good practices when creating loops. Here we can see the difference on the deformation of the mesh for different loop cuts:

[JointDeformation]({{< ref “/static/images/wearables/40_joints.gif”>}})

A good way to ensure that everything is deforming correctly is to do a weight paint like the following example:

[JointDeformation_01]({{< ref “/static/images/wearables/41_joint_weight.png”>}})

[JointDeformation_02]({{< ref “/static/images/wearables/42_joint_weight_02.png”>}})

### **Skirts**

A useful tip and good practice when modeling skirts/dresses is to add additional loopcuts in the intersections of the folds. This will be very handy when you have to paint the weights of the rig.

[Skirt]({{< ref “/static/images/wearables/43_skirt.png”>}})

With this loopcuts the vertex influence look a lot more smooth and give you better results when you’re animating a skirt/dress.

Here is an example of how the bone influence should be:

[Skirt]({{< ref “/static/images/wearables/44_skirt.gif”>}})

### **Hats**

A good practice when creating hats is to add a hair to the base mesh of the hat and then hide the category *hair* using the editor. Doing this is going to prevent that the hat clips with other hairs and reduce unexpected results.

[Hat]({{< ref “/static/images/wearables/45_hat.png”>}})

## **Add Polygon Count**

A valuable tip is to always keep on track of the polycount of your models. To do that in blender you need to turn on statistics on the viewport overlays panel.

[PolyCount]({{< ref “/static/images/wearables/46_poly_count”>}})

## **Resources**

In this shared folder you can find base models, textures, and various other resources, including examples of fully-created wearables. Feel free to leverage these resources when creating your own.

**[Wearables Reference Models](https://drive.google.com/drive/u/1/folders/12hOVgZsLriBuutoqGkIYEByJF8bA-rAU)**
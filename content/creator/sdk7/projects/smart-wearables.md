---
date: 2022-02-02
title: Smart Wearables
description: Create wearables with interactive capabilities
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/smart-wearables/
weight: 4
---

Smart wearables are a kind of global scene that is associated to a wearable, and activated based on if the player is using that wearable. These global scenes are turned on when the player puts on a certain item of clothing, and turned off when the player takes off the item.

Smart wearables can grant players new abilities, like a jetpack that lets them fly, or add a new layer of content on top of the rest of the world, like randomly placing coins to be collected throughout the whole of genesis city.

{{< hint warning >}}
**📔 Note**: Smart Wearables can only be created using SDK 7.

The **Creator Hub** doesn't currently support creating Smart Wearables projects.
{{< /hint >}}

## Getting started

### Using the CLI

Open a command line in a new folder and run

`npx @dcl/sdk-commands init --project smart-wearable`

This command creates the basic files and structure for a new smart wearable.

You can also copy the project template from the Github repository: [Smart Wearable Sample](https://github.com/decentraland/smart-wearable-sample).

## The files in the template

The folder of a brand new Smart Wearable project is very similar to that of a [Decentraland scene]({{< ref "/content/creator/sdk7/projects/scene-files.md">}}), but you will notice the following differences:

- `wearable.json` includes all of the metadata for the smart wearable
- There’s a placeholder 3D model (glasses.glb) and thumbnail (glasses.png) for a pair of dark glasses. You should replace these with the actual wearable you are creating
- `scene.json` is a lot shorter, it doesn’t include properties that are irrelevant to a wearable, like parcels or spawn points

## About wearable.json

The default `wearable.json` file looks like this:

```json
{
  "data": {
    "replaces": [],
    "hides": [],
    "tags": [
      "special",
      "new",
      "eyebrows"
    ],
    "representations": [
      {
        "bodyShapes": [
          "urn:decentraland:off-chain:base-avatars:BaseMale",
          "urn:decentraland:off-chain:base-avatars:BaseFemale"
        ],
        "mainFile": "glasses.glb",
        "contents": [
          "glasses.glb"
        ],
        "overrideHides": [],
        "overrideReplaces": []
      }
    ],
    "category": "eyewear"
  },
  "name": "Smart Wearable Example",
  "description": "Smart wearable desription here.",
  "rarity": "mythic"
}
```

The following fields are required in `wearable.json`:

- `id`: Unique id of the smart wearable.
- `name`: The name for the wearable that users will see in the marketplace
- `description`: The description of the wearable that users will see in the marketplace. Make sure you indicate what the smart wearable can do, as users of the marketplace will have no way to preview its functinality before buying it.
- `rarity`: The rarity supply of the token. Possible values are:
  - unique (1 copy)
  - mythic (10 copies)
  - exotic (50 copies)
  - legendary (100 copies)
  - epic (1000 copies)
  - uncommon (10.000 copies)
  - common (100.000 copies)

{{< hint warning >}}
**📔 Note**: If you forked your project from an existing one, make sure the `id` value is unique before publishing your wearable. Use [uuidgenerator.net](https://www.uuidgenerator.net/) to generate a new random UUID
{{< /hint >}}

The following fields can also optionally be included. These settings can also be configured from the Builder UI, once you upload the smart wearable.

- `data`: Includes the following

  - `replaces`: List of categories of other wearables that should be unequipped when equipping this wearable, in addition to the default of this category. Eg: When putting on a cape top-body, also hide feet.
  - `hides`: List of categories of other wearables that should be hidden (but not unequipped) when equipping this wearable, in addition to the default of this category.
  - `tags`: Tags used to make the wearable searchable in the marketplace.
  - `representations`:
    - `bodyShapes`: The list of avatar representations that can use this wearable. All smart wearables must be available for both male and female body shapes.
    - `mainFile`: The main file with the 3D model of the wearable.
    - `contents`: The full list of files used to render the 3D model of the wearable. For example, the 3D model could include textures as separate files.
    - `overrideHides`: Any exceptions from the default _hide_ behavior of this wearable category.
    - `overrideReplaces`: Any exceptions from the default _replace_ behavior of this wearable category.
  - `category`: What wearable category to use. Possible values are:

    - 'eyebrows'

    - 'eyes'

    - 'facial_hair'

    - 'hair'

    - 'mouth'

    - 'upper_body'

    - 'lower_body'

    - 'feet'

    - 'earring'

    - 'eyewear'

    - 'hat'

    - 'helmet'

    - 'mask'

    - 'tiara'

    - 'top_head'

    - 'skin'

    - 'hands_wear'

- `menuBarIcon`: Image to use on the “experiences” menu, to represent this portable experience, to represent the portable experience. This image should be at root level in your folder. The recommended image size is 256x256.
- `model`: The 3D model to use for the wearable. This file should be at root level in your folder.
- `bodyShape`: The avatar body type that this wearable is compatible with. Possible values:
  - male
  - female
  - both
- `collectionAddress`: The ethereum address of the published collection of wearables. This address is assigned once publishing, it can be left blank.

## The thumbnail

You must include an image named `thumbnail.png` at root level in your folder. This image will be shown both in the backpack and the marketplace, to represent your wearable in 2d. The recommended required image size is 256x256.

Chose an image that sets player expectations and properly represents your creation.

This image can also be set in the Builder UI after uploading the smart wearable.

## The Preview

Running a preview of a portable experience is just like running that of a scene, simply click *Preview** on the Creator Hub, or run `npm run start` on the command line. If the `wearable.json` file is properly configured and the project is recognized as a smart wearable, you’ll notice that all the visible around you are the default empty parcels. In this preview mode, you are not restricted to any set of parcels, you can add 3D models or sounds anywhere in the world.

To test how the smart wearable behaves in the context of a scene, upload the smart wearable to the Builder and click the **See in world** button. This will open Decentraland with the wearable avialable in your backpack.

<!-- you can also run a preview of your wearable at the same time as you run a preview of one or several scenes by using a [Workspace]({{< ref "/content/creator/sdk7/projects/workspaces.md" >}}). For example, you can run your smart wearable together with the [Genesis Plaza](https://github.com/decentraland-scenes/Genesis-Plaza) scene to test how it behaves on a busy scene, while on an elevator, etc. -->

## Tips

When writing the code for your smart wearable, keep the following in mind:

- When positioning an entity, note that positions are global, relative to the 0,0 coordinates of Genesis Plaza.
- Other players surrounding you will not see or hear the entities in your smart wearable's global scene, as they don't have the same global scene loaded.
- To react to nearby players:
  - See [Fetch all players]({{< ref "/content/creator/sdk7/interactivity/user-data.md#fetch-all-players" >}}) to know how to obtain data from other players in the surroundings.
  - Be mindful that the loading of the smart wearable, surrounding scenes and other players may occur in different orders depending on the situation. If the player enters Decentraland with the smart wearable already on, it’s likely that your wearable's global scene will load before other players do. On the other hand, if the player first loads into a scene and then puts on the wearable, it’s likely that other players will already be loaded by the time the wearable's scene starts running.
  - The `syncEntity` method can't be used to sync entities with other players. To have multiplayer behavior between players that are wearing the same wearable, use an external server to send information between players, see [3rd party servers]({{< ref "/content/creator/sdk7/networking/authoritative-servers.md" >}}).
- To interact with surrounding scenes:
  - You can’t directly send any instructions to nearby scenes or other smart wearables, the `messageBus` is currently sandboxed for each smart wearable.
  - You can use an intermediate server to send information between the smart wearable and a scene.
  <!-- - If you do a raycast, you can detect hits against the colliders of entities from the surrounding scenes. This can tell you the exact hit location, normal direction, and even the entity name and mesh name of the 3D model. This only works when hitting entities on scenes written with SDK7. -->

## Publish

To publish your smart wearable:

1. Make sure the information in `wearable.json` is accurate. If you used another project as a starting point, make sure the `id` is a unique identifier, not used by other wearables.

2. Run `npm run pack` on your project folder. This generates a `smart-wearable.zip` file in your project folder.

{{< hint warning >}}
**📔 Note**: The output of `npm run pack` will indicate the size of the uncompressed exported project, it must be under 3MB. If larger than that, it won’t be accepted by the builder.
{{< /hint >}}

3. Open the Builder, open the Collections tab, click **Create Collection** and select **Wearables or Emotes** , then name your collection and click **Create**.

4. Click the **Add Items** button, then drag your compressed `smart-wearable.zip` file into the Builder, verify that all the information is accurate.

> Note: If your wearable contains different model representations, you need to do a workaround:
>
> <ol type="a">
> <li>In your project, create a new folder for each representation(<code>male</code> and <code>female</code>), and put the 3D model for each representation in its corresponding folder.</li>
> <li>Update your <code>wearable.json</code> file to include the new representations.</li>
>
> ```lang-json
> "representations": [{
>   "bodyShapes": ["urn:decentraland:off-chain:base-avatars:BaseMale"],
>   "mainFile": "male/glasses.glb",
>   "contents": ["male/glasses.glb"],
>   "overrideHides": [],
>   "overrideReplaces": []
> },
> {
>   "bodyShapes": ["urn:decentraland:off-chain:base-avatars:BaseFemale"],
>   "mainFile": "female/glasses.glb",
>   "contents": ["female/glasses.glb"],
>   "overrideHides": [],
>   "overrideReplaces": []
> }],
> ```
>
> <li>Run <code>npm run pack</code> to generate a new smart-wearable.zip file.</li>
> <li>Drag the new smart-wearable.zip file into the Builder.</li>
> </ol>

5. Make sure the “hide” and “remove” categories are correctly set to disable other wearable categories when this wearable is on.
6. Upload a video showcase for your smart wearable. This will be displayed in the marketplace for buyers to see how the smart wearable works.
7. Click the **See in Decentraland** button. This will open the Decentraland explorer with all of the wearables in your collection availale for testing in your backpack. Try them out and see how they behave in a more real scenario, for example running around Genesis Plaza.
8. When you're happy with the wearables in your collection, click the **Publish Collection** button.

## Restricted actions

To prevent abuse, certain features aren't permitted on portable experiences by default, and require adding a permission flag.

See [Required permissions]({{< ref "/content/creator/sdk7/projects/scene-metadata.md#required-permissions">}}) for more details.


## Terminate a smart wearable

To terminate a smart wearable, run the `kill()` method.

```ts
kill()
```

## Limitations

{{< hint warning >}}
**📔 Note**: The entire smart wearable needs to fit within 3MB. This includes the 3D model, thumbnail, code, libraries, sound files, additional 3D models, UI images, etc. This limit is for the uncompressed folder. The builder will not let you upload larger wearables than this.

To check the size of your smart wearable, run `npm run pack`, the project size is specified in the output text of the command. You can also verify this by uncompressing the generated `smart-wearable.zip` file and checking the size of the folder.
{{< /hint >}}


Smart wearables only run the global scene for the player wearing the wearable. Other players don't see the effects. For example, if the global scene renders a pet that follows the player, other players around won't see this pet. However, other players will see avatars perform animations that run as part of the wearable's scene. 

<!-- even [custom avatar animations]({{< ref "/content/creator/sdk7/interactivity/trigger-emotes.md#custom-animations">}}) uploaded as part of the smart wearable's files. -->

Smart wearables only work when players have them on. For this reason, players can only have a limited number of activated smart wearables, and depending on what part of the body they take up, some will be incompatible with others. For example, you can’t have two hats at the same time, or a helmet and hair at the same time.

If a wearable is “hidden” but not “removed” by other wearables being worn, then the smart wearable can still be on, even if the corresponding wearable is not visible.

## Examples

[Smart wearable sample](https://github.com/decentraland/smart-wearable-sample))

---
date: 2024-07-25
title: Editor FAQs
description: Frequently asked questions about the editor
categories:
  - scene-editor
type: Document
url: /creator/editor/faq
---

Below you can find the **frequently asked questions** about the Scene Editor.

{{< details class="faq-details" anchor="true" title="How do scene limits work? What are triangles? How about materials? What’s going on?" >}}

Genesis City is a really, really big place. In order to make sure everyone has a smooth experience, there’s a limit to how much stuff each scene can hold.

In the bottom left corner of the Scene Editor, if you click on the set of squares, you’ll find a little list explaining what each of these limits are, and how far along you are to reaching each one. Let’s take a look at each of these:

- **Geometries:** these define different simple shapes, like a box or a wheel.
- **Bodies:** a body is just a copy of a geometry. For example, a bike might have three bodies: the frame and two wheels. By copying similar geometries, we can save resources.
- **Triangles:** each surface of a body is shaped like a triangle. More complex models have more triangles than simpler models.
- **Materials:** materials make your scenes more realistic by describing how a model or shape should look. They change the way light is reflected (or emitted) from different models, and can include one or more textures.
- **Textures:** these are the images used in materials. Textures are images of different patterns and colors - like wood, stone, or grass.
- **Entities:** an entity can include one or more bodies, like the bike in the example above. Entities include everything you need for an asset: the geometries, bodies, materials, and textures.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I upload custom assets?" >}}

Yes, you can import 3D models in `.gltf` and `.glb` formats. See [**Import items**]({{< ref "/content/creator/scene-editor/import-items.md" >}}).

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I deploy my scene to my land?" >}}

Yes, you can deploy to land you own, or land where you have deploy permissions. You can also deploy to a Decentraland WORLD if you own a Decentraland NAME or an ENS name. To do this, open your scene project and click the **Publish** button.

See [**Publish scene**]({{< ref "/content/creator/scene-editor/publish-scene.md" >}}).

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I move items underground?" >}}

Yes, you can place an object underground, or partially underground. However, the floor on the scene can't be removed, so you can't do tunnels or holes for players to see what's underground.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How do I add images to my scene?" >}}

You can import an image as you would import a 3D model. Then you can assign this image as a texture on a plane. See [**Import items**]({{< ref "/content/creator/scene-editor/import-items.md" >}}).

You can also reference an external image by URL in one of your materials. Make sure that the image is hosted in a site that has open policies about their content shared on other sites, otherwise it may not be displayed.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I share my scenes with other users of the Scene Editor?" >}}

Scenes are stored on your local disk, which allows you to upload the files to any sharing platform, like Google Drive or GitHub.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How do I save projects?" >}}

Projects are saved automatically to your local disk. Any change you make on the visual editor is immediately saved.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I import scenes from the SDK?" >}}

Yes, any Decentraland scene built with SDK7 can be imported into the Scene Editor. This includes scenes built with the Web Editor or entirely in code with the SDK. See See [**Manage scenes**]({{< ref "/content/creator/scene-editor/manage-scenes.md#import-a-scene" >}}).

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I group objects?" >}}

You can multi-select objects by pressing _control_ and keeping it pressed while selecting more, and then apply actions to that group.

You can also nest items, so that any change to the parent's transform also affects the children. For example, you could set books as children of a bookshelf, so that moving the bookshelf also brings books with it.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I snap/attach items to other items?" >}}

No, but you can press and hold Shift for more precise placement when moving objects.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="How does Preview mode work?" >}}

Use the W, A, S, and D keys to move around in Preview mode, and Space to jump.

If you can’t move, you may be stuck inside an item's geometry. Check your scene's spawn points, you might have to move them to avoid starting stuck.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Can I pick the color or texture of items?" >}}

Right now, all of the models come with one texture, but we agree that it’d be awesome to have more control over each model’s appearance. You can however export a 3D model, edit it in a 3D modeling tool, and import it again into a custom asset pack.

{{</ details >}}

{{< details class="faq-details" anchor="true" title="Where can I find the default 3D models in the Editor's asset packs, in case I want to edit them?" >}}

The model's files get added to your project's folder on your local machine as soon as you drag an item into your scene. You'll find all your scene's models under the sub folder `./assets/builder/<item name>` inside the project folder.

You can also find all of these models in [this repo](https://github.com/decentraland/builder-assets/tree/master/assets).

Before editing the models, see the [3D Modeling section of our docs]({{< ref "/content/creator/3d-modeling/3d-models.md" >}}).

{{</ details >}}

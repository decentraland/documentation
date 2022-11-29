---
date: 2022-10-25
title: Create a project
description: How to create a new project using the editor
categories:
  - editor
type: Document
url: /creator/editor/create-a-project
weight: 3
---

To create your first scene using the Decentraland Editor, follow these steps.

Make sure you've [installed the Decentraland editor]({{< ref "/content/creator/editor/installation-guide.md" >}}), then:

1) Open a Visual Studio Code window on an _empty folder_.
2) Select the Decentraland tab on Visual Studio's left margin sidebar
3) Click **Create Project**
4) The editor will prompt you about what kind of project to create. Select **Scene**.

Preview the 3D scene by clicking **Run Scene** in the Decentraland tab of Visual Studio Code.

Read more about the scene preview in [preview a scene]({{< ref "/content/creator/editor/preview-scene.md" >}})

Visit the [Decentraland Awesome repository a](https://github.com/decentraland-scenes/Awesome-Repository) for a large catalogue of example scenes, each tackling one particular challenge.

## Edit the scene

Open the `src/game.ts` file from your scene folder.

Change anything you want from this code, for example change the _x_ position of the first `cube` entity that's spawned (on line 42). If you kept the preview running in an open tab, you should now see the changes show in the preview.

> **Tip:**  
>
Visual Studio Code helps you by marking syntax errors, autocompleting while you write and even showing smart suggestions that depend on context. Also click on an object to see the full definition of its class.

Download this 3D model of an avocado from the scene's [GitHub repo](https://github.com/decentraland-scenes/avocado) in _glTF_ format. [link](https://github.com/decentraland-scenes/avocado/raw/main/Avocado.zip).

![](/images/media/avocado.jpg)

Create a new folder under your scene’s directory named `/models`. Extract the downloaded file and drop all of its contents in that folder. Note that there are several files that make up the 3D model, all of them must be in the same path.

At the end of your scene’s code, add the following lines:

```ts
let avocado = new Entity()
avocado.addComponent(new GLTFShape("models/avocado.gltf"))
avocado.addComponent(
  new Transform({
    position: new Vector3(3, 1, 3),
    scale: new Vector3(10, 10, 10),
  })
)
engine.addEntity(avocado)
```

You can also download the finished scene from its [GitHub repo](https://github.com/decentraland-scenes/avocado).

Check your scene preview once again to see that the 3D model is now there too.

![](/images/media/avocado.jpg)

The lines you just added create a new [entity]({{< ref "/content/creator/scenes/architecture/entities-components.md" >}}), give it a [shape]({{< ref "/content/creator/scenes/3d-essentials/shape-components.md" >}}) based on the 3D model you downloaded, and [set its position and scale]({{< ref "/content/creator/scenes/3d-essentials/entity-positioning.md" >}}).

Note that the avocado you added rotates, just like all other entities in the scene. That's because the `RotatorSystem` [system]({{< ref "/content/creator/scenes/architecture/systems.md" >}}) that was defined in the default code of this scene is iterating over every entity in the scene and rotating it. If you remove this system, entities stop rotating.


## The Utils library

The Decentraland ESC Utils library includes a number of helper functions and specialized components that make it easier to carry out a lot of common use cases.

To use any of the helpers provided by the Utils library:

1. Install it as a [dependency]({{< ref "/content/creator/editor/manage-dependencies.md" >}}) of your scene. At the bottom of the Decentraland tab, in Visual Studio Code, click the **+** icon on the **Dependencies** section. Then write the name of the dependency you wish to install:

   ```
   @dcl/ecs-scene-utils
   ```

2. Add this line at the start of your `game.ts` file:

   ```ts
   import * as utils from "@dcl/ecs-scene-utils"
   ```

4. Further down in the `game.ts` file, write `utils.` and let the suggestions show the available helpers. You'll see there are a number of functions you can run and of components that can be added to entities.

5. Add the following component from the `utils` library to your avocado entity to make it slowly grow. The provided arguments make it grow from a scale of 1 to a scale of 5 over a period of 10 seconds:

	```ts
	avocado.addComponent(new utils.ScaleTransformComponent(
		new Vector3(1,1,1), 
		new Vector3(5, 5, 5), 
		10
	))
	```
	The `ScaleTransformComponent` requires the following parameters:

	 * `start`: Starting scale.
     * `end`: Ending scale.
     * `duration`: Duration (in seconds) of start to end scaling.

	 > TIP: Your code editor will hint this information to you once you typed `new utils.ScaleTransformComponent(`.

6. Notice that the `ScaleTransformComponent` component also takes two other optional more advanced parameters that you can play around with:

	* `onFinishCallback`: A function that is called when the transition ends.
    * `interpolationType`: Type of interpolation to be used.

	```ts
	avocado.addComponent(new utils.ScaleTransformComponent(
		new Vector3(1,1,1), 
		new Vector3(5, 5, 5), 
		4,
		()=>{ log("FINISHED") },
		utils.InterpolationType.EASEOUTELASTIC
	))
	```
	In the fourth parameter, a very simple function prints the text "FINISHED" to the browser console once the transition is over. 
	
	> TIP: To read the message that is printed to the console, in Chrome go to **View > Developer > Javascript console**.

	The final parameter tells the component to perform the transition using an ease-out elastic interpolation, which results in a speed curve that goes from fast to slow and ends with a bouncy effect.

To learn more about the ECS Utils library, read its full documentation [here](https://github.com/decentraland/decentraland-ecs-utils).

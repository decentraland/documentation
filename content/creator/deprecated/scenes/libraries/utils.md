---
date: 2020-08-04
title: Utils library
description: A handy library to simplify many common tasks with the SDK
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/utils/
url: /creator/development-guide/utils
weight: 2
---

{{< hint danger >}}
**❗Warning**: This is a legacy page covering functionality with the old SDK version 6. See the latest version of this topic [here]({{< ref "/content/creator/sdk7/libraries/libraries.md" >}}).
{{< /hint >}}

The **Decentraland ECS Utils** library includes a number of helpful pre-built tools that include components, methods, and systems. They offer simple solutions to common scenarios that you're likely to run into while building scenes.

- [Gradual Movement](#gradual-movement)
  - [Move an entity](#move-an-entity)
  - [Follow a path](#follow-a-path)
  - [Follow a curved path](#follow-a-curved-path)
  - [Rotate an entity](#rotate-an-entity)
  - [Sustain rotation](#sustain-rotation)
  - [Change scale](#change-scale)
  - [Non-linear changes](#non-linear-changes)
  - [Callback on finish](#callback-on-finish)
- [Toggle](#toggle)
- [Time](#time)
  - [Delay a function](#delay-a-function)
  - [Delay removing an entity](#delay-removing-an-entity)
  - [Repeat at an Interval](#repeat-at-an-interval)
- [Triggers](#triggers)
  - [Trigger Component](#trigger-component)
  - [Trigger layers](#trigger-layers)
- [Conversions](#conversions)
  - [clamp](#clamp)
  - [map](#map)
  - [world position](#world-position)
  - [world rotation](#world-rotation)
- [Send requests](#send-requests)
- [Labels](#labels)
- [Debug helpers](#debug-helpers)
  - [Debug cube](#debug-cube)
- [Action sequence](#action-sequence)
  - [IAction](#iaction)
  - [Action Sequence Builder](#action-sequence-builder)
  - [Action Sequence System](#action-aequence-system)
  - [Full example](#full-example)

## Using the Utils library

To use any of the helpers provided by the utils library

1. Install it as an `npm` package. Run this command in your scene's project folder:

```
npm install @dcl/ecs-scene-utils -B
```

2. Run `dcl start` or `dcl build` so the dependencies are correctly installed.

3. Import the library into the scene's script. Add this line at the start of your `game.ts` file, or any other TypeScript files that require it:

```ts
import * as utils from '@dcl/ecs-scene-utils'
```

4. In your TypeScript file, write `utils.` and let the suggestions of your IDE show the available helpers.

## Gradual Movement

### Move an entity

To move an entity over a period of time, from one position to another, use the `MoveTransformComponent` component.

`MoveTransformComponent` has three required arguments:

- `start`: `Vector3` for the start position
- `end`: `Vector3` for the end position
- `duration`: duration (in seconds) of the translation

This example moves an entity from one position to another over 2 seconds:

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define start and end positions
let StartPos = new Vector3(1, 1, 1)
let EndPos = new Vector3(15, 1, 15)

// Move entity
box.addComponent(new utils.MoveTransformComponent(StartPos, EndPos, 2))

// Add entity to engine
engine.addEntity(box)
```

### Follow a path

To move an entity over several points of a path over a period of time, use the `FollowPathComponent` component.

`FollowPathComponent` has two required arguments:

- `points`: An array of `Vector3` positions that form the path.
- `duration`: The duration (in seconds) of the whole path.

This example moves an entity over through four points over 5 seconds:

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define the positions of the path
let path = []
path[0] = new Vector3(1, 1, 1)
path[1] = new Vector3(1, 1, 15)
path[2] = new Vector3(15, 1, 15)
path[3] = new Vector3(15, 1, 1)

// Move entity
box.addComponent(new utils.FollowPathComponent(path, 2))

// Add entity to engine
engine.addEntity(box)
```

### Follow a curved path

To move an entity following a curved path over a period of time, use the `FollowCurvedPathComponent` component.

The curved path is composed of multiple straight line segments put together. You only need to supply a series of fixed path points and a smooth curve is drawn to pass through all of these.

`FollowCurvedPathComponent` has three required arguments:

- `points`: An array of `Vector3` positions that the curve must pass through.
- `duration`: The duration (in seconds) of the whole path.
- `numberOfSegments`: How many straight-line segments to use to construct the curve.

{{< hint info >}}
**💡 Tip**: Each segment takes at least one frame to complete. Avoid using more than 30 segments per second in the duration of the path, or the entity will move significantly slower while it stops for each segment.
{{< /hint >}}

This example moves an entity over through a curve that's subdivided into 40 segments, over a period of 5 seconds. The curve passes through four key points.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define the positions of the path
let path = []
path[0] = new Vector3(1, 1, 1)
path[1] = new Vector3(1, 1, 15)
path[2] = new Vector3(15, 1, 15)
path[3] = new Vector3(15, 1, 1)

// Move entity
box.addComponent(new utils.FollowCurvedPathComponent(path, 5, 40))

// Add entity to engine
engine.addEntity(box)
```

The `FollowCurvedPathComponent` also lets you set:

- `turnToFaceNext`: If true, the entity will rotate on each segment of the curve to always face forward.
- `closedCircle`: If true, traces a circle that starts back at the beginning, keeping the curvature rounded in the seams too

### Rotate an entity

To rotate an entity over a period of time, from one direction to another, use the `rotateTransformComponent` component, which works very similarly to the `MoveTransformComponent` component.

`rotateTransformComponent` has three required arguments:

- `start`: `Quaternion` for the start rotation
- `end`: `Quaternion` for the end rotation
- `duration`: duration (in seconds) of the rotation

This example rotates an entity from one rotation to another over 2 seconds:

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define start and end directions
let StartRot = Quaternion.Euler(90, 0, 0)
let EndRot = Quaternion.Euler(270, 0, 0)

// Rotate entity
box.addComponent(new utils.RotateTransformComponent(StartRot, EndRot, 2))

// Add entity to engine
engine.addEntity(box)
```

### Sustain rotation

To rotates an entity continuously, use `KeepRotatingComponent`. The entity will keep rotating forever until it's explicitly stopped or the component is removed.

`KeepRotatingComponent` has one required argument:

- `rotationVelocity`: A quaternion describing the desired rotation to perform each second second. For example `Quaternion.Euler(0, 45, 0)` rotates the entity on the Y axis at a speed of 45 degrees per second, meaning that it makes a full turn every 8 seconds.

The component also contains the following method:

- `stop()`: stops rotation and removes the component from any entities its added to.

In the following example, a cube rotates continuously until clicked:

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform({ position: new Vector3(1, 1, 1) }))

// Rotate entity
box.addComponent(new utils.KeepRotatingComponent(Quaternion.Euler(0, 45, 0)))

// Listen for click
box.addComponent(
	new OnPointerDown(() => {
		box.getComponent(utils.KeepRotatingComponent).stop()
	})
)

// Add entity to engine
engine.addEntity(box)
```

### Change scale

To adjust the scale of an entity over a period of time, from one size to another, use the `ScaleTransformComponent` component, which works very similarly to the `MoveTransformComponent` component.

`ScaleTransformComponent` has three required arguments:

- `start`: `Vector3` for the start scale
- `end`: `Vector3` for the end scale
- `duration`: duration (in seconds) of the scaling

This example scales an entity from one size to another over 2 seconds:

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define start and end positions
let StartSize = new Vector3(1, 1, 1)
let EndSize = new Vector3(0.75, 2, 0.75)

// Move entity
box.addComponent(new utils.ScaleTransformComponent(StartSize, EndSize, 2))

// Add entity to engine
engine.addEntity(box)
```

### Non-linear changes

All of the translation components, the `MoveTransformComponent`, `rotateTransformComponent`, `ScaleTransformComponent`, and `FollowPathComponent` have an optional argument to set the rate of change. By default, the movement, rotation, or scaling occurs at a linear rate, but this can be set to other options.

The following values are accepted:

- `Interpolation.LINEAR`
- `Interpolation.EASEINQUAD`
- `Interpolation.EASEOUTQUAD`
- `Interpolation.EASEQUAD`

The following example moves a box following an ease-in rate:

```ts
box.addComponent(
	new utils.MoveTransformComponent(
		StartPos,
		EndPos,
		2,
		null,
		utils.InterpolationType.EASEINQUAD
	)
)
```

### Callback on finish

All of the translation components, the `MoveTransformComponent`, `rotateTransformComponent`, `ScaleTransformComponent`, `FollowPathComponent`, and `FollowCurvedPathComponent` have an optional argument that executes a function when the translation is complete.

- `onFinishCallback`: function to execute when movement is done.

The following example logs a message when the box finishes its movement. The example uses `MoveTransformComponent`, but the same applies to `rotateTransformComponent` and `ScaleTransformComponent`.

```ts
box.addComponent(
	new utils.MoveTransformComponent(StartPos, EndPos, 2, () => {
		log('finished moving box')
	})
)
```

The `FollowPathComponent` has a two optional arguments that execute functions when a section of the path is complete and when the whole path is complete.

- `onFinishCallback`: function to execute when movement is complete.

- `onPointReachedCallback`: function to execute when each section of the path is done.

The following example logs a messages when the box finishes each segment of the path, and another when the entire path is done.

```ts
box.addComponent(
	new utils.FollowPathComponent(
		path,
		2,
		() => {
			log('finished moving box')
		},
		() => {
			log('finished a segment of the path')
		}
	)
)
```

## Toggle

Use the `ToggleComponent` to switch an entity between two possible states, running a same function on every transition.

The `ToggleComponent` has the following arguments:

- `startingState`: Starting state of the toggle (ON or OFF)
- `onValueChangedCallback`: Function to call every time the toggle state changed.

It exposes three methods:

- `toggle()`: switches the state of the component between ON and OFF
- `isOn()`: reads the current state of the component, without altering it. It returns a boolean, where `true` means ON.
- `setCallback()`: allows you to change the function to be executed by `onValueChangedCallback`, for the next time it's toggled.

The following example switches the color of a box between two colors each time it's clicked.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define two different materials
let greenMaterial = new Material()
greenMaterial.albedoColor = Color3.Green()
let redMaterial = new Material()
redMaterial.albedoColor = Color3.Red()

// Add a Toggle component
box.addComponent(
	new utils.ToggleComponent(utils.ToggleState.Off, (value) => {
		if (value == utils.ToggleState.On) {
			//set color to green
			box.addComponentOrReplace(greenMaterial)
		} else {
			//set color to red
			box.addComponentOrReplace(redMaterial)
		}
	})
)

//listen for click on the box and toggle it's state
box.addComponent(
	new OnPointerDown((event) => {
		box.getComponent(utils.ToggleComponent).toggle()
	})
)

// Add entity to engine
engine.addEntity(box)
```

### Combine Toggle with Translate

This example combines a toggle component with a move component to switch an entity between two positions every time it's clicked.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// Create entity
const box = new Entity()

// Give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

//Define two positions for toggling
let Pos1 = new Vector3(1, 1, 1)
let Pos2 = new Vector3(1, 1, 2)

//toggle for wine bottle
box.addComponent(
	new utils.ToggleComponent(utils.ToggleState.Off, (value) => {
		if (value == utils.ToggleState.On) {
			box.addComponentOrReplace(
				new utils.MoveTransformComponent(Pos1, Pos2, 0.5)
			)
		} else {
			box.addComponentOrReplace(
				new utils.MoveTransformComponent(Pos2, Pos1, 0.5)
			)
		}
	})
)

//listen for click on the box and toggle it's state
box.addComponent(
	new OnPointerDown((event) => {
		box.getComponent(utils.ToggleComponent).toggle()
	})
)

// Add entity to engine
engine.addEntity(box)
```

## Time

These tools are all related to the passage of time in the scene.

### Delay a function

Add a `Delay` component to an entity to execute a function only after an `n` amount of milliseconds.

This example creates an entity that only becomes visible in the scene after 100000 milliseconds (100 seconds) have passed.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// create entity
const easterEgg = new Entity()

// give entity a shape and set invisible
const easterEggShape = new BoxShape()
easterEggShape.visible = false
easterEgg.addComponent(easterEggShape)

// add a delayed function
easterEgg.addComponent(
	new utils.Delay(100000, () => {
		easterEgg.getComponent(BoxShape).visible = true
	})
)

// add entity to scene
engine.addEntity(easterEgg)
```

To delay the execution of a task that isn't directly tied to any entity in the scene, create a dummy entity that only holds a `Delay` component.

### Delay removing an entity

Add an `ExpireIn` component to an entity to remove it from the scene after an `n` amount of milliseconds.

This example creates an entity that is removed from the scene 500 milliseconds after it's clicked.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// create entity
const box = new Entity()

// give entity a shape
box.addComponent(new BoxShape())

// add a function to run when clicked
box.addComponent(
	new OnPointerDown(() => {
		box.addComponent(new utils.ExpireIn(500))
	})
)

// add entity to scene
engine.addEntity(box)
```

### Repeat at an Interval

Add an `Interval` component to an entity to make it execute a same function every `n` milliseconds.

This example creates an entity that changes its scale to a random size every 500 milliseconds.

```ts
import * as utils from '@dcl/ecs-scene-utils'

// create entity
const box = new Entity()

// give entity a shape and transform
box.addComponent(new BoxShape())
box.addComponent(new Transform())

// add a repeated function
box.addComponent(
	new utils.Interval(500, () => {
		let randomSize = Math.random()
		box.getComponent(Transform).scale.setAll(randomSize)
	})
)

// add entity to scene
engine.addEntity(box)
```

To repeat the execution of a task that isn't directly tied to any entity in the scene, create a dummy entity that only holds an `Interval` component.

## Triggers

### Trigger Component

The trigger component can execute whatever you want whenever the player's position or the position of a specific entity or type of entity overlaps with an area.

The `TriggerComponent` has the following arguments:

- `shape`: Shape of the triggering collider area, either a cube or a sphere (`TriggerBoxShape` or `TriggerSphereShape`)
- `data`: An object of type `TriggerData` containing several optional parameters to configure the behavior of the trigger area.

The `TriggerData` type may contain the following parameters:

- `onCameraEnter`: Callback function for when the player enters the trigger area
- `onCameraExit`: Callback function for when the player leaves the trigger area
- `layer`: Layer of the Trigger, useful to discriminate between trigger events. You can set multiple layers by using a `|` symbol.
- `triggeredByLayer`: Against which layers to check collisions
- `onTriggerEnter`: Callback when an entity of a valid layer enters the trigger area
- `onTriggerExit`: Callback function for when an entity of a valid layer leaves the trigger area
- `enableDebug`: When true, makes the trigger area visible for debug purposes. Only visible when running a preview locally, not in production.

The following example creates a trigger that changes its position randomly when triggered by the player.

```ts
import * as utils from '@dcl/ecs-scene-utils'

//create entity
const box = new Entity()

//create shape for entity and disable its collision
box.addComponent(new BoxShape())
box.getComponent(BoxShape).withCollisions = false

//set transform component with initial position
box.addComponent(new Transform({ position: new Vector3(2, 1, 2) }))

// create trigger area object, setting size and relative position
let triggerBox = new utils.TriggerBoxShape()

//create trigger for entity
box.addComponent(
	new utils.TriggerComponent(
		triggerBox, //shape
		{
			onCameraEnter: () => {
				log('triggered!')
				box.getComponent(Transform).position = new Vector3(
					1 + Math.random() * 14,
					0,
					1 + Math.random() * 14
				)
			},
		}
	)
)

//add entity to engine
engine.addEntity(box)
```

{{< hint warning >}}
**📔 Note**: The trigger shape can be positioned or stretched, but it can't be rotated on any axis. This is a design decision taken for performance reasons. To cover a slanted area, we recommend adding multiple triggers if applicable.
{{< /hint >}}

Each trigger area has a shape for its area to check for collisions, which is completely independent of the visible shape of the entity. The shape of the area can either be determined by a `TriggerBoxShape` or a `TriggerSphereShape`. When instancing these, can set the scale and an offset position. By default, the trigger shape starts in the same position as the entity that has the `TriggerComponent`.

You can check where exactly the trigger area is and its scale by setting the `enableDebug` flag to true. You will then see this shape in the scene when running a preview. This debug shape is only visible in the context of a preview, not once the scene is deployed.

### Dissable a collision component

`TriggerComponent` components have an `enabled` property, which is set to `true` by default when creating it. You can use this property to disable the behavior of the component without removing it.

```TypeScript
box.getComponent(utils.TriggerComponent).enabled = false
```

### Set a custom shape for player

You can optionally configure a custom shape and size for the player's trigger area, according to your needs:

```ts
utils.TriggerSystem.instance.setCameraTriggerShape(
	new utils.TriggerBoxShape(
		new Vector3(0.5, 1.8, 0.5),
		new Vector3(0, -0.91, 0)
	)
)
```

Changing this configuration affects the behavior of all `onCameraEnter` and `onCameraExit` functions of all TriggerComponents in the scene.

### Trigger layers

You can define different layers (bitwise) for triggers, and set which other layers can trigger it.

The following example creates a scene that has:

- food (cones)
- mice (spheres)
- cats (boxes)

Food is triggered (or eaten) by both cats or mice. Also, mice are eaten by cats, so a mouse's trigger area is triggered by only cats.

Cats and mice always move towards the food. When food or mice are eaten, they respawn in a random location.

```ts
import * as utils from '@dcl/ecs-scene-utils'

//define layers
const foodLayer = 1
const mouseLayer = 2
const catLayer = 4

//define a reusable collision shape object
let triggerBox = new utils.TriggerBoxShape(Vector3.One(), Vector3.Zero())

//create food
const food = new Entity()
food.addComponent(new ConeShape())
food.getComponent(ConeShape).withCollisions = false
food.addComponent(
  new Transform({
    position: new Vector3(1 + Math.random() * 14, 0, 1 + Math.random() * 14)
  })
)
food.addComponent(new utils.TriggerComponent(
  triggerBox,
  {
	layer: foodLayer
	triggeredByLayer: mouseLayer | catLayer
	onTriggerEnter: () => {
	  food.getComponent(Transform).position = new Vector3(
	    1 + Math.random() * 14,
	    0,
	    1 + Math.random() * 14
	  )
	  mouse.addComponentOrReplace(
	    new utils.MoveTransformComponent(
		mouse.getComponent(Transform).position,
		food.getComponent(Transform).position,
		4
	    )
	  )
	  cat.addComponentOrReplace(
	    new utils.MoveTransformComponent(
		cat.getComponent(Transform).position,
		food.getComponent(Transform).position,
		4
	    )
	 )
       }
  }
))

//create mouse
const mouse = new Entity()
mouse.addComponent(new SphereShape())
mouse.getComponent(SphereShape).withCollisions = false
mouse.addComponent(
  new Transform({
    position: new Vector3(1 + Math.random() * 14, 0, 1 + Math.random() * 14),
    scale: new Vector3(0.5, 0.5, 0.5)
  })
)
mouse.addComponent(new utils.TriggerComponent(
  triggerBox,
  {
	layer: mouseLayer
	triggeredByLayer: catLayer
	onTriggerEnter: () => {
	  mouse.getComponent(Transform).position = new Vector3(
	    1 + Math.random() * 14,
	    0,
	    1 + Math.random() * 14
	  )
	  mouse.addComponentOrReplace(
	    new utils.MoveTransformComponent(
	      mouse.getComponent(Transform).position,
	      food.getComponent(Transform).position,
	      4
	    )
          )
        }
  }
))

//create cat
const cat = new Entity()
cat.addComponent(new BoxShape())
cat.getComponent(BoxShape).withCollisions = false
cat.addComponent(
  new Transform({
    position: new Vector3(1 + Math.random() * 14, 0, 1 + Math.random() * 14)
  })
)
cat.addComponent(new utils.TriggerComponen(
	triggerBox,
	{
		layer: catLayer
	}
))

//set initial movement for mouse and cat
mouse.addComponentOrReplace(
  new utils.MoveTransformComponent(
    mouse.getComponent(Transform).position,
    food.getComponent(Transform).position,
    4
  )
)
cat.addComponentOrReplace(
  new utils.MoveTransformComponent(
    cat.getComponent(Transform).position,
    food.getComponent(Transform).position,
    4
  )
)

//add entities to engine
engine.addEntity(food)
engine.addEntity(mouse)
engine.addEntity(cat)
```

## Conversions

This library includes a number of helpful functions for common value conversions.

### Clamp

Use the `clamp()` function to easily clamp possible values between a maximum and a minimum.

The `clamp()` function takes the following arguments:

- `value`: Input number to convert
- `min`: Minimum output value.
- `max`: Maximum output value.

The following example limits an incoming value between 5 and 15. If the incoming value is less than 5, it will output 5. If the incoming value is more than 15, it will output 15.

```ts
let input = 200
let result = utils.clamp(input, 5, 15)
log(result)
```

### Map

Use the `map()` function to map a value from one range of values to its equivalent, scaled in proportion to another range of values, using maximum and minimum.

The `map()` function takes the following arguments:

- `value`: Input number to convert
- `min1`: Minimum value in the range of the input.
- `max1`: Maximum value in the range of the input.
- `min2`: Minimum value in the range of the output.
- `max2`: Maximum value in the range of the output.

The following example maps the value _5_ from a scale of 0 to 10 to a scale of 300 to 400. The resulting value is 350, as it keeps the same proportion relative to the new maximum and minimum values.

```ts
let input = 5
let result = utils.map(input, 0, 10, 300, 400)
log(result)
```

### World position

If an entity is parented to another entity, or to the player, then its Transform position will be relative to its parent. To find what its global position is, taking into account any parents, use `getEntityWorldPosition()`.

The `getEntityWorldPosition()` function takes a single argument:

- `entity`: The entity from which to get the global position

The function returns a `Vector3` object, with the resulting position of adding the given entity and all its chain of parents.

The following example sets a cube as a child of the player, and logs its true position when clicked.

```ts
const cube = new Entity()
cube.addComponent(new Transform({ position: new Vector3(0, 0, 1) }))cube.addComponent(new BoxShape())
engine.addEntity(cube)
cube.setParent(Attachable.FIRST_PERSON_CAMERA)

cube.addComponent(
  new OnPointerDown(() => {
	log(getEntityWorldRotation(myCube))
  }))
```

### World rotation

If an entity is parented to another entity, or to the player, then its Transform rotation will be relative to its parent. To find what its global rotation is, taking into account any parents, use `getEntityWorldRotation()`.

The `getEntityWorldRotation()` function takes a single argument:

- `entity`: The entity from which to get the global rotation

The function returns a `Quaternion` object, with the resulting rotation of multiplying the given entity to all its chain of parents.

The following example sets a cube as a child of the player, and logs its true rotation when clicked.

```ts
const cube = new Entity()
cube.addComponent(new Transform({ position: new Vector3(0, 0, 1) }))cube.addComponent(new BoxShape())
engine.addEntity(cube)
cube.setParent(Attachable.FIRST_PERSON_CAMERA)

cube.addComponent(
  new OnPointerDown(() => {
	log(getEntityWorldRotation(myCube))
  }))
```

## Send requests

Use the `sendRequest()` function to easily send HTTP requests to APIs.

The `sendRequest()` function has a single required argument:

- `url`: The URL to send the request

```ts
async function request() {
	let response = await utils.sendRequest(
		'https://events.decentraland.org/api/events/?limit=5'
	)

	log(response)
}
```

{{< hint warning >}}
**📔 Note**: The sendRequest() function is asynchronous, since it must wait for the external server to respond back before it can return a response. If you need your code to access the data on the request's response, you must use the sendRequest() within an `async` block of code, and add an `await` to the function.
{{< /hint >}}

The `sendRequest()` function also lets you use the following arguments, for sending more advanced requests:

- `method`: The HTTP method to use. `GET` is the default, other common options are `POST`, `PUT`, and `DELETE`.
- `headers`: The HTTP headers of the request, as a JSON object.
- `body`: The body of the request, as a JSON object.

```ts
async function request() {
  let response = await utils.sendRequest(
  	'https://jsonplaceholder.typicode.com/posts',
    'POST',
    {
      'content-type': 'application/json',
    },
    {
      content: 'My test JSON',
    }
}
```

## Labels

Add a text label floating over an entity using `addLabel()`.

The `addLabel()` function has just two required arguments:

- `text`: The string of text to display
- `parent`: The entity to set the label on

```ts
const cube = new Entity()
cube.addComponent(new Transform({ position: new Vector3(8, 1, 8) }))
cube.addComponent(new BoxShape())
engine.addEntity(cube)

utils.addLabel('Random Cube', cube)
```

The `addLabel()` function also lets you set the following:

- `billboard`: If true, label turns to always face player. True by default.
- `color`: Text color. Black by default.
- `size`: Text font size, 3 by default.
- `textOffset`: Offset from parent entity's position. By default 1.5 meters above the parent.

{{< hint info >}}
**💡 Tip**: The `addLabel()` function returns the created entity used for the text. You can then tweak this entity in any way you choose.
{{< /hint >}}

## Debug helpers

### Debug cube

Render a simple clickable cube to use as a trigger when debugging a scene with `addTestCube()`.

{{< hint warning >}}
**📔 Note**: The test cube is only shown in preview, unless configured to appear also in production.
{{< /hint >}}

The `addTestCube()` function has just two required arguments:

- `pos`: The position, rotation and/or scale of the cube, expressed as a TransformConstructorArgs object, as gets passed when creating a `Transform` component.
- `triggeredFunction`: A function that gets called every time the cube is clicked.

```ts
utils.addTestCube({ position: new Vector3(2, 1, 2) }, () => {
	log('Cube clicked')
})
```

The `addTestCube()` function also lets you set the following:

- `label`: An optional label to display floating over the cube
- `color`: A color for the cube's material.
- `sphere`: If true, it renders as a Sphere instead of a cube.
- `noCollider`: If true, the cube won't have a collider and will let players walk through it.
- `keepInProduction`: If true, it will be visible for players in-world once the scene is deployed. Otherwise, the cube is only present when previewing he scene locally.

{{< hint info >}}
**💡 Tip**: The `addTestCube()` function returns the created entity for the cube. You can then tweak this entity in any way you choose. `addTestCube()` is an async function (because the function first checks if you're in preview or in production). If you need the function to return the cube (instead of a promise of a cube) use it inside an async block of code with an await on the `addTestCube()` function.
{{< /hint >}}

```ts
async function addMyCube() {
	myCube = await utils.addTestCube({ position: new Vector3(0, 0, 1) }, () => {
		log('Cube clicked')
	})
}
```

## Action sequence

Use an action sequence to play a series of actions one after another.

### IAction

The `IAction` interface defines the actions that can be added into a sequence. It includes:

- `hasFinished`: Boolean for the state of the action, wether it has finished its execution or not.
- `onStart()`: First method that is called upon the execution of the action.
- `update()`: Called on every frame on the action's internal update.
- `onFinish()`: Called when the action has finished executing.

### Action Sequence Builder

This object creates action sequences, using simple building blocks.

The `SequenceBuilder` exposes the following methods:

- `then()`: Enqueue an action so that it's executed when the previous one finishes.
- `if()`: Use a condition to branch the sequence
- `else()`: Used with if() to create an alternative branch
- `endIf()`: Ends the definition of the conditional block
- `while()`: Keep running the actions defined in a block until a condition is no longer met.
- `breakWhile()`: Ends the definition of the while block

### Action Sequence System

The action sequence system takes care of running the sequence of actions. The `ActionsSequenceSystem` exposes the following methods:

- `startSequence()`: Starts a sequence of actions
- `setOnFinishCallback()`: Sets a callback for when the whole sequence is finished
- `isRunning()`: Returns a boolean that determines if the sequence is running
- `stop()`: Stops a running the sequence
- `resume()`: Resumes a stopped sequence
- `reset()`: Resets a sequence so that it starts over

### Full example

The following example creates a box that changes its scale until clicked. Then it resets its scale and moves.

```ts
import * as utils from '@dcl/ecs-scene-utils'

//set clicked flag
let boxClicked = false

//create box entity
const box = new Entity()
box.addComponent(new BoxShape())
box.addComponent(new Transform({ position: new Vector3(14, 0, 14) }))
box.addComponent(new OnPointerDown(() => (boxClicked = true)))
engine.addEntity(box)

//Use IAction to define action for scaling
class ScaleAction implements utils.ActionsSequenceSystem.IAction {
	hasFinished: boolean = false
	entity: Entity
	scale: Vector3

	constructor(entity: Entity, scale: Vector3) {
		this.entity = entity
		this.scale = scale
	}

	//Method when action starts
	onStart(): void {
		const transform = this.entity.getComponent(Transform)
		this.hasFinished = false

		this.entity.addComponentOrReplace(
			new utils.ScaleTransformComponent(
				transform.scale,
				this.scale,
				1.5,
				() => {
					this.hasFinished = true
				},
				utils.InterpolationType.EASEINQUAD
			)
		)
	}
	//Method to run on every frame
	update(dt: number): void {}
	//Method to run at the end
	onFinish(): void {}
}

//Use IAction to define action for movement
class MoveAction implements utils.ActionsSequenceSystem.IAction {
	hasFinished: boolean = false
	entity: Entity
	position: Vector3

	constructor(entity: Entity, position: Vector3) {
		this.entity = entity
		this.position = position
	}

	//Method when action starts
	onStart(): void {
		const transform = this.entity.getComponent(Transform)

		this.entity.addComponentOrReplace(
			new utils.MoveTransformComponent(
				transform.position,
				this.position,
				4,
				() => {
					this.hasFinished = true
				}
			)
		)
	}
	//Method to run on every frame
	update(dt: number): void {}
	//Method to run at the end
	onFinish(): void {}
}

//Use sequence builder to create a sequence
const sequence = new utils.ActionsSequenceSystem.SequenceBuilder()
	.while(() => !boxClicked)
	.then(new ScaleAction(box, new Vector3(1.5, 1.5, 1.5)))
	.then(new ScaleAction(box, new Vector3(0.5, 0.5, 0.5)))
	.endWhile()
	.then(new ScaleAction(box, new Vector3(1, 1, 1)))
	.then(new MoveAction(box, new Vector3(1, 0, 1)))

//Create a sequence system, and add it to the engine to run the sequence
engine.addSystem(new utils.ActionsSequenceSystem(sequence))
```

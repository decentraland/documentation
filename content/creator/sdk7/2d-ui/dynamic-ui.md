---
date: 2022-10-20
title: Dynamic UIs
description: Learn how to make UIs dynamic, responding to changes in data.
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/dynamic-ui/
weight: 2
---


You can define a UI that includes dynamic elements, that are updated on every tick. You only need to handle the updating the variable that represents this data, and the UI will adapt in response to the new values.

This is very useful for including elements like a timer, a player's score, etc. But you can even take this a step forward and define entire UI structures based on state.

## Reference variables

You can simply reference a variable in any property of one of the components in a uiEntity. As the variable changes value, the UI will adapt accordingly.

The example below defines a variable `playerCurrentPosition` and references it as part of a string in a `uiText` component. A system then updates the value of this variable on every tick, using the player's current position. As the value of the variable changes, the UI updates accordingly, without ever needing to explicitly modify the UI.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

// define variable
let playerCurrentPosition: string = ""

// draw UI
ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
			width: '100%',
			height: '100px',
			justifyContent: 'center',
			alignItems: 'center',
    }}
    uiText={{ value: `Player: `+  playerCurrentPosition, fontSize: 40 }}
    uiBackground={{ color: Color4.create(0.5, 0.8, 0.1, 0.6) }}
  />
))

// system to update variable
engine.addSystem(() => {
  const playerPosition = Transform.getOrNull(engine.PlayerEntity)
  if (!playerPosition) return
  const { x, y, z } = playerPosition.position
  playerCurrentPosition =  `{x: ${x.toFixed(2)}, y: ${y.toFixed(2)}, z: ${z.toFixed(2)} }`
})
```

In the example above, you could also include the variable as part of the string, by signaling the variable with a `$`.

```ts
uiText={{
	value: `Player: $playerCurrentPosition`,
	fontSize: 40
}}
```


## Call functions from inside a UI

You can also call a function from inside a JSX definition, returning a value to use in a property of the UI. Functions that are called from inside this JSX definition are called recurrently, on every tick of the game loop.

In the example below, a `uiText` component calls the `getPlayerPosition()` function to define part of the string to display.

This example is similar to the one in the previous section, but by calling a function from inside the UI definition we avoid declaring a separate variable and defining a system to alter that variable. Note that `getPlayerPosition()` gets called on every tick of the game loop, without needing to explicitly declare a system.


```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: '100%',
      height: '100px',
      justifyContent: 'center',
      alignItems: 'center',
    }}
    uiText={{ value: `Player: `+  getPlayerPosition(), fontSize: 40 }}
    uiBackground={{ color: Color4.create(0.5, 0.8, 0.1, 0.6) }}
  />
))

function getPlayerPosition(){
  const playerPosition = Transform.getOrNull(engine.PlayerEntity)
  if (!playerPosition) return
  const { x, y, z } = playerPosition.position
  return `{x: ${x.toFixed(2)}, y: ${y.toFixed(2)}, z: ${z.toFixed(2)} }`
}
```


## Toggle a UI on and off

The easiest way to toggle a UI on and off is to use a variable for the value of the `display` property in an entity's `uiTransform`. The `display` property makes a UI entity and all of its children invisible if set to `none`.

The following example uses a variable to set the `display` field of a part of the UI. The value of this variable can be toggled by clicking on another UI element.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

// Variable to reflect current state of menu visibility
var isMenuVisible: boolean = false

ReactEcsRenderer.setUiRenderer(() => (
   // parent
   <UiEntity>
      // Menu
      <UiEntity
       uiTransform={{
          width: '80%',
          height: '100px',
          alignContent: 'center',
          justifyContent: 'center',
          display: isMenuVisible ? 'flex': 'none'
        }}
         uiText={{
          value: "Menu",
          fontSize: 30
        }}
        uiBackground={{ color: Color4.Green() }}
      />
      // button
      <UiEntity
        uiTransform={{
          width: 100,
          height: 30,
          margin: { top: '35px', left: '500px' }
        }}
        uiText={{
          value: "Toggle Menu",
          fontSize: 40
        }}
        uiBackground={{ color: Color4.Red() }}
        onClick = {{toggleMenuVisibility}}
      />
   </UiEntity>
))

// Function to toggle the state of the menu
function toggleMenuVisibility(){
  isMenuVisible = !isMenuVisible
}
```

<!-- TODO: Make example pretty, with better positioning of entities -->





## Dynamic UI entities

The examples in the sections above show how to dynamically change a single property in an entity, but you can also define entire structures of entities that can scale based on dynamically changing data. This kind of pattern is common in web development when using libraries like React, and is extremely powerful. With this you can define extremely flexible and scalable UI applications.

The following example lists the ids of all entities in the scene that have a `MeshRenderer` and `Transform`. It creates a `uiText` for each. As the scene's content changes, the list of UI entities also adapts on every tick.

```ts
import { ReactEcsRenderer} from '@dcl/sdk/react-ecs'

ReactEcsRenderer.setUiRenderer(() => (
  <UiEntity
    uiTransform={{
      width: '100%',
      height: '300px',
      justifyContent: 'center',
      alignItems: 'center',
    }}
    uiBackground={{ color: Color4.create(0.5, 0.8, 0.1, 0.6) }}
  >
    <UiEntity>
      {generateText()}
    </UiEntity>
  </UiEntity>
))


function generateText(){
  return Array.from(engine.getEntitiesWith(
    MeshRenderer,
    Transform
  )).map(([entity]) => <TextComponent value={entity.toString()} key={entity} /> )
}


function TextComponent(props: { value: string; key: string | number }) {
  return <UiEntity
    key={props.key}
    uiTransform={{ width: 80, height: 20 }}
    uiText={{ value: props.value, textAlign: 'middle-center', fontSize: 12 }}
    uiBackground={{ color: { r: 255, g: 45, b: 85, a: 1 } }}
  />
}
```



<!-- TODO: explain how `key` is used
  to give an element in a query a reference
  required when iterating over a query of elements
Only used for recursive react-like things with queries -->
---
date: 2025-07-12
title: Skybox control
description: Change the skybox time
categories:
  - development-guide
type: Document
url: /creator/development-guide/sdk7/skybox-control/
weight: 16
---

You can change how a player sees the skybox whenever they are standing in your scene, this also affects the hue and direction of the global lighting.

The sky in Decentraland follows a default day/night cycle where 1 minute passes each second, so a full cycle takes 24 minutes to complete. If the scene is not enforcing any fixed time of day, then players are also able to switch to a particular time of day by changing a slider in their UI.

Whenever players enter a scene with a different time of day, or the scene changes the time of day dynamically, the skybox transitions smoothly over a few seconds to this new value.

## Fixed time of day

To set the skybox in your scene to a fixed time of day, add the following section to your `scene.json` at root level:

```json
 "skyboxConfig": {
    "fixedTimeOfDay": 36000
  }
``` 

The number refers to the number of seconds since the start of the day, ranging from 0 (that refers to _00:00_) to 86400 (that refers to _24:00_). Any number higher than 86400 is interpreted also as midnight.

Here are some more examples of valid values:

- 0 seconds  =>   _00:00_
- 21600 seconds   =>   _06:00_
- 43200 seconds    =>   _12:00_
- 64800 seconds    =>   _18:00_
- 86400 seconds    =>   _24:00_

## Reading the time of day

You can read the time of day from your scene code using the `getWorldTime()` function.

```ts
import { getWorldTime } from '~system/Runtime'

executeTask(async () => {
  let time = await getWorldTime({})
  console.log(time.seconds)
})
```

The function returns a number between 0 and 86400, where 0 is midnight and 86400 is 24:00. This value is updated if the scene changes the time of day dynamically or if the player changes the time of day in the UI.

<!--
## Changing the time of day dynamically

You can change the time of day dynamically using the 

```ts
import { setWorldTime } from '~system/Runtime'

setWorldTime({ seconds: 36000 })
```

-->
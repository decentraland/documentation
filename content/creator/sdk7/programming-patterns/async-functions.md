---
date: 2018-02-25
title: Asynchronous code
description: Learn when and how to run asynchronous functions in your scene's code.
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/async-functions/
  - /creator/development-guide/async-functions
url: /creator/development-guide/sdk7/async-functions/
weight: 1
---

## Overview

Most of the code in your scene runs synchronously using a single thread. That means that commands are executed sequentially line by line. Each command must first wait for the previous command to finish executing before it can start.

Even the functions in your scene's systems are executed one by one, following a [priority order]({{< ref "/content/creator/sdk7/architecture/systems.md#system-execution-order">}}).

Running code synchronously ensures consistency, as you can always be sure you'll know the order in which the commands in your code run.

On the other hand, your scene needs to be updated many times per second, building the next frame. If a part of your code takes too long to respond, then the whole main thread is stuck and this results in lagging frame rates.

That's why, in some cases you want some commands to run asynchronously. This means that you can start off a task in a new thread, and meanwhile the main thread can keep running over the the next lines of code.

This is especially useful for tasks that rely on external services that could take time to respond, as you don't want that idle time waiting for that response to block other tasks.

For example:

- When retrieving data from a REST API
- When performing a transaction on the blockchain

{{< hint warning >}}
**📔 Note**: Keep in mind that several frames of your scene might be rendered before the task finishes executing. Make sure your scene's code is flexible enough to handle the in-between scenarios while the asynchronous task is being completed.
{{< /hint >}}

## Run an async function

Mark any function as `async` so that it runs on a separate thread from the scene's main thread every time that it's called.

```ts
// declare async function
async function myAsyncTask() {
	// run function's steps
}

// call async function
myAsyncTask()

// rest of the code keeps being executed
```

## The executeTask function

The `executeTask()` function executes a lambda function asynchronously, in a separate thread from the scene's main thread. `executeTask()` allows us to declare and execute the function all in one same statement.

```ts
executeTask(async () => {
	let data = await myAsyncTask()
	console.log(data)
})

// rest of the code keeps being executed
```

## The then function

The `then` function takes in a lambda function as an argument, that only gets executed once the prior statement is finished. This lambda function can optionally have inputs that are mapped from whatever the prior statement returns.

```ts
myAsyncTask().then((data) => {
	console.log(data)
})
```

{{< hint warning >}}
**📔 Note**: It's generally better to use the `executeTask` approach rather than the `then` function. In this example, the scene won't be considered fully loaded by the explorer till the `myAsyncTask()` function is completed, which may affect load times. Also, if relying too much on the `then` function at multiple nested levels, you can end up with what's known as "callback hell", where the code can become very hard to read and maintain.
{{< /hint >}}

## PointerEvents and RayCast functions

When your scene uses a `PointerEvent` or a `RayCast` component, the calculations of collisions are carried out async in the engine. The engine then returns a results event to the scene, which can arrive one or several ticks of the game loop later than when the event was invoked.

You then need to create a system to process these results in the frame when they arrive.

{{< hint warning >}}
**📔 Note**: If you handle clicks via the [**Register a callback**]({{< ref "/content/creator/sdk7/interactivity/button-events/register-callback.md" >}}) approach, you don't need to explicitly create a system to handle this, but the same occurs in the background.
{{< /hint >}}

See [click events]({{< ref "/content/creator/sdk7/interactivity/button-events/click-events.md" >}}) and [raycasting]({{< ref "/content/creator/sdk7/interactivity/raycasting.md" >}}).

{{< hint info >}}
**💡 Tip**: If the processing of the results of a raycast takes a lot of calculations (like running a path-finding algorithm) you might want to run that computation in an asynchronous function.
{{< /hint >}}

## The await statement

An `await` statement forces the execution to wait for a response before moving over to the next line of code. `await` statements can only be used inside an async block of code.

```ts
// declare function
async function myAsyncTask() {
	try {
		let response = await fetch(callUrl)
		let json = await response.json()
		console.log(json)
	} catch {
		console.log('failed to reach the URL')
	}
}

// call function
myAsyncTask()

// Rest of the code keeps being executed
```

The example above executes a function that includes a `fetch()` operation to retrieve data from an external API. The `fetch()` operation is asynchronous, as we can't predict how long the server will take to respond. However, the next line needs the output of this operation to be ready before we can parse it as a json. The `await` statement here ensures that the next line will only run once that operation has returned a value. Similarly, the `response.json()` function is also asynchronous, but the next line needs the json to be parsed before it can log it. The second `await` statement forces the next line to only be called once the parsing of the json is finished, however long it takes.

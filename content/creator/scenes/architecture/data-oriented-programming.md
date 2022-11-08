---
date: 2022-07-15
title: Data oriented programming
description: The Data Oriented Programming is a powerful approach to programming gets the most out of performance.
categories:
  - development-guide
type: Document
url: /creator/development-guide/data-oriented-programming
---


Data Oriented Programming is a powerful approach to programming that results in big improvements to performance. It focuses on treating _data_ as the cental element, all else is organized around it, to either access or modify that data. This approach is also very multiplayer friendly, as it makes the data that needs to be synchronized between players easier and faster to access.

Data Oriented Programming encourages you to think about everything in your scene as data that needs to be copied and mutated throughout the various systems. The main benefit of this approach is on optimizing the speed at which data can be read from memory, which is often the main bottleneck while running modern applications and games. Adopting this approach very often results in improvements that are very noticeable.

Because of this remarkable improvement in performance, much of the game making industry has been shifting towards adopting this approach over the last few years.

## How it looks

Data Oriented Programming is different from Object Oriented Programming, an approach that many developers are currently familiar with. In Object Oriented Programming, the code is structured following abstractions that try to replicate real-world constructs: objects. Each of these objects can hold both data and functionality. Applications that use this approach are often easy to plan out conceptually, but also more inefficient to run.

In Data oriented Programming, data is not structured around objects, it's structured to optimize its ease of access. The real-world constructs that the data represents play no part in the different flows that mutate that data.

The Entity Component System (ECS) model that the Decentraland SDK is built upon is very compatible with the Data Oriented Programming approach. Each component is part of a structured collection of data. Components belong to an entity by reference, but the data is not structured around the entity, the data is structured as a collection of similar components. For example, all `Transform` components in a scene are equal. One of these transforms might belong to the model of your main building, another to a glass that is a child of a table. The systems in the scene then processes the list of `Transform` components one by one, without making any distinctions. All `Transform` components have the same fields and undergo the same checks.

Imagine a scene that has a dozen doors that can either be open or closed. You can represent the state of all of these doors as a simple "isOpen" component that holds a boolean value. If "isOpen" is true the door should be open; if false the door should be closed. If a player clicks on a door, it should toggle state, and other players should also see it toggle. While your scene is processing a change in the state of a door, and syncing it with other players, the scene doesn't really care about what "isOpen" represents. The whole set of components is just a collection of booleans that need to be synchronized with other players. A separate system on your scene can then take care of regularly matching the state of each "isOpen" to its corresponding door's rotation.

Data Oriented Programming is not necessarily harder, but it's a different approach that needs to be learnt and adopted. Developers that are not used to this approach might need some time to get familiar with it, we encourage that you explore and play with examples to get a better feel.

## Why it works

To understand why data oriented programming makes such a big difference, we need to take a look at the hardware.

When the processor needs to fetch data from memory, it fetches a whole chunk of data into cache, including data that just happens to be written onto memory next to the value we wanted. The more your code can make use of data that is already in cache, the faster your code will run.

Imagine the machine's memory is a literal warehouse, where data is stored in lots of stacked boxes. Whenever we need a certain bit of data, we need to call a forklift to go fetch the box where that data is located, and bring it over to the front desk for inspection. That front desk can only fit a couple of boxes at a time, so you can't keep much data around.

It takes a long time for the forklift to go over to the back of the warehouse and bring us a box. If the data you want from these boxes is scattered, that will mean asking the forklift to do a lot of trips. Most of the time, you'll be twiddling your thumbs standing by the front desk, waiting for the next box you requested to arrive.

You can avoid much of that wasted time if you stacked these boxes intelligently, and packed data so that the things you will likely need at the same time are mostly grouped together. If you group data cleverly, you'll often find that the next thing you need is already in one of the boxes in the front desk. You'll be able to jump right into it without bothering the fork lift operator.

For example, if you have a scene that needs to fetch the state of a door to check if it's open or closed, the hardware is not just fetching the value of the particular boolean that describes the state of that door, it's fetching a whole lot of other data that may or may not be relevant.

Suppose that your scene has a system that needs to update the open/door state of a dozen doors, once every frame. If your code is organized following an Object Oriented Programming approach, there's no telling how the different relevant bits of information may be grouped. Maybe a "box" from our warehouse holds door A's "isOpen" state and also holds door A's texture and the audio it plays when opening. You might have to make a trip to fetch a new "box" of data for each of the dozen doors. And of course, this whole process needs to happen again on every frame. So that's 360 (30 x 12) metaphorical trips to the back of the warehouse per second, even when none of the doors have changed state.

If your code follows a Data Oriented approach, on the other hand, it's very likely that all those 12 booleans will be in the same box. This is because all these booleans are part of a single array that was recorded into memory at once. You're never explicitly organizing how this data fits into memory, so in the worst case scenario the array could end up split across two boxes. But even in that worst scenario, 2 trips is much better than 12.

Checking the state of every door on every frame sounds like a lot of work, but it's actually super quick if all the data is already in the memory cache. If your data is neatly organized, your scene can run processes like these over a lot of entities and still run really fast.


---
date: 2022-10-01
title: Voice Chat
aliases:
  - /docs/voice-chat
  - /voice-chat
  - /docs/voice-chat
  - /decentraland/voice-chat
description: In-World Voice Chat
categories:
  - Decentraland
type: Document
url: /player/general/in-world-features/voice-chat
weight: 20
---

### Accessing the chat

When you enter the world, the voice chat will be automatically connected. You can confirm that voice chat is connected, when you see this UI in the taskbar.

<img src="/images/media/voice-chat-1.png" style="margin: 2rem auto; display: block;width: 90%;"/>

### Sending audio message

By keeping pressed the microphone button (or the T key), you will be able to send audio messages to the nearby users also connected to the Voice Chat.
It is possible that the first time you do this, the browser will ask you about microphone permissions. You will see a browser’s modal similar to this

<img src="/images/media/voice-chat-2.png" style="margin: 2rem auto; display: block;width: 90%;"/>

> You have to grant the website required permission to be able to use voice chat feature

### Seeing nearby users

You can see all nearby users by opening the Voice Chat window. For that, you will have to click on the headphones button in the taskbar and this window will be showed
<img src="/images/media/voice-chat-3.png" style="margin: 2rem auto; display: block;width: 90%;"/>

### Filtering users I want to listen to

At the top left corner of the Voice Chat window you will find a selector with which allow you to choose which people you want to listen to

- **All** You will listen to everyone connected to the Voice Chat.
- **Verified Users** You will only listen to those users with a verified name in Decentraland.
- **Friends** You will only listen to your friends.

### Muting unwanted users

You will be able to mute/unmute nearby users. For that you can click on the speaker button you will find next to the name of each user. Remember that the mute status of each user will be remembered in your next sessions in Decentraland.
You will also be able to mute/unmute ALL the nearby users using the top right `MUTE ALL` toggle.

### Leaving chat

By clicking on the `LEAVE` button (you can find it in the top right corner of the Voice Chat window or in the right side of the Voice Chat bar), you will be disconnected from the Voice Chat. From this point on you won’t hear anything from the nearby users.
You will know it is disconnected because you will see this Voice Chat bar in the taskbar

<img src="/images/media/voice-chat-4.png" style="margin: 2rem auto; display: block;width: 90%;"/>

Clicking on the `JOIN VOICE CHAT` button, you will be connected again.

# Troubleshooting

### The Voice Chat get disconnected when I try to send audio message

For some users, when they try to send an audio message for the first time, may receive this warning message in the top of the screen.

<img src="/images/media/voice-chat-5.png" style="margin: 2rem auto; display: block;width: 90%;"/>

If you experience this, you will notice that just after that happens the Voice Chat is disconnected. Simply click on the `JOIN VOICE CHAT` button in the taskbar and it will be connected again.

<img src="/images/media/voice-chat-6.png" style="margin: 2rem auto; display: block;width: 90%;"/>

### My Voice Chat is connected but I can’t send neither hear audio messages

- **Check your microphone device is correctly connected<br/>**
Sometimes we can notice that we can hear other users but they don’t hear us. So, first of all, please check your microphone is correctly connected to your computer and, if needed, do a quick test in any recording audio software to be sure your microphone is capturing your voice correctly.
- **Check the mute/unmute status of the nearby users<br/>**
Check if you have some users (or even all of them) muted. It does not usually happen but, as the mute/unmute status of the users is stored between sessions, could be a possible reason.
- **Check the mute/unmute status of your tab in your browser<br/>**
You might have forgotten that your tab is muted in the browser, check the settings.
- **Microphone permissions wrongly configured<br/>**
Another possible cause could be not having the microphone permissions allowed in your browser. 
This could happen in case you missed the permissions popup the first time the browser asked you for, or maybe you forgot to apply any action when the browser asked you. 
In any case, we can check this configuration again by opening our browser’s configuration: **Settings** → **Privacy and Security** → **Site Settings** and look for `play.decentraland.org` in **Recent activity**. 
You will see a list of permissions

<img src="/images/media/voice-chat-7.png" style="margin: 2rem auto; display: block;width: 90%;"/>

> It is important that, after doing this, you close and re-open the browser to apply the changes. From this point on you should be able to send and receive audio messages correctly.


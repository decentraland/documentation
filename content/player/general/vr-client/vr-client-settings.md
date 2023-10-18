---
date: 2023-09-21
title: VR Client Login Screen
aliases:
description: Intro to the DCL VR Client.
categories:
  - Decentraland
type: Document
url: /player/general/vr-client/vr-client-settings
weight: 4
---

### **Startup Screen**

The Startup Screen provides methods to sign into Decentraland, as well as some customization options for those that want to utilize advanced functionality.
You will also be able to sign in with your wallet, or opt to play as a guest. 

<b>Wallet </b>

<img src="/images/media/VRClient/LoginScreen.png" style="margin: 2rem auto; display: block;width: 70%;"/>

 Wallet options that work within the VR client is:<br>
* **Fortmatic:** Allows signing in using an email or phone number.<br>
* **WalletConnect:** Allows signing in using a QR code.  Works with the Metamask phone application.  PCVR duplicates the QR code to the monitor screen.  Android requires scanning the QR code through the headset lens. 
* **CoinBase:** Allows signing in using a QR code.  Works with the Coinbase phone application. PCVR duplicates the QR code to the monitor screen.  Android requires scanning the QR code through the headset lens.

### **Settings Screen**
<img src="/images/media/VRClient/VRSettingsButton.png" style="margin: 2rem auto; display: block;width: 20%;"/>

<img src="/images/media/VRClient/StartupSettings.png" style="margin: 2rem auto; display: block;width: 70%;"/>

Some of these settings require restarting the application after modifying to apply. <br>
<B>Use New UI:</B> allows you to switch between the graphical login and browser view. Helpful if something in the UI breaks.<br>
<B>Open Browser on Start:</b> Disabling this requires opening the browser manually. Do not do on Android native build.<br>
<B>Internal Browser:</b>On uses the embedded webview. Off uses your default browser.  Do not turn off for Android native build.<br>
<B>WebSocket SSL:</b>Turn on to use SSL certificate for .org base url mode.  Turn off for Android native build<br>
<B>BaseURLMode:</b>Allows to set to use .org or .zone website.  play.decentraland.org requires SSL turned on. play.decentraland.zone requires SSL turned off  Android native build only works with .zone with ssl turned off.<br>
<B>Network:</b>Mainnet or Sepolia etherium networks<br>
<B>Start in coords:</b>Initial coordinate settings<br>
<B>Solo Scene:</b>If enabled, only the single parcel will load<br>
<B>Disable Asset Bundles:</b>Asset Bundles are optimized models to import for each scene. Turning this on will default to importing the original gltf models. Asset bundles are not built for android native builds currently so enabling this will help models load in faster.<br>
<B>Kernel Version:</b>Setting a specific kernel version will use that version. This might be helpful if something changes in the future that breaks functionality between new versions of the VR client<br>
<B>Catalyst:</b>If you have a personal catalyst set up running your own customized version of Decentraland, you can set it here<br>
<B>Realm:</b>You can set your default realm or automatically load into your own world by setting this field. <br>
<B>Use Custom Content Server:</b>Enabling this will allow you to connect to a specific content server if you build your own asset bundle server.<br>
<B>Custom Content Server:</b>the URI to your custom content server<br>
<B>Enable Debug Mode:</b>Enables Decentralands internal debugger<br>
<B>Debug Panel Mode:</b>Debugs the Scene or the Engine<br>
<B>Multithreaded Download:</b>Enabled allows multithreaded download of scene contents. This will speed up loading based on network and hardware capabilities.  It is generally advised to allow this.<br>
<B>Disable GLTF Download Throttle:</b>Turning this on removes the thread count limit which allows faster loading, but can cause instability based on your system.<br>
<B>Restart Application to Apply Changes:</b>This closes the application so you can re-open it to open a session running the changed settings.<br>
<B>Reset All Settings:</b>This resets the settings to the default settings.  Settings can also be manually modified or backed up in your applications persistent data folder.  For PCVR this will be "C:\Users\<user>\AppData\LocalLow\Decentraland\Decentraland\vrsettings1.2.dat"<br>

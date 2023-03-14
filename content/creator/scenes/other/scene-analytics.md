---
date: 2022-06-20
title: Scene analytics
description: Track player analytics for your scene
categories:
  - development-guide
type: Document
aliases:
  - /development-guide/scene-analytics/
url: /creator/development-guide/scene-analytics
---

As a creator, it's very valuable to track player visits and the way in which players interact with your scene. Instead of assuming, you can obtain real data and make informed decisions while iterating on your designs.

- The [Atlas Corporation](https://atlascorp.io) built the [Atlas Analytics](https://analytics-app.atlascorp.io) platform for use in Decentraland scenes. This solution is built by Decentraland builders, for Decentraland builders.

	Through adding a [single file](https://gitlab.com/atlas-corporation/atlas-analytics) to your scene, you can access your scene's analytics dashboard [which you can find here](https://analytics-app.atlascorp.io). You can use your scene.json file to govern access to your scene's analytics dashboards. By default, the owner of the land will have access. To grant access to another user, assign their wallet in the tags field of your scene.json file with an "atlas" tag as follows:

	`"tags": [
	    "atlas:0xE400A85a6169bd8BE439bB0DC9eac81f19f26843",
	    "atlas:0x3fB38CEe8d0BA7Dcf59403a8C397626dC9c7A13B"
	 ]`,

	Alternatively, you may opt to grant public access to your scenes using the following in your tags field:

	`"tags" = ["atlas:*"]`

	Check out the [Atlas Analytics documentation](https://atlas-corporation.gitbook.io/atlas-analytics/) for detailed instructions about how to 		implement it in your scenes.
	
- The [Decentraland Builder](https://builder.decentraland.org) exposes basic data about user weekly visits to your scenes. This data is only available to users with ownership or operator rights on these parcels, and there is no historical record for checking past periods. As a scene creator you don't need to do any prior actions, this data is available for all published scenes.

	To access this data, visit the [Decentraland Builder](https://builder.decentraland.org), select the **Land** tab, then select a parcel or estate that you own or have rights on. There you will find data for any scene in that location. The data includes total user visits, median session time and peak concurrent users during the last 7 days.
	
- The [WeMeta team](https://wemeta.world/about) produced a powerful analytics tool that is specially designed for using in Decentraland scenes. It was originally funded by [a grant in the Decentraland DAO](https://forum.decentraland.org/t/dao-qmdxcqc-wemeta-builder-tag/8194). 

	Through a one-line code snippet (the 'Builder Tag'), you can expose/access (via API or dashboard) a myriad of interesting scene data including unique visitors, heat maps of visitor foot traffic, visitor activity, your scene rank and more. 
	
	Read the [WeMeta documentation](https://docs.wemeta.world/docs/quick-start-decentraland) for detailed instructions about how to implement it in your scenes.
	
	For additional help or suggestions you can reach out to the WeMeta team [here](https://docs.wemeta.world) or [by mail](mailto:contact@wemeta.world)




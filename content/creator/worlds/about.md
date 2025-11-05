---
title: 'Worlds Overview'
url: /creator/worlds/about
weight: 1
---

Decentraland Worlds are your own personal 3D space in the Decentraland ecosystem, separate from Genesis City’s map of LAND parcels.
A World can be kept private or shared with anyone with just a link.
Able to host up to 100 concurrent users, you can use your World to host events, display your work, or as a blank canvas where you
can unleash your creativity and experiment. A World is available to anyone who owns a Decentraland NAME or an ENS domain.

# What are Worlds?

Worlds are personal 3D spaces located beyond the boundaries of Genesis City. Worlds can serve various purposes, such as:

- Hosting events
- Unleashing your creativity
- Building new experiences
- Hosting a portfolio of scenes
- Testing scenes before deploying them to Genesis City

You can get your own Decentraland World by getting a [Decentraland NAME](https://builder.decentraland.org/names), which are
NAME NFTs within the DCL ecosystem, or you can get a World by having an [ENS domain](https://ens.domains), a decentralized name that can be used across both Web2 & 3.

Acquiring a Decentraland NAME requires 100 MANA and can be assigned to your avatar, LAND, or Estate. Alternatively, you can purchase an
already-minted NAME from a previous owner in the Marketplace. These NAMEs are then used by the Decentraland Explorer to load the associated World.

Worlds serve as a gateway for aspiring content creators, providing an accessible entry point to creating in Decentraland and the freedom to
experiment with scene creation.

## Worlds Size Limit

The maximum file size you can upload to your World is an essential consideration when deploying your scenes.
It is important to note that the maximum scene file size you can upload to your World differs between Worlds
granted by Decentraland NAMEs and those from ENS domains.

### Worlds from Decentraland NAMEs

Decentraland NAME holders enjoy dynamic storage capacity within the Foundation Worlds Content Server, which depends on their wallet holdings. The following rules govern this allocation:

- Each Decentraland NAME you own grants 100 Mb of storage capacity (as well as a World).
- Each Decentraland LAND parcel you own grants an additional 100 Mb of storage capacity.
- For every 2,000 MANA held in your wallet, an additional 100 Mb of storage capacity is granted.

The space in the Foundation Worlds Content Server can be used to host scenes as large as users want, utilizing the Decentraland NAMEs they own and the combined space granted by their collective Decentraland assets. For instance, a user with multiple Worlds (granted by owning multiple NAMES) and a combined storage capacity of 500 Mb can choose to deploy one World with a 200 MB scene file, another with a 200 MB scene file, and a third with a 100 MB scene file. Alternatively, they could opt to deploy one World with a 300 MB scene file and another with a 200 MB scene file.. This flexibility allows users to create and manage their virtual experiences efficiently within the allocated server storage space.

The maximum server storage capacity for your Decentraland Worlds is calculated dynamically, adhering to the rules outlined above. If, by any chance, a user exceeds their allocated storage space—for instance, through asset sales or transfers to another wallet– they will be provided with a 24-hour window to address the situation. Failure to do so will result in their Worlds becoming inaccessible after this grace period.

To regain access to a blocked World, users can either acquire more MANA, Decentraland NAMEs, or LANDS, increasing their storage capacity or un-deploy existing scenes from the World Content Server to free up their storage space.

### Worlds from ENS Domains

In contrast, Worlds granted from ENS domains have a fixed maximum scene file size of 36 Mb per World, regardless of the user’s other Decentraland holdings. Users with Worlds from ENS domains cannot increase their ENS World scene size limit by purchasing additional MANA or LAND.

However, Worlds granted by ENS domain ownership serve as the perfect first step into realizing the creative freedom offered by Decentraland. At the same time, get your own little corner of the metaverse where you are free to begin transforming your ideas into reality.

## Publish a World

Users have various options to publish content on their World. As a prerequisite for any of the options below, you must hold a Decentraland NAME or ENS Domain in your wallet, or have permissions granted by an owner.

### 1. Use the Creator Hub (no-code / code)

The Creator Hub is the go-to option for creating Decentraland Scenes. It can be used to create no-code scenes via an easy drag-and-drop interface, or you can also combine it with Visual Studio Code to write code freely.

See [Publish Scene]({{< ref "/content/creator/scene-editor/publish/publish-scene.md" >}}) for more details.

### 2. Using the Web Editor (no-code)

The Builder is the ideal choice for non-developers. Scenes can be created from scratch using the Scene Builder by simply dragging and dropping items into the scene. [Smart items]({{< ref "/content/creator/scene-editor/interactivity/smart-items.md" >}}) can also be used for player interaction once the scene is deployed.

The [Builder](https://builder.decentraland.org/worlds) also serves as the go-to place for visualizing your allocated space and monitoring how much is consumed by each Decentraland NAME or ENS Domain. Additionally, users can easily undeploy scenes to release storage space, view when their storage capacity is exceeded, and access comprehensive information about their Worlds, whether they are hosted on Decentraland NAMES or ENS Domains.

### 3. Using the SDK and Editor

If you wish to know more about how to create a scene, check out the [Decentraland SDK]({{< ref "/content/creator/sdk7/getting-started/sdk-101.md" >}}) documentation.

If you are a Content Creator, you may be already familiar with how the [publishing of a scene]({{< ref "/content/creator/sdk7/publishing/publishing.md" >}}) works, the experience is quite similar, but with a small caveat:

You need to specify under what **name** your deployment is to be made. Add the following section in your
`scene.json`:

```json
{
	"worldConfiguration": {
		"name": "my-name.dcl.eth"
	}
}
```

The **name** specified en the `scene.json` can be either a Decentraland NAME or an ENS Domain and must be owned by the wallet signing the deployment (or by any wallet that has been given permission explicitly via Access Control Lists (ACL), as explained further down).

Keep the following in mind:

- The wallet signing the deployment must own the NAME specified in the `scene.json` file
- The scene has no parcel limitations (since January 2023)
- All Worlds are automatically listed on the Places page unless you opt out as detailed below

Some of the Worlds deployed to the Foundation's Worlds Content Server may be eligible for being listed in Decentraland Places.

If you wish to opt-out from your Worlds being indexed in Places, you can add the following section in your `scene.json`:

```json
{
	"worldConfiguration": {
		"name": "my-name.dcl.eth",
		"placesConfig": {
			"optOut": true
		}
	}
}
```

### 5. Publish via the CLI

To deploy a scene to a world via the CLI, you need to specify the target server in the deployment command-line and use the Worlds Content Server URL.

For SDK6 scenes, use the following command:

```bash
dcl deploy --target-content https://worlds-content-server.decentraland.org
```

For SDK7 scenes, use the following command:

```bash
npm run deploy -- --target-content https://worlds-content-server.decentraland.org
```

Once you run the command, you will be prompted to sign the deployment with your wallet and a set of validations will be executed to allow or reject the scene.

## Joining a World

Once a scene is uploaded to the Worlds server you can access it by using the
Decentraland Explorer with the following friendly URL `https://decentraland.org/jump/?realm=NAME.dcl.eth`, where `NAME` should be replaced by the Decentraland NAME or ENS Domain to which the deployment was done to.

On the other hand, NAMEs also work as realms, so you can leverage the existing change realm mechanisms to access a world. One way would be by typing the `/goto NAME.dcl.eth` command in the chatbox and another possibility is by changing the query parameter in the Explorer URL: if your NAME is `my-name.dcl.eth` you can use the following URL to access the world: ` decentraland://?realm=my-name.dcl.eth`

## Migrating a World to the Genesis City

If you are a LAND owner and you wish to deploy a World scene to the Genesis City, it is completely possible. You just need to re-deploy your scene to the decentralized Catalyst network, the targeted content server for Genesis City

Things to remember:

- remove the `worldConfiguration` section from `scene.json`
- the size limitation for Worlds (100 Mb total size) is different from that for LAND parcels (15MB per parcel), so make sure your scene is sized correctly for deployments to Genesis City!

## World defaults

A couple of optional custom settings can be specified in the `scene.json` when deploying a world scene:

**skybox**: This property indicates how many seconds have passed (in Decentraland time) since the start of the day, assuming the full cycle lasts 24 hours. Divide the seconds value by 60 to obtain minutes, and by 60 again to obtain the hours since the start of the day. For example, if the seconds value is 36000, it corresponds to 10:00 am. If no value is set for this field, the world will follow the same day/night cycle as Genesis City.

**fixedAdapter**: indicates which Communication Service should be used by the scene. For the time being only the `offline:offline` value is allowed and when set, the scene will have no Communication Service at all and each user joining that world will always be alone. If not set, the Worlds content server will generate a proper value based on how it is configured.

**Example:**

```json
{
	"worldConfiguration": {
		"name": "my-name.dcl.eth",
		"skyboxConfig": {
			"fixedTime": 36000
		},
		"fixedAdapter": "offline:offline"
	}
}
```

## Access Control Lists (ACL)

When a team (more than one person) are contributing to the development of a scene, it may be beneficial to have each contributor have the ability to publish the scene under a single NAME. As stated above, the NAME owner is the only one allowed to run such deployment.

So the concept of Access Control List (or ACL for short) was introduced. The idea is that the owner of the NAME can grant other wallets permission to publish a scene under his NAME. This way the whole team (or a group of selected members) can be added to the world ACL and those will be able to publish the scene.

This ACL is stored in the World Content Server where the world is deployed. It is not stored on the blockchain. This makes it much more flexible, giving more granular control. For e.g. if you want to deploy a scene under the same NAME in two different World Content Server hosting providers, then you can have different sets of permissions in each server. And also, there is no transaction fees involved in maintaining the ACL (granting or revoking permissions).

A new command has been added to Decentraland CLI that allows to show the current ACL stored in the Worlds Content Server for a given NAME, and it also allows granting access to more wallets or revoking access to wallets that are already in the ACL.

![world-acl help screen](/images/worlds/world-acl-help.png)

In order to grant permission for publishing a scene to another wallet you have to:

- Make sure to have the latest version of Decentraland CLI (v3.20.0 or later).
- Make sure you own the NAME for which you want to manage the ACL.
- Use command `dcl world-acl NAME.dcl.eth grant 0x1..` where `0x1...` is the address of user receiving the permission.

By default, `world-acl` will act on `worlds-content-server.decentraland.org`. If you are using a different hosting provider, make sure to add `--target-content https://your-hosting.com` to each of the subcommands (`show`, `grant` and `revoke`).

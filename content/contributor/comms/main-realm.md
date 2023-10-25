---
title: "MAIN Realm"
sidebartitle: "MAIN Realm"
url: "/contributor/comms/main"
weight: 2
---

Decentraland has as many realms as there are Catalyst with communications services, but there is one distinctive realm known as MAIN which exists outside the Catalysts network. The MAIN realm was specifically designed to streamline the user connection process, making it easier for users to interact and meet. It is constructed with a set of services capable of substituting the communication service of a Catalyst node. This realm serves as the default destination for users upon logging into Decentraland.

<img src="/images/main-realm.png" width="600"/>

The [realm provider](https://github.com/decentraland/realm-provider) services exposes an [/about](https://realm-provider.decentraland.org/main/about) endpoint with a realm description according to the [ADR-110: Realm description](https://adr.decentraland.org/adr/ADR-110). This provides the information to stablish a connection with the content management network, known as one of Catalyst node's services, and also supplies the connection details for the MAIN realm communication services. 

The MAIN communications service is accessed through the [WebSocket Connector](https://github.com/decentraland/archipelago-workers). This lightweight component enables the interaction with the rest of the backend components and can be easily scaled with additional instances to accommodate an expanding user load, efficiently managing a greater number of active connections. Via the WebSocket connection, the client acquires the necessary data for establishing a connection with LiveKit Cloud, alongside the `islandId` assigned by the Archipelago Service. The Archipelago Service bears identical responsibilities in both the MAIN realm and the Catalyst nodes communications service. It effectively manages the processing of users' positions and their subsequent allocation to distinct islands, each of which corresponds to a Livekit room, thus efficiently organizing user clusters based on their spatial locations within the virtual world. For further insights into the Archipelago Service, you can refer to the [Archipelago]({{< relref "archipelago" >}}) page.

[NATS](https://nats.io/) functions as a broadcasting system facilitating seamless communication between various services. It can supports multiple WebSocket Connector instances communicating with the same Archipelago Service. Moreover, it enables the Stats service to gather user statistics from Archipelago, such as positions and island groupings, making this data accessible for external utilization.

The Archipelago stats service shares the same API implementation as the Archipelago service in the Catalyst node. You can explore the API at this link: [Catalyst API Specs](https://decentraland.github.io/catalyst-api-specs/#tag/Archipelago) and the service is accessible through the following URL `https://archipelago-stats.decentraland.org/`. 

The [LiveKit]({{< relref "transport-types/livekit" >}}) Cloud platform manages the intricate task of exchanging users' information through WebRTC and it is the primary cloud platform shared by the majority of Catalyst nodes for the same purpose. 

The fundamental concept derived from the MAIN realm is that different users have the flexibility to connect to any Catalyst node for content management purposes (downloads scenes, wearables, emotes, or send profile updates) but despite the selection of a specific content management node, the connection to the communication service **can** be the same. As a result, even if users are utilizing different Catalyst nodes as content servers but they find themselves at close scene coordinates, they will have the ability to interact with each other. On the other hand, the MAIN realm just serves as the default destination upon logging in, yet users retain the freedom to switch realms to any Catalyst node equipped with a communication service. This can be achieved through the existing mechanisms, such as the '/changerealm' chatbox command or by utilizing the realms navigation UI.

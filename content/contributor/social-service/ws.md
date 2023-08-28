---
title: WS Implementation API
url: /contributor/social-service/ws
weight: 1
---

The Social Service is a server that manages friendships within Decentraland. Utilizing the Matrix platform, it serves as the authoritative source for handling Friendships updates, such as requests, accepts, rejects, cancels and deletes.

## Use Cases

The Social Service addresses the following use cases related to friendships:
- Requesting a Friendship
- Accepting a Friendship Request
- Rejecting a Friendship Request
- Canceling a Friendship Request
- Removing a Friend
- Listing all my friends
- Listing mutual friends between me and another user

## Context

Before the introduction of the Social Service, friendship data was stored and retrieved directly from Matrix. This led to various issues with friendship workflows and unreliable information. Additionally, implementing new features was challenging. Since Matrix primarily handles chat features, the Social Service acts as a proxy, applying necessary business logic before interacting with Matrix.

## Architecture

### Version History

1. [First Version](https://adr.decentraland.org/adr/ADR-113): Initially, the Social Service was a REST API that only offered GET endpoints for listing all friends and mutual connections. It lacked features related to updates or sending requests.

2. [Second Version](https://adr.decentraland.org/adr/ADR-189): This version introduced updates to the friendship flow. To address these changes, a WebSocket RPC server was implemented. This server handles essential messages, maintaining open connections with clients to provide timely updates. The WebSocket connections also facilitate features such as [presence tracking](https://github.com/decentraland/adr/blob/420e63926d20166ae832e3de62dd9e3f2370cd49/content/ADR-246-poc-presence.md) within the Social Service.

### URLs

#### .zone Domain

Development Environment Servers for testing and when using testnets.

- [Login with Matrix](https://social.decentraland.zone)
- [REST API](https://social.decentraland.zone)
- [WebSocket API](https://rpc-social.decentraland.zone)

#### .org Domain

Production Environment Servers and when using mainnet.

- [Login with Matrix](https://social.decentraland.org)
- [REST API](https://social.decentraland.org)
- [WebSocket API](https://rpc-social.decentraland.org)

## Use the Javascript Client

To use the Javascript Client please refer to [https://github.com/decentraland/social-rpc-client-js#using-the-client](https://github.com/decentraland/social-rpc-client-js#using-the-client)

## Reference Client Implementations

- [Matrix Client](https://github.com/decentraland/matrix-client)
- [JS Client](https://github.com/decentraland/social-rpc-client-js)
- [Rust Reference Client](https://github.com/decentraland/social-client)

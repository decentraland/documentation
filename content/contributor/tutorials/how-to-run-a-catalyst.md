---
title: How to run your own DCL Node
sidebartitle: Run a DCL Node
url: /contributor/tutorials/how-to-run-a-catalyst
---

Ever felt curious about how Decentraland Catalyst nodes work? Ever wanted to run your own node and felt overwhelmed about where to start? Are you building content for Decentraland and finding it hard to do the whole development and testing cycles on production servers?

If you are (or have been there), fear no more. This tutorial will help you in the process of planning, figuring out what you need to decide and then guide you step by step in starting up the server. Also, in case something might not go according to the plan, there is a troubleshooting section at the end with a few of the most common problems and how to fix them.

Ready? Hands on to the task.

## Hardware requirements

The Decentraland Foundation servers are deployed on Amazon AWS on `t2.xlarge` instances. So while those servers are meant for public use, your own one may be ok with much smaller specs, depending on what the intended use will be.

An AWS EC2 `t2.xlarge` has the following hardware:

- 4 vCPUs.
- 16 Gb RAM

And for file storage + DB storage, an SSD / HDD with 2 Tb capacity should be more than sufficient. At the time of this writing the foundation servers are using a little over 1 Tb for all storage.

## Software pre-requisites

The following are required for running catalyst-owner:

- Linux / MacOS operating system.
- Docker / docker-compose.
- Git.

## Some options to consider before we start

- Do you want your node to be publicly exposed on the Internet? If so, you will need an internet-exposed instance and a public URL to connect to it.
- Is the node going to be used for the development of scenes, wearables, etc? In this case, the hardware specs can be a lot smaller, as it will probably be one or two people accessing it, not hundreds of users.
- Do you want to sync all entity types? If you are using this for developing scenes, probably you want to skip synchronization of profiles, as they take a lot of time, bandwidth and most importantly disk space and won’t benefit you for your goal.

## Step by step guide

First thing to do is clone `catalyst-owner` the repository from GitHub

```bash
> git clone https://github.com/decentraland/catalyst-owner.git
Cloning into 'catalyst-owner'...
remote: Enumerating objects: 2392, done.
remote: Counting objects: 100% (602/602), done.
remote: Compressing objects: 100% (168/168), done.
remote: Total 2392 (delta 506), reused 481 (delta 430), pack-reused 1790
Receiving objects: 100% (2392/2392), 926.05 KiB | 1.09 MiB/s, done.
Resolving deltas: 100% (1257/1257), done.
> cd catalyst-owner
```

Once that’s done, it’s time to configure the environment variables for the node, and make any changes as appropriate.

```bash
# On the /catalyst-owner folder
> cp .env.example .env
> cp .env-advanced.example .env-advanced
```

Now using your favorite text editor, make any needed changes in these files. For e.g., setting up the `EMAIL` environment variable with valid email is required so that we can receive updates about Certbot certificate expiration.

Also setting up your particular value for `CATALYST_URL` may be required, especially if your server is going to be exposed publicly on the Internet. For use in your local machine, the default of `http://localhost` will do.

There is a variable called `CONTENT_SERVER_STORAGE` that defines the local folder that the content server will use for storage. This defaults to `CONTENT_SERVER_STORAGE=./storage`. You may change this value to store files somewhere else, or at least make sure that the referenced folder exists. You may need to create it like this:

```bash
# On the /catalyst-owner folder or wherever CONTENT_SERVER_STORAGE is pointing to
> mkdir storage
```

There is another interesting variable `SYNC_IGNORED_ENTITY_TYPES` which allows ignoring certain entity types during the synchronization process. If you are going to use the Catalyst server for development, perhaps you don't need all content type to be synchronized. You can set env var `SYNC_IGNORED_ENTITY_TYPES="profile,store"` so that only scenes and wearables will be brought from the DAO servers. This will save a lot of time, bandwidth and disk storage in your server.

>💡 For a more exhaustive list of supported environment variables please have a look at the [Environment variables](https://www.notion.so/Environment-variables-b83dc993bf114f218bf893c0db4a5639) section below.

Once all environment variables have been set up, it is time to start the node. That should be as easy as running the `init.sh` script in the root folder.

```bash
# On the /catalyst-owner folder

> ./init.sh
## Loading env variables... [ OK ]
[ OK ]
## Checking if email is configured... [ OK ]
## Checking if storage is configured... [ OK ]
## Checking if catalyst url is configured... [ OK ]
 WARNING: You are not running latest image of Catalyst's Content and Catalyst's Lambdas Nodes.
 WARNING: You are not running latest image of Catalyst's Archipelago Node.
 WARNING: You are not running latest image of Catalyst's Explorer BFF Node.
 - DOCKER_TAG:               45a5154f11b53d55aadfdf7f958e2fce6a964824
 - LIGHTHOUSE_DOCKER_TAG:    latest
 - CATALYST_URL:             http://localhost
 - CONTENT_SERVER_STORAGE:   ./storage
 - EMAIL:                    a@a.com
 - ETH_NETWORK:              mainnet
 - REGENERATE:               0

Starting in 5 seconds...
45a5154f11b53d55aadfdf7f958e2fce6a964824: Pulling from decentraland/catalyst-content
Digest: sha256:d6c2981c57cb9367fdb3228d15b07e4d26e62c902944115937de24ecd3ab6aac
Status: Image is up to date for decentraland/catalyst-content:45a5154f11b53d55aadfdf7f958e2fce6a964824
docker.io/decentraland/catalyst-content:45a5154f11b53d55aadfdf7f958e2fce6a964824
45a5154f11b53d55aadfdf7f958e2fce6a964824: Pulling from decentraland/catalyst-lambdas
Digest: sha256:5605812dd29316afc32e561d2a2ce1311f164f07ef3cd99a1cd60727518636e5
Status: Image is up to date for decentraland/catalyst-lambdas:45a5154f11b53d55aadfdf7f958e2fce6a964824
docker.io/decentraland/catalyst-lambdas:45a5154f11b53d55aadfdf7f958e2fce6a964824
latest: Pulling from decentraland/catalyst-lighthouse
Digest: sha256:fedc10b714823909f0a1c17955eed2f22a02e4f784090848d3253ef734e410d4
Status: Image is up to date for decentraland/catalyst-lighthouse:latest
docker.io/decentraland/catalyst-lighthouse:latest
latest: Pulling from decentraland/archipelago-service
Digest: sha256:e2c1d6fa96a5cfbbf6fb37e3840c0724fb5abeef8c366025a28fab3ad33d6480
Status: Image is up to date for quay.io/decentraland/archipelago-service:latest
quay.io/decentraland/archipelago-service:latest
latest: Pulling from decentraland/explorer-bff
Digest: sha256:fa9e305c44972a8613b01f4cd573d6fb84b0fb03ce953a506fbb06053202913c
Status: Image is up to date for quay.io/decentraland/explorer-bff:latest
quay.io/decentraland/explorer-bff:latest
Stopping nginx ... done
## Using HTTP because CATALYST_URL is set to http://localhost
## Replacing value $katalyst_host on nginx server file... [ OK ]
## Restarting containers...
WARNING: The LIVEKIT_URL variable is not set. Defaulting to a blank string.
WARNING: The LIVEKIT_API_KEY variable is not set. Defaulting to a blank string.
WARNING: The LIVEKIT_API_SECRET variable is not set. Defaulting to a blank string.
WARNING: The WS_ROOM_SERVICE_URL variable is not set. Defaulting to a blank string.
WARNING: The WS_ROOM_SERVICE_SECRET variable is not set. Defaulting to a blank string.
Creating network "catalyst-owner_default" with the default driver
Creating catalyst-owner_comms-server_1 ... done
Creating node-exporter                   ... done
Creating catalyst-owner_lambdas_1      ... done
Creating postgres                      ... done
Creating catalyst-owner_certbot_1        ... done
Creating nats                            ... done
Creating postgres-exporter               ... done
Creating catalyst-owner_content-server_1 ... done
Creating catalyst-owner_archipelago_1    ... done
Creating catalyst-owner_explorer-bff_1   ... done
Creating nats-exporter                   ... done
Creating cadvisor                        ... done
Creating nginx                           ... done
## Catalyst server is up and running at http://localhost
```

If all went well, we now have a full Decentraland node running. You can now head to the browser and type the URL. If using the default, it should be [`http://localhost`](http://localhost/).

We can check the content server logs with this docker command:

```bash
> docker logs catalyst-owner_content-server_1
```

Even though the server is now running, it’s not 100% ready to be in business. It needs to synchronize the content from the other [servers of the DAO](https://decentraland.github.io/catalyst-monitor) so it can offer the same experience to users connected to it. Synchronization can take a long time. On a good internet connection, 6 hours should be pretty common. So… time to have a coffee, a nap, a good night's rest, and come back tomorrow.

One way of knowing whether synchronization is complete consists of checking the results of the content status endpoint: [http://localhost/content/status](http://localhost/content/status) (use your URL here).
```json
{
  "synchronizationStatus": {
    "lastSyncWithDAO": 1658153514917,
    "synchronizationState": "Bootstrapping"
  },
  "snapshot": {
    "entities": {
      "profile": 1271331,
      "scene": 23477,
      "wearable": 17351,
      "store": 890
    },
    "lastUpdatedTime": 1658153414530
  },
  "version": "v3",
  "commitHash": "9a2e0d5d05d02646df2e1e5d00436d3166a07aa1",
  "catalystVersion": "4.8.6",
  "ethNetwork": "mainnet"
}
```

While `synchronizationState` is `Bootstrapping`, you can use the node for deploying new content, but it is still not up-to-date with other nodes from the DAO. Once the status changes to `Syncing` it means it has already caught up and is continuously receiving the latest updates. This is the healthy state in which the node is fully working.

```json
{
  "synchronizationStatus": {
    "lastSyncWithDAO": 1658153872301,
    "synchronizationState": "Syncing"
  },
  "snapshot": {
    "entities": {
      "profile": 1271317,
      "scene": 23477,
      "store": 890,
      "wearable": 17350
    },
    "lastUpdatedTime": 1658152050030
  },
  "version": "v3",
  "commitHash": "9a2e0d5d05d02646df2e1e5d00436d3166a07aa1",
  "catalystVersion": "4.8.6",
  "ethNetwork": "mainnet"
}
```

If you are more of cli-kind-of-guy, you can grep the content server docker image logs for this message: `Starting to sync entities from servers pointer changes`. Once you see that text, the content server is fully synchronized and ready for full use.

## Environment variables

The following is a comprehensive list of all the content server environment variables with their default values, as logged in the content server logs during startup:

```jsx
STORAGE_ROOT_FOLDER: "/app/storage/content_server/"
DENYLIST_FILE_NAME: "denylist.txt"
DENYLIST_URLS: "https://config.decentraland.org/denylist"
SYNC_IGNORED_ENTITY_TYPES: ""
FOLDER_MIGRATION_MAX_CONCURRENCY: 1000
SERVER_PORT: 6969
LOG_REQUESTS: false
UPDATE_FROM_DAO_INTERVAL: 1800000
SYNC_WITH_SERVERS_INTERVAL: 45000
CHECK_SYNC_RANGE: 1200000
DECENTRALAND_ADDRESS: "0x1337e0507eb4ab47e08a179573ed4533d9e22a7b"
DEPLOYMENTS_DEFAULT_RATE_LIMIT_TTL: 60
DEPLOYMENTS_DEFAULT_RATE_LIMIT_MAX: 300
ETH_NETWORK: "mainnet"
LOG_LEVEL: "debug"
FETCH_REQUEST_TIMEOUT: "2m"
USE_COMPRESSION_MIDDLEWARE: false
BOOTSTRAP_FROM_SCRATCH: false
REQUEST_TTL_BACKWARDS: 1200000
LAND_MANAGER_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/land-manager"
COLLECTIONS_L1_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/collections-ethereum-mainnet"
COLLECTIONS_L2_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/collections-matic-mainnet"
THIRD_PARTY_REGISTRY_L2_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/tpr-matic-mainnet"
BLOCKS_L1_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/blocks-ethereum-mainnet"
BLOCKS_L2_SUBGRAPH_URL: "https://api.thegraph.com/subgraphs/name/decentraland/blocks-matic-mainnet"
PSQL_DATABASE: "content"
PSQL_HOST: "postgres"
PSQL_SCHEMA: "public"
PSQL_PORT: "5432"
GARBAGE_COLLECTION: true
GARBAGE_COLLECTION_INTERVAL: 21600000
PG_IDLE_TIMEOUT: 30000
PG_QUERY_TIMEOUT: 60000
PG_STREAM_QUERY_TIMEOUT: 600000
SNAPSHOT_FREQUENCY_IN_MILLISECONDS: 21600000
CUSTOM_DAO: undefined
DISABLE_SYNCHRONIZATION: false
SYNC_STREAM_TIMEOUT: "10m"
CONTENT_SERVER_ADDRESS: "http://localhost/content/"
REPOSITORY_QUEUE_MAX_CONCURRENCY: 50
REPOSITORY_QUEUE_MAX_QUEUED: 300
REPOSITORY_QUEUE_TIMEOUT: "1m"
ENTITIES_CACHE_SIZE: 150000
DEPLOYMENT_RATE_LIMIT_MAX: {}
DEPLOYMENT_RATE_LIMIT_TTL: {}
VALIDATE_API: false
RETRY_FAILED_DEPLOYMENTS_DELAY_TIME: 900000
```

## Using your node for scene development

One of the main reasons for willing to have your own private development environment may be for development of scenes (or wearables, emotes, etc). So you might want to have an easy way to deploy different versions of the scene, test them locally, iterating until you come up with a final version for deploying into one of the [DAO servers](https://decentraland.github.io/catalyst-monitor) for everyone to use.

This node is not part of the DAO, it’s just your own node for your own purposes. It will pull new content continuously from the other servers in the DAO, but the content you deploy locally will never be pushed to the DAO-approved nodes. So it works as a sandbox where nothing you do here can really harm or affect anything for Decentraland users.

In order to use it for this purpose, you deploy a node and perhaps use it with ownership validations disabled, to do this you just need to add the property `IGNORE_BLOCKCHAIN_ACCESS_CHECKS=true` to your `.env` file. This way you can deploy your scene in any parcel (no need to be owner), then you can explore the world in order to test the new scene, share it with your QA team or a selected group of users.

For testing your new scene, you can enter explorer by specifying the URL for your Catalyst node. For e.g.

- [https://play.decentraland.org/?CATALYST=catalyst.my-domain.com](https://play.decentraland.org/?CATALYST=peer-uw-1.decentraland.zone&island=Iyu&position=39%2C12&realm=testing) (if you have a publicly exposed server)
- [https://play.decentraland.org/?CATALYST=localhost](https://play.decentraland.org/?CATALYST=localhost) (if you run it on your own machine).

## Using your node for production

If, on the other hand, you want to run your own server and help scale the network, first of all that’s awesome, the community and the foundation really appreciate you doing so.

In this case, you’ll have to go through the process of requesting the DAO for approval to join the network by visiting [this link](https://governance.decentraland.org/submit/catalyst/). You may also ask for a MANA grant in order to cover the expenses.

It is important that your hardware specs are more inline with what is suggested above in the hardware requirements, as the server will be used by any members of the community to enter Decentraland.

## API Specs

For more details on the APIs for content, lambdas and comms servers you can check the [API specs](https://decentraland.github.io/catalyst-api-specs).

## Troubleshooting/FAQ

A few things could go wrong while starting your server. Here is a few of the most common issues encountered over time and how to fix them.

### Port 5432 is used by local postgres

If you run the node on a machine used for development, or if it is already hosting other services, chances are there’s already a postgres database server running on that machine. So port 5432 will be already taken.

The easiest way to fix this is to stop the postgres that is already running locally and then restart the postgres docker container using `docker start postgres`.

If you have knowledge on docker compose, you can start fiddling with `docker-compose.yml` and environment variables to try to get it to work on a different port. For the sake of keeping things simple here, we will avoid going that path in this tutorial.

### Port 80 port is used by local nginx

Same thing can happen with port 80 (and even port 443). If you are running nginx in the local machine, chances are that ports 80/443 are already bound that that service, so the Catalyst Docker container won’t be able to use them.

Again, the simplest approach would be to stop the local nginx service and then restart the docker container using `docker start nginx`. Or alternatively, you need to leverage `docker-compose.yml` and `.env` to get it to work on a different port.

## Additional docs for reference

If you want to understand better what a Catalyst server does, what services it includes, etc. you can check the architecture repo https://github.com/decentraland/architecture that explains the parts in detail.

If you would like to contribute to Catalyst servers code, make sure to check the [contributing guide](https://github.com/decentraland/catalyst/blob/main/docs/CONTRIBUTING.md) to learn about our development process, how to propose bug fixes and improvements, and how to build and test your changes.

And finally, if you need to contact the team, you can do so via [Discord](https://discord.com/channels/417796904760639509/948230185457696820) or submitting [GitHub issues](https://github.com/decentraland/catalyst/issues).
#!/usr/bin/env python3

import sys
import json
import urllib.request

# Decentraland Content Indexing Example

# See:
# - Guide to this script: https://docs.decentraland.org/contributor/content/practice/python
# - More complex version: https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots.py
# - Snapshot documentation https://docs.decentraland.org/contributor/content/snapshots
# - Entity documentation: https://docs.decentraland.org/contributor/content/entities


def fetch(path):
    url = f"https://peer.decentraland.org/{path}"
    headers = { "User-Agent": "urllib" } # important on some servers (if empty, 403 Forbidden)

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    return response


# Check the server status:
about = json.load(fetch('about'))

if not about['healthy']:
    print("Server not healthy!")
    sys.exit(1)

# Get the list of snapshots:
all_snapshots = json.load(fetch('content/snapshots'))

# Take the smallest snapshot, in terms of included entities:
snapshot = min(all_snapshots, key=lambda s: s['numberOfEntities'])

# Request the file from the content API:
response = fetch('content/contents/' + snapshot['hash'])

# Verify the snapshot header:
header = response.readline().decode('utf-8').strip()

if header != '### Decentraland json snapshot':
    print("Invalid snapshot header: " + header)
    sys.exit(1)

# Read and decode all items, one JSON per line:
for line in response:
    item = json.loads(line)
    print(item['entityType'], item['entityId'])


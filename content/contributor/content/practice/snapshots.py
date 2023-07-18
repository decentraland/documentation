#!/usr/bin/env python3

import sys
import json
import urllib.request
from datetime import datetime

# Decentraland Content Indexing Example

# See:
# - Simpler version: https://github.com/decentraland/documentation/blob/main/content/contributor/content/practice/snapshots_mini.py
# - Guide for it: https://docs.decentraland.org/contributor/content/practice/python
# - Snapshot documentation https://docs.decentraland.org/contributor/content/snapshots
# - Entity documentation: https://docs.decentraland.org/contributor/content/entities


def fetch(path):
    url = f"https://peer.decentraland.org/{path}" # any compatible content server will do
    headers = { "User-Agent": "urllib" } # important on some servers (if empty, 403 Forbidden)

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    return response


# Check the server status:
about = json.load(fetch('about'))

if not about['healthy']:
    print("server: not healthy!")
    sys.exit(1)

# Get the list of currently active snapshots:
print("Fetching current snapshots...")
all_snapshots = json.load(fetch('content/snapshots'))

print(f"Found {len(all_snapshots)} snapshots\n")

# Sort them, newest to oldest, so we can process entities in a convenient order:
all_snapshots.sort(key=lambda s: s['timeRange']['initTimestamp'], reverse=True)

# NOTE:
# Normally, if we were keeping an up-to-date entity index, we'd want to skip files
# we already downloaded, including those replaced by later snapshots.

# Index all entities!
seen_pointers = set()

for snapshot in all_snapshots:
    # Extract relevant properties:
    hash       = snapshot['hash']
    init_dt    = datetime.fromtimestamp(snapshot['timeRange']['initTimestamp'] / 1000)
    end_dt     = datetime.fromtimestamp(snapshot['timeRange']['endTimestamp'] / 1000)
    n_days     = (end_dt - init_dt).days
    n_entities = snapshot['numberOfEntities']

    # Show some information about the snapshot:
    print(f"Snapshot {hash}")
    print(f"  {n_days} days, {n_entities} entities ({init_dt} to {end_dt})")

    print("  requesting file...")
    response = fetch(f"content/contents/{hash}")

    # Verify the snapshot header:
    header = response.readline().decode('utf-8').strip()

    if header != '### Decentraland json snapshot':
        print("  error: invalid snapshot header: " + header)
        sys.exit(1)

    # Read all entities, one JSON per line:
    print(f"  processing entities...")

    for line in response:
        item = json.loads(line)

        if any(pointer in seen_pointers for pointer in item['pointers']):
            continue # skip if we already found a more entity for this pointer

        seen_pointers.update(item['pointers'])

    print(f"  done ({len(seen_pointers)} accumulated entities)\n")

# Done!
print(f"Finished with {len(seen_pointers)} total entities")

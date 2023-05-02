---
title: "Content API with Python"
bookhidden: true
url: "/contributor/content/practice/python"
---

This practice shows how to write a simple program that downloads and analyzes some content.

We'll be using the Decentraland Foundation's instance at `peer.decentraland.org`, and Python 3 as our language of choice. You can find the full script [in this gist](https://gist.github.com/slezica/bbe58316c9cf09c22099eade87bcd49c).

This is what we'll do:

1. Query the status of the content server.
2. Locate and download the [snapshot]({{< relref "snapshots" >}}) for a list of entities.
3. Print the ID of all entities that were deployed after a certain date.

Let's begin our script with some preparations. We'll use standard library modules only, but in real practice you'll probably want a more comfortable HTTP client (like the [requests](https://github.com/psf/requests) library).

```python3
#!/usr/bin/env python3

import sys
import json
import urllib.request

def http_get(url):
    headers = {
        "User-Agent": "urllib" # Important! If empty, 403 Forbidden
    }

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content
```

Our simple helper makes an HTTP `GET` request, and decodes the response body. Nothing fancy. We'll be using the `json` module to parse some responses, such as the one from `/about` we're starting with:

```python3
# Check the server status:
about = json.loads(http_get('https://peer.decentraland.org/about'))

if not about['healthy']:
    print("Server is not healthy!")
    sys.exit(1)
```

If we get past this point, the server is up and running (we got a `200` response) and reports being operational. We can request the current set of snapshots (which comes in JSON format):

```python3
# Get the list of snapshots:
snapshots = json.loads(http_get('https://peer.decentraland.org/content/snapshots'))
```

Let's obtain the identifier for the emote snapshot file, as we did in the manual practice above:

```python3
# Obtain the file identifier tor the emote snapshot, and download it:
emote_snapshot_hash = snapshots['entities']['emote']['hash']
emote_snapshot_url = f'https://peer.decentraland.org/content/contents/{emote_snapshot_hash}'
emote_snapshot = http_get(emote_snapshot_url)
```

It's important to note that snapshot files are potentially huge, so buffering the entire content might be a bad idea. We happen to know that the emote snapshot is tiny, so we're not going to worry about memory.

Let's split the snapshot into lines, and check for the correct header:

```python3
emote_snapshot_lines = emote_snapshot.split('\n')

# Check the header:
if emote_snapshot_lines[0] != '### Decentraland json snapshot':
    print("Invalid snapshot header!")
    sys.exit(1)
```

The rest of the lines in this list are JSON documents describing entities. We have decided that we only care about items deployed after an arbitrary date, so let's go through the list and print the relevant entity identifiers:

```python3
emote_min_timestamp = 1667798160000

for line in emote_snapshot_lines[1:]:
    if len(line) == 0:
        break # the snapshot can end with a newline

    emote = json.loads(line)

    if emote['localTimestamp'] >= emote_min_timestamp:
        print(emote['entityId'])
```

Note the `break` in the loop: snapshot files can (and often will) end with an empty line, which we must be prepared to handle.

Running this script at the moment of writing outputs a list of 68 results, beginning with...

```
bafkreigcreq7rv6b2wf4zc4fsnif43ziwb4q46v4qhsewpf7gbsyxew3om
bafkreidk3hyw3sq7frwc6qtv3cp3xq3jx5ogcznla7ru4yznhtbayx5no4
bafkreiacjqf7uzt7isdsbtqrwlvfjajrit4vye6kjoy647dggki6gfv7by
bafkreickzvceg2w7ac73ir3gaybt4okxzntqn4nd7rx3jhilwnlibqiz7e
```

Cheers! We've systematically explored the available emotes by leveraging the content API.
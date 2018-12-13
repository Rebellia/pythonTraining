#!/usr/bin/env python3

import json
import urllib.request
import webbrowser

apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=DEMO_KEY'

apodurlobj = urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()

#Make a series of lists and dictionaries
decodeapod = json.loads(apodread.decode('utf-8'))

print("\n\n\n", decodeapod)

input("Press ENTER key to open url")

webbrowser.open(decodeapod['url'])

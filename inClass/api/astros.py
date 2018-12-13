#!/usr/bin/env python3

import urllib.request
import json


MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
   ## call the web service (send HTTP GET)
   groundctrl = urllib.request.urlopen(MAJORTOM)

   ## put file object into helmet
   helmet = groundctrl.read()

   ## decode our string into lists and dicts
   helmetson = json.loads(helmet.decode('utf-8'))

   print("     Heroes in Space:\n")
   for x in helmetson["people"]:
      print(x["name"])   

main() 

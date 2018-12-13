#!/usr/bin/env python3
import json
import yaml

yammyfile = open('example.yml', 'r')

parsed_yaml = yaml.load(yammyfile)

print(parsed_yaml.get("thins_to_do", "The princess must be in another castle"))

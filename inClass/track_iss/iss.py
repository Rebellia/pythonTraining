#!/usr/bin/env python3

import urllib.request
import json 
import turtle
import time

eoss = 'http://api.open-notify.org/iss-now.json'

while(True):
	trackiss = urllib.request.urlopen(eoss)

	#Reads it in as a string
	ztrack = trackiss.read()

	#Change json into lists and dictionaries
	result = json.loads(ztrack.decode('utf-8'))

	#location = result['iss_position']
	lat = result['iss_position']['latitude']
	lon = result['iss_position']['longitude']


	screen = turtle.Screen()
	screen.setup(720, 360)
	screen.setworldcoordinates(-180,-90,180,90)
	screen.bgpic('iss_map.gif')
	screen.register_shape('spriteiss.gif')
	iss = turtle.Turle()
	iss.shape('spriteiss.gif')
iss.setheading(90)
lon = round(float(lon))
lat = round(float(lat))

iss.penup()
iss.goto(lon, lat)
turtle.mainloop()


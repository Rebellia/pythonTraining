#!/usr/bin/env python3
import re

contact = "Contact: <sip:+15552224987@[2600:2340:9214:ec::2]:5060;eri-generated-at=10172.0.132,;+sip.instance+g.3gpp.icsi>"

#The r prevents python from parsing the slashes and removing them 
#The alternative is to do double slashes
##conobj = re.search('<sip:\\+(\\d+)@\\[(.*)\\]:?(\\d+)?')
conobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', contact)

#conobj is now a match object
##Prints just what your pattern matched on
print(conobj.group())

#Group 1 -- Phone number
print(conobj.group(1))

#Group 2 -- IP address
print(conobj.group(2))

#Group 3 -- Port
print(conobj.group(3))

#Where in the string the match started
print(conobj.start())
#Where in the string the match ended
print(conobj.end())

#returns a tuple
#The end number is non-inclusive
print(conobj.span())

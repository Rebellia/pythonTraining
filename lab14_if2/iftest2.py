#!/usr/bin/env python3

nameCheck = input("Provide a name: ")

#If any data is provided, this will test true
if nameCheck == 'Steve':
   print("It\'s our favorite person: " + nameCheck)
elif nameCheck:
   print("The name is: " + nameCheck)
else:
   print('You did not provide input')

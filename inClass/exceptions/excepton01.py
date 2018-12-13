#!/usr/bin/env python3

try:
   print("Enter a file name: ")
   name = input()
   filename = open(name, 'w')
except FileNotFoundError:
   print("You probably did not enter a string. Try again.")
except:
   print("Something went wrong. Try again.")
finally:
   print("\nThis is code that always executes")

#!/usr/bin/env python3

vendors = ['Dell', 'HP', 'Apple', 'Lenovo', 'Acer', 'ASUS']

approved = ['Dell', 'Apple']

for vendor in vendors:
   print("\nThe vendors are " + vendor, end="")
   if vendor not in approved:
      print(" - NOT APPROVED", end="")


print("\n The for-loop is over")

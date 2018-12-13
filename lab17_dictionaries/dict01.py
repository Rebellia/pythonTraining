#!/usr/bin/env python3

##create a dictionary
laptops = {'Dell':'XPS 15', 'HP':'Spectre x360', 'Microsoft': 'Surface Book', 'Lenovo':'Thinkpad'}

##display parts of the dictionary
print(laptops['Dell'])
print(laptops['HP'])

## request a 'fake' key
print("\nFirst test -- .get() with a fake key")
print(laptops.get('ASUS'))

print("\nSecond test -- get() with a fake key and alternative")
print(laptops.get('ASUS', "This key does not exist"))

print("\nThird test -- get() with the correct key")
print(laptops.get('Microsoft'))

print("\nList of all the keys")
print(laptops.keys())

print("\nPrinting all the values")
print(laptops.values())

print("\nTesting pop()")
laptops.pop('HP')
print(laptops.keys())
print(laptops.values())

print("\nTesting adding values")
laptops['Razerblade'] = 'Stealth'
print(laptops.keys())
print(laptops.values())

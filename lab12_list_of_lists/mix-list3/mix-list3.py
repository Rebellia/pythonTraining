#!/usr/bin/env python3

list1 = ['apples', 'bananas', 'oranges']

#list1 with no additions
print(list1, "\n")

#The second item in list1
print(list1[1],"\n")

#Extending with a list will turn the input into a list item
list1.extend(['peach'])
print(list1, "\n")

#Appending with a list will make the list itself a list item
list1.append(['pear', 'plum', 'strawberry'])
print(list1, "\n")

print(list1[4], "\n")

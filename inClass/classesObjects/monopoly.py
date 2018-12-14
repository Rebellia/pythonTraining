#!/usr/bin/env python3

class Monopoly:
   def __init__(self, name, street, price):
        self.n = name
        self.st = street
        self.pr = price
        self.util = []

   def __str__(self):
        return "Name: " + self.n + "\nPrice: $" + str(self.pr)
   
   def utility(self, serv):
        self.util.append(serv)

   def utility_get(self):
        return self.util

   def utility_del(self, serv):
        self.util.remove(serv) #remove requires specific value, pop requires specific index

myprop = Monopoly("My house", "Timber Rd", 500)

print(myprop)

myprop.utility("natural gas")
myprop.utility("electric")
myprop.utility("sewer")

print(myprop.utility_get())
myprop.utility_del("sewer")
print(myprop.utility_get())


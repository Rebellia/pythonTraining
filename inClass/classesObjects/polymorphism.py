#!/usr/bin/env python3

class Bear(object):
    def sound(self):
       print("Groar")

class Dog(object):
    def sound(self):
       print("Woof")

def makeSound(animalType):
    animalType.sound()


bearObj = Bear()

dogObj = Dog()

makeSound(bearObj)

makeSound(dogObj)

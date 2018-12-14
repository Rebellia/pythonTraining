#!/usr/bin/env python3

class Dog:
    def __int__(self, name, age):
      self.n = name
      self.a = age

    def __str__(self):
      return self.n
    
    def aged(self, yearsolder):
      try:
         self.a = self.a + yearsolder
      except:
         return "try passing int"


    def age_get(self):
      return self.a

class GermanShort(Dog):
    def __init__(self, name, age, isTrained, isBob):
      Dog.__init__(self, name, age)
      set.t = isTrained
      self.b = isBob


    def __str__(self):
      return self.n + " " + str(self.a) + " " + str(self.t)

doge1 = Dog("Derpy" , 3)
print(dofe1)

doge1.aged(1)

print(doge1.age_get())


doge2 = GermanShortHair("Hanna", 7, True, False)
print(doge2)

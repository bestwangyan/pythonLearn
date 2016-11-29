#! /usr/bin/python
# coding=utf-8
# FileName: *.py
# Author:Wang Yan
# CreationDate:20160909

class Animal:
    '''class of animal test'''
    animals = 0

    # leg=4
    # color="black"
    def __init__(self, leg=4, color="black"):
        self.leg = leg
        self.color = color
        self.__private="private"
        Animal.animals += 1

    def __del__(self):
        Animal.animals -= 1

    def introduce(self):
        print(
            "I hava {0} legs and my color is {1}\nNow we have {2} animals\nThe private is {3}".format(self.leg, self.color, Animal.animals,self.__private))

class Cat(Animal):
    def __init__(self,name, leg=4, color="black"):
        Animal.__init__(self,leg=leg,color=color)
        self.name=name

    def introduce(self):
        print(
            "I hava {0} legs and my color is {1}\nNow we have {2} animals\nMy name is {3}".format(self.leg,
                                                                                                      self.color,
                                                                                                      Animal.animals,
                                                                                                      self.name))

print(Animal.__doc__)
animal = Animal()
animal.introduce()
animal2 = Animal(leg=3, color="white")
animal2.introduce()
animal.__del__()
print(Animal.animals)



cat=Cat(name="Cathy",leg=4,color="black")
aa=[animal,cat]
for i in aa:
    i.introduce()
#cat.introduce()

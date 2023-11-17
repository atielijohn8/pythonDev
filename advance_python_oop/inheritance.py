#!/usr/bin/python3
class pet: #general
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'i am {self.name} and i am {self.age} years old')

    def speak(self):
        print('i dont know')

class Cat(pet): #inheriting upper level class(pet)
    def speak(self):
        print('meow')

class Dog(pet):
    def speak(self):
        print('bark')

class fish(pet):
    pass


p = pet('Tim', 19)
p.show()
c = Cat("Bill", 34)
c.show()
d = Dog('ken', 19)
d.show()
f = fish('bubble', 10)
f.speak() #used speak defined in parent class

#!/usr/bin/python3
class PlayerCharacter:
    def __init__(self, name, age):#dunder method
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

Player1 = PlayerCharacter('cindy', 41)#instanciate(calling class to create an object)
Player2 = PlayerCharacter('Tom', 19)

#print(Player1)
#print(Player2)

#!/usr/bin/python3
class PlayerCharacter:
    def __init__(self, name, age):
        if(age > 18):
            self.name = name#attributes
            self.age = age

    def run(self):
        print(f"my name is {self.name}")
        return 'done'

Player1 = PlayerCharacter("cindy", 41)#instanciate
Player2 = PlayerCharacter("Tom", 19)

print(Player1)
print(Player2.run())

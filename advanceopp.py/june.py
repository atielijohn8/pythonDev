#!/usr/bin/python3
import time
class june:
    def __init__(self,name,age,Character):
        self.name = name
        self.age = age
        self.Character = Character
    def load(self):
        print("loading...", end="", flush=True)
        time.sleep(6)
        print("loading complete.")
        return 'done'

    def job(self):
        print("i am a chemist")
        return 'done'

person = june('anindo',18,'blanck')

print(person.load())
print(person.name,person.age)
person.job()
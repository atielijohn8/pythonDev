#!/usr/bin/python3
class Dog:
    def __init__(self, name, age=0):
        # attributes
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

d = Dog("tim", 7)
d.set_age(23)  # modifying bills age(attributes)
print(d.get_age())

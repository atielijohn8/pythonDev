class Person:
    total_people = 0  # not different for each instance (constant)
    gravity = 9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def get_total_people(cls):  # acts on class itself
        return cls.total_people

    @classmethod
    def add_person(cls):
        cls.total_people += 1

p1 = Person('Tim')
p2 = Person('Jill')
p3 = Person('Tata')

print(Person.get_total_people())

#!/usr/bin/python3
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade


class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []#allows us to enter student into the course
    
    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = student('tim', 19, 95)
s2 = student('bill', 19, 75)
s3 = student('jill', 19, 65)

#adding students to the course
course = course('physics', 3)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)
print(course.get_average_grade())

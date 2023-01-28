from random import random, randint


class Student:

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.educational_platform = "udemy"


    def greet(self):
        greetings = [f"Hi, I'm {self.name}", f"Hey there, my name is {self.name}",
                     f"Hi. Oh, my name is {self.name}"]
        print(greetings[randint(0, len(greetings))-1])



student_names = ['Madeleine', 'Patrick', 'Tim']
for student_name in student_names:
    student = Student(student_name)
    student.greet()
    print(student.age)
    print(student.educational_platform)

aged_student = Student('Douglas', 6)
aged_student.greet()
print(aged_student.age)
aged_student.educational_platform = 'Hard knox'
print(aged_student.educational_platform)

bad_student = Student('Kitty')
print(bad_student.educational_platform)



class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Student object (name = %s)"% self.name


print(Student('may'))
Student('may')
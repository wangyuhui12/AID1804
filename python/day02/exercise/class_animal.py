
class Animal():
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print("Dog is running...")
        return ' '

Bart = Dog()
Bart.run()

class Person:

    def __init__ (self, name):
        self.name = name
    
    def __str__ (self):
        return f'Hi, my name is {self.name}.'


class Student(Person):
    def learn(self):
        return "I get it!"


class Instructor(Person):
    def teach(self):
        return "An object is an instance of a class."

    


instructor1 = Instructor("Nadia")
student1 = Student("Chris")
print(instructor1)
print(student1)
print(instructor1.teach())
print(student1.learn())

print(student1.teach())
#doesn't work because student object has no attribute teach. It has an attribute of learn




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, age {self.age}")


class Student(Person):  # Student inherits from Person
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.grades = []

    def study(self):
        print(f"{self.name} is studying...")
class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def teach(self):
        print(f"{self.name} is teaching...")

student = Student("Victor", 20, "S1234")
student.introduce()
student.study()

teacher = Teacher("Mr. Bob", 38, "T1234")
teacher.teach()

# Inheritance is important because it allows you to avoid writing repetitive or redundant code. Instead, you can define a common blueprint (a base class), and then create objects or subclasses that reuse and extend its functionality.
# i created teacher class so i won't just have to create variables in a function to define this, when i can use the class as a reusable component
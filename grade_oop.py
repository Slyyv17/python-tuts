def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []  # Empty list to store grades

    def add_grade(self, grade):
        # Add a grade to the student's grade list
        self.grades.append(grade)

    def get_average(self):
        # Calculate average of all grades
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        # Use the calculate_grade function you wrote earlier
        average = self.get_average()
        return calculate_grade(average)

student = Student("Victor", 20)
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(f"Average: {student.get_average()}")
print(f"Letter Grade: {student.get_letter_grade()}")

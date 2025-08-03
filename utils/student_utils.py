def calculate_average(grades):
    # Your task: implement this
    return sum(grades) / len(grades)
    pass

def validate_grades(grades):
    # Your task: return True if all grades are valid numbers
    return all(isinstance(grade, (int, float)) for grade in grades)
    pass

def process_student(student_data):
    # Your task: process one student, return result dict
    # Should handle missing grades, invalid grades, etc.
    pass
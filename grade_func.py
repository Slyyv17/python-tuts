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


scores = [95, 83, 67, 45]
# Use a loop to test the function
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} → Grade: {grade}")
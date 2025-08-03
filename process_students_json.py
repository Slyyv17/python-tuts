import json

# Step 1: Create the initial file (only do this once)
students_data = {
    "students": [
        {"name": "Alice", "age": 20, "grades": [85, 92, 78], "major": "CS"},
        {"name": "Bob", "age": 19, "grades": [90, 88, 95], "major": "Math"}
    ]
}

with open("students.json", 'w') as file:
    json.dump(students_data, file, indent=4)

# Step 2: Load existing data from file
with open("students.json", 'r') as file:
    students_data = json.load(file)

# Step 3: Add Eve
new_student = {"name": "Eve", "age": 21, "grades": [88, 90], "major": "Physics"}
students_data["students"].append(new_student)

# Step 4: Write updated list back to the file
with open("students.json", 'w') as file:
    json.dump(students_data, file, indent=4)

# Step 5: Process the updated data
results = []
for student in students_data["students"]:
    name = student["name"]
    grades = student["grades"]

    if grades:
        results.append({"name": name, "grades": grades})
    else:
        results.append({"name": name, "grades": "No grades"})

# Step 6: Save results to a separate file
with open("processed_students.json", 'w') as file:
    json.dump(results, file, indent=4)

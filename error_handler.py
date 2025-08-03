import json

# Step 1: Create bad data and save it to a file
bad_data = {
    "students": [
        {"name": "Alice", "grades": [85, "invalid", 78]},  # Contains invalid data
        {"name": "Bob", "grades": []},                    # Empty grades
        {"name": "Charlie"}                               # No 'grades' key
    ]
}

with open("bad_data.json", 'w') as file:
    json.dump(bad_data, file, indent=4)

# Step 2: Load data with error handling
try:
    with open("bad_data.json", 'r') as file:
        bad_data = json.load(file)
except FileNotFoundError:
    print('The file bad_data.json was not found.')
    exit()

# Step 3: Process each student with robust handling
results = []

for student in bad_data['students']:
    name = student.get('name', 'Unknown')

    if 'grades' not in student:
        results.append({"name": name, "grades": "Missing grades key"})
        continue

    grades = student['grades']

    if not grades:
        results.append({"name": name, "grades": "Grades are empty"})
    elif not all(isinstance(g, (int, float)) for g in grades):
        results.append({"name": name, "grades": "Contains invalid grade(s)"})
    else:
        results.append({"name": name, "grades": grades})

# Step 4: Save processed results
with open("bad_data_result.json", 'w') as file:
    json.dump(results, file, indent=4)
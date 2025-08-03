try:
    with open('students.txt', 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print('The file students.txt was not found.')
    exit()

results = []
for line in lines:
    parts = line.strip().split(',')
    name = parts[0]
    grades = list(map(int, parts[1:]))
    average = sum(grades) / len(grades)
    results.append(f"{name}, Average: {average:.2f}")

with open('results.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')

print("Results written to 'results.txt'.")
score = 85

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
elif score < 60:
    print('F')
else:
    print("Invalid score")

# If score = 85, which condition gets checked first? = the second condition below the A grade
# If score = 95, how many conditions does Python check before finding a match? = the first one
# What happens if score = 100? Does it get an A? = Based on my code base, Yes it will
# What happens if score = 110? (edge case) = my code base will print the else statement

print(score)
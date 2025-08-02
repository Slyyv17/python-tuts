username = "Victor"
birth_year = 2005
current_year = 2025
current_age = current_year - birth_year

if current_age >= 18:
    can_vote = True
else:
    can_vote = False

print(f"You are {current_age} years old...")
print(f"You can vote: {can_vote}")

# type(birth_year) = int
# type(current_age) = int
# str(birth_year) + str(current_age) = 202520
# print(str(birth_year) + str(current_age))

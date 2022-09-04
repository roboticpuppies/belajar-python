# Day 2: 30 Days of python programming
first_name = "Yor"
last_name = "Forger"
full_name = "Yor Forger"
country = "JP"
city = "Kawagoe"
age = 27
year = 2021
is_married = True
is_true = True
is_light_on = False
# Declare multiple variables in one line
daughter_first_name, daughter_last_name, daughter_hair_color = "Anya", "Forger", "Pink"

# Check the data type of all your variables using type() built-in function
print("Type of first_name is ", type(first_name))
print("Type of last_name is ", type(last_name))
print("Type of full_name is ", type(full_name))
print("Type of country is ", type(country))
print("Type of city is ", type(city))
print("Type of age is ", type(age))
print("Type of year is ", type(year))
print("Type of is_married is ", type(is_married))
print("Type of is_true is ", type(is_true))
print("Type of is_light_on is ", type(is_light_on))
print("Type of daughter is ", type(daughter_first_name))
# Using the len() built-in function, find the length of your first name
print("Length of first name is ", len(first_name), "chars")
# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("First name is ", len(first_name) - len(last_name), "characters longer.")
else:
    print("Last name is", len(last_name) - len(first_name), "characters longer.")
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = sum([num_one, num_two])
print("Total of", 5, "and", 4, "is", total)

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print("Subtraction :", diff)

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print("Divide num_one by num_two :", division)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modulus = num_two % num_one
print("Modulus divison :", modulus)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = pow(num_one, num_two)
print("Power :", exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print("Floor division :", floor_division)

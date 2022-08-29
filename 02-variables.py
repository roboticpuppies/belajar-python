# Python has no command for declaring a variable.
# Variable names are case-sensitive
x = 5
y = "Hello, World!"

print(x)
print(y)

# ===================================================
# Variables do not need to be declared with any particular type
# and can even change type after they have been set.
b = 4       # x is of type int
b = "Sally" # x is now of type str
print(b)

# ===================================================
# Variable casting
# If you want to specify the data type of a variable,
# this can be done with casting.
h = str(3)    # h will be '3'
i = int(3)    # i will be 3
j = float(3)  # j will be 3.0
print(type(h))
print(type(i))
print(type(j))

# ===================================================
# String variables can be declared either by using single or double quotes
# x = "John"
# is the same as
# x = 'John'
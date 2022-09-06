# Day 3: 30 Days of python programming

age = 27
height = 160.6
complex_num = 4 + 1j

print('Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).')
print('Calculate triangle area.')
triangle_base = int(input('Enter base :'))
triangle_height = int(input('Enter height :'))
triangle_area = 0.5 * triangle_base * triangle_height
print('Area of triangle is', triangle_area)

print('Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).')
print('Calculate triangle perimeter.')
side_a = int(input('Enter side a :'))
side_b = int(input('Enter side b :'))
side_c = int(input('Enter side c :'))
triangle_perimeter = sum([side_a, side_b, side_c])
print('Perimeter of triangle is', triangle_perimeter)
print('\n')

print('Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))')
print('Calculate rectangle area.')
rec_width = int(input('Enter width :'))
rec_length = int(input('Enter length :'))
rec_area = rec_width * rec_length
print('Area of rectangle is', rec_area)
print('\n')

print('Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.')
cir_rad = int(input('Enter circle radius :'))
cir_area = 3.4 * cir_rad * cir_rad
cir_circumference = 2 * 3.14 * cir_rad
print('Area of circle is', cir_area)
print('Circumference of circle is', cir_circumference)
print('\n')

print('Find the length of \'python\' and \'dragon\' and make a falsy comparison statement')
x = 'python'
y = 'dragon'
print(len(x) > len(y))
print('Use and operator to check if \'on\' is found in both \'python\' and \'dragon\'')
print('on' in x and 'on' in y)
print('\n')

print('\'I hope this course is not full of jargon\'. Use in operator to check if jargon is in the sentence.')
print('jargon' in 'I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.')
print('\n')

print('There is no \'on\' in both dragon and python')
print('on' not in x and 'on' not in y)
print('\n')

print('Find the length of the text python and convert the value to float and convert it to string')
x_length = str(float(len(x)))
print('Value is', x_length, 'with type', type(x_length))
print('\n')

print('Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?')
sample_num = 44
print('Sample number :', sample_num)
print(sample_num%2 == 0)
print('\n')

print('Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.')
print(7//3 == int(2.7))
print('\n')

print('Check if type of \'10\' is equal to type of 10')
print(type('10') == type(10))
print('\n')

print('Check if int(\'9.8\') is equal to 10')
print(int(9.8) == 10)
print('\n')

print('Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?')
hours = int(input('Enter hour :'))
rate = int(input('Enter rate :'))
print('Earning :', hours * rate)
print('\n')

print('Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years')
years_you_have_avoided_death = int(input('Enter number of years you have lived :'))
print('You have lived for', 3.154e+7 * years_you_have_avoided_death, 'seconds.')
print('\n')

print('Write a Python script that displays the following table')
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')

print('Answer :')
for x in range(1, 6):
    print(x, x ** 0, x ** 1, x ** 2, x ** 3)
# First column print current index
# For the rest of column is exponentiation of that index

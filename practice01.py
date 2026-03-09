"""
print("Anuradha VD")
print("--o---")
print("   ||||--")
print('*' * 10)

# Define varaibles and input function
name = input('What is your name? ')
color = input('What is your favorate color? ')
print(name + ' likes ' + color )

#Type conversion
birth_year = input('Birth year: ')
age = 1971 - int(birth_year)
print(type(age))
print(age)

weight_pounds = input('What is your weight (lbs)' )
weight_kg = int(weight_pounds) * 0.45
print(weight_kg)


#Python string and index
course = 'Python for Beginners'
print(course[6:])
print(course[1:-1])

#Formated strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)

"""
# String methods


# This is Single Line Comment

# print("Hello World")
"""
y=30
x=40
z=60
"""
"""
This is Multiline
Comments
"""

"""

add = y +x
sub = x-z

"""



#  List Data Type

"""
city = ['Sunamganj', 'sylhet', 'Sunamganj', "Dhaka", 44, True]

# Tuple
latter =("A", "B", 33, True, "C", "D")
print(latter[3])
"""

"""


# Range Data Type
numbers1 = range(0, 10)
print(*numbers1)
numbers2 = range(0, 20, 2)
print(* numbers2)

"""


# None Data Type
"""
isAvailable = None
print(isAvailable)
"""
# Boolean Data Type
"""
isBangladeshi = True
print(isBangladeshi)
"""

# Dictionary Data Type Like JS Object
"""

persion = {
    "first_name": "Hammad",
    "last_name": "Sadi",
    "isBangladeshi": True,
    "isAvailable": None
}
print(persion['first_name'])

"""

# Set Mutable Data Type ( It Ignore Duplicate Value )
"""
numberList = {1,2,3,4,5,6, 1, 2,3}
print(numberList)
"""

# Frozenset Immutable Data Type ( it also Ignore Duplicate Value and cannot Maintain Order )
"""
numbersList = frozenset([1, 2, 3, 4, 5, 6, 1, 2])
print(numbersList)
"""

# Data Type Check Using Build in type() function

"""
x =3
print(type(x))

z = 2 + 3j
print(z)

"""




"""
Data Type Mutable-
Data Type Immutable-
"""


#  Immutable Data Types ( Int, Float, String, Tuple, Frozenset, Set etc )
"""

x =2
firstLocation= id(x)
x=5
second_location = id(x)
print(firstLocation)
print(second_location)
"""


# Mutable Data Type ( List, sets, Dictionaries )
"""
x = [1,2,3,4]
first_location = id(x)
print(first_location)

x[1]=10
second_location = id(x)
print(second_location)
"""

"""
x = {'a':1, "b":30, "c": 40}
first_location = id(x)
print(first_location)
x['b'] = 100
second_location = id(x)
print(second_location)
"""

"""

x = {1,2,3,4,5}
first_location = id(x)
print(first_location)
x.add(100)
second_location = id(x)
print(second_location)

"""

# Type of Conversion
# Explicit Conversion => int(), float(), str()
# Implicit Conversion => x =2, y=5, x+y

"""
try:
    name = "Sadi"
    print(int(name))
except Exception as e:
    print(e)
"""


# Console Project

# Greetings
"""
name = input("Enter your name: ")
print("Hello " + name + "!")
"""

# Sum Console Project

"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print('The Sum is', int(num1) + int(num2))
"""




# String Slicing
name = "Hello World! My Name is Sadi"
# print(name[4])
# print(name[-1])

#  Start Slicing
# print(name[0:2])
# print(name[:4])

# Stop Slicing
# print(name[4:])


# Step Slicing
# print(name[1::2])


"""

#  String Menupulation
str1 = 'I love'
str2 = " No Love"

final_str = str1 + str2

new_str = str1 + ',' + str2

# Using Method
str_method = ',,'.join([str1, str2])

# Format Method
# new_str2 = "{} {} !".format(str1, str2)


# Modulas
new_str3 ="%s %s -"%(str1, str2)

print(new_str3)


"""



#  String Method

#  Upper case
# name = 'hammad sadi'
# print(name.upper())
# Lower case
# user_name = "HAMMAD SADI"
# print(user_name.lower())

# capitalize word first latter Capital
# text = 'hammad sadi'
# print(text.capitalize())


# Title case
# text = 'hammad sadi'
# print((text.title()))


# Swap case
# text = 'hammad sadi'
# print(text.swapcase())



# Replace a substring
# text = "hello World"
# print(text.replace("World", "Python"))



#  Split a String into List
# text = 'hello my name is hammad sadi'
# print(text.split(' '))


# Join a List into a String

# textList = ['Hello', 'My', 'Name', 'Is', 'Hammad', 'Sadi']
# print(" ".join(textList))


# Remove Whitespace

# text = "  Hammad Sad  "

# Remove White space from both side
# print(text.strip())

# Remove Whitespace from left side
# print(text.lstrip())
# Removed Whitespace from Right side
# print(text.rstrip())



#  Check String if Start with sub string
text = 'Hello World'
# print(text.startswith("Hello"))

#  Check if String if Ends with Substring
# print(text.endswith("World"))

# Check Substring Position
# print(text.find('World'))

# Count the Substring
# print(text.count('l'))


#  Check if all characters are alphanumeric
# print(text.isalnum())

# Check if all characters are alphabetic
# print(text.isalpha())

# Check if all Characters are Digits
number_val = '11212324'
# print(number_val.isdigit())


#  Check if string contains whitspace
white_space = '  '
# print(white_space.isspace())


#  Check if string Titlecase
title_case_str= 'Hammad Sadi'
# print(title_case_str.istitle())

#  Remove Whitespace and converting to uppercase
space_upp = "  Hello Im Sadi   "
print(space_upp.strip().upper())









































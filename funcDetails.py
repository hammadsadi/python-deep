# Define a Normal Function
def say_hello ():
    print("Hello")
# Call the function
# say_hello()

#  Define Function with Arguments
def greet(name):
    print("Hello, " + name)

# greet("Alice")

#  Define Function and Receive Arguments as Tuple
def print_numbers(*numbers):
    print(numbers)

# print_numbers(1, 2, 3, 4, 5)

#  Define Function and Receive Arguments as Dictionary
def print_info(**info):
    print(info)
    for key, value in info.items():
        print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="New York")






#  Return , A function Can Return anything ( Tuple, List, Dictionary, String, Integer, Float, Boolean, Object, etc..)
def add(a, b):
    return a + b

result = add(5, 3)
# print(result)

#  A Function Can Action but not Return Anything
def print_greeting(name):
    print(f"Hello, {name}!")

# print_greeting("Alice")



#  A Function Can Return Early
def check_number(numbers):
    for number in numbers:
        if number%2==0:
            return number

    return None


# result = check_number([1, 3, 5, 9, 7])
# print(result)





#  Lmbda Function ( Anonymous Function )
#  A Lambda Function is a small anonymous function that can take any number of arguments, but can only have one expression. The expression is evaluated and returned when the function is called.
#  Syntax: lambda arguments: expression
result = lambda : 1+2
# print(result())

#  Send Arguments to Lambda Function
calculate_tow_number = lambda  x, y: x + y
# print(calculate_tow_number(2, 3))



#  Short condition with Lambda Function
is_even = lambda x, y : "Even" if x%2==0 and y%2==0 else "Odd"
# print(is_even(2, 3))



from datetime import date

# Functional check: is today Friday in Ramadan?
is_ramadan = lambda d: d.month in (2, 3)          # approximate Ramadan months
is_friday  = lambda d: d.weekday() == 4           # Friday = 4

today = date.today()

status = "Focus × Faith × Discipline" if is_ramadan(today) and is_friday(today) else "Normal day"

print(f"{today}: {status}")




































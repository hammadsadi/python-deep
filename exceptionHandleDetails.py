
"""
#  Single except block
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError as e:
    print(ZeroDivisionError)
"""

"""
#  Multiple except blocks
try:
    with open('new.text', 'r') as file:
        content = file.read()
        result = 10/ int(content)
        print(result)
except FileNotFoundError:
    print("File not found.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Invalid type for division.")
except ValueError:
    print("Invalid value for division.")
   """



"""
#  Smartly handling multiple exceptions in a single except block
try:
    with open('new.text', 'r') as file:
        content = file.read()
        result = 10 / int(content)
        print(result)
except Exception as e:
    print(e)

"""

#  Handle Finally block
try:
    with open('new.text', 'r') as file:
        content = file.read()
        result = 10 / int(content)
        print(result)
except Exception as e:
    print(e)
finally:
    print('This block will always execute, regardless of whether an exception occurred or not.')



import os


 # File Handle

# Write to a file
"""

with open('example.text', 'w') as file:
    file.write("Hello World")
    

"""

#  Read File

"""
with open('example.text', 'r') as file:
     content = file.read()
     print(content)
    
"""

#  Rename file name Using os module
# os.rename('example.text', 'sadi.text')

#  Remove file Using os module
# os.remove('sadi.text')


#  Delete / Remove a file from a directory
# os.remove('test/sadi.text')
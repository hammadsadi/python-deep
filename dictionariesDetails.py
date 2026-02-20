user_info = {
     "name": "John Doe",
     "age": 30,
     "email": "jhon@gmail.com"
 }
# print(user_info)
# Access values
# print(user_info['name'])
# Access Value by get method
# print(user_info.get("age"))
# Get all keys
# for item in user_info:
#     print(user_info[item])


#  Mutable
"""
print(id(user_info))
user_info.update({"name":"Saadi"})
print(id(user_info))
print(user_info)
"""

# Get all Keys
# print(user_info.keys())

# Get all values
# print(user_info.values())


#  Get Tuples of key and values
# print(user_info.items())


#  Update value
user_info.update({"age": 300})
# print(user_info)

#  Remove a key-value pair
user_info.pop("age")
# print(user_info)

#  Clear the dictionary
user_info.clear()
print(user_info)





















import  json

"""user_info = {
     "name": "John Doe",
     "age": 30,
     "email": "jhon@gmail.com",
    "skills":["Python", "JavaScript", "SQL"],
    "isDeveloper": True
 }

#  Convert Python dictionary to JSON string
person_info = json.dumps(user_info, indent=4)
print(person_info)"""


#  Convert JSON string to Python dictionary

"""user_info = '''{
    "name": "John Doe",
    "age": 30,
    "email": "jhon@gmail.com",
    "skills": ["Python", "JavaScript", "SQL"],
    "isDeveloper": true
}'''

person_info = json.loads(user_info)
print(person_info['name'])"""



#  Convert Python object to JSON string and write to a file

"""user_info = {
     "name": "John Doe",
     "age": 30,
     "email": "jhon@gmail.com",
    "skills":["Python", "JavaScript", "SQL"],
    "isDeveloper": True
 }
with open('person.json', 'w') as jsonFile:
    json.dump(user_info, jsonFile, indent=4)"""

#  Read JSON file and convert to Python object
with open('person.json', 'r') as jsonFile:
    person_info = json.load(jsonFile)
    print(person_info['email'])
#     Convert it again JSON string
    person_json = json.dumps(person_info, indent=4)
    print(person_json)











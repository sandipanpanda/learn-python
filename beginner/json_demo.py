import json

# Create a dictionary object
person = {'first': 'Steve', 'last': 'Smith'}
person['city'] = 'Paris'

# Convert dictionary to JSON object
person_json = json.dumps(person)
print(person_json)

# Create nested staff dictionary
staff = {}
staff['Manager'] = person
staff_json = json.dumps(staff)

print(staff_json)

# Create a list object of languages
lang_list = ['French', 'English', 'Japanese']
person['languages'] = lang_list

person_json =json.dumps(person)
print(person_json)

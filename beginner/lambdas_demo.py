staff = [
    {'name': 'Steve', 'age': 30},
    {'name': 'Zack', 'age': 25}
]
print(staff)
staff.sort(key = lambda item: item['name'])
print(f'Alphabeticallly: \n{staff}')
print(staff)
staff.sort(key = lambda item: len(item['name']))
print(f'Based on length: \n{staff}')

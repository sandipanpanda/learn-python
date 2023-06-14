# lists
names = ['Bill', 'Steve']
print(names)
print(len(names))
names.insert(0, 'Richard')
print(names)
names.sort()
print(names)

runs = []
runs.append(6)
runs.append(4)
print(runs)
print(runs[1])

# arrays
from array import array
scores = array('d')
scores.append(2)
scores.append(1)
print(scores)
print(scores[1])

# dictionaries
person = {'first': 'Guido'}
person['last'] = 'Rossum'
print(person)
print(person['first'])

steve = {}
steve['name'] = 'Steve'
steve['age'] = 40

dennis = {}
dennis['name'] = 'Dennis'
dennis['age'] = 56

people = []
people.append(steve)
people.append(dennis)
people.append({
    'first': 'Linus', 'last': 'Torvalds'
})

print(people)

galaxy = input('What galaxy do you live in? ')
if galaxy.lower() == 'milky way':
    planet = input('What planet do you live in? ')
    if planet.lower() in('earth', 'mars', 'saturn'):
        tax = 0.07
    elif planet.lower() == 'jupiter':
        tax = 0.09
    else:
        tax = 0.12
else:
    tax = 0.05
print(f'Tax rate: {tax}')

# complex conditionals
gpa = float(input('Enter your GPA: '))
lowest_grade = float(input('Enter your lowest grade: '))
if gpa >= 0.85 and lowest_grade >= 0.70:
    scholar = True
else:
    scholar = False
if scholar:
    print("You're eligible for scholarship!")
else:
    print('Not eligible for scholarship')

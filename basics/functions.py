from datetime import datetime

fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# Get initials of a name
def get_initials(name, forced_uppercase = True): #default value for uppercase set to True
    if forced_uppercase:
        initial = name[0].upper()
    else:
        initial = name[0]
    return initial

def get_code():
    today = datetime.now()
    birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
    unique_code = str(birthday_date.year) + str(today.microsecond)
    return unique_code

print(f'Your initials are: {get_initials(name = fname)}{get_initials(lname)}')
print(f'Suggested email ID: {get_initials(fname, forced_uppercase = False)}{get_initials(lname, forced_uppercase = False)}{get_code()}@mail.com')

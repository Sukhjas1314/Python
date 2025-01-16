# Q.Write a Python program to check the validity of password input by users.
# Validation:
#  At least 1 letter between [a-z] and 1 letter between [A-Z].
#  At least 1 number between [0-9].
#  At least 1 character from [$#@].
#  Minimum length 6 characters.
#  Maximum length 16 characters.

password = input('Enter a password : ')

valid = True
errors = []

if len(password) < 6:
    valid = False
    errors.append('Password must be atleast 6 characters long.')
if len(password) > 16:
    valid = False
    errors.append('Password must not exceed 16 characters.')

has_lower = False
has_upper = False
has_digit = False
has_specialchar = False

for i in password:
    if 'a' <= i <= 'z':
        has_lower = True
    elif 'A' <= i <= 'Z':
        has_upper = True
    elif '0' <= i <= '9':
        has_digit = True
    elif i in '@#$!%^&*()':
        has_specialchar = True

if not has_lower:
    valid = False
    errors.append('Password must have atleast 1 lowercase character [a-z].')
if not has_upper:
    valid = False
    errors.append('Password must have atleast 1 uppercase character [A-Z].')
if not has_digit:
    valid = False
    errors.append('Password must have atleast 1 digit [0-9].')
if not has_specialchar:
    valid = False
    errors.append('Password must have atleast 1 special character [!@#$%^&*()].')

if valid:
    print('Password is valid.')
else:
    print('Password is invalid.')
    for j in errors:
        print(f'- {j}')
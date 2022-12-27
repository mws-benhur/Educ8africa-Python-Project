#  Judabenhur Kofi-Markin
#  CEH - Python Fundamentals Project'

import secrets  # import secrets for better security
import string

uppercase = string.ascii_uppercase
lowercase = string. ascii_lowercase
numbers = string.digits
symbols = string.punctuation

alphabet = uppercase + lowercase + numbers + symbols

# password length
pwd_length = 12

# select at least one character from each type
rand_number = secrets.choice(numbers)
rand_uppercase = secrets.choice(uppercase)
rand_lowercase = secrets.choice(lowercase)
rand_symbol = secrets.choice(symbols)

# store random generated as temporary password
temp_pwd = rand_symbol + rand_lowercase + rand_uppercase + rand_number

# fill the rest of 8 empty space in password
for i in range(pwd_length - 4):
    temp_pwd = temp_pwd + secrets.choice(alphabet)


# to generate the password string
password = ""
for i in temp_pwd:
    password = password + i

print(password)

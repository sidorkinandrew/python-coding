#Password Generator Project
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
exclude_symbols = input(f"Any symbols you would like to exclude?\n")

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

password_list = [char for char in password_list if char not in set(exclude_symbols)]
random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")

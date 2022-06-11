# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 📍 Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# 📍 Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#   USE shuffle(), sample(list, num)
#   random.shuffle(letters)
#   print(letters)

# Method1) My answer (TOO COMPLICATED) + WRONG ANSWER!!
password_made = []
symbols_chosen = random.sample(symbols, nr_symbols)
numbers_chosen = random.sample(numbers, nr_numbers)
num_of_letters = nr_letters-nr_symbols-nr_numbers
letters_chosen = random.sample(letters, num_of_letters)

for i in range(0, nr_letters):
    if i < len(symbols_chosen):
        password_made.append(symbols_chosen[i])
    elif i < len(symbols_chosen)+len(numbers_chosen):
        password_made.append(numbers_chosen[i-len(symbols_chosen)])
    else:
        password_made.append(
            letters_chosen[i-len(symbols_chosen)-len(numbers_chosen)])

print(password_made)
random.shuffle(password_made)
print(password_made)

password_final = ''
for i in password_made:
    password_final += i
print(password_final)


# Method2)
password = []
for char in range(0, nr_letters):
    password.append(random.choice(letters))

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

password_final = ''
for char in password:
    password_final += char

print(password_final)

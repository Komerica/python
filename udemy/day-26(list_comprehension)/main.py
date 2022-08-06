######################
# List Comprehension #
######################
# Python Sequence
# 1. List
# 2. Range
# 3. String
# 4. Tuple
# -> These Python Sequence has a specific order, that's why they're called Sequences!
# When performing a list comprehension, it's going to take that sequence and
# it's going to go through it in order either be it the letters in the string or the items in a list.
# And then it's going to take each of those items in that correct order and then do something with it.

# Ex1) List
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# Ex2) String
name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

name2 = "Leo"
for i in range(len(name2)):
    letters_list = [letter + f" {i}" for letter in name2]
print(letters_list)

# Ex3) Range
new_range = [n * 2 for n in range(1, 5)]
print(new_range)

##################################
# Conditional List Comprehension #
##################################
# -> new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

################
# Coded myself #
################
# with open("Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#     print(names)
#
# for name in names:
#     stripped_name = name.strip("\n")
#     with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
#         letter_contents = letter_file.read()
#         new_letter = letter_contents.replace("[name]", stripped_name)
#     with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as data:
#         data.write(new_letter)

##############
# Udemy code #
##############
# PLACEHOLDER = "[name]"
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#     print(names)
#
# with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip("\n")
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

####################
### Coded myself ###
# Without any help #
####################
PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    print(letter)

for name in names:
    new_name = name.replace("\n", "")
    print(new_name)
    with open(f"Output/ReadyToSend/letter_for_{new_name}", mode="w") as new_letter:
        completed_letter = letter.replace(PLACEHOLDER, new_name)
        new_letter.write(completed_letter)


# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

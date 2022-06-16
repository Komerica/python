from caesar_cipher_logo import logo
##########
# 방법1) #
##########
print(logo)
print("""
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░░░███╗░░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗░████║░░
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██╔██║░░
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║╚═╝██║░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)
# 26개 알파벳
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt(plain_text, shift_amount):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shift_amount
        if new_position < 26:
            cipher_text += alphabet[new_position]
        else:
            cipher_text += alphabet[26-new_position]
    print(cipher_text)


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position-shift_amount
        if new_position > 0:
            plain_text += alphabet[new_position]
        else:
            plain_text += alphabet[26+new_position]
    print(plain_text)
    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)


##########
# 방법2) # 👉 Easier way!
##########
print("""
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░░███╔═╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══╝░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)
alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction2 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text2 = input("Type your message:\n").lower()
shift2 = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def encrypt2(plain_text, shift_amount):
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet2 by the shift amount and print the encrypted text.
    cipher_text = ""
    for letter in plain_text:
        position = alphabet2.index(letter)
        new_position = position+shift_amount
        cipher_text += alphabet2[new_position]
    print(cipher_text)


def decrypt2(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet2.index(letter)
        new_position = position-shift_amount
        plain_text += alphabet2[new_position]
    print(plain_text)
    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list


# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction2 == "encode":
    encrypt2(plain_text=text2, shift_amount=shift2)
elif direction2 == "decode":
    decrypt2(cipher_text=text2, shift_amount=shift2)

##########
# 방법3) # combine two functions into one!
##########
print("""
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░█████╔╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░ """)
alphabet3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction3 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text3 = input("Type your message:\n").lower()
shift3 = int(input("Type the shift number:\n"))


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet3.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_amount
            end_text += alphabet3[new_position]
        elif cipher_direction == "decode":
            new_position = position - shift_amount
            end_text += alphabet3[new_position]
    print(end_text)


caesar(start_text=text3, shift_amount=shift3, cipher_direction=direction3)


# ##########
# # 방법4) # combine two functions into one (with less code) 👉Udemy code
# ########## ..BUT encode always works whatever I type in direction4!
print("""
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░░░██╗██╗
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗░██╔╝██║
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██╔╝░██║
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║███████║
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝╚════██║
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░░░╚═╝ """)
alphabet4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction4 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text4 = input("Type your message:\n").lower()
shift4 = int(input("Type the shift number:\n"))


def caesar2(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet4.index(letter)
        new_position = position + shift_amount
        end_text += alphabet4[new_position]
    print(f"Here's the {direction4}d result: {end_text}")


caesar2(start_text=text4, shift_amount=shift4, cipher_direction=direction4)


# ##########
# # 방법5) # Add continue / shift that's greater than 26 / Symbols,numbers,space
# ##########

print("""
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░███████╗
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██████╗░
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║╚════██╗
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═════╝░ """)

alphabet5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar3(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char in alphabet5:
            position5 = alphabet5.index(char)
            new_position5 = position5 + shift_amount
            end_text += alphabet5[new_position5]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

    # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar3() function again?
    # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:
    direction5 = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text5 = input("Type your message:\n").lower()
    shift5 = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet5?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).
    shift5 = shift5 % 26

    caesar3(start_text=text5, shift_amount=shift5, cipher_direction=direction5)
    more_game = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if more_game == "no":
        # should_continue = False
        print("Goodbye")
        break  # break 대신에 👆위의 should_continue = False 를 해도 된다!
    else:
        continue

##########
# 방법1) #
##########
print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░░░███╗░░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗░████║░░
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║██╔██║░░
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║╚═╝██║░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)
# 26개 알파벳
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
# 방법2) #
##########
print(""" 
███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░██████╗░
████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗╚════██╗
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║░░███╔═╝
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║██╔══╝░░
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝ """)
alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

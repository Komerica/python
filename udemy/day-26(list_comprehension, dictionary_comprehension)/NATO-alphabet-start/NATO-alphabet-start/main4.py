import pandas

###########
# My code #
###########

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

phonetic_dict = {}
for index, row in data.iterrows():
    phonetic_dict[row.letter] = row.code

phonetic_list = []
word = input("Enter a word: ").upper()
for letter in word:
    if letter in phonetic_dict.keys():
        phonetic_list.append(phonetic_dict[letter])

print(phonetic_list)

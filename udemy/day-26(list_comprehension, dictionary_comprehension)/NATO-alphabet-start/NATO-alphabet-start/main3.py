import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

# for index, row in data.iterrows():
#     print(row.letter)

phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
phonetic_list = [phonetic_dict[letter] for letter in word]
print(phonetic_list)

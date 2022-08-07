import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(df)
print(alphabet_dataframe)

phonetic_code_dict = {}
for (index, row) in alphabet_dataframe.iterrows():
    phonetic_code_dict[f"{row.letter}"] = row.code

print(phonetic_code_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
phonetic_code_words = []
word = input("Enter a word: ").upper()
for letter in word:
    for key in phonetic_code_dict:
        if letter == key:
            phonetic_code_words.append(phonetic_code_dict[key])
print(phonetic_code_words)
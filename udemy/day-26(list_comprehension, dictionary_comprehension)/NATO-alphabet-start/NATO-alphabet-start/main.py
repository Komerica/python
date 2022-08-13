import pandas

################################################
# My Code ######################################
# Using for loop instead of List Comprehension #
################################################

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(type(data))  # pandas를 사용해 read_csv를 하면 tpye이 DataFrame으로 바로 나온다!
# alphabet_dataframe = pandas.DataFrame(data)  # 굳이 이 과정을 안 거쳐도 위에서 바로 DataFrame으로 저장됨
# print(type(alphabet_dataframe))

phonetic_code_dict = {}
for (index, row) in data.iterrows():
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

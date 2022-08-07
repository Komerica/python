sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

#########################################
# Method1 Using Dictionary Comprehension #
#########################################
# Write your code below:
word_list = sentence.split(" ")
print(word_list)

result = {word: len(word) for word in word_list}
print(f"Method1 result: {result}")

##########################
# Method2 Using For loop #
##########################
word_list2 = sentence.split(" ")

word_count_dict = {}
for word in word_list2:
    word_count_dict[f"{word}"] = len(word)

print(f"Method2 result: {word_count_dict}")


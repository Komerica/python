# Method1) My answer

name1 = input("What is the first person's name? ")
name2 = input("What is the second person's name? ")

count1 = 0
count2 = 0
true = "TRUE"
love = "LOVE"
for i in true:
    print(f"{i} occurs {name1.lower().count(i.lower())+name2.lower().count(i.lower())} times")
    count1 += name1.lower().count(i.lower())
    count1 += name2.lower().count(i.lower())
print(f"Total = {count1}")

for i in love:
    print(f"{i} occurs {name1.lower().count(i.lower())+name2.lower().count(i.lower())} times")
    count2 += name1.lower().count(i.lower())
    count2 += name2.lower().count(i.lower())
print(f"Total = {count2}")

print(f"Love Score = {count1}{count2}")

score = int(f"{count1}{count2}")
if score < 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


#Method2) Udemy answer
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

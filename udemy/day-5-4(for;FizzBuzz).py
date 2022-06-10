
# # Instructions

# You are going to write a program that automatically prints the solution to the FizzBuzz game.

# > `Your program should print each number from 1 to 100 in turn.`

# >   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".`

# >     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# >       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# 숫자 넣으면 답을 알 수 있는 기계
num = int(input("Please enter a number: "))

if num % 15 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(f"{num}")

# Method1) Answers between 1 and 100
# 👇아래과정 굳이 안해줘도 in range(1,101)하면 list로 됨!
# num_list = []
# for num in range(1, 101):
#     num_list.append(num)

for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(f"{num}")

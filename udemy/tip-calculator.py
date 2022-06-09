#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

result = (bill*(1+tip/100))/people
#formatting to decimal places(소수점 둘째자리까지 표현하기)
#Method 1)👇
final_amount = "{:.2f}".format(result)
print(f"Each person should pay: ${final_amount}")
#Method 2)👇
#print(f"Each person should pay: ${result:.2f}")
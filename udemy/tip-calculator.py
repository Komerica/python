#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.πͺ

#Write your code below this line π
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

result = (bill*(1+tip/100))/people
#formatting to decimal places(μμμ  λμ§Έμλ¦¬κΉμ§ νννκΈ°)
#Method 1)π
final_amount = "{:.2f}".format(result)
print(f"Each person should pay: ${final_amount}")
#Method 2)π
#print(f"Each person should pay: ${result:.2f}")
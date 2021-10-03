#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("The tip Calculator")
bill = float(input("Total Bill?: $"))
tip = float(input("Would you like to give 12, 15, or 20?: "))
people = int(input("How many people to split the bill?: "))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip
bill_person = total_bill / people
result = round(bill_person,2)
print(f"Each person shoud pay: ${result}")





print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage would you like to give? 10, 12, or 15? "))
nop=int(input("How many people to split the bill? "))
bill_with_tip = total_bill+(total_bill*(tip_percentage/100))
per_person =  bill_with_tip/nop
print("Each person should pay:",round(per_person,2))

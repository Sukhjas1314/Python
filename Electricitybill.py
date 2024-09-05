units = int(input("Enter the number of units consumed in a month : "))

if units <= 100 :
    print("No charge or ₹ 0 is your electricity bill")
elif units > 100 and units <= 200 :
    amount = units * 5 
    print("Your electricity bill amount is :₹",amount)
else :
    amount = units * 10 
    print("Your electricity bill amount is :₹",amount)
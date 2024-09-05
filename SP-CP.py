CP = float(input("Enter the Cost price : "))
SP = float(input("Enter the Selling price : "))

if SP > CP :
    Profit = SP - CP 
    print("The profit is : ",Profit)
elif SP == CP : 
    print("It is neither profit nor loss.")
else :
    Loss = CP - SP
    print("The loss is : ",Loss)
x = float(input("Enter the cost price of your bike : "))

if x > 100000 :
    road_tax = x * 0.15
    print("The road tax for your bike is :",road_tax)
elif x >50000 and x<=100000 :
    road_tax = x * 0.1
    print("The road tax for your bike is :",road_tax)
else :
    road_tax = x * 0.05 
    print("The road tax for your bike is :",road_tax)
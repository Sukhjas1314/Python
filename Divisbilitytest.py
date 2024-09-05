x = int(input("Enter any positive no. : "))
print(x)

if x%5==0 or x%3==0 :
    if x%15!=0 :
        print(x,"is divisible by 5 or 3 but not 15.")
    else :
        print(x,"is divisible by 5 and 3 and by 15 also.")
else :
    print(x,"is not divisible by 5 or 3 and not by 15 also.")
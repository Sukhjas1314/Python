n1 = float(input("Enter 1st number : "))
n2 = float(input("Enter 2nd number : "))
n3 = float(input("Enter 3rd number : "))

if n1>n2 and n3>n2 :
    print(n2,"is the smallest of the 3")
elif n2>n1 and n3>n1 :
    print(n1,"is the smallest of the 3")
elif n2>n3 and n1>n3 :
    print(n3,"is the smallest of the 3")
else :
    print("Either of the 3 are equal")
a = float(input("Enter side a length : "))
b = float(input("Enter side b length : "))
c = float(input("Enter side c length : "))

if a==b==c :
    print("It is an equilateral triangle.")
elif (a==b and a!=c and b!=c) or (a==c and b!=a and b!=c) or (b==c and a!=c and b!=a) :
    print("It is an isosceles triangle.")
else :
    print("It is a scalene triangle.")
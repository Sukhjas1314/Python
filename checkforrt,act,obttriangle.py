a = float(input("Enter side a length : "))
b = float(input("Enter side b length : "))
c = float(input("Enter side c length : "))

if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
    print("It is an right angled triangle.")
elif a**2+b**2<c**2 or a**2+c**2<b**2 or c**2+b**2<a**2 :
    print("It is an obtuse angled triangle.")
else :
    print("It is an acute angled triangle.")
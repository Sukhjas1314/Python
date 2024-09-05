a = float(input("Enter side a length : "))
b = float(input("Enter side b length : "))
c = float(input("Enter side c length : "))

if a+b>c or a+c>b or b+c>a :
    if a==0 or b==0 or c==0 :
        print("These are not the sides of the triangle.")
    else :
        print("These are the sides of a triangle.")
else :
    print("These are not the sides of the triangle.")
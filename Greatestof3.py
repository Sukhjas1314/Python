n1 = int(input("Enter the first no. : "))
n2 = int(input("Enter the second no. : "))
n3 = int(input("Enter the third no. : "))

print(n1,n2,n3)
# if n1>n2 and n1>n3 :
#     print(n1,"is greater than",n2,"and",n3)
# elif n2>n1 and n2>n3 :
#     print(n2,"is greater than",n1,"and",n3)
# elif n3>n1 and n3>n2 :
#     print(n3,"is greater than",n1,"and",n2)

                                # OR (by nested if-else)

if n1>n2 :
    if n1>n3 :
        print(n1,"is greater than",n2,"and",n3)
    else :
        print(n3,"is greater than",n1,"and",n2)
else :
    if n2>n3 :
        print(n2,"is greater than",n1,"and",n3)
    else :
        print(n3,"is greater than",n2,"and",n1)

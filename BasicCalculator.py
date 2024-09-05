# n1 = float(input("Enter the first no. : "))
# n2 = float(input("Enter the second no. : "))

# operator = input("Enter the operator : ")

# match operator :
#     case "+" :
#         print("Sum :",n1 + n2)
#     case "-" :
#         print("Difference :",n1 - n2)
#     case "*" :
#         print("Multiplication :",n1 * n2)
#     case "/" :
#         print("Division :",n1 / n2)
#     case "%" :
#         print("Remainder :",n1 % n2)
#     case "//" :
#         print("Whole no. part of  Quotient :",n1 // n2)
#     case "&" :
#         print(n1,"and",n2,":",n1 & n2)
#     case "|" :
#         print(n1,"or",n2,":",n1 | n2)
#     case "^" :
#         print(n1,"xor",n2,":",n1 ^ n2)
#     case _ :
#         print("Invalid operator!")
    

                                                #or
n1 = float(input("Enter number n1 = "))
n2 = float(input("Enter number n2 = "))

operator = input("Enter the operator : ")

match operator :
    case "+" :
        print(n1,"+",n2,"=",n1+n2)
    case "-" :
        print(n1,"-",n2,"=",n1-n2)
    case "*" :
        print(n1,"*",n2,"=",n1*n2)
    case "/" :
        print(n1,"/",n2,"=",n1/n2)
    case "//" :
        print(n1,"//",n2,"=",n1//n2)
    case "%" :
        print(n1,"%",n2,"=",n1%n2)
    case "**" :
        print(n1,"**",n2,"=",n1**n2)
    case "|" :
        print(n1,"|",n2,"=",n1|n2)
    case "&" :
        print(n1,"&",n2,"=",n1&n2)
    case "^" :
        print(n1,"^",n2,"=",n1^n2)
    case _ :
        print("Invalid operator!!")
    
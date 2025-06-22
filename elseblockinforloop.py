                        # (1)
            # Printing no. from a starting to end point
# for i in range(1,6,1):
#     print(i)
# else :
#     print("Done!")


                        # (2)
            # Prime no. from a starting to end point
# n = int(input("Enter the no. till which you want to access the prime numbers : ")) 
# for i in range(1,n+1):
#     if i > 1 :
#         for j in range(2,i):
#             if (i%j)== 0 :
#                 break
#         else :
#             print(i)



                        # (3)
# Fibonnaci series
# num1 = 0
# num2 = 1
# n = int(input("Enter the end point till which you want to stop the fibonnaci series : "))
# result = 0
# for i in range(0,n):
#     print(num1,end = " ")
#     result = num1+num2
#     num1 = num2
#     num2 = result




                        # (4)
        # Factorial of a number
# n = int(input("Enter the no. for which you want to have the factorial : "))
# f = 1
# if n < 0:
#     print("The factorial of",n,"doesn't exist.") 
# elif n == 0:
#     print("The factorial of",n,"is 1")
# else:
#         for i in range(1,n+1):
#                 f = f * i
#         print("The factorial of",n,"is",f)






                        # (5)
        # Reverse of a number
# n = int(input("Enter any no.(2 digit and above) : "))
# rev_no = 0
# while n > 0:
#     rem = n % 10
#     rev_no = (rev_no * 10) + rem
#     n = n // 10
# print("The reversed no. is :",rev_no)
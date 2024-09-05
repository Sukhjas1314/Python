# def factorial(a):
#   ans = 1
#   if a == 0 :
#     ans = 1
#   else :
#     for i in range(1,n+1):
#       ans *= i

#   return ans




# def factorial(n):
#   ans = 1
#   if n == 0:
#     return 1
#   ans = n * factorial(n-1)
#   return ans

# n = int(input("Enter the number  : "))
# result = factorial(n)
# print('The factorial of',n,'is :',result)


# def printn(n):
#   if n == 0:
#     return
  
#   printn(n-1)
#   print(n)

# n = int(input("Enter the number : "))
# print(printn(n))



# def sum(n):
#   ans = 0
#   if n == 0:
#     return 0
#   ans = n + sum(n-1)
#   return ans


# n = int(input("Enter the number : "))
# print(sum(n))


# def powera_b(a,b):
#   ans = 1
#   if b == 0:
#     return 1
#   ans = a * powera_b(a,b-1)
#   return ans

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# print(powera_b(a,b))



def fibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else :
    return (fibonacci(n-1) + fibonacci(n-2))
  
n = int(input("Enter the number : "))
for i in range(1,n+1):
  print(fibonacci(i))


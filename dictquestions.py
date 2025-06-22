#         # Q1.
# dict = {
#     "a" : 100,
#     "b" : 200,
#     "c" : 300
# }
# print(dict.values())
# print("The sum is :",sum(dict.values()))

# print("--------------------------------")

#         # Q2.
# dict2 = {
#     "x" : 25,
#     "y" : 18,
#     "z" : 45
# }
# print(dict2.values())
# print("The sum is :",sum(dict2.values()))


        # Q3.
# input_str = input("Enter the string : ")
# n = int(input("Enter n : "))

# alphabets = "abcdefghijklmnopqrstuvwxyz"
# reverse = alphabets[::-1]
# dict1 = dict(zip(alphabets,reverse))

# prefix = input_str[0:n-1]
# suffix = input_str[n-1:]

# mirror = ""
# for i in range(0,len(suffix)):
#     mirror = mirror + dict1[suffix[i]]

# result = prefix + mirror
# print(result)
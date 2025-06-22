# name1 = "Sukhman"
# name2 = "Jashan"

# for i in name1:                   # to print all the characters of the the word
#   print(i)

# print(type(name1))
# print(name2)
# print(name1[-1])
# print("\n")
# # using list comprehension
# list = [char for char in name1]           # to print all the characters of the the word
# for i in list:
#   print(i)
# print("\n")

# print(len(name1))             # to find the length of the string

# print(name1.find('k'))        # to search for the character

# print(name1[1:])        # slicing


# print(name1.upper())      # to convert into uppercase
# print(name2.lower())      # to convert into lowercase


# str = "sukhmanpreet singh singh"
# print(str.capitalize())       # to capitalize the first letter of each word

# str1 = "    Hello"            # to remove the space
# print(str1.strip())


# print(str.replace("singh","Singh",1))         # to replace the the character or word


# S = "apple banana mango"
# list = S.split(" ",1)             # to split the words having different kinds of seperations
# print(list)


# str2 = "Hello World"
# str3 = ", What a great day!"
# print(str2 + str3)                 # to concatenate two or more strings

# std_name = "Sukhman"
# std_marks = 100                         # to format the data 

# str = "The student name is {s}, and his marks are {m}".format(s = std_name , m = std_marks)
# print(str)


# def palindrome(string):
#   if string[::-1]==string:
#     print(True)
#   else :
#     print(False)

  

def check_palindrome(str):
  clean_str = (str.replace(" ","")).lower()

  reverse_str = clean_str[::-1]
  return clean_str == reverse_str


str = input("Enter any string : ")
if check_palindrome(str):
  print("It is a palindrome string.")
  
else :
  print("It is not a palindrome string.")



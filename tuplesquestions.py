# Q1.                   # reversed of a tuple
n= int(input("Enter the size of the tuple : "))
input_tuple = []

for i in range(n) :
    num = int(input("Enter the item : "))
    input_tuple.append(num)
print(input_tuple)

list = []
for x in reversed(input_tuple) :
    list.append(x)

input_tuple = tuple(input_tuple)
print(input_tuple)
output_tuple = tuple(list)
print(output_tuple)
                    # Q1.
list = [23,65,19,90]
temp = list[0]
list[0] = list[2]
list[2] = temp
print(list)

print("--------------------------------")

                    # Q2.
list1 = [1,2,3,4,5]
temp1 = list1[1]
list1[1] = list1[4]
list1[4] = temp1
print(list1)

                                    # OR
                    # to create a list and then do swapping
n = int(input("Enter size of the list : "))
list = []
for i in range(n) : 
    num = int(input("Enter the item : "))
    list.append(num)
print(list)

idx1 = int(input("Enter index 1 : "))
idx2 = int(input("Enter index 2 : "))
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)
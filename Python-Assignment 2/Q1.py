# Q.Create a List L defined as [10, 20, 30, 40, 50, 60, 70, 80] and perform the following operations:
# i. Add 200 and 300 to L.
# ii. Remove 10 and 30 from L.
# iii. Sort L in ascending order.
# iv. Sort L in descending order.

L = [10,20,30,40,50,60,70,80]

L.append(200)
L.append(300)
print('\nAfter adding 200 and 300 in the list :',L)

L.remove(10)
L.remove(30)
print('\nAfter removing 10 and 30 in the list :',L)

L.sort()
print('\nAfter sorting the list in ascending order :',L)

L.reverse()
print('\nAfter sorting the list in descending order :',L)




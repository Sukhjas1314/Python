# Q.D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}.
# (i) WAP to add new entry in D; key=6 and value is “Six”
# (ii) WAP to remove key=2.
# iii) WAP to check if 6 key is present in D.
# (iv) WAP to count the number of elements present in D.
# (v) WAP to add all the values present D.

D = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five' }

D[6] = 'Six'
print('\nAfter adding 6 in the Dictctionary : \n\t',D)

del D[2]
print('\nAfter removing 2 from the Dictctionary : \n\t',D)

is_there = False
if 6 in D:
    is_there = True
    print('\nChecking if 6 is there in the Dictctionary : \n\t',is_there)
else:
    is_there = False
    print('\nChecking if 6 is there in the Dictctionary : \n\t',is_there)

print('\nNo. of elements in the dictionary : \n\t',len(D))

sum = 0
for i in D:
    sum += i
print('\nSum of all values in the dictionary : \n\t',sum)
    

# Q.Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and perform the following operations:
# i. Identify the highest score and its index in the tuple.
# ii. Find the lowest score and count how many times it appears.
# iii. Reverse the tuple and return it as a list.
# iv. Check if a specific score 76 (input by the user) is present in the tuple and print its first occurrence index, or a message saying it’s not present.

score = (45,89.5,76,45.4,89,92,58,45)

print('\nHighest score :',max(score))
print('\nIndex of the highest score :',score.index(max(score)))

print('\nLowest score :',min(score))
print('\nCount of the lowest index :',score.count(min(score)))

print('\nAfter reversing the tuple :',score[::-1])

if 76 in score:
    print('\n76 is present in the tuple')
    print('First occurence of 76 in the tuple :',score.index(76))
else:
    print('\n76 is not present in the tuple')
print('\n')


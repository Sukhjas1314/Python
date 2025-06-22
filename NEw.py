# w = input("Enter any string value : ")
# word = w.upper()
# n = len(word)
# print(word)
# print(n)


w = input("Enter any word : ")
word = w.upper()
for i in range(1,len(word)+1):
    for j in range(i):
        print(word[j], end=" ")
    print()
for k in range(len(word)-1,0,-1):
    for h in range(k):
        print(word[h],end = " ")
    print()

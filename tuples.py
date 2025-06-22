            # for a single entity
# fruits = ("apple")
# print(type(fruits))
# print("--------------------------------")

# fruits1 = tuple("apple")
# print(type(fruits1))
# print("--------------------------------")

# fruits2 = list("apple")
# print(type(fruits2))
# print("--------------------------------")


colours = ("red", "blue", "green", "red")

print(type(colours))                # checking the type of class                
print("--------------------------------")

print(len(colours))                 # checking length
print("--------------------------------")

print(colours[-2])                  # accessing items through indexing
print("--------------------------------")

print(colours[-3:])                 # accessing items through range indexing
print("--------------------------------")

if "green" in colours :             # use of in operator
    print("Green is there in the tuple colours.")
print("--------------------------------")

for i in colours :                  # traversing through the tuple
    print(i)
print("--------------------------------")

new_colours = ("yellow","brown")    # concatenation of 2 tuples
colours = colours + new_colours
print(colours)
print("--------------------------------")

colour1 , colour2 , colour3 , colour4 , colour5 , colour6 = colours  # unpacking a tuple
print(colour1)
print(colour2)
print(colour3)
print(colour4)
print(colour5)
print(colour6)
print("--------------------------------")
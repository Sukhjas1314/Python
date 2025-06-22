fruits = ["apple","banana","mango","grapes"]

print(fruits[3])                            # print the item from the list
print("--------------------------------")

print(type(fruits))                         # print the datatype of the item    
print("--------------------------------")

print(len(fruits))                          # print the length of the list
print("--------------------------------")

print(fruits[-4])                           # print the value of the particular index of the list
print("--------------------------------")

print(fruits[0:4])                          # print the values of the particular range of the list
print("--------------------------------")

appended = fruits.append("guava")           # add an item at the end of the list
print(fruits)
print("--------------------------------")

fruits.insert(2,"watermelon")               # add the item at a particular index in the list
print(fruits)
print("--------------------------------")

fruits2 = ["melon","blueberry"]             # adding 2 or more lists to make a single list
fruits.extend(fruits2)
print(fruits)
print("--------------------------------")

fruits.remove("melon")                      # removing an item by its name
print(fruits)
print("--------------------------------")

fruits.pop(3)                               # removing item by its index
print(fruits)
print("--------------------------------")

fruits.pop()                                # removing the last item from the list
print(fruits)
print("--------------------------------")

if "banana" in fruits :                     # Use of in
    print("Banana is there in the list of fruits.")
print("--------------------------------")

if "kiwi" not in fruits:                    # Use of not in
    print("Kiwi is not included in the list of fruits.")
print("--------------------------------")
        
fruits[1]= "dragon fruit"                   # Changing item in a list at an index
print(fruits)
print("--------------------------------")

fruits[1:3]= ["kiwi","dragon fruit"]      # Changing item in a list in a range
print(fruits)
print("--------------------------------")

fruits.sort()                               # ascending order
print(fruits)
print("--------------------------------")

fruits.sort(reverse = True)                 # descending order
print(fruits)
print("--------------------------------")

fruits.reverse()                            # to reverse the items in the list
print(fruits)
print("--------------------------------")

new_fruits = [fruit for fruit in fruits if "a" in fruit]  # to make a new list from the items from the existing list
print(new_fruits)
print("--------------------------------")

new_fruits = fruits.copy()                  # to copy a list in another
print(new_fruits)
print("--------------------------------")

new_fruits = fruits + new_fruits            # to add 2 list using '+' operator
print(new_fruits)
print("--------------------------------")

fruits.insert(2,["kiwi","papaya"])            # nested list
print(fruits)
print(fruits[2])
print(fruits[2][0])
print("--------------------------------")


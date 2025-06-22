names = {"Sukhman", "Daksh", "Harith"}       
          
# print(names)                                            # printing a set
# print("--------------------------------")

# print(len(names))                                       # checking length of the set
# print("--------------------------------")

# print(type(names))                                      # checking the type of class 
# print("--------------------------------")

# for i in names :                                        # accessing all items or traversing the set
#     print(i)
# print("--------------------------------")

# if "Sukhman" in names :                                 # using in operator
#     print("He is present in the class.")
# print("--------------------------------")

# if "Gaurav" not in names :                              # using not in operator
#     print("He is absent today.")
# print("--------------------------------")

# names.add("Gaurav")                                     # to add an item in the set
# print(names)
# print("--------------------------------")

# names1 = {"Jashan","Seerat", "Daksh"}                            # to add another sequence
# names.update(names1)
# print(names)
# print("--------------------------------")

# names.remove("Gaurav")                                  # to remove an item
# print(names)
# print("--------------------------------")

# names.discard("Pritish")                                # to remove an item which is not present in the set
# print(names)
# print("--------------------------------")

# names2 = names.union(names1)                            # to join 2 sets with no duplicate values
# print(names2)
# print("--------------------------------")

# names1 = {"Jashan","Seerat", "Daksh"}                   # to get intersection of 2 sets
# names.intersection_update(names1)
# print(names)
# print("--------------------------------")

names1 = {"Jashan","Seerat", "Daksh"}                     # to get everything except duplicates
names.symmetric_difference_update(names1)
print(names)
print("--------------------------------")

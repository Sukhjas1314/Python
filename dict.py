phones = {"Sukhman" : 9876589414,
          "Mumma" : 9717680309,
          "Papa"  : 9810416719}
print(phones)
print("--------------------------------")


print(type(phones))
print("--------------------------------")

print(len(phones))
print("--------------------------------")

print(phones["Sukhman"])
print(phones["Mumma"])
print(phones["Papa"])
print("--------------------------------")

print(phones.keys())
print("--------------------------------")

phones["Nannu"] = 9872777348
print(phones)
print("--------------------------------")

phones.pop("Sukhman")
print(phones)
print("--------------------------------")

phones.popitem()
print(phones)
print("--------------------------------")

for i,j in phones.items():
    print(i,":",j)



print("-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-------x-------")

Area = {"Area1" : {
            "x" : 0,
            "y" : 1,
            "z" : 2
        },
        "Area2" : {
            "a" : 3,
            "b" : 4,
            "c" : 5
        }
}
print(Area)
print("--------------------------------")

print(Area["Area1"]["z"])
print("--------------------------------")

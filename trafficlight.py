# x =input("Enter the colour of the signal : ")
# print("As the signal is :"+x+". The message it gives is :")
# if x=="red" :
#     print("Stop")
# elif x=="yellow" :
#     print("Ready to move")
# elif x=="green" :
#     print("Go")
# else :
#     print("Invalid signal")


                                # Or 

x =input("Enter the colour of the signal : ")
print("\nAs the signal is :"+x+".\nThe message it gives is :")

match x :
    case "red" :
        print("Stop")
    case "yellow" :
        print("Ready to move")
    case "green" :
        print("Go")
    case _ :
        print("Invalid signal!!")


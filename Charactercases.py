x = input("Enter any character(alphabet[any case],numbers[0-9],special symbols): ")

if chr(65) <= x and chr(90) >= x :
    print(x,"is a uppercase letter/alphabet.")
elif chr(97) <= x and chr(122) >= x :
    print(x,"is a lowercase letter/alphabet.")
elif chr(48) <= x and chr(57) >= x :
    print(x,"is a string integer.")
elif (chr(0) <= x and chr(48) >= x) or (chr(58) <= x and chr(64) >= x) or (chr(91) <= x and chr(96) >= x) :
    print(x,"is a special symbol.")


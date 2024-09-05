n = int(input("Enter any positive no. : "))

if n==1 :
    print("It is neither prime nor composite no.")
elif n>1 :
    for i in range(2,n) :
        if (n%i)==0 :
            print(n,"is a composite no.")
            break
    else :
        print(n,"is a prime no.")

    
        
       
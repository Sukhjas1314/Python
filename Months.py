month = input("Enter the month : ")

match month :
    case "January" :
        days = 31
        print("Welcome to the 1st month of the year and my mammu's birthday fall in this month with no. of days =",days)
    case "February" :
        year = input("Which year are you asking for (Leap year/Normal year) :")
        if year== "Leap year" :
            days = 29
            print("Welcome to the shortest month of the year and the month of the birth anniversary of my brother and masadji with no. of days =",days)
        else :
            days = 28
            print("Welcome to the shortest month of the year and the month of the birth anniversary of my brother and masadji with no. of days =",days)
    case "March" :
        days = 31 
        print("Welcome to the month of holi festival with no. of days =",days)
    case "April" :
        days = 30
        print("Welcome to the month of Birth anniversary of my naani with no. of days =",days)
    case "May" :
        days = 31
        print("Welcome to the month of birth anniversary of my sister with no. of days =",days)
    case "June" :
        days = 30
        print("Welcome to the hottest month of the year and the month of the birth anniversary of my massi with no. of days =",days)
    case "July" :
        days = 31
        print("Welcome to the month of July with no. of days =",days)
    case "August" :
        days = 31
        print("Welcome to the month of the birth anniversary of my dadaji with no. of days =",days)
    case "September" :
        days = 30
        print("Welcome to the month of the September with no. of days =",days)
    case "October" :
        days = 31
        print("Welcome to the month of festivals and the birth anniversary of my papa and naanu with no. of days =",days)
    case "November" :
        days = 30
        print("Welcome to the month of the birth anniversary of my mumma with no. of days =",days)
    case "December" :
        days = 31
        print("Welcome to the last month and the month of the birth anniversary of my dadi mumma with no. of days =",days)
    case _ :
        print("Invalid month!")
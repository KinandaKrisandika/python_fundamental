print("How to find out a leap year\n")

year = int(input("Enter year : "))

if (year % 4) == 0 or (year % 100) == 0 or (year % 400) == 0 :
    print("It's a leap year")
else :
    print("It's not a leap year")
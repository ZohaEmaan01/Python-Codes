def magicdateornot():
    month = int(input("enter a month: "))
    day = int(input("enter a day: "))
    year = int(input("enter last two digits of year: "))

    if month * day == year:
        print("the date is magic")
    else:
        print("the date is not magic")


magicdateornot()

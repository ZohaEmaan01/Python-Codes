def magicdate_or_not(dd,mm,yy):
    if dd * mm == yy:
        return "The date is magic date"
    else:
        return "The date is not magic date"


def main():
    a = int(input("enter a day: "))
    b = int(input("enter a month: "))
    c = int(input("enter last two digits of year: "))
    g = magicdate_or_not(a,b,c)
    print(g)


main()

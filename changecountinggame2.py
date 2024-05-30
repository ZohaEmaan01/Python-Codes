def change_counting_game(p,n,d,q):
    pennies = p * 1/100
    nickels = n * 1/20
    dimes = d * 1/10
    quarters = q * 1/4
    total = pennies + nickels + dimes + quarters
    dollar = 1
    if total == dollar:
        return('Congratulations you have won the game')
    elif total > dollar:
        return('The amount entered is more than one dollar')
    else:
        return('The amount entered is less than one dollar')
    print('$',total)
def main():
    p = float(input('enter number of pennies: '))
    n = float(input('enter number of nickels: '))
    d = float(input('enter number of dimes: '))
    q = float(input('enter number of quarters: '))
    e = change_counting_game(p,n,d,q)
    print(e)
main()


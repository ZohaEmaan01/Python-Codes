def factorial(n):
    i = 1
    fac = 1
    while i <= n:
        fac = fac * i
        i = i + 1
    return(fac)

def main():
    num = int(input('enter number: '))
    a = factorial(num)
    print(a)
main()

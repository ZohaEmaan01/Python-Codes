def cuberoot(x):
    print('cube: ',end=' ')
    return x * x * x

def main():
    x = 0
    while x > -1:
        x =  int(input('number: '))
        if x > -1:
            result = cuberoot(x)
            print(result)
main()

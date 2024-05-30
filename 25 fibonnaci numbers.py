def fibbonacci_numbers():

    a = [0] * 25
    n = 25
    i = 0
    a[0] = 0
    a[1] = 1
    print(a[0],a[1],end=',')
    s = 0
    while i < (n - 2):
        a[i + 2] = a[i] + a[i + 1]
        print(a[i + 2],end=',')
        s = s + a[i] + a[i + 1]
        i = i + 1

    print('sum is',s)


fibbonacci_numbers()

n = 249

i = 1
while i <= 8:
    if n & 2 ** (i - 1) == 0:
        pass
    else:
        print(i,'bit is on')
    i = i + 1

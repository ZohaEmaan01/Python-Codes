class rationalnumbers:
    pass
def main():
    r = rationalnumbers()
    r.p = int(input('enter the numerator: '))
    r.q = int(input('enter the denomenator: '))
    if r.q != 0:
        print(r.p/r.q)
    else:
        print('enter non negative denomenator')
main()

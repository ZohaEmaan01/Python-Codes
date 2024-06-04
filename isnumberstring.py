def is_Number(a):
    i = 0
    r = ""
    while i < (len(a)):
        if ord(a[i]) >= ord("0") and ord(a[i]) <= ord("9"):
            r = r + a[i]
        else:
            return False
        i = i + 1
    return True


def main():
    string = input("enter string:")
    c = is_Number(string)
    print(c)


main()

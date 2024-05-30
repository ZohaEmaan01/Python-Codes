def count_vowel(a):
    count = 0
    r = ""
    i = 0
    while i < (len(a)):
        if a[i] == "a":
            count = count + 1
        elif a[i] == "e":
            count = count + 1
        elif a[i] == "i":
            count = count + 1
        elif a[i] == "o":
            count = count + 1
        elif a[i] == "u":
            count = count + 1
        else:
            r = r + a[i]
        i = i + 1
    return count


def main():
    string = input("enter string: ")
    b = count_vowel(string)
    print(b)


main()

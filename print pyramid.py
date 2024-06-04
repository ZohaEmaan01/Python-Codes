def print_pyramid(m, u):
    i = 0
    max = (ord(u) - ord(m) + 1) / 2
    max = int(max)
    while i <= max:
        j = max
        while j > i:
            print(" ", end="")
            j = j - 1
        j = 0
        st = m
        while j <= i:
            print(st, end="")
            st = chr(ord(st) + 1)
            j = j + 1
        k = 0
        while k < i:
            print(st, end="")
            st = chr(ord(st) + 1)
            k = k + 1
        print("")
        i = i + 1


def main():
    print_pyramid("m", "u")
main()

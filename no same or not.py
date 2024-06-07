def same_no():
    n = int(input('enter no: '))
    r = int(input('enter no: '))
    count_diff_bit = 0
    for i in range (4):
        if n % 2 != r % 2:
            count_diff_bit = + 1
            n = n / 2
            r = r / 2

    if count_diff_bit == 0:
            print('number is same')
    else:
            print('number is different')
same_no()

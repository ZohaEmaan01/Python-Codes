import random
def display(x):
    for i in range(5):
        for j in range(5):
            print(x[i][j],end=' ')
        print()
    print('==================================')
def row_sum(x):
    i = 0
    j = 0
    sum1 = 0
    if i <= 0 and j <= 5:
        print(x[0][0],x[0][1],x[0][2],x[0][3],x[0][4],end=' ')
        sum1 = sum1 + (x[0][0]+x[0][1]+x[0][2]+x[0][3]+x[0][4])
    print(' ','Sum is: ',sum1)

    i = 1
    j = 0
    sum2 = 0
    if i <= 1 and j <= 5:
        print(x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],end=' ')
        sum2 = sum2 + (x[1][0]+x[1][1]+x[1][2]+x[1][3]+x[1][4])
    print(' ','Sum is: ',sum2)

    i = 2
    j = 0
    sum3 = 0
    if i <= 2 and j <= 5:
        print(x[2][0],x[2][1],x[2][2],x[2][3],x[2][4],end=' ')
        sum3 = sum3 + (x[2][0]+x[2][1]+x[2][2]+x[2][3]+x[2][4])
    print(' ','Sum is: ',sum3)


    i = 3
    j = 0
    sum4 = 0
    if i <= 3 and j <= 5:
        print(x[3][0],x[3][1],x[3][2],x[3][3],x[3][4],end=' ')
        sum4 = sum4 + (x[3][0]+x[3][1]+x[3][2]+x[3][3]+x[3][4])
    print(' ','Sum is: ',sum4)

    i = 4
    j = 0
    sum5 = 0
    if i <=4  and j <= 5:
        print(x[4][0],x[4][1],x[4][2],x[4][3],x[4][4],end=' ')
        sum5 = sum5 + (x[4][0]+x[4][1]+x[4][2]+x[4][3]+x[4][4])
    print(' ','Sum is: ',sum5)

def main():

    x=[[random.randint(11,99) for i in range(5)] for j in range(5)]
    display(x)
    row_sum(x)
main()

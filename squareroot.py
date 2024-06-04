def squareroot(x,sq = 1):
    if abs(x/sq - sq) < 0.000001:
        return sq
    return(squareroot(x,(sq+x/sq)/2))

print(squareroot(25))

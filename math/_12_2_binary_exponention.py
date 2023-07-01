
def binaryExponentiation(x, y):
    if y == 0:
        return 1
    
    res = 1
    while y>0:

        if y%2 == 1:
            res *= x

        x *= x
        y //= 2

    return res

print(binaryExponentiation(3, 4))
print(binaryExponentiation(4, 5))

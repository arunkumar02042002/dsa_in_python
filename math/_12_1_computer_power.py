def power(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    
    temp = power(x, y//2)
    temp *= temp

    if y % 2 == 0:
        return temp
    
    else: return temp*x

print(power(2, 10))
print(power(2, 11))
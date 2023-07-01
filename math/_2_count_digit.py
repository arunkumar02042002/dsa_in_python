import math

def countDigit(n):
    return int(math.log10(n))+1

print(countDigit(1028))
print(countDigit(1))
print(countDigit(15646464))
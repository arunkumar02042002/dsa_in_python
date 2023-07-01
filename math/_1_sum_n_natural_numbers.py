def sumN(n):
    """
    You must perform the division first to avoid overflow.
    However, the integer size has no limit in Python.
    """
    return int(n*((n+1)/2))

print(sumN(9))
print(sumN(10))
print(sumN(5))
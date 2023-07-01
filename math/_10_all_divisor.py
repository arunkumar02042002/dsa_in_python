def allDivisor(n):
    all_divisors = []
    for i in range(1, int(n**0.5)):
        if n%i == 0:
            all_divisors.append(i)

    while i >= 1:
        if n%i == 0:
            all_divisors.append(n//i)
        i -= 1
    return all_divisors

print(allDivisor(10))
print(allDivisor(100))
print(allDivisor(150))
print(allDivisor(50))
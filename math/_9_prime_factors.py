def primeFactors(n):
    prime_factors = []

    while n%2 == 0:
        prime_factors.append(2)
        n //= 2

    i = 3
    while i < (n**0.5+1):
        while n%i == 0:
            prime_factors.append(i)
            n //= i
        i += 2
        
    
    if n > 2:
        prime_factors.append(n)

    return prime_factors



print(primeFactors(200))
print(primeFactors(405))
print(primeFactors(711))
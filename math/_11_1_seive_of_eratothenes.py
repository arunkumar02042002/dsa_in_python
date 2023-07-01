from _8_isPrime import isPrime

def sieveOfEratosthenes(n):
    all_primes = [2]
    i = 3
    while i <= n:
        if isPrime(i):
            all_primes.append(i)
        i += 2

    return all_primes

print(sieveOfEratosthenes(10))
print(sieveOfEratosthenes(2))
print(sieveOfEratosthenes(3))
print(sieveOfEratosthenes(5))
print(sieveOfEratosthenes(100))
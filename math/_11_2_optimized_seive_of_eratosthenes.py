def sieveOfEratosthenes(n):
    isPrime = [True]*(n+1)

    i = 2
    while i <= n:
        if isPrime[i]:
            print(i, end=" ")

            j = i
            while j <= n:
                isPrime[j] = False
                j += i
        i += 1
sieveOfEratosthenes(25)
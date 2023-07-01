def isPrime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n%2 == 0 or n%3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2)==0:
            return False
        i += 6

    return True

if __name__ == "__main__":
    print(isPrime(5))
    print(isPrime(2))
    print(isPrime(3))
    print(isPrime(1))
    print(isPrime(13))
    print(isPrime(17))
    print(isPrime(25))
    print(isPrime(91))
def gcd(x, y):
    if x%y == 0:
        return y
    
    return gcd(y, x%y)

if __name__ == "__main__":
    print(gcd(98, 56))
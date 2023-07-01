from _6_GCD import gcd

def lcm(x, y):
    if x == 0 or y == 0:
        return 0
    
    return int(x / gcd(x, y) * y)

if __name__ == "__main__":
    print(lcm(5, 13))
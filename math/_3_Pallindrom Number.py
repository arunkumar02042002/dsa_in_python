def pallindormNumber(n):
    temp = n
    reverse = 0

    while temp > 0:
        reverse = reverse*10 + temp%10
        temp = temp//10
    return reverse == n

print(pallindormNumber(1001))
print(pallindormNumber(125))
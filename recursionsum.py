def sum(n):
    if n==1:
        return 1
    s=(2*n-1)+sum(n-1)
    return s

print(sum(5)) # Expected output: 15
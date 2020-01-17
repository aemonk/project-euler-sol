# 6-problem
def squaresumdiff(n):
    x = [i**2 for i in range(n+1)]
    y = [i for i in range(n+1)]
    z = sum(y)**2
    ret = z - sum(x)
    return ret

print(squaresumdiff(100))
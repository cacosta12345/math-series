def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0,1
    for i in range(2, n+1):
        a,b = b, a+b
    return b

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    a, b = 2,1
    for i in range(2, n+1):
        a,b = b, a+b
    return b
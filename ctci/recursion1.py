def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def taylor(x, n):
    if n == 0:
        return 1
    else:
        return (((2*x)**n)/fact(n)) + taylor(x, n-1)

print(taylor(3,4))
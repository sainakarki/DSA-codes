def fibo(n):
    fibo = 2
    first=0
    second=0
    for i in range(2, n, +1):
        fibo = first + second
        a , b = b, fibo
    return fibo

n = int(input('Enter the value of n:'))
print("The reuired series is:", fibo(n))
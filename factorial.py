def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact
    
n = int(input('Enter the value of n:'))
if n<1:
    print('Factorial is not defined')
else:    
 print('The reuired factorial is:', fact(n))
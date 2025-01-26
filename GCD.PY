def gcd(a, b):
    if( a == 0):
       return 
    elif(b == 0):
      return a
    else:
       while(b != 0):
        r = a % b
        a, b = b, r
    return a

a = int (input('Enter the value of a:'))
b = int(input("Enter the value of b:"))
print('The required gcd is:', gcd(a,b))    
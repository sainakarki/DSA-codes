def linear_search(arr, n, key):
    flag=0
    for i in range(n):
        if(arr[i]== key):
            flag = 1

    if(flag == 1):
        print('Search succesfull')
    else:
        print('Search unsuccessfull')

arr = list(map(int, input("Enter numbers to be sorted, separated by spaces: ").split()))
n = int(input('Enter the value of n:'))
key = int(input('Enter the value of key:'))
linear_search(arr, n, key)   
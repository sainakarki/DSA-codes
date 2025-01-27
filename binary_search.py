def binary_search(arr, key):
    n = len(arr)
    l = 0
    h = n-1
    while(l<=h):
        mid = (l+h)//2
        if(arr[mid] == key):
            return mid
        elif(arr[mid]<key):
            l = mid+1
        else:
            h = mid-1
    return 1

arr = list(map(int, input('Enter the array elements, seperated by comma:').split()))
print('The original array is:', arr)
key = int(input('Enter the value of key:'))
result = binary_search(arr, key)
if result != 1:
    print(f"The key {key} is found in index {result}.")
else:
    print('Search unsuccessful')
        
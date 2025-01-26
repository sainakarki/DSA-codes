def selection_sort(arr):
    n = len (arr)
    for i in range (n):
        for j in range ( i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input("Enter numbers to be sorted, separated by spaces: ").split()))

print('The original array is:', arr)
selection_sort(arr)
print('The sorted array is:', arr)


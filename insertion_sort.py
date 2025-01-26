def insertion_sort(arr):
 n = len(arr) 
 for i in range(1, n, +1):
   temp = arr[i]
   j = i-1
   while j>=0 and temp < arr[j]:
     arr[j+1] = arr[j]
     j= j-1
 arr[j+1] = temp


arr = list(map(int, input("Enter numbers to be sorted, separated by spaces: ").split()))
print('The original array is:', arr)
insertion_sort(arr)
print('The sorted array is:', arr)
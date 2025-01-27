def min_max(arr):
 n = len(arr)
 if n == 0:
  print('The array is empty')
  return None, None
 min = arr[0]
 max = arr[0]
 for i in range(1, n, +1):
  if(max < arr[i]):
   max = arr[i]
  else:
   min = arr[i]
 return min , max

arr = list(map(int, input("Enter the array elements, seperated by comma:").split()))
print('The original array is:', arr)
min, max = min_max(arr)
if min is not None and max is not None:
 print('Minimum value is:', min)
 print('Maximun value is:', max)
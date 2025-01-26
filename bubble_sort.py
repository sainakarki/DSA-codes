def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break

arr = list(map(int, input("Enter numbers to be sorted, separated by spaces: ").split()))
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)

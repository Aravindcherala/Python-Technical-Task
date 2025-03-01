def second_largest(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr[-2]  
arr = [10, 20, 4, 45, 99, 34]
print(second_largest(arr)) 
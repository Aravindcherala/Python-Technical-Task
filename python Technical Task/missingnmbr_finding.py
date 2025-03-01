def find_missing_number(lst, n):
    expected_sum = (n * (n + 1)) // 2
    actual_sum = 0
    
    for num in lst:
        actual_sum += num
    
    return expected_sum - actual_sum

lst = [1, 2, 4, 5, 6]  
print(find_missing_number(lst, 6))
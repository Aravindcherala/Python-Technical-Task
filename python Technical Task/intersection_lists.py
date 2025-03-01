def intersection(lst1, lst2):
    common = []
    seen = {}

    for num in lst1:
        seen[num] = True

    for num in lst2:
        if num in seen:
            common.append(num)

    return common

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print(intersection(lst1, lst2)) 
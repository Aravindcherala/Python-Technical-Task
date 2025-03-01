def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1

    return merged_list

lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6, 8]
print(merge_sorted_lists(lst1, lst2))
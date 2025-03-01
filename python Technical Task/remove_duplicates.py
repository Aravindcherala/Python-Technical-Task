def remove_duplicates(lst):
    unique_list = []
    seen = {}
    
    for elem in lst:
        if elem not in seen:
            seen[elem] = True
            unique_list.append(elem)
    
    return unique_list

lst = [1, 3, 2, 3, 4, 3, 5, 1, 1]
print(remove_duplicates(lst)) 
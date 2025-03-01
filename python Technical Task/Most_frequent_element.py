from collections import Counter

def most_frequent_element(lst):
    counter = Counter(lst)
    max_count = 0
    most_frequent = None
    
    for key in counter:
        if counter[key] > max_count:
            max_count = counter[key]
            most_frequent = key
    
    return most_frequent

lst = [1, 3, 2, 3, 4, 3, 5, 1, 1, 1]
print(most_frequent_element(lst))
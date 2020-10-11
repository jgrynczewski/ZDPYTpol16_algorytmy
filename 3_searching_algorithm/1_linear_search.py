def linear_search(search_list, target):
    for idx in range(len(search_list)):
        if search_list[idx] == target:
            return idx
    return None

a_list = [1, 4, 6, 23, 5, 2]
print(linear_search(a_list, 6))  # 2
print(linear_search(a_list, 10))  # None
print(linear_search(a_list, 5))  # 4

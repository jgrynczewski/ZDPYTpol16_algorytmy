# Założenie
# Zbiór wejściowy jest uporządkowany
# Złożoność obliczeniowa O(logn)

def binary_search_iter(sorted_list, target):
    start_idx = 0
    end_idx = len(sorted_list)-1

    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        mid_value = sorted_list[mid_idx]

        if mid_value == target:
            return mid_idx
        elif mid_value > target:
            end_idx = mid_idx - 1
        elif mid_value < target:
            start_idx = mid_idx + 1
    return None

a_list = [1, 2, 4, 5, 6, 23]
print(binary_search_iter(a_list, 6))
print(binary_search_iter(a_list, 10))
print(binary_search_iter(a_list, 4))
print(binary_search_iter(a_list, 23))


def binary_search_rec(sorted_list,  target, start_idx=0, end_idx=None):
    if end_idx is None:
        end_idx = len(sorted_list) - 1

    if start_idx > end_idx:
        return None

    mid_idx = (start_idx + end_idx) // 2
    mid_value = sorted_list[mid_idx]

    if mid_value == target:
        return mid_idx
    elif mid_value > target:
        return binary_search_rec(sorted_list, target, start_idx, mid_idx-1)
    elif mid_value < target:
        return binary_search_rec(sorted_list, target, mid_idx+1, end_idx)

a_list = [1, 2, 4, 5, 6, 23]
print(binary_search_rec(a_list, 6))
print(binary_search_rec(a_list, 10))
print(binary_search_rec(a_list, 4))
print(binary_search_rec(a_list, 23))
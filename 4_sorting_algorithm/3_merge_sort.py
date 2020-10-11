# Sortowanie przez scalanie

def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    middle_idx = len(a_list) // 2
    left = a_list[:middle_idx]
    right = a_list[middle_idx:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    """Scala dwie UPORZĄDKOWANE LISTY"""
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    else:
        result += right

    return result

print(merge_sort([9, 4, 6, 2, 7, 1, 3, 5]))

# Złożonośc obliczeniowa
# O(nlogn)

# Quicksort
# Timsort (sort)
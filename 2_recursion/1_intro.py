# Podejście iteracyjne
def sum_list_iter(a_list):
    result = 0
    for item in a_list:
        result += item

    return result

a_list = [5, 6, 7]
print(sum_list_iter(a_list))

# Podejście rekurencyjne
def sum_list_rec(a_list):
    if len(a_list) == 0:
        return 0
    return a_list[0] + sum_list_rec(a_list[1:])

print(sum_list_rec(a_list))
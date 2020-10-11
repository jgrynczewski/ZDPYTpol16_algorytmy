# Sortowanie bąbelkowe
def bubble_sort(a_list):
    for i in range(len(a_list)-1): # n, n, n, ... n
        for idx in range(len(a_list)-1):
            if a_list[idx] > a_list[idx+1]: # 12
                a_list[idx], a_list[idx+1] = a_list[idx+1], a_list[idx]

a_list = [3,2,1]
bubble_sort(a_list)
print(a_list)

# Złożoność
# T(n) = 12n^2
# f(n) = n^2
# O(n^2)
# Złożoność pamięciowa O(1)

# Optymalizacja sortowania bąbelkowego
def bubble_sort_2(a_list):
    for i in range(len(a_list) - 1):  # n, n-1, n-2, ... 1
        for idx in range(len(a_list) - i - 1):
            if a_list[idx] > a_list[idx + 1]:  # 12
                a_list[idx], a_list[idx + 1] = a_list[idx + 1], a_list[idx]


a_list = [3, 2, 1]
bubble_sort_2(a_list)
print(a_list)

# n, n-1, n-2, ... 1
# T(n) = n*(n+1)/2 * 12 = 6n(n+1) = 6n^2 + 6n
# f(n) = n^2
# 0(n^2)

def bubble_sort_3(a_list):
    swapped = True
    i=0
    while swapped:
        swapped = False
        for idx in range(len(a_list) - i - 1):
            if a_list[idx] > a_list[idx + 1]:  # 12
                a_list[idx], a_list[idx + 1] = a_list[idx + 1], a_list[idx]
                swapped = True
        i += 1

a_list = [3, 2, 1]
bubble_sort_3(a_list)
print(a_list)

# Przyjmujemy pesymistyczną estymatę złożoności obliczeniowej
# Dlatego nic się nie zminiło.
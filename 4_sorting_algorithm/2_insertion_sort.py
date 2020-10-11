# Sortowanie przez wstawianie
def insertion_sort(a_list):
    for i in range(1, len(a_list)): # n
        current = a_list[i]  # 3

        j = i-1 # 2
        while a_list[j] > current and j>=0: # 1, 2, 3, ... n # 2
            a_list[j+1] = a_list[j]  # przesuwamy # 4
            j -= 1  # 2

        a_list[j+1] = current  # wstawiamy # 2

a_list = [3, 2, 1]
insertion_sort(a_list)
print(a_list)

# T(n) = 7n + 8(n+1)/2*n = 7n + 4n^2 + 4n = 4n^2 + 11n
# f(n) = n^2
# Złożonośc przestrzenna O(n^2)
# Złożoność pamięciowa O(1)
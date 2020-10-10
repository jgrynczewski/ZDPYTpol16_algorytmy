# Sumowanie od podanej liczby do 1

# A. Iteracyjnie
def sum_to_one_iteration(n):
    result = 0 # jedna instrukcja
    for item in range(n, 0, -1):
        result += item # 3n
    return result

print(sum_to_one_iteration(2))  # 3
print(sum_to_one_iteration(5))  # 15

# Instrukcjami podstawowymi są:
# - instrukcja przypisania
# - podstawowe operatory (dodawania, odejmowanie, mnożenie, dzielenie)

# T(n) = 3n + 1
# f(n) = n -> O(n)

# B. Rekurencyjnie
def sum_to_one_recursion(n):
    if n==1:
        return 1
    return n + sum_to_one_recursion(n-1)

print(sum_to_one_recursion(2))  # 3
print(sum_to_one_recursion(5))  # 15

# T(n) = 2n -> O(n)

# C. Analitycznie

def sum_to_one_analitic(n):
    return n*(n+1)/2

print(sum_to_one_recursion(2))  # 3
print(sum_to_one_recursion(5))  # 15

# T(n) = 3 -> O(1)

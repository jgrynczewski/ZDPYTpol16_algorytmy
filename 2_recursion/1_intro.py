# Podejście iteracyjne
# Liczebność danych wejściowych: n
def sum_list_iter(a_list):
    result = 0  # 1
    for item in a_list:
        result += item  # 3

    return result

a_list = [5, 6, 7]
print(sum_list_iter(a_list))

# Instrukcje podstawowe:
# instrukcja przypsania
# operatory: dodawanie, odejmowanie, mnozenie, dzielenie, potegowanie
# porownanie
# wyciągnięcie elementu listy

# Złożoność obliczeniowa
# A. Czasowa:
# T(n) = 1 + 3*n
# f(n) = n
# O(n)


# Podejście rekurencyjne
def sum_list_rec(a_list):
    if len(a_list) == 0: #2
        return 0
    return a_list[0] + sum_list_rec(a_list[1:]) #3

a_list = [5, 6, 7]
print(sum_list_rec(a_list))

# Złożoność obliczeniowa
# Czasowa:
# T(n) = 5*n
# f(n) n
# O(n)
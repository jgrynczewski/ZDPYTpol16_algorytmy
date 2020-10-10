# Algorytm Euklidesa
# Mamy dwie liczby całkwite a, b
# Opis słowny algorytmu:
# 1. Powtarzaj dopóki b > 0
#    I. a -> b
#    II. b -> a % b
# 2. Zwróć a

def nwd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

print(nwd(16, 12))
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
#
# for i in range(1, 101):
#     print(f"fib({i}) = {fib(i)}")

fib_cache = {}

def fib_memo(n):
    if n in fib_cache:
        return fib_cache[n]
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        result = fib_memo(n-1) + fib_memo(n-2)
    fib_cache[n] = result
    return result
#
# for i in range(1, 201):
#     print(f"fib({i}) = {fib_memo(i)}")

from functools import lru_cache

@lru_cache(maxsize=100)
def fib_memo2(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib_memo2(n-1)+fib_memo2(n-2) # Błąd


for i in range(1, 201):
    print(f"fib({i}) = {fib_memo2(i)}")
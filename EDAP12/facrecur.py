def factorial_recursivo(n):
    if n < 2:
        return 1
    return n * factorial_recursivo(n-1)


print(factorial_recursivo(5))
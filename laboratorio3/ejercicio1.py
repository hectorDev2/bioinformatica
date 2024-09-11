def conejos_fibonacci(n, k):
    if n == 1 or n == 2:
        return 1
    return conejos_fibonacci(n - 1, k) + k * conejos_fibonacci(n - 2, k)

n = 5
k = 3
resultado = conejos_fibonacci(n, k)
print(resultado)

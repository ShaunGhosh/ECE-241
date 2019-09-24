def factorial(n):
    if n >= 1:
        result = n * factorial(n-1)
        return result
    else:
        return 1


Factorial = factorial(3)
print(Factorial)
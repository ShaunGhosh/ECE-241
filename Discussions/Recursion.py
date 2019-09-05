def recursive_add(n):
    if n > 0:
        return n + recursive_add(n-1)
    else:
        return 0

summation = recursive_add(100)
print(summation)
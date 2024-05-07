def ehprimo(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

print(ehprimo(45))
print(ehprimo(7))
print(ehprimo(11))
print(ehprimo(10))
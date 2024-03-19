a = int(input("Digite A:"))
b = int(input("Digite B:"))
c = int(input("Digite C:"))

if a+b < c or b+c < a or a+c < b:
    print("Não é um triangulo!")
elif a == b and a == c:
    print("É um triangulo Equilátero")
elif a == b or a == c or b == c:
    print("É um triangulo isósceles")
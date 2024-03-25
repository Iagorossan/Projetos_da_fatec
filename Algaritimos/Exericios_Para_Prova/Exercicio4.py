import math


def calcular_raizes(a, b, c):
    # Verificar se a é zero
    if a == 0:
        print("A equação não é do segundo grau.")
        return

    # Calcular o delta
    delta = b ** 2 - 4 * a * c

    # Verificar se o delta é negativo
    if delta < 0:
        print("A equação não possui raízes reais.")
        return

    # Calcular as raízes
    if delta == 0:
        raiz = -b / (2 * a)
        print("A equação possui apenas uma raiz real:", raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais:", raiz1, "e", raiz2)


# Solicitar os valores de a, b e c ao usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Chamar a função para calcular as raízes
calcular_raizes(a, b, c)
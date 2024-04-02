soma = 0
for i in range(1,6):
    idade = int(input(f"Entre com a idade {i}: "))
    soma = soma + idade
media = soma / 5
print(f"A Média das idades é {round(media:5.2f)} ")
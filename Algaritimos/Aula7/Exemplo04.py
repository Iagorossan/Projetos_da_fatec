soma = 0
idade =100
quantidade = 0
while idade != 0:
    idade = int(input(f"Entre com a idade {quantidade+1}: "))
    if idade != 0:
        soma = soma + idade
        quantidade = quantidade+1
media = soma / quantidade
print(f"A Média das idades é {round(media)} anos ")
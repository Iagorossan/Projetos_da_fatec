idade_por_sobrenome = {}

for _ in range(3):
    sobrenome = input("Digite o sobrenome da pessoa:")
    idade = int(input("Digite a idade da pessoa:"))
    idade_por_sobrenome[sobrenome] = idade

sobrenome_mais_velho = max(idade_por_sobrenome, key=idade_por_sobrenome.get)

print(f"\no sobrenome da pessoa mais velha é: {sobrenome_mais_velho}")
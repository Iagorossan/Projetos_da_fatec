salario_atual = float (input('Digite o salario atual:'))
porcentual_de_aumento = float(input('Digite o porcentual de aumento:'))

valor_de_aumento = (float(salario_atual * porcentual_de_aumento)/100)
novo_salario = salario_atual + valor_de_aumento

print(f"Salario_atual: R$  {novo_salario:8.2f}")
print(f"valor_de_aumento: R$ {valor_de_aumento:8.2f}")
print("_________________")
print ('Salario_novo: R$', novo_salario)
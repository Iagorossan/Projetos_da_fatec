soma_altura = 0
soma_peso = 0
maior_imc = 0
menor_imc = 100
peso = 0
altura = 0
media_peso = 0
media_altura = 0
quantidade = 0
for k in range (1,6):
    altura = float(input(f"entre com altura {k}:"))
    peso = float(input(f"entre com peso {k}:"))
    imc = peso / ( altura * altura )
    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

soma_altura = soma_altura + altura
soma_peso = soma_peso + peso
peso_medio = soma_peso / 5
altura_media = soma_altura / 5
print ("-----------RESULTADOS-----------------")
print (f"Maior IMC =  {maior_imc}")
print (f"Menor IMC =  {menor_imc}")
print (f"Peso medio = {peso_medio}")
print (f"Altura media = {altura_media}")


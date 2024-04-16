lista1 = []
for i in range(0,5):
    v1 = int(input(f"Digite um valor{i+1}:"))
    lista1.append(v1)
lista2 = []
for a in range(0,5):
    v2 = int(input(f"Digite um valor{a+1}:"))
    lista2.append(v2)
lista3 = (lista1.extend(lista2))
print(lista3)
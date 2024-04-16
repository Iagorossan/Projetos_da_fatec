lista = []
for i in range(0,5):
    v = int(input(f"Digite o valor{i+1}:"))
    lista.append(v)
print(max(lista), lista.index(max (lista)))

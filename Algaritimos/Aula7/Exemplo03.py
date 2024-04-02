quantidade = 0
frase = input("Digite uma frase: ")
for letra in frase:
    if letra in 'AEIOUaeiouáéíóiÁÉÍÓÚ':
        quantidade = quantidade + 1
print(f"Existem {quantidade} 'a' na frase.")

palavra = input('Digite sua frase: ')
palavra_ao_contrario = palavra[::-1]
palavra_palindroma = palavra_ao_contrario == palavra
if palavra_palindroma:
    print(f"A palavra {palavra} é uma palavra palindroma")
else:
    print(f"A palavra {palavra} não é uma palavra palindroma")

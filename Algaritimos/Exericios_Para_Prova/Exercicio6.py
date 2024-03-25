def imprimir_numeros_por_extenso(numero):
    # Dicionários para mapear os números por extenso
    unidades = {
        0: '',
        1: '1 Unidade',
        2: '2 Unidades',
        3: '3 Unidades',
        4: '4 Unidades',
        5: '5 Unidades',
        6: '6 Unidades',
        7: '7 Unidades',
        8: '8 Unidades',
        9: '9 Unidades'
    }

    dezenas = {
        0: '',
        1: '1 Dezena',
        2: '2 Dezenas',
        3: '3 Dezenas',
        4: '4 Dezenas',
        5: '5 Dezenas',
        6: '6 Dezenas',
        7: '7 Dezenas',
        8: '8 Dezenas',
        9: '9 Dezenas'
    }

    centenas = {
        0: '',
        1: '1 Centena',
        2: '2 Centenas',
        3: '3 Centenas',
        4: '4 Centenas',
        5: '5 Centenas',
        6: '6 Centenas',
        7: '7 Centenas',
        8: '8 Centenas',
        9: '9 Centenas'
    }

    # Separar o número em centenas, dezenas e unidades
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10

    # Imprimir o número por extenso
    if centena > 0:
        print(centenas[centena], end='')
        if dezena > 0 or unidade > 0:
            print(',', end=' ')
            if dezena == 0 or unidade == 0:
                print('e', end=' ')
    if dezena > 0:
        print(dezenas[dezena], end='')
        if unidade > 0:
            print(' e', end=' ')
    if unidade > 0 or (centena == 0 and dezena == 0):
        print(unidades[unidade], end='')


# Números de teste
numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

# Testando para cada número
for numero in numeros:
    print(numero, '=', end=' ')
    imprimir_numeros_por_extenso(numero)
    print()
frase = input('Digite sua frase: ').lower()    #ou .upper
numero_de_vogais = 0
vogais = ["a","e","i","o","u","á","é","í","ó","ú","ã"]
for vogal in frase:
    if vogal in vogais:
        numero_de_vogais += 1  #ou numero_de_vogais = numero_de_vogais + 1

print (f" seu numero de vogais é:{numero_de_vogais}")



ano = int(input(print("Entre com o ano: ")))
if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    print("É um ano bissexto!!")
else: print("Não é um ano bissexto!!" )

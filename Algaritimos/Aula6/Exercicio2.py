valor_da_compra = float(input(print("entre com valor da compra: ")))

if valor_da_compra <= 1000:
    desconto = valor_da_compra * 10 / 100
elif 1000< valor_da_compra <= 5000:
    desconto = valor_da_compra * 20 / 100
else:
    desconto = valor_da_compra * 30 / 100

valor_final = valor_da_compra - desconto
print("Valor final........:",valor_final)




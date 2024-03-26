largura_aposento = float(input("Digite a largura do aposento em metros: "))
comprimento_aposento = float(input("Digite o comprimento do aposento em metros: "))
lata = float(input(input("Tamanho da lata de tinta (1, 3.7 ou 18 litros)")))

altura_parede = 2.80
largura_porta = 0.80
altura_porta = 2.10

area_paredes = 2 * altura_parede * (largura_aposento + comprimento_aposento) - (largura_porta * altura_porta)

rendimento_tinta = 3
litros = (area_paredes / rendimento_tinta)

latas = int(litros/ lata)
if latas < litros / lata:
    latas = lata+1
print("Você precisará de latas de tinta.",latas_tinta)
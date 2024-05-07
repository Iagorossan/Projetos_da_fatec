#Funções que chamam outras funções
def area_circulo(raio):
    PI = 3.141592
    area = PI * pow(raio, 2)
    return area

def area_cilindro(altura, raio):
    area = area_circulo(raio)*altura
    return area
#...
r = float(input("Digite o raio: "))
h = float(input("Digite a altura: "))
print(f"A área do cilindro de raio {r} e altura {h} é igual a {area_cilindro(r,h)}")
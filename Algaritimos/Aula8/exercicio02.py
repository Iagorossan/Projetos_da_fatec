nascimento = input("Digite sua data nasc DD/MM/AAAA: ")
data = nascimento.split('/')
print (data[2] + "/" + data[1] + "/" + data[0])

#ou
#data = input("Digite a Data dd/mm/aaaa: ")
#dia = data[0:2]
#mes = data[3:5]
#ano = data[6::]
#data_invertida = ano+mes+dia
#print(data, " - ", data_invertida)
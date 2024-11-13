#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input('Escreva uma data (dd/mm/aaaa): ').split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if (dia >= 1 and dia <= 31) and (mes >=1 and mes <= 12) and (ano >=1 and ano < 3000):
    print('Data válida!')
    print(f"{dia}/{mes}/{ano}")
else:
    print("Data inválida !")
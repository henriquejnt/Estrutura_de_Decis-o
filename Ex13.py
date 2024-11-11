#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

dia = int(input('Digite um número: '))
if dia == 1:
    print("Esse dia é correspondente ao DOMINGO.")
elif dia == 2:
    print("Esse dia é correspondente á SEGUNDA.")
elif dia == 3:
    print("Esse dia é correspondente á TERÇA.")
elif dia == 4:
    print("Esse dia é correspondente á QUARTA.")
elif dia == 5:
    print("Esse dia é correspondente á QUINTA.")
elif dia == 6:
    print("Esse dia é correspondente á SEXTA.")
elif dia == 7:
    print("Esse dia é correspondente ao SÁBADO.")
else:
    print("Valor inválido.")
#Faça um Programa que peça um número correspondente a um determinado ano e em 
# seguida informe se este ano é ou não bissexto.

from decimal import Decimal

ano = int((input('Digite um ano: ')))
bissexto_4 = ano / 4
bissexto_100 = ano / 100
bissexto_400 = ano / 400
if bissexto_4.is_integer() and not Decimal(bissexto_100): #se for divisivel por 4 e não for por 100
    print(f"O ano {ano} é um ano bissexto !")
#se for divisivel pelas duas opções, ele nao tem que ser divisivel por 400
elif bissexto_400.is_integer():
    print(f"O ano {ano} é um ano bissexto !")
else:
    print(f"O ano {ano} não é um ano bissexto !")
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário 
# a valor do saque e depois informar quantas notas de cada valor
# serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
#  com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
#  uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input('Valor do saque [min 10/ max 600]: '))
if valor_saque >= 10 and valor_saque <= 600:
    nota_100 = valor_saque // 100
    nota_50 = (valor_saque - (nota_100*100) ) // 50
    nota_10 = ((valor_saque - (nota_100*100) ) - nota_50*50) // 10
    nota_5 = (((valor_saque - (nota_100*100) ) - nota_50*50) - nota_10*10) // 5
    nota_1 = ((((valor_saque - (nota_100*100) ) - nota_50*50) - nota_10*10) - nota_5*5) // 1
    print("Você receberar:")
    if nota_100 >=1 :
         print(f"{nota_100} notas de 100")
    
    if nota_50 >= 1:
         print(f"{nota_50} notas de 50")

    if nota_10 >= 1:
         print(f"{nota_10} notas de 10")
    
    if nota_5 >= 1:
         print(f"{nota_5} notas de 5")

    if nota_1 >= 1:
         print(f"{nota_1} notas de 1")
else:
     print("Valor fora de saque !")

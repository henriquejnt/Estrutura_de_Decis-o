#Um posto está vendendo combustíveis com a seguinte tabela de descontos: Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro.
#Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros_vendidos = int(input('Quantidade de litros vendidos: '))
tipo_litro = input("Tipo de litro [A-álcool/G-gasolina]: ").upper()
if tipo_litro == 'A':
    valor_alcool = litros_vendidos * 1.90
    if litros_vendidos <= 20:
        alcool_desconto = 0.03
    else:
        alcool_desconto = 0.05
    valor_alcool_desconto = valor_alcool - (valor_alcool * alcool_desconto)
    print(f"O valor de {litros_vendidos} litros de álcool é de R${valor_alcool_desconto}")
elif tipo_litro == 'G':
    valor_gasolina = litros_vendidos * 2.50
    if litros_vendidos <= 20:
        gasolina_desconto = 0.04
    else:
        gasolina_desconto = 0.06
    valor_gasolina_desconto = valor_gasolina - (gasolina_desconto * valor_gasolina)
    print(f"O valor de {litros_vendidos} litros de gasolina é de R${valor_gasolina_desconto}")
else:
    print('Tipo de combustivel inválido !')
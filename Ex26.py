#                   Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#  receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
#  morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos_kg = float(input('Quantidade de morangos[KG]: '))
macas_kg = float(input('Quantidade de maças[KG]: '))
if morangos_kg <= 5:
    valor_total_morangos = morangos_kg * 2.50
elif morangos_kg > 5 and morangos_kg <= 8:
    valor_total_morangos= morangos_kg * 2.20
else:
    valor_total_morangos = morangos_kg * 2.20
    desconto_10_morangos =  valor_total_morangos - ((10/100) * valor_total_morangos) 

if macas_kg <= 5:
    valor_total_macas = macas_kg * 1.80
elif macas_kg > 5 and macas_kg <= 8:
    valor_total_macas = macas_kg * 1.50
else:
    valor_total_macas = macas_kg * 1.50
    desconto_10_macas =  valor_total_macas - ((10/100) * valor_total_macas) 

valor_total = valor_total_macas + valor_total_morangos
valor_total_desconto = desconto_10_morangos + desconto_10_macas
print(f'O valor total de todos os quilos das frutas é de R${valor_total}')
print(f'Valor total com desconto: R${valor_total_desconto}')
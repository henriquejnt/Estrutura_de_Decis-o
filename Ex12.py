#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% 
valor_hora = float(input('Valor da sua hora: '))
horas_mes = int(input("Horas por mês:"))
salario_bruto = (horas_mes * valor_hora)
ir_5 = (5/100)*salario_bruto
inss_10 = (10/100)*salario_bruto
fgts = (11/100)*salario_bruto

print(f'Salário bruto: {salario_bruto}')
print(f"IR: {ir_5}")
print(f"INSS: {inss_10}")
print(f"FGTS: R${fgts}")
print(f"Total de descontos: R${ir_5+inss_10}")
print(f"Salário Líquido: R${salario_bruto - (ir_5+inss_10)}")






































"""if salario_bruto <= 900:
    print(f"Salário Bruto: R${salario_bruto}")
    print("Desconto do IR: s")
elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_5 = (5/100)*salario_bruto
elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_5 = (10/100)*salario_bruto
elif salario_bruto > 2500:
    desconto_5 = (20/100)*salario_bruto"""
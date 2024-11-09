#Faça um programa que recebe o salário de um colaborador e 
# o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Salário do colaborador: "))
porcentagem = 0
print(f"O seu salário antes do reajuste foi de R${salario}")
if salario <= 280.00:
    porcentagem = ((20/100)*salario)
    print("O percentual de aumento foi de 20%")
    print(f"O valor do aumento foi de R${porcentagem}")
    print(f"O seu novo salário foi é R${porcentagem+salario}")
elif salario >= 280.00 and salario <= 700.00:
    porcentagem = ((15/100)*salario)
    print("O percentual de aumento foi de 15%")
    print(f"O valor do aumento foi de R${porcentagem}")
    print(f"O seu novo salário foi é R${porcentagem+salario}")
elif salario > 700.00 and salario <= 1500.00:
    porcentagem = ((10/100)*salario)
    print("O percentual de aumento foi de 10%")
    print(f"O valor do aumento foi de R${porcentagem}")
    print(f"O seu novo salário foi é R${porcentagem+salario}")
elif salario > 1500.00:
    porcentagem = ((5/100)*salario)
    print("O percentual de aumento foi de 5%")
    print(f"O valor do aumento foi de R${porcentagem}")
    print(f"O seu novo salário foi é R${porcentagem+salario}")

#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

n = int(input('Digite um valor: '))
if n % 2 == 0:
    print(f"O valor {n} é um número par.")
else:
    print(f"O valor {n} é um número ímpar.")
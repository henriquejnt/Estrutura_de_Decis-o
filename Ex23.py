#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.
num_original = input('Digite um número: ')
num_decimal = float(num_original)

if num_decimal.is_integer():
    print(f"O número {num_original} é um número inteiro !")

else:
    print(f"O número {num_original} é um número decimal !")
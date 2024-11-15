#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#  O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite o segundo número: '))
print('''Digite essas opções: 
      multiplicação
      divisão
      soma
      subtração''')
operacao = input('Digite a operação: ').upper()
positivo_negativo = par_impar = inteiro_decimal = ''
if operacao == 'SOMA':
    operacional = n1 + n2
elif operacao == 'MULTIPLICAÇÃO':
    operacional = n1 * n2
elif operacao == 'SUBTRAÇÃO':
    operacional = n1 - n2
elif operacao == 'DIVISÃO':
    operacional = n1 / n2
else:
    print("ERROR !!!")
    operacional = None


if operacional is not None:
    if operacional > 0:
        positivo_negativo = 'é positivo,'
    else:
        positivo_negativo = 'é negativo,'

    if operacional.is_integer():
        if operacional % 2 == 0 :
            par_impar = 'é par'
        else:
            par_impar = 'é ímpar'
        inteiro_decimal = 'e é inteiro.'
    else:
        inteiro_decimal = 'e é decimal.'

    print(f"O resultado: {operacional} {positivo_negativo}{par_impar} {inteiro_decimal}")
#Faça um Programa que leia um número inteiro menor que 1000 e 
# imprima a quantidade de centenas, dezenas e unidades do mesmo.

num = int(input('Digite um número inteiro abaixo de 1000: '))

centenas_int = int(num // 100)
dezenas_int = int(num / 10)
unidades_int = num - (dezenas_int * 10) 
centenas_str = dezenas_str = unidades_str = ''

if centenas_int == 1:
    centenas_str = '1 centena'
elif centenas_int > 1:
    centenas_str = f'{centenas_int} centanas'

if dezenas_int == 1:
    dezenas_str = '1 dezena'
elif dezenas_int > 1:
    dezenas_str = f'{dezenas_int} dezenas'

if unidades_int == 1:
    unidades_str = "1 unidade"
elif unidades_int > 1:
    unidades_str = f"{unidades_int} unidades"

if num >= 1000:
    print("erro!")

print(f"{centenas_str} centenas, {dezenas_str} dezenas e {unidades_str} unidades .")
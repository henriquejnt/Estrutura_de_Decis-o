#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
maior_valor = 0
valor_do_meio = 0
menor_valor = 0

#maior valor
if n1 >= n2 and n1 >= n3:
    maior_valor = n1
    #valor do meio e menor valores se n1 for o maior
    if n2 >= n3: 
        valor_do_meio = n2
    elif n3 >= n2:
        valor_do_meio = n3
elif n2 >= n1 and n2 >= n3:
    maior_valor = n2
    #valor do meio e menor valores se n2 for o maior
    if n1 >= n3:
         valor_do_meio = n1
         menor_valor = n3
    elif n3 >= n1:
         valor_do_meio = n3
         menor_valor = n1
elif n3 >= n1 and n3 >= n2:
    valor_do_meio = n3
    #valor do meio e menor valores se n3 for o maior
    if n2 >= n1:
         valor_do_meio = n2
         menor_valor = n1
    elif n1 >= n2:
         valor_do_meio = n1 
         menor_valor = n2

print(f"Os valores acima em ordem decrescente: {maior_valor}, {valor_do_meio}, {menor_valor}")
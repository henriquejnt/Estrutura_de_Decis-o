#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

#para encontrar o maior
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número")
elif n3 > n1 and n3 > n2:
    print(f"{n3} é maior número.")
else:
    print("Não existe número MAIOR, todos são iguais.")

#para encontrar o menor
if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número.")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor número.")
else:
    print("Não existe número MENOR, todos são iguais.")
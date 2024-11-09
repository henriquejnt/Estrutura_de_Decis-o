#Faça um Programa que leia três números e mostre o maior deles.
n1 = float(input("Digite o primeiro valor:"))
n2 = float(input('Digie o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior valor!")
elif n2 > n1 and n2 > n3:
      print(f"{n2} é o maior valor!")
elif n3 > n1 and n3 > n2:
     print(f"{n3} é o maior valor!")
else:
     print("Não existe valor maior, todos são iguais.")
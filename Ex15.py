#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
# isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

l1 = float(input("Primeiro lado: "))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
triangulo = (l1 + l2) 
if triangulo > l3:
    print("Os valores podem ser um triângulo !")
    if l1 == l2 and l3:
        print("É um triângulo Equilátero !")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("É um triângulo Isósceles !") 
    else:
        print("É um triângulo Escaleno !")
else:
    print("Os lados não formam um triângulo !")
#Faça um programa que calcule as raízes de uma equação do segundo grau, 
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
#  fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero, a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a = float(input('Coeficiente de A: '))
if a == 0:
    print("A equação não é do segundo grau !")
else:
    b = float(input('Coeficiente de B: '))
    c = float(input('Coeficiente de C: '))
    delta = math.sqrt((b**2)-(4*a*c))
    x1_negativo = (-b-delta)/(2*a)
    x2_positivo = (-b+delta)/(2*a)
    if delta < 0:
            print("A equação não possui raizes reais !")
    elif delta == 0:
            delta_igual_zero = (-b)/(2*a)
            print(f"A equação possui apenas uma raiz real: {delta_igual_zero}")
    elif delta > 0:
            print(f"A equação possui duas raízes reais: x1 = {x1_negativo} e x2 = {x2_positivo}")
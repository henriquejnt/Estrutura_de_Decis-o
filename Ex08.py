#Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
p1 = float(input('Preço do produto 01: '))
p2 = float(input('Preço do produto 02: '))
p3 = float(input('Preço do produto 03: '))
if p1 < p2 and p1 < p3:
    print(f"Compre o produto 01, pois é o mais barato !")
elif p2 < p1 and p2 < p3:
    print(f"Compre o produto 02, pois é o mais barato !")
elif p3 < p2 and p3 < p1:
    print(f"Compre o produto 03, pois é o mais barato !")
else:
    print(f"Compre qualquer dos 3 produtos, pois todos tem preços iguais!")
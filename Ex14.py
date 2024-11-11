n1 = float(input("Digite sua primeira nota: "))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
conceito = ''
aprovado_reprovado = ''
if media >= 9.0 and media <= 10.0:
    conceito = 'A'
    aprovado_reprovado = 'APROVADO'
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
    aprovado_reprovado = 'APROVADO'
elif media >= 6.0 and media < 7.5:
    conceito = 'C'
    aprovado_reprovado = 'APROVADO'
elif media >= 4.0 and media < 6.0:
    conceito = 'D'
    aprovado_reprovado = 'REPROVADO'
elif media < 4.0 :
    conceito = 'E'
    aprovado_reprovado = 'REPROVADO'
print(f"As notas são {n1} e {n2}")
print(f"Sua média é de {media}")
print(f'O conceito correspondente: {conceito}')
print(aprovado_reprovado)
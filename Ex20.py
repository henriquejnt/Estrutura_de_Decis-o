#Faça um Programa para leitura de três notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

nome = input('Seu nome: ')
sexo = input('Sexo [M/F]: ').upper()[0]
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1+n2+n3) / 3
print(f'Seu nome é {nome}')
if sexo == 'M':
    if media == 10.0:
        print("APROVADO COM DISTINÇÃO !")
    elif media >= 7.0:
        print("APROVADO !")
    elif media < 7.0:
        print('REPROVADO !')
elif sexo == 'F':
    if media == 10.0:
        print("APROVADA COM DISTINÇÃO !")
    elif media >= 7.0:
        print("APROVADA !")
    elif media < 7.0:
        print('REPROVADA !')
else:
    print("Sexo inválido !")
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever:
#  F - Feminino, M - Masculino, Sexo Inválido.

m_f = str(input("Digite seu sexo M(masculino), F(feminino) e I(indefinido):")).upper()
if m_f == 'M':
    print("O seu sexo é masculino.")
elif m_f == 'F':
    print("O seu sexo é feminino.")
elif m_f == 'I':
    print("O seu sexo é indefinido.")
else:
    print("Sexo inválido.")
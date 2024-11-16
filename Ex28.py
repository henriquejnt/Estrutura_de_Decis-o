tipo_carne = input("Tipo de carne [Filé duplo/Alcatra/Picanha] : ").upper()
quantidade_carne = int(input("Quantidade de carne [kg]: "))
tipo_pagamento = input("Tipo de pagamento [dinheiro/cartão/cartão da Tabajura/pix]: ").upper()
valor_com_desconto = desconto_10 = valor_total = 0
if tipo_carne == 'FILE DUPLO':
    if quantidade_carne <= 5:
        valor_file = 4.90
        valor_total = quantidade_carne * valor_file
    else:
        valor_file = 5.80
        valor_total = quantidade_carne * valor_file
elif tipo_carne == 'ALCATRA':
    if quantidade_carne <= 5:
        valor_alcatra = 5.90
        valor_total = quantidade_carne * valor_alcatra
    else:
        valor_alcatra = 6.80
        valor_total = quantidade_carne * valor_alcatra
elif tipo_carne ==  'PICANHA':
    if quantidade_carne <= 5:
        valor_picanha = 6.90
        valor_total = quantidade_carne * valor_picanha
    else:
        valor_picanha = 7.80
        valor_total = quantidade_carne * valor_picanha
else:
    print('Tipo de carne inválida')
    tipo_carne = None

if tipo_pagamento == 'CARTÃO DA TABAJURA':
    desconto_10 =  ((10/100)*valor_total)

if tipo_pagamento is not None and tipo_carne in ['DINHEIRO','PIX','CARTÃO','CARTÃO DA TABAJURA']:
    print('=-'*25)
    print('Cupom fiscal:')
    print(f'Tipo de carne: {tipo_carne}')
    print(f'Quantidade de carne: {quantidade_carne} kg')
    print(f'Tipo de pagamento: {tipo_pagamento} ')
    print(f'Preço total: {valor_total}')
    if tipo_pagamento == 'CARTÃO DA TABAJURA':
        print(f'Valor a pagar com desconto: {valor_com_desconto}')
    else:
        print(f'Valor a pagar: {valor_total}')
else:
    print('Informações inválidas !')
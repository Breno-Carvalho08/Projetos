import random

for cpf in range(5):
    cpf_numerico = ''
    soma_digitos = 0
    soma_digito_2 = 0
    for i in range(9):
        cpf_numerico += str(random.randint(0,9))

    cont_1 = 10
    for valor in cpf_numerico:
        if cont_1 >= 2:
            valor_num = int(valor)
            soma_digitos += valor_num * cont_1
            cont_1 -= 1
        else: 
            break

    mult_soma_digito_1 = soma_digitos * 10
    primeiro_digito = (mult_soma_digito_1 % 11) if (mult_soma_digito_1 % 11) <= 9 else 0

    cpf_numerico += str(primeiro_digito)

    cont_2 = 11
    for valor in cpf_numerico:
        if cont_2 >= 2:
            valor_num = int(valor)
            soma_digito_2 += valor_num * cont_2
            cont_2 -= 1
        else: 
            break
    mult_soma_digito_2 = soma_digito_2 * 10
    segundo_digito = (mult_soma_digito_2 % 11) if (mult_soma_digito_2 % 11) <= 9 else 0

    cpf_numerico += str(segundo_digito)

    print(f'CPF {cpf + 1}: {cpf_numerico}')
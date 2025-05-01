import re
import sys

cpf_cliente = '57501534660'
cpf_gerado = ''
cpf_numerico = ''
soma_digitos = 0
soma_digito_2 = 0
cont_1 = 10

try:
    for num in cpf_cliente:
        if num == '.' or num == '-':
            cpf_cliente = re.sub(r'[^0-9]','','395.245.380-32')
        else:
            cpf_numerico += num
    cpf_gerado = cpf_numerico[:9]
except TypeError:
    print('ERRO: Informe um CPF válido.')

cpf_sequencial = cpf_cliente[0] * len(cpf_cliente)

if cpf_cliente == cpf_sequencial:
    print('Informe um CPF válido')
    sys.exit()


for valor in cpf_numerico:
    if cont_1 >= 2:
        valor_num = int(valor)
        soma_digitos += valor_num * cont_1
        cont_1 -= 1
    else: 
        break

mult_soma_digito_1 = soma_digitos * 10
primeiro_digito = (mult_soma_digito_1 % 11) if (mult_soma_digito_1 % 11) <= 9 else 0

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

cpf_gerado_calculo = f'{cpf_gerado}{primeiro_digito}{segundo_digito}'

if cpf_numerico == cpf_gerado_calculo:
    print('CPF Válido:',cpf_cliente)
else:
    print('CPF Inválido')

#print(f'{cpf_cliente[:2]}*.***.**{cpf_cliente[10]}-{primeiro_digito}{segundo_digito}')





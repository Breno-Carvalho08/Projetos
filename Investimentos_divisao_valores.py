
fundos_imobiliarios = 0.25
acoes = 0.25
renda_fixa = 0.25
etfs = 0.25
concordar = False

fundos_imobiliarios_valor = float(input('Valor em fundos imobiliários: R$'))
acoes_valor = float(input('Valor em ações: R$'))
renda_fixa_valor = float(input('Valor em renda fixa: R$'))
etfs_valor = float(input('valor em ETFs: R$'))

total_investido = (fundos_imobiliarios_valor + acoes_valor + renda_fixa_valor + etfs_valor)
print(f'Total Investido: R${total_investido}')

if (fundos_imobiliarios_valor > total_investido * 0.25 or acoes_valor > total_investido * 0.25 or
    renda_fixa > total_investido * 0.25 or
    etfs_valor > total_investido * 0.25):
    while not concordar:
        concordar = str(input('Sua carteira parece desbalanceada. Deseja rebalancear ela automaticamente? [S/N]\n')).upper()
        if concordar == 'S':
            fundos_imobiliarios_valor = total_investido * 0.25
            acoes_valor = total_investido * 0.25
            renda_fixa_valor = total_investido * 0.25
            etfs_valor = total_investido * 0.25
            print(f'Fundos imobiliarios: R${fundos_imobiliarios_valor}\nAções: R${acoes_valor}\nRenda fixa: R$'
                  f'{renda_fixa_valor}\nETFs: R${etfs_valor }')
        else:
            print(f'Sua carteira está com a seguinte divisão:'
                  f'\nFundos Imobilários: {(fundos_imobiliarios_valor/total_investido) * 100:.2f}%\n'
                  f'Ações: {(acoes_valor/total_investido) * 100:.2f}%\n'
                  f'Renda fixa: {(renda_fixa_valor/total_investido) * 100:.2f}%\n'
                  f'ETFs: {(etfs_valor/total_investido) * 100:.2f}%'
                  )
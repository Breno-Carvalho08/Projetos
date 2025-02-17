#Perfil de risco
from time import sleep

perfil_risco = int(input('Qual o seu perfil de risco:\n[1] - Conservador\n[2] - Moderado\n[3] - Arriscado\n'))

while perfil_risco not in (1,2,3):
    print('Escolha inválida!')
    perfil_risco = int(input('Qual o seu perfil de risco:\n[1] - Conservador\n[2] - Moderado\n[3] - Arriscado\n'))

valor_investimento = float(input('Valor para o investimento (Recomendamos > R$1000: R$'))
if valor_investimento <= 1000:
    escolha = int(input('Recomendamos que você tenha um pouco mais para ser efetivo. Deseja continuar?\n[1] - Sim\n[2] - Não\n'))
    while escolha not in (1, 2):
        print('Escolha inválida!')
        escolha = int(input('Deseja continuar\n[1] - Sim\n[2] - Não\n'))
    if escolha == 1:
        match perfil_risco:
            case 1:
                fiis = 0.1
                acoes = 0.1
                renda_fixa = 0.7
                etfs = 0.1
                print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                      f'Ações: R${valor_investimento * acoes}\n'
                      f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                      f'ETFs: R${valor_investimento * etfs}')

            case 2:
                fiis = 0.25
                acoes = 0.25
                renda_fixa = 0.25
                etfs = 0.25
                print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                      f'Ações: R${valor_investimento * acoes}\n'
                      f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                      f'ETFs: R${valor_investimento * etfs}')

            case 3:
                fiis = 0.35
                acoes = 0.35
                renda_fixa = 0.10
                etfs = 0.2
                print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                      f'Ações: R${valor_investimento * acoes}\n'
                      f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                      f'ETFs: R${valor_investimento * etfs}')

    elif escolha == 2:
        print('Encerrando...')
        sleep(1)
        print('Processo encerrado.')

else:
    match perfil_risco:
        case 1:
            fiis = 0.1
            acoes = 0.1
            renda_fixa = 0.7
            etfs = 0.1
            print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                  f'Ações: R${valor_investimento * acoes}\n'
                  f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                  f'ETFs: R${valor_investimento * etfs}')

        case 2:
            fiis = 0.25
            acoes = 0.25
            renda_fixa = 0.25
            etfs = 0.25
            print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                  f'Ações: R${valor_investimento * acoes}\n'
                  f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                  f'ETFs: R${valor_investimento * etfs}')

        case 3:
            fiis = 0.35
            acoes = 0.35
            renda_fixa = 0.10
            etfs = 0.2
            print(f'Fundos imobiliários: R${valor_investimento * fiis}\n'
                  f'Ações: R${valor_investimento * acoes}\n'
                  f'Renda fixa: R${valor_investimento * renda_fixa}\n'
                  f'ETFs: R${valor_investimento * etfs}')



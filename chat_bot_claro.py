import os
import time
import random
import datetime

num_protocolo = random.randint(100000000000, 999999999999)
num_protocolo_str = str(num_protocolo)
data_atual = datetime.datetime.now()
cpf_exemplo = [
    {'cpf':18884082277, 'status_fatura': 'Sua fatura do mês está em aberto com vencimento para o dia 20.','valor':69.90},
    {'cpf':66155220395, 'status_fatura':'Sua fatura do mês está em aberto com vencimento para o dia 25.','valor': 99.99},
    {'cpf':11914273311, 'status_fatura':'Sua fatura do mês está em aberto com vencimento para o dia 30.','valor': 149.99}
    ]

protocolo = f'{num_protocolo_str[:5]}.{num_protocolo_str[6:13]}/{data_atual.year}-{data_atual.day}'

def planos_claro():
    os.system('cls')
    print('Plano 20GB\n\
- 20 GB de internet + ligações ilimitadas\n\
- Apps liberados: WhatsApp, Instagram, TikTok\n\
- Preço: R$69.90/mês\n''')
    print('Plano 50GB\n\
- 50 GB de internet + ligações ilimitadas\n\
- Apps liberados: WhatsApp, Instagram, TikTok (além dos anteriores) \n\
- R$99.99/mês\n')
    print('Plano 100GB\n\
- 100GB em 5G + todos os apps sem consumir dados\n\
- Claro Video Premium incluso  \n\
- R$ 149.99/mês')
    
def status_fatura():
        os.system('cls')
        cpf_cliente = input('Por favor, informe seu CPF (somente números): ')
        cpf_cliente_int = int(cpf_cliente)
        cpf_encotrado = False

        for cliente in cpf_exemplo:
            if cliente['cpf'] == cpf_cliente_int:
                cpf_encotrado = True
                break
            
        if cpf_encotrado is True:
            print(f"CPF encontrado! Status: {cliente['status_fatura']}\nValor: R${cliente['valor']}")
        if cpf_encotrado is False:
            print("CPF não cadastrado. Verifique o número ou entre em contato.")

def problemas_tecnicos():
    os.system('cls')
    print('Aqui algumas soluções para os problemas mais comuns: ')
    print("- Reiniciar seu aparelho")
    print("- Verificar a cobertura na sua região")
    print("- Caso o problema persista, entre em contato com nosso suporte.")
    outro = input('Nenhum desses problemas te atende? Aperta 1 para entrar em contato com um de nossos atendentes\n')
    try:
        outro_int = int(outro)
        if outro_int == 1:
            atendimento_humano()
        else:
            print('Opção inválida')
    except ValueError:
        print('Valor inválido.')

def atendimento_humano():
    os.system('cls')
    print('Redirecionando para o atendimento humano. Aguarde...')
    time.sleep(3) 
                  
def chat_bot_claro():
    os.system('cls')
    print(f'Olá! Seja bem-vindo a nossa central de atendimento rápido Claro, seu número de protocolo é {protocolo} como podemos ajudar?')
    print('[1] - Planos Claros\n[2] - Status Fatura\n[3] - Problemas técnicos\n[4] - Atendimento humano\n')
    opcao = input('Qual desses atendimentos mais te interessa? ')

    try:
        opcao_int = int(opcao)
        match opcao_int:
            case 1:
                planos_claro()
            case 2:
                status_fatura()        
            case 3:
                problemas_tecnicos()
            case 4:
                atendimento_humano()              

    except ValueError:
        print('Valor inválido.')

print(protocolo)  
chat_bot_claro()

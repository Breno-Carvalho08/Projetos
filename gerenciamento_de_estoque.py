#Exercício 1: Gerenciamento de Estoque
estoque = [] #Lista criada aqui no inicio para não interfirir no funcionamento do programa

#ADICIONAR PRODUTOS AO ESTOQUE
def add_produto():
    quant_produtos_add = int(input('Quantos produtos deseja adicionar: '))
    if quant_produtos_add < 0:
        print('Insira uma quantidade válida de produtos.')
        add_produto()

    for produtos in range (1, quant_produtos_add + 1):
        nome_produto = str(input('Nome do produto: '))
        quant_produto = int(input('Quantidade do produto: '))

        produto_existente = False #Váriavel criada para auxiliar na procura do item em questão
        for item in estoque: #variavel item percorre a lista estoque através do 'for'
            if item['Nome'] == nome_produto:
                item['Quantidade'] += quant_produto
                produto_existente = True
                break
                #Explicação else dentro do for está no arquivo gerenciamento_estoque_explicação_else_dentro_do_for.txt
        if not produto_existente:
            produto = {'Nome': nome_produto, 'Quantidade': quant_produto}
            estoque.append(produto)

#CONSULTAR PRODUTOS NO ESTOQUE
def consultar_produto():
    escolha = int(input('Deseja ver todos os produtos ou algum específico?\n1 - Total\n2 - Específico\n'))

    #Tratamento para uma opção inválida
    while escolha != 1 and escolha != 2:
        print('Informe uma opção válida.')
        escolha = int(input('Deseja ver todos os produtos ou algum específico?\n1 - Total\n2 - Específico\n'))

    #match case com base na opção selecionada
    match escolha:
        case 1:
            for item in estoque:
                print(f'{item['Nome']}: {item['Quantidade']} unidade(s)')
        case 2:
            produto = input('Qual produto deseja ver no estoque: ')
            localizar_item = False
            for item in estoque:
                if item['Nome'] == produto:
                    print(f'{produto}: {item['Quantidade']} unidade(s)')
                    localizar_item = True
                    break
                if not localizar_item:
                    escolha = input(f'Produto não encontrado... Deseja adicionar {produto} ao estoque? [S/N]\n').upper()
                    match escolha:
                        case 'S':
                            quant = int(input('Informe a quantidade: '))
                            produto = {'Nome': produto, 'Quantidade': quant}
                            estoque.append(produto)
                            print(f'{produto['Nome']}: {produto['Quantidade']} unidade(s)')
                            localizar_item = True
                            break

#EXCLUIR PRODUTOS DO ESTOQUE
def excluir_produto():
    if not estoque:
        print('Estoque vázio')
        print('Vamos de novo')
        main()

    produto = input('Qual item deseja excluir da lista: ')
    localizar_item = False
    # Enumerate: facilita a interação com uma lista, não necessitando de um contador externo no programa
    # Pode ser definido um início para ele também, for cont, 'item' in enumerate(estoque, start = 1) Começando pelo número 1. Padrão é 0
    for cont, item in enumerate(estoque):
        if item['Nome'] == produto:
            print(f'Você excluiu o item {produto} ')
            estoque.pop(cont)
            localizar_item = True
            break

    if not localizar_item:
        print('Produto não encontrado')

#FUNÇÃO PRINCIPAL
def main():
    acao = int(input('O que deseja fazer no estoque?\n[1] - Adicionar produto\n[2] - Consultar estoque\n[3] - Remover produto\n'))
    while acao not in (1, 2, 3):
        print('Escolha uma opção válida...')
        acao = int(input('O que deseja fazer no estoque?\n[1] - Adicionar produto\n[2] - Consultar estoque\n[3] - Remover produto\n'))

    match acao:
        case 1:
            add_produto()
            escolha = input('Deseja realizar mais alguma operação no estoque? [S/N]').upper()
            if escolha == 'S':
                main()
            else:
                print('Encerrando...')
        case 2:
            consultar_produto()
            escolha = input('Deseja realizar mais alguma operação no estoque? [S/N]').upper()
            if escolha == 'S':
                main()
            else:
                print('Encerrando...')
        case 3:
            excluir_produto()
            escolha = input('Deseja realizar mais alguma operação no estoque? [S/N]').upper()
            if escolha == 'S':
                main()
            else:
                print('Encerrando...')

print('-------------------------------')
print('Gerenciamento de Estoque')
print('-------------------------------')
main()
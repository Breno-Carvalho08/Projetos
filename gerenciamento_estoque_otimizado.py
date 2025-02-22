estoque = [
    {'Nome': 'Caneta', 'Quant': 5},
    {'Nome': 'Caderno', 'Quant': 7}
]

#Função para adicionar um novo produto a lista 'estoque'
def add_produto(nome_produto,quant_produto):
    produto = next((produto for produto in estoque if produto['Nome'] == nome_produto), None)
    if produto:
        produto['Quant'] += quant_produto
        return True, f'Foram adicionados {quant_produto} unidade(s) ao produto {produto['Nome']}'
    else:
        produto = {'Nome': nome_produto, 'Quant': quant_produto}
        estoque.append(produto)
        return False, f'Produto "{produto['Nome']}" foi adicionado.'

#Função para mostrar a lista 'estoque' no console
def verificar_produtos_estoque():
    for cont, produto in enumerate(estoque):
        print(f'{produto['Nome']}: {produto['Quant']} unidade(s).')

#Função para excluir um produto da lista 'estoque' com base no seu nome
def excluir_produto(nome_produto):
    cont = 0
    if next((produto for cont, produto in enumerate(estoque) if produto['Nome'] == nome_produto),None):
        estoque.pop(cont)
        return True, f'Produto "{nome_produto}" excluído com sucesso.'
    else:
        return False, 'Produto não encontrado'

def main():
    escolha = False
    while not escolha:
        acao = int(input(
        'O que deseja fazer no estoque?\n[1] - Adicionar produto\n[2] - Consultar estoque\n[3] - Remover produto\n'))

        match acao:
            case 1:
                produto = input('Nome do produto: ')
                quant = int(input('Quantidade do produto: '))
                valido, mensagem = add_produto(produto,quant)
                if not valido:
                    print(mensagem)
                else:
                    print(mensagem)
            case 2:
                verificar_produtos_estoque()
            case 3:
                produto = input('Nome do produto: ')
                valido, mensagem = excluir_produto(produto)
                if not valido:
                    print(mensagem)
                else:
                    print(mensagem)
        escolha = input('Deseja sair da operação? [S/N]').upper()
        if escolha != 'S':
            main()
            break

main()










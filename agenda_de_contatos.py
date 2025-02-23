contatos = [
    {'Nome': 'Breno', 'Tel': '99999999'}
]

def add_contato(contato,tel):
    #Utilizado para a verificação
    if not any(novo_contato['Nome'] == contato for novo_contato in contatos): #Caso possua um unico valor correspondente, o any() retorna True
        novo_contato = {'Nome': contato, 'Tel':tel}
        contatos.append(novo_contato)
        print('Contato adicionado.')
    else:
        print('Contato já existente.')

def ver_contatos():
    listar_contatos = next((listar_contatos for listar_contatos in contatos),None)
    if not listar_contatos:
        print('Lista de contatos vazia')
    else:
        print(f'{listar_contatos['Nome']} -> Tel: {listar_contatos['Tel']}')

def buscar_contato_pelo_nome(nome):
    #Next -> um for reduzido
    contato = next((contato for contato in contatos if contato['Nome'] == nome), None)
    if contato:
        print(f'{contato['Nome']} -> {contato['Tel']}')
    else:
        print('Contato não encontrado')

def deletar_contato(contato):
    cont = 0
    if any(novo_contato['Nome'] == contato for cont, novo_contato in enumerate(contatos)):
        contatos.pop(cont)
        print('Contato deletado')

def main():
    escolha = int(input('[1] - Adicionar um contato\n[2] - Ver contatos\n[3] - Buscar pelo nome do contato\n[4] - Deletar contato\n'))
    match escolha:
        case 1:
            nome = input('Nome do contato: ')
            tel = input('Telefone: ')
            add_contato(nome, tel)
        case 2:
            ver_contatos()
        case 3:
            nome = input('Nome do contato que deseja buscar: ')
            buscar_contato_pelo_nome(nome)
        case 4:
            nome = input('Nome do contato que deseja deletar: ')
            deletar_contato(nome)
main()


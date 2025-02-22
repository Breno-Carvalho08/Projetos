import re
import bcrypt
import maskpass
lista_login = []

def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao_email,email) is not None

def email_cadastrado(email):
    return any(conta['Email'] == email for conta in lista_login)

def validar_senha(senha):
    if len(senha) < 8:
        return False,'Sua senha tem que ter no mínimo 8 caracteres'
    if not any(c.isupper() for c in senha):
        return False, 'A senha deve conter pelo menos uma letra maiuscula.'
    if not any(c.isdigit() for c in senha):
        return False, 'A senha deve contar pelo menos um número.'
    return True, 'Senha válida'

def hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

#Principal
def cadastro_conta():
    while True:
        login = input('Email: ')
        if not validar_email(login):
            print('Email inválido')
        elif email_cadastrado(login):
            print('Email já cadastrado')
        else:
            break

    while True:
        senha = input('Senha: ')
        valido,mensagem = validar_senha(senha)

        if not valido:
            print(mensagem)
        else:
            senha_confirmacao = input('Digite sua senha novamente: ')
            if senha == senha_confirmacao:
                senha_hash = hash_senha(senha)
                conta = {'Email': login, 'Senha': senha_hash}
                print('Cadastro realizado com sucesso!')
                lista_login.append(conta)
                break
            else:
                print('Senhas devem ser iguais')

def encontrar_login(login):
    return any(conta['Email'] == login for conta in lista_login) is not None

def verificar_senha(senha_digitada, senha_hash):
    #Compara as senhas que estão armazenadas com a digitada
    return bcrypt.checkpw(senha_digitada.encode('utf-8'),senha_hash)


def login_conta():
    #Validar email
    login = input('Email: ')
    senha = maskpass.advpass('Senha: ','*',True)
    conta = next((conta for conta in lista_login if conta['Email'] == login), None)


    if conta: #Caso a conta seja encontrada
        if verificar_senha(senha,conta['Senha']): #verifica a senha
            print('Login realizado')
        else:
            print('Senha Incorreta')
            login_conta()
    else:
        print('Email não encontrado')
        login_conta()

cadastro_conta()
login_conta()


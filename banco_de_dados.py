import pymysql

#Conectando ao banco de dados
try:
    conexao = pymysql.connect(host='localhost',user='root',password='',database='testepython')
    print('Conexão bem-sucedida')

    #Criando uma tabela no banco de dados
    with conexao.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(200) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                telefone VARCHAR(20)
                 )'''
        )
        print('Tabela criada com sucesso!')

        escolha = int(input('Selecione uma opção\n[1] - Inserir valor\n[2] - Atualizar valor\n[3] - Deletar valor\nOpção:'))

        match escolha:
            case 1:
                #Inserindo valores dentro da tabela
                nome = input('Nome: ')
                email = input('Email: ')
                telefone = input('Telefone: ')

                inserir = 'INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)'
                valores = (nome, email, telefone)
                cursor.execute(inserir, valores)
            case 2:
                #Atualizando valores
                identificar_nome = input('Nome: ')
                identificar_valor = input('Qual o valor que deseja atualizar: ').lower().strip()
                if identificar_valor == 'email':
                    editar_email = input('Email novo: ').lower().strip()
                    atualizar = f'UPDATE clientes SET email = %s WHERE nome = %s'
                    atualizar_dados = (editar_email, identificar_nome)
                    cursor.execute(atualizar,atualizar_dados)
                elif identificar_valor == 'telefone':
                    editar_telefone = input('Telefone novo: ').lower().strip()
                    atualizar = f'UPDATE clientes SET telefone = %s WHERE nome = %s'
                    atualizar_dados = (editar_telefone, identificar_nome)
                    cursor.execute(atualizar, atualizar_dados)

            case 3:
                #Deletando valores
                identificar_nome = input('Nome: ')
                encontrar_nome = False
                cursor.execute('SELECT nome FROM clientes')
                for cliente in cursor.fetchall():
                    if cliente[0].lower() == identificar_nome.lower():
                        encontrar_nome = True
                if encontrar_nome:
                    deletar = f'DELETE FROM clientes WHERE nome = %s'
                    deletar_dados = (identificar_nome,)
                    cursor.execute(deletar, deletar_dados)
                else:
                    print('Usuário não encotrado.')

        #Mostrando os valores da tabela
        cursor.execute('SELECT * FROM clientes')
        for cliente in cursor.fetchall():
            print(f'{cliente}')

    conexao.commit()
    conexao.close()

except pymysql.MySQLError as err:
    print(f'Erro:{err}')




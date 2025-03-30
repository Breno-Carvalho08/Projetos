import pymysql

try:
    conexao = pymysql.connect(host='localhost', user='root', password='', database='contato')
    if conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
            '''CREATE TABLE IF NOT EXISTS contatos(
                nome VARCHAR(50),
                tel VARCHAR(11) NOT NULL             
                )''')

            escolha = int(input('[1] - Adicionar contato\n[2] - Consultar contatos\n[3] - Deletar contato\n'))

            match escolha:
                case 1:
                    nome_contato = input('Nome do contato: ').strip()
                    tel_contato = input('Telefone do contato: ').strip()
                    cursor.execute('''INSERT INTO contatos(nome, tel) VALUES (%s, %s)''', (nome_contato,tel_contato))
                    print('Contato adicionado com sucesso')

                case 2:
                    cursor.execute('SELECT * FROM contatos')
                    for nome,tel in cursor.fetchall():
                        print(f'Nome: {nome} - Telefone: {tel}')
                        print('--------------------------------')

                case 3:
                    excluir_contato = input('Nome do contato: ').strip().lower()
                    contato_exluido = cursor.execute('DELETE FROM contatos WHERE nome = LOWER(%s)', (excluir_contato,))

                    if not contato_exluido:
                        print('Contato não encontrado')
                    else:
                        print(f'Contato {excluir_contato.capitalize()} deletado com sucesso.')





    conexao.commit()
    conexao.close()


except pymysql.MySQLError as err:
    print(f'Erro:{err}')
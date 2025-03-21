import pymysql

try:
    conexao = pymysql.connect(
        host= 'localhost',
        user= 'root',
        password= '',
        database= 'estoque'
    )
    with conexao.cursor() as cursor:
        cursor.execute('''
         CREATE TABLE IF NOT EXISTS estoque(
         nome VARCHAR(20) NOT NULL,
         quant INT          
        )''')

        escolha = int(input('[1] - Visualizar estoque\n[2] - Adicionar ao estoque\n[3] - Remover do estoque\n[4] - Deletar do estoque\nOpção: '))
        match escolha:
            case 1:
                cursor.execute('SELECT * FROM estoque')
                for nome,quant in cursor.fetchall():
                    print(f'Produto: {nome} | Quantidade: {quant}')
            case 2:
                nome = input('Nome do produto:')
                quant = int(input('Quantidade do produto: '))
                #Verificando se o produto ja existe dentro do banco de dados
                cursor.execute('SELECT quant FROM estoque WHERE nome = %s',(nome,))
                resultado = cursor.fetchone()

                if resultado:
                    nova_quant = resultado[0] + quant
                    cursor.execute('UPDATE estoque SET quant = %s WHERE nome = %s',(nova_quant,nome))

                else:
                    cursor.execute('INSERT INTO estoque (nome, quant) VALUES (%s, %s)',(nome,quant))
            case 3:
                nome = input('Nome do produto:')
                quant = int(input('Quantidade do produto que deseja retirar: '))
                cursor.execute('SELECT quant FROM estoque WHERE nome = %s',(nome,))
                resultado = cursor.fetchone()

                if resultado:
                    if quant > resultado[0]:
                        print('Esse valor excede a quantidade que temos em estoque')
                    else:
                        nova_quant = resultado[0] - quant
                        cursor.execute('UPDATE estoque SET quant = %s WHERE nome = %s', (nova_quant, nome))

            case 4:
                nome = input('Nome do produto: ').strip()
                cursor.execute('SELECT nome FROM estoque WHERE LOWER(nome) = LOWER(%s)',(nome,))
                produto_encontrado = cursor.fetchone() #fetch = Buscar

                if produto_encontrado:
                    cursor.execute('DELETE FROM estoque WHERE nome = %s',(nome,))
                    print('Produto deletado com sucesso.')
                else:
                    print('Produto não encontrado')

    conexao.commit()
    conexao.close()

except pymysql.MySQLError as err:
    print(f'Erro:{err}')
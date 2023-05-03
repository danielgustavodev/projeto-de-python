import sqlite3 as cone
# CRIAR UM BANCO DE DADOS:
try:
    # Abertura de conexão e aquisição de cursor:
    conexao = cone.connect("meu_banco.db")
    cursor = conexao.cursor()

    # Execução de comandos: (CREATE, SELECT, UPDATE, DELETE - CRUD)
    comando = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''

    cursor.execute(comando)

    # Efetivação do comando:
    conexao.commit:(cursor)

except cone.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    # Fechamento das conexões:
    if conexao:
        cursor.close()
        conexao.close()
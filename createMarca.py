import sqlite3 as cone
#abertura de conexão e aquisição de cusor
conexao = cone.connect('meu_banco.db')
cursor = conexao.cursor()

#execução de um comando sql
comando = '''CREATE TABLE Marca(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY (id)
);'''
cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()
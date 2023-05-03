import sqlite3 as cone
conexao = cone.connect('meu_banco.db')
cursor = conexao.cursor()

comando = '''CREATE TABLE Veiculo(
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY(placa)
                FOREIGN KEY (proprietario) REFERENCES pessoa (cpf)
                FOREIGN KEY (marca) REFERENCES marca (id)
                );'''
cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()

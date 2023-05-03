import sqlite3 as cone

class Marca:
    def __init__(self, nome, sigla):
        self.id = None
        self.nome = nome
        self.sigla = sigla
 
        self.conexao = cone.connect('meu_banco.db')
        self.conexao.execute('PRAGMA foreign_keys = on')
        self.cursor = self.conexao.cursor()
        
    def visualizar(self):
        comando_Vi_Mar = '''SELECT * FROM Marca;'''
        resultados = self.cursor.execute(comando_Vi_Mar).fetchall()
        for linha in resultados:
            print(linha)
            
    def inserir(self):
        comando_Ins_Mar = '''INSERT INTO Marca (nome , sigla ) VALUES ( ?, ?)'''
        nome = input('Digite o nome da marca: ')
        sigla = input('Digite a sigla da marca: ')
        self.cursor.execute(comando_Ins_Mar, ( nome, sigla))
        print('Cadastro inserido com sucesso!')
        
    def excluir(self):
        comando_Exc_Mar = '''DELETE FROM Marca WHERE id = ?'''
        id = input('Digite o ID do cadastro para ser deletado: ')
        self.cursor.execute(comando_Exc_Mar, (id,))
        print('Cadastro excluído com sucesso!')
        
    def fechar_conexao(self):
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

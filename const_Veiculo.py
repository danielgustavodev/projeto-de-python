import sqlite3 as cone

class Veiculo:
    def __init__(self, placa, ano, cor, proprietario, marca, motor):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.proprietario = proprietario
        self.marca = marca
        self.motor = motor

    def visualizar(self, placa = None):
        with cone.connect('meu_banco.db') as conexao:
            conexao.execute('PRAGMA foreign_keys = on')
            cursor = conexao.cursor()
            if placa:
                comando_Vi_Vei = '''SELECT * FROM Veiculo WHERE placa = ?;'''
                resultados = cursor.execute(comando_Vi_Vei, (placa,)).fetchall()
            else:
                comando_Vi_Vei = '''SELECT * FROM Veiculo;'''
                resultados = cursor.execute(comando_Vi_Vei).fetchall()
            for linha in resultados:
                print(linha)
        
    def inserir(self):
        with cone.connect('meu_banco.db') as conexao:
            conexao.execute('PRAGMA foreign_keys = on')
            cursor = conexao.cursor()
            comando_Ins_Vei = '''INSERT INTO Veiculo (placa, ano, cor, proprietario, marca, motor) VALUES (?, ?, ?, ?, ?, ?)'''
            cursor.execute(comando_Ins_Vei, (self.placa, self.ano, self.cor, self.proprietario, self.marca, self.motor))
            print('Cadastro inserido com sucesso!')

        
    def excluir(self, placa):
        with cone.connect('meu_banco.db') as conexao:
            conexao.execute('PRAGMA foreign_keys = on')
            cursor = conexao.cursor()
            comando_Exc_Vei = '''DELETE FROM Veiculo WHERE placa = ?'''
            cursor.execute(comando_Exc_Vei, (placa,))
            print('Cadastro excluído com sucesso!')
        

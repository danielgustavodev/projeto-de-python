import sqlite3 as cone

class Pessoa:
    def __init__(self, cpf, nome, nascimento, oculos):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.oculos = oculos
        
        self.conexao = cone.connect('meu_banco.db')
        self.conexao.execute('PRAGMA foreign_keys = on')
        self.cursor = self.conexao.cursor()
        
    def visualizar(self):
        comando_Vi_Pess = '''SELECT * FROM Pessoa;'''
        resultados = self.cursor.execute(comando_Vi_Pess).fetchall()
        for linha in resultados:
            print(linha)
            
    def inserir(self):
        comando_Ins_Pess = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)'''
        cpf = input('Digite o CPF: ')
        nome = input('Digite o nome: ')
        nascimento = input('Digite a data de nascimento (no formato AAAA-MM-DD): ')
        oculos = bool(input('Usa óculos use 1 para sim e 0 para não: '))

        nova_pessoa = Pessoa(cpf, nome, nascimento, oculos)
        self.cursor.execute(comando_Ins_Pess, (cpf, nome, nascimento, oculos))
        print('Cadastro inserido com sucesso!')
        
    def excluir(self):
        comando_Exc_Pess = '''DELETE FROM Pessoa WHERE cpf = ?'''
        cpf = input('Digite o CPF do cadastro para ser deletado: ')
        self.cursor.execute(comando_Exc_Pess, (cpf,))
        print('Cadastro deletado com sucesso!')
        
    def alterar(self):
        comando_Alt_Pess = '''UPDATE Pessoa SET nome = ?, nascimento = ?, oculos = ? WHERE cpf = ?'''
        cpf = input('Digite o CPF da pessoa a ser alterada: ')
        nome = input('Digite o novo nome: ')
        nascimento = input('Digite a nova data de nascimento: ')
        oculos = bool(int(input('Usa óculos? Digite 1 para sim ou 0 para não: ')))

        self.cursor.execute(comando_Alt_Pess, (nome, nascimento, oculos, cpf))
        print('Cadastro alterado com sucesso!')
        
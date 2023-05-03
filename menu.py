import sqlite3 as cone
from const_Marca import Marca
from const_Veiculo import Veiculo
from const_Pessoa import Pessoa #, comando_Vi_Pess , comando_Ins_Pess , comando_Exc_Pess , comando_Alt_Pess


conexao =cone.connect('meu_banco.db')
conexao.execute('PRAGMA foreign_keys = on')
cursor = conexao.cursor()

pessoa = Pessoa(None, None, None, None)

menu_Principal = ["1: Pessoa ", "2: Veículo", "3: Marca" , "0: para encerrar"]
menu_Pessoa = ["1 - Visualizar", "2 - Inserir", "3 - Excluir", "4 - Alterar", "0 para voltar ao menu principal"]
print('escolha uma tabela')
print(menu_Principal)
escolha_Menu_Prin = input()

if escolha_Menu_Prin == "1":
    print('voce escolheu a tabela pessoas')
    print('escolha uma opção ')
    print(menu_Pessoa)
    escolha_Menu_Pess = input()
    
    
    if escolha_Menu_Pess == "1":
        pessoa.visualizar()
        
    elif escolha_Menu_Pess == "2":
        pessoa.inserir()
          
    elif escolha_Menu_Pess == "3":
        pessoa.excluir()
        
    elif escolha_Menu_Pess == "4":
        pessoa.alterar()
    
        
    elif escolha_Menu_Pess == "0":
        print(menu_Principal)
        
    else:
        print("digitado uma opção invalida")
        pessoa.fechar_conexao()




 
 
veiculo = Veiculo(None, None, None, None , None , None) 

menu_Veiculo = ["1 - Visualizar", "2 - Inserir", "3 - Excluir", "4 - Alterar" , "0 para voltar ao menu principal"]

if escolha_Menu_Prin == "2":
    print('voce escolheu a tabela veiculos')
    print('escolha uma opção ')
    print(menu_Veiculo)
    escolha_Menu_Vei = input()
    
    
    if escolha_Menu_Vei == "1":
        veiculo.visualizar()
        
    elif escolha_Menu_Vei == "2":
        veiculo = Veiculo("ABC-1234", 2022, "Preto", "João Silva", "Chevrolet", "Motor V8")

        veiculo.inserir()
          
    elif escolha_Menu_Vei == "3":
        veiculo.excluir()
        
    elif escolha_Menu_Vei == "4":
        veiculo.alterar()
        
    elif escolha_Menu_Vei == "0":
        menu_Principal
        
    else:
        print("digitado uma opção invalida")
        veiculo.fechar_conexao()

marca = Marca ( None, None)

menu_Marca = ["1 - Visualizar", "2 - Inserir", "3 - Excluir", "4 - Alterar" , "0 para voltar ao menu principal"]
print('escolha uma tabela')

if escolha_Menu_Prin == "3":
    print('cove escolheu a tabela marca')
    print('escolha uma opção ')
    print(menu_Marca)
    escolha_Menu_Mar = input()
    
    
    if escolha_Menu_Mar == "1":
        marca.visualizar()
        
    elif escolha_Menu_Mar == "2":
        marca.inserir()
          
    elif escolha_Menu_Mar == "3":
        marca.excluir()
        
    elif escolha_Menu_Mar == "4":
        marca.alterar()
        
    elif escolha_Menu_Mar == "0":
        menu_Principal
        
    else:
        print("digitado uma opção invalida")
        

marca.fechar_conexao()
escolha_Menu_Prin =="0"
conexao.commit()
cursor.close()
conexao.close()




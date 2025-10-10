import Cadastro_Clientes
import CadastroCamisa
import CadastroEquipe

# Função para o submenu de cadastro
def menu_cadastro():
    #submenu de cadastro
    while True:
        print("--- Menu de Cadastro ---")
        print("1 - Cadastrar Camisa")
        print("2 - Cadastrar Cliente")
        print("0 - Voltar ao Menu Principal")
        
        opcao_cadastro = input("Escolha uma opção: ")
        
        if opcao_cadastro == '1':
            print("CADASTRAR CAMISA")
            CadastroEquipe.CadastroEquipe()
        elif opcao_cadastro == '2':
            print("CADASTRAR CLIENTE")
            Cadastro_Clientes.Cadastro_Clientes()
        elif opcao_cadastro == '0':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção incorreta! Tente outra vez.")

# submenu de pesquisa
def menu_pesquisa():
    while True:
        print("--- Menu de Pesquisa ---")
        print("1 - Pesquisar Cliente")
        print("2 - Pesquisar Camisa")
        print("0 - Voltar ao Menu Principal")
        
        opcao_pesquisa = input("Escolha uma opção: ")
        
        if opcao_pesquisa == '1':
            print("PESQUISISAR CLIENTE")
            break
        elif opcao_pesquisa == '2':
            print("PESQUISAR CAMISA")
            break
        elif opcao_pesquisa == '0':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção incorreta! Tente outra vez.")

# Função para o menu principal
def menu_principal():

    while True:
        print("===== MENU DA LOJA =====")
        print("1 - Cadastrar")
        print("2 - Vendas")
        print("3 - Pesquisar")
        print("4 - Estoque")
        print("5 - Login")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_cadastro()
        elif opcao == '2':
            print("VENDAS")

        elif opcao == '3':
            menu_pesquisa()
        elif opcao == '4':
            print("ESTOQUE")

        elif opcao == '5':
            print("LOGIN")

        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção incorreta! Por favor, escolha uma opção do menu.")


# Inicia o programa chamando a função do menu principal
menu_principal()
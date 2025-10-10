import Cadastro_Clientes
import CadastroEquipe
import vendas 
import login


def menu_cadastro():
    #submenu de cadastro
    while True:
        print("--- Menu de Cadastro ---")
        print("1 - Cadastrar Camisa")
        print("2 - Cadastrar Cliente")
        print("0 - Voltar ao Menu Principal")
        
        opcao_cadastro = input("Escolha uma opção: ")
        
        if opcao_cadastro == '1':
            CadastroEquipe.CadastroEquipe()
        elif opcao_cadastro == '2':
            Cadastro_Clientes.Cadastro_Clientes()
        elif opcao_cadastro == '0':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção incorreta! Tente outra vez.")

def menu_pesquisa():
    while True:
        print("--- Menu de Pesquisa ---")
        print("1 - Pesquisar Cliente")
        print("2 - Pesquisar Camisa")
        print("0 - Voltar ao Menu Principal")
        
        opcao_pesquisa = input("Escolha uma opção: ")
        
        if opcao_pesquisa == '1':
            print("PESQUISAR CLIENTE")

        elif opcao_pesquisa == '2':
            print("PESQUISAR CAMISA")

        elif opcao_pesquisa == '0':
            print("Voltando ao menu principal")
            break
        else:
            print("Opção incorreta! Tente outra vez.")

def menu_principal():

    while True:
        print("\n===== BEM-VINDO À LOJA =====")
        print("Você precisa fazer login para continuar.")
        print("1 - Fazer Login")
        print("2 - Cadastrar Novo Usuário")
        print("0 - Sair do Programa")
        
        opcao_login = input("Escolha uma opção: ")

        if opcao_login == '1':
            # Chama a função de login. Se retornar True, o loop é quebrado.
            if login.fazer_login():
                break
        elif opcao_login == '2':
            login.cadastrar_usuario()
        elif opcao_login == '0':
            print("Saindo...")
            return
        else:
            print("Opção inválida. Tente novamente.")


    # Este loop só será executado após um login correto
    while True:
        print("===== MENU PRINCIPAL DA LOJA =====")
        print("1 - Cadastrar")
        print("2 - Vendas")
        print("3 - Pesquisar")
        print("4 - Estoque")
        print("0 - Sair (Logout)")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            menu_cadastro()
        elif opcao == '2':
            vendas.menu_vendas()
        elif opcao == '3':
            menu_pesquisa()
        elif opcao == '4':
            print("ESTOQUE")
        elif opcao == '0':
            print("Fazendo logout e saindo...")
            break
        else:
            print("Opção incorreta! Por favor, escolha uma opção do menu.")


# Inicia o programa chamando a função do menu principal
menu_principal()
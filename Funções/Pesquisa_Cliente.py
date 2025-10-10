import json
import Cadastro_Clientes
# Função para pesquisar clientes por um termo específico
def Pesquisa_Cliente():
    # Exibe o título do menu de pesquisa
    print("--- Menu de Pesquisa de Clientes ---")
    # Exibe as opções de pesquisa disponíveis
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por CPF/CNPJ")
    print("0 - Sair")
    # Inicia um loop para manter o menu ativo até o usuário decidir sair  
    while True:
        # Solicita ao usuáro que escolha a opção desejada
        opcao = input("Escolha uma opção (1, 2 ou 0): ")
        # Se a opção for '0', sai do loop e encerra a função
        if opcao == '0':
            print("Saindo do menu de pesquisa.")
            break 
        # Se a opção for '1', pesquisa por nome
        elif opcao == '1': 
            termo = input("Digite o nome do cliente para pesquisar: ")
            Cadastro_Clientes.pesquisar_clientes( termo, campo='nome')  # Chama a função de pesquisa
        # Se a opção for '2', pesquisa por CPF/CNPJ
        elif opcao == '2':    
            termo = input("Digite o CPF/CNPJ do cliente para pesquisar: ")
            Cadastro_Clientes.pesquisar_clientes( termo, campo='Chave')  # Chama a função de pesquisa
        # Se a opção for inválida, exibe uma mensagem de erro e volta ao início
        else:
            print("Opção inválida. Tente novamente.")
            continue #Volta para o início do loop se a opção for inválida
  
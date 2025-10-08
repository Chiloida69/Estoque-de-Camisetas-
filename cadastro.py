#Criação do menu de cadastro

def cadastro():
    print("Menu da Loja")
    print("1 - Cadastrar ")
    print('2 - Vendas')
    print('3 - Pesquisar')
    print('4 - Estoque')
    print('5 - Login')
    print('0 - Sair')
opcao = int(input("Digite a opção desejada: "))

lista_camisas = []

if opcao == 1:
    nome = input("Digite o nome da camisa: ")
    tamanho = input("Digite o tamanho da camisa (P, M, G, GG): ")
    cor = input("Digite a cor da camisa: ")
    preco = float(input("Digite o preço da camisa: "))
    
    camisa = {
        'nome': nome,
        'tamanho': tamanho,
        'cor': cor,
        'preco': preco
    }
    
    lista_camisas.append(camisa)
    print("Camisa cadastrada com sucesso!")
    print(lista_camisas)

elif opcao == 2:
    print("Opção de Vendas selecionada.")
    # Implementar funcionalidade de vendas aqui

elif opcao == 3:
    print("Opção de Pesquisar selecionada.")
    # Implementar funcionalidade de pesquisa aqui

elif opcao == 4:
    print("Opção de Estoque selecionada.")
    # Implementar funcionalidade de estoque aqui

elif opcao == 5:
    print("Opção de Login selecionada.")
    # Implementar funcionalidade de login aqui

elif opcao == 0:
    print("Saindo do programa.")

else:
    print("Opção inválida. Tente novamente.")#Criação do menu de cadastro  

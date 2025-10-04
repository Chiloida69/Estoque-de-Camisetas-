import CadastroCamisa
def CadastroEquipe(Cadastro): #Define a função para cadastro dos equipe para dentro das marcas.
    while True: #Loop infinito para manter o menu ativo até o usuário decidir sair.
        print("\nSelecione a marca para cadastrar a equipe:")
        print("1 - Nike")
        print("2 - Adidas")
        print("3 - Puma")
        print("4 - Voltar ao menu principal")
        try: #tradar exceção de erro caso o usuário digite algo diferente de número.
            ListaEquipes = [] #Cria uma lista vazia para armazenar as equipes cadastradas.
            marca = int(input("Digite o número da marca: "))   #Solicita ao usuário que digite o número da marca.
            if marca == 1: #Direciona para o cadastro da marca 1.
                print("Nike selecionada para cadastro de equipe")   
                equipe = input('Cadastre a equipe: ') #Solicita ao usuário que digite o nome da equipe.
                print(f'A equipe {equipe} foi cadastrada com sucesso!') #Confirmação de cadastro.
                CadastroCamisa.CadastroCamisa() #Chama a função para cadastrar camisas após cadastrar a equipe.
                ListaEquipes.append(("Nike", equipe,CadastroCamisa)) #Adiciona a equipe cadastrada na lista.
            elif marca == 2:
                print("Adidas selecionada para cadastro de equipe")
                equipe = input('Cadastre a equipe: ')
                ListaEquipes.append(("Adidas", equipe))
                print(f'A equipe {equipe} foi cadastrada com sucesso!') #Confirmação de cadastro.
            elif marca == 3:
                print("Puma selecionada para cadastro de equipe")
                equipe = input('Cadastre a equipe: ')
                ListaEquipes.append(("Puma", equipe))
                print(f'A equipe {equipe} foi cadastrada com sucesso!') #Confirmação de cadastro.
            elif marca == 4:
                print("Voltando ao menu principal...")
                break
            else:
                print("Seleção inválida. Tente novamente.")
            print(f'Equipes cadastradas: {ListaEquipes}') #Exibe a lista de equipes cadastradas.
        except ValueError: #validação de erro.
            print("Digite uma seleção válida/Número")
CadastroEquipe(1) #Chama a função para testar o cadastro de equipes.



import Funções.CadastroEquipe as CadastroEquipe

while True:
        print("\nSelecione a marca para cadastrar a equipe:")
        print("1 - Nike")
        print("2 - Adidas")
        print("3 - Puma")
        print("4 - Voltar ao menu principal")
        try:
            ListaEquipes = []
            marca = int(input("Digite o número da marca: "))
            if marca == 1:
                print("Nike selecionada para cadastro de equipe")
                equipe = input('Cadastre a equipe: ')
                ListaEquipes.append(("Nike", equipe))
                CadastroCamisas()
            elif marca == 2:
                print("Adidas selecionada para cadastro de equipe")
                equipe = input('Cadastre a equipe: ')
                ListaEquipes.append(("Adidas", equipe))
            elif marca == 3:
                print("Puma selecionada para cadastro de equipe")
                equipe = input('Cadastre a equipe: ')
                ListaEquipes.append(("Puma", equipe))
            elif marca == 4:
                print("Voltando ao menu principal...")
                break
            else:
                print("Seleção inválida. Tente novamente.")
            print(f'Equipes cadastradas: {ListaEquipes}') #Exibe a lista de equipes cadastradas.
        except ValueError: #validação de erro.
            print("Digite uma seleção válida/Número")
    # Para testar o menu, descomente a linha abaixo:

import CadastroCamisa
def CadastroEquipe(Cadastro): #Define a função para cadastro dos equipe para dentro das marcas.
    
    while True: #Loop infinito para manter o menu ativo até o usuário decidir sair.
        print("\nSelecione a marca para cadastrar a equipe:")
        print("1 - Nike")
        print("2 - Adidas")
        print("3 - Puma")
        print("4 - Voltar ao menu principal")
        Equipe = input("Digite o número da marca: ")
        
        if Equipe.lower() == '4': #Condição para sair do loop
            print("Voltando ao menu principal...")
            break #Sai do loop se o usuário digitar 'sair' ou escolher voltar ao menu principal.
        
        elif Equipe == '1' : #Escolha da marca
            print('1 - Barcelona')
            print('2 - Brasil')
            print('3 - Corinthians')
            print('4 - Ineter de Milão')
            print('5 - Paris Saint-Germain')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':  #Escolha do time
                print("Barcelona selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa() #Chama a função de cadastro de camisas.
            elif Escolha == '2':
                print("Brasil selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '3':
                print("Corinthians selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '4':
                print("Inter de Milão selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '5':
                print("Paris Saint-Germain selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
                
        elif Equipe == '2' :
            print('1 - Alemanha')
            print('2 - Arsenal')
            print('3 - Real Madrid')
            print('4 - Manchester United')
            print('5 - Juventus')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':  
                print("Alemanha selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '2':
                print("Arsenal selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '3':
                print("Real Madrid selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '4':
                print("Manchester United selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa() 
            elif Escolha == '5':
                print("Juventus selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
            
        elif Equipe == '3' :
            print('1 - Bahia')    
            print('2 - Borussia Dortmund')    
            print('3 - Manchester City')    
            print('4 - Milan')    
            print('5 - Valencia')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':  
                print("Bahia selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '2':
                print("Borussia Dortmund selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '3':
                print("Manchester City selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '4':
                print("Milan selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()
            elif Escolha == '5':    
                print("Valencia selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa()     
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
                
        else:
            print ("Seleção inválida. Tente novamente.")
        

CadastroEquipe(1)       
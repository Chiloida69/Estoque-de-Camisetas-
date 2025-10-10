import CadastroCamisa
def CadastroEquipe(): #Define a função para cadastro dos equipe para dentro das marcas.
    
    while True: #Loop infinito para manter o menu ativo até o usuário decidir sair.
        print("\nSelecione a marca para cadastrar a equipe:")
        print("1 - Nike")
        print("2 - Adidas")
        print("3 - Puma")
        print("0 - Voltar ao menu principal")
        Equipe = input("Digite o número da marca: ")
        Marca='' #Variável global para armazenar a marca selecionada
        time=''  #Variável global para armazenar o time selecionado
        if Equipe.lower() == '0': #Condição para sair do loop
            print("Voltando ao menu principal...")
            break #Sai do loop se o usuário digitar 'sair' ou escolher voltar ao menu principal.
        
        elif Equipe == '1' : #Escolha da marca
            Marca = 'Nike'
            print('1 - Barcelona')
            print('2 - Brasil')
            print('3 - Corinthians')
            print('4 - Inter de Milão')
            print('5 - Paris Saint-Germain')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':  #Escolha do time
                time='Barcelona'
                print("Barcelona selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca, time) #Chama a função de cadastro de camisas.
            elif Escolha == '2':
                time='Brasil'
                print("Brasil selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca, time)
            elif Escolha == '3':
                time='Corinthians'
                print("Corinthians selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca, time)
            elif Escolha == '4':
                time='Inter de Milão'
                print("Inter de Milão selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca, time)
            elif Escolha == '5':
                time='Paris Saint-Germain'
                print("Paris Saint-Germain selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca, time)
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
                
        elif Equipe == '2' :
            Marca = 'Adidas'
            print('1 - Alemanha')
            print('2 - Arsenal')
            print('3 - Real Madrid')
            print('4 - Manchester United')
            print('5 - Juventus')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':
                time='Alemanha'
                print("Alemanha selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa( Marca, time)
            elif Escolha == '2':
                time='Arsenal'
                print("Arsenal selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time)
            elif Escolha == '3':
                time='Real Madrid'
                print("Real Madrid selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time)
            elif Escolha == '4':
                time='Manchester United'
                print("Manchester United selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time) 
            elif Escolha == '5':
                time='Juventus'
                print("Juventus selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time)
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
            
        elif Equipe == '3' :
            Marca = 'Puma'
            print('1 - Bahia')    
            print('2 - Borussia Dortmund')    
            print('3 - Manchester City')    
            print('4 - Milan')    
            print('5 - Valencia')
            print('6 - Voltar ao menu anterior')
            Escolha=input("Digite o número do time: ")
            if Escolha == '1':  
                time='Bahia'
                print("Bahia selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time)
            elif Escolha == '2':
                time='Borussia Dortmund'
                print("Borussia Dortmund selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time)
            elif Escolha == '3':
                time='Manchester City'
                print("Manchester City selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca,time )
            elif Escolha == '4':
                time='Milan'
                print("Milan selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca , time )
            elif Escolha == '5':
                time='Valencia'    
                print("Valencia selecionada para cadastro de equipe")
                CadastroCamisa.CadastroCamisa(Marca , time )     
            elif Escolha == '6':
                print("Voltando ao menu anterior...")
            else:
                print ("Seleção inválida. Tente novamente.")
                
        else:
            print ("Seleção inválida. Tente novamente.")
        

 
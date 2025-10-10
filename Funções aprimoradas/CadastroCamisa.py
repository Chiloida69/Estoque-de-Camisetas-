
import banco_de_dados

def CadastroCamisa():
    
    print("Função de cadastro de camisas chamada.")
    while True:
        Modelo = input('Cadastre o modelo da camisa (ou digite "sair" para terminar): ')
        #sair do loop
        if Modelo.lower() == 'sair':
            break #Sai do loop se o usuário digitar 'sair'.
            
        # Verifica se o modelo já existe para evitar sobreescrever
        if Modelo in banco_de_dados.estoque_camisas:
            print(f"Modelo '{Modelo}' já cadastrado. Use a função de estoque para adicionar mais unidades.")
            continue
            
        # Solicita os dados da camisa
        Tamanho = input(f'Cadastre o tamanho da camisa (P, M, G, GG) para o modelo {Modelo}: ')
        Cor = input(f'Cadastre a cor da camisa para o modelo {Modelo}: ')
        
        try:
            Codigo= int(input(f'Cadastre um codigo para a camisa {Modelo}: '))
            Quantidade= int(input(f'Cadastre a quantidade de camisas para o modelo {Modelo}: '))
        except ValueError:
            print("Entrada inválida para código ou quantidade. Por favor, digite apenas números.")
            continue #Volta para o início do loop para tentar novamente
            
        # Cria um dicionário com os detalhes da camisa
        detalhes_camisa = {
            'Tamanho': Tamanho,
            'Cor': Cor,
            'Quantidade': Quantidade,
            'Codigo': Codigo
        }
        
        # Adiciona o novo dicionário ao dicionário do nosso banco de dados
        banco_de_dados.estoque_camisas[Modelo] = detalhes_camisa
        
        print(f" Camisa '{Modelo}' cadastrada com sucesso!")
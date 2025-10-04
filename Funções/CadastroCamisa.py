def CadastroCamisa(): #Define a função para cadastro das camisas.
    TableCamisas = {} #Cria um dicionário vazio para armazenar as camisas cadastradas.
    print("Função de cadastro de camisas chamada.") #Mensagem para indicar que a função foi chamada.
      # Loop para permitir o cadastro de várias camisas
    while True:
        Modelo = input('Cadastre o modelo da camisa (ou digite "sair" para terminar): ')
        # Condição para sair do loop
        if Modelo.lower() == 'sair':
            break #Sai do loop se o usuário digitar 'sair'.
        # Solicita os dados da camisa
        Tamanho = input(f'Cadastre o tamanho da camisa (P, M, G, GG) para o modelo {Modelo}: ')
        Cor = input(f'Cadastre a cor da camisa para o modelo {Modelo}: ')
        # Converte a quantidade para número inteiro para garantir que é um número.
        try:
            Quantidade= int(input(f'Cadastre a quantidade de camisas para o modelo {Modelo}: '))
        except ValueError:
            print("Entrada inválida para a quantidade. Por favor, digite um número inteiro.")
            continue #Volta para o início do loop para tentar novamente
        # Cria um dicionário com os detalhes da camisa
        detalhes_camisa = {
            'Tamanho': Tamanho,
            'Cor': Cor,
            'Quantidade': Quantidade
        }
        # Adiciona o novo dicionário ao dicionário principal, usando o modelo como chave
        TableCamisas[Modelo] = detalhes_camisa
        print(f"Camisa '{Modelo}' cadastrada com sucesso!") #Mensagem de confirmação de cadastro.
    # Retorna o dicionário com todas as camisas cadastradas
    return TableCamisas

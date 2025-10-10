def CadastroCamisa():
    TableCamisas = {}
    print("Função de cadastro de camisas chamada.")

    while True:
        Modelo = input('Cadastre o modelo da camisa (ou digite "sair" para terminar): ')
        

        if Modelo.lower() == 'sair':
            break

        Tamanho = input(f'Cadastre o tamanho da camisa (P, M, G, GG) para o modelo {Modelo}: ')
        Cor = input(f'Cadastre a cor da camisa para o modelo {Modelo}: ')
        
        try:
            Quantidade = int(input(f'Cadastre a quantidade de camisas para o modelo {Modelo}: '))
        except ValueError:
            print("Entrada inválida para a quantidade. Por favor, digite um número inteiro.")
            continue  # Volta para o início do loop para tentar novamente

        # Cria um dicionário com os detalhes da camisa
        detalhes_camisa = {
            'Tamanho': Tamanho,
            'Cor': Cor,
            'Quantidade': Quantidade
        }
        
        # Adiciona o novo dicionário ao dicionário principal, usando o modelo como chave
        TableCamisas[Modelo] = detalhes_camisa
        print(f"Camisa '{Modelo}' cadastrada com sucesso!")

    # Retorna o dicionário com todas as camisas cadastradas
    return TableCamisas

# Exemplo de como usar a função:
inventario = CadastroCamisa()
print("\nInventário de camisas finalizado:")
print(inventario)

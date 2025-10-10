import json

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
        while True:
            Modelo = input('Cadastre o modelo da camisa (ou digite "sair" para terminar): ')
            if Modelo.lower() == 'sair':
                break
            Tamanho = input(f'Cadastre o tamanho da camisa (P, M, G, GG) para o modelo {Modelo}: ')
            Cor = input(f'Cadastre a cor da camisa para o modelo {Modelo}: ')
            try:
                Codigo = int(input(f'Cadastre um código para a camisa {Modelo}: '))
                Quantidade = int(input(f'Cadastre a quantidade de camisas para o modelo {Modelo}: '))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
                continue
            detalhes_camisa = {
                'Modelo': Modelo,
                'Tamanho': Tamanho,
                'Cor': Cor,
                'Quantidade': Quantidade,
                'Codigo': Codigo
            }
            TableCamisas[Modelo] = detalhes_camisa
            print(f"Camisa '{Modelo}' cadastrada com sucesso!")
        print("Cadastro de camisas finalizado.")
        return TableCamisas

def carregar_camisas(nome_arquivo="camisas.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado, retornando dicionário vazio.")
        return {}

# Exemplo de uso:
# camisas = CadastroCamisa()
# salvar_camisas(camisas)
# camisas_carregadas = carregar_camisas()
# print(camisas_carregadas)
import CadastroCamisa # Importa o módulo que contém as funções de carregar e salvar

def menu_vendas():
    """
    Função para gerenciar o processo de venda de camisas,
    dando baixa no estoque.
    """
    
    # 1. Carrega o estoque do arquivo JSON
    estoque_camisas = CadastroCamisa.carregar_camisas()
    
    while True:
        print("--- Menu de Vendas ---")

        # Verifica se o estoque está vazio
        if not estoque_camisas:
            print("Nenhuma camisa cadastrada no estoque. Cadastre uma camisa primeiro.")
            break

        # 2. Listar as camisas disponíveis (usando o estoque carregado)
        print("Camisas em estoque:")
        # Listagem mais clara para o usuário
        for modelo, detalhes in estoque_camisas.items():
            qtd = detalhes.get('Quantidade', 0)
            if qtd > 0:
                print(f"-> Modelo: {modelo} | Tamanho: {detalhes.get('Tamanho', 'N/A')} | Cor: {detalhes.get('Cor', 'N/A')} | Qtd: {qtd}")
        
        print('Digite "voltar" a qualquer momento para sair.')
        
        # 3. Pedir para o usuário escolher o modelo
        modelo_venda = input("Digite o nome do MODELO da camisa que deseja vender: ")

        if modelo_venda.lower() == 'voltar':
            print("Voltando ao menu principal...")
            break
        
        # 4. Verificar se a camisa existe no estoque
        if modelo_venda in estoque_camisas:
            camisa_selecionada = estoque_camisas[modelo_venda]
            estoque_atual = camisa_selecionada.get('Quantidade', 0) # Usa .get para segurança
            
            print(f"Estoque atual da camisa '{modelo_venda}': {estoque_atual} unidades.")
            
            # Checa se há estoque disponível antes de pedir a quantidade
            if estoque_atual <= 0:
                print(f"Aviso: O estoque da camisa '{modelo_venda}' está zerado.")
                continue # Volta ao início do loop
            
            try:
                # 5. Perguntar a quantidade a ser vendida
                qtd_venda = int(input(f"Quantas unidades de '{modelo_venda}' deseja vender? "))

                # 6. Validar o estoque e dar baixa
                if qtd_venda <= 0:
                    print("Quantidade inválida. Por favor, insira um número maior que zero.")
                elif qtd_venda <= estoque_atual:
                    # Se há estoque suficiente, realiza a baixa
                    camisa_selecionada['Quantidade'] -= qtd_venda
                    
                    # 7. Salva a alteração no arquivo JSON
                    CadastroCamisa.salvar_camisas(estoque_camisas)
                    
                    print(f"\nVenda de {qtd_venda} unidades realizada com sucesso!")
                    print(f"   Estoque atualizado de '{modelo_venda}': {camisa_selecionada['Quantidade']} unidades.")
                else:
                    # Se não há estoque suficiente, informa o usuário
                    print(f"Estoque insuficiente! Temos apenas {estoque_atual} unidades dessa camisa.")
            
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números inteiros para a quantidade.")

        else:
            print(f"Modelo '{modelo_venda}' não encontrado no estoque. Tente novamente.")
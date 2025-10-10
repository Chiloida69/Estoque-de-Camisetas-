import json
from Funções.CadastroCamisa import CadastroCamisa
def pesquisa():
    # Exibe o título do menu de pesquisa
    print("--- Menu de Pesquisa ---")
    # Exibe as opções de pesquisa disponíveis
    print("1 - Pesquisar por modelo")
    print("2 - Pesquisar por equipe")
    print("3 - Pesquisar por marca")
    print("4 - Pesquisar por cor")
    print("5 - Pesquisar por tamanho")
    print("6 - Pesquisar por múltiplos requisitos")
    print("0 - Sair")
    # Inicia um loop para manter o menu ativo até o usuário decidir sair
    while True:
        # Solicita ao usuário que escolha uma opção do menu
        opcao = input("Escolha uma opção: ")
        # Pesquisa por modelo
        if opcao == '1':
            termo = input("Digite o modelo: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa()   # Chama a função que retorna o dicionário de camisas cadastradas
            pesquisar_camisa(table_camisas, termo)  # Realiza a pesquisa pelo termo informado
        # Pesquisa por equipe
        elif opcao == '2':
            termo = input("Digite a equipe: ")  # Recebe o termo de pesquisa
            pesquisar_equipe(EquipesCadastradas, termo)  # Realiza a pesquisa pelo termo informado nas equipes
        # Pesquisa por marca
        elif opcao == '3':
            termo = input("Digite a marca: ")  # Recebe o termo de pesquisa
            pesquisar_equipe(EquipesCadastradas, termo)  # Realiza a pesquisa pelo termo informado nas equipes
        # Pesquisa por cor
        elif opcao == '4':
            termo = input("Digite a cor: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa()  # Chama a função que retorna o dicionário de camisas cadastradas
            pesquisar_camisa(table_camisas, termo)  # Realiza a pesquisa pelo termo informado
        # Pesquisa por tamanho
        elif opcao == '5':
            termo = input("Digite o tamanho: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa()  # Chama a função que retorna o dicionário de camisas cadastradas
            pesquisar_camisa(table_camisas, termo)  # Realiza a pesquisa pelo termo informado
        # Pesquisa por múltiplos requisitos
        elif opcao == '6':
            modelo = input("Modelo (ou Enter para ignorar): ")  # Recebe o termo para modelo
            cor = input("Cor (ou Enter para ignorar): ")        # Recebe o termo para cor
            tamanho = input("Tamanho (ou Enter para ignorar): ")# Recebe o termo para tamanho
            table_camisas = CadastroCamisa()  # Chama a função que retorna o dicionário de camisas cadastradas
            resultados = []  # Lista para armazenar os resultados encontrados
            for modelo_camisa, detalhes in table_camisas.items():  # Percorre todas as camisas cadastradas
                if (modelo and modelo.lower() not in modelo_camisa.lower()):  # Se modelo foi informado e não bate, pula
                    continue
                if (cor and cor.lower() not in detalhes.get('Cor', '').lower()):  # Se cor foi informada e não bate, pula
                    continue
                if (tamanho and tamanho.lower() not in detalhes.get('Tamanho', '').lower()):  # Se tamanho foi informado e não bate, pula
                    continue
                resultados.append({modelo_camisa: detalhes})  # Adiciona ao resultado se todos os filtros baterem
            print("Resultados da pesquisa:", resultados)  # Exibe os resultados encontrados
        # Sai do menu de pesquisa
        elif opcao == '0':
            print("Saindo do menu de pesquisa...")  # Mensagem de saída
            break  # Sai do loop e encerra a função
        # Se o usuário digitar uma opção inválida
        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro
    
# Quiz utilizando o console para utilização
"""
Este é um programa de quiz de futebol que usa a API-FOOTBALL (https://rapidapi.com/api-sports/api/api-football/details). 
Para obter dados sobre jogadores de várias ligas de futebol.
O usuário pode escolher a liga e o ano do campeonato, e o programa irá gerar perguntas sobre os jogadores dessa liga e ano.
As categorias do quiz incluem 'artilheiro', 'assistências' e 'cartões amarelos'.
"""
# Importando as bibliotecas necessárias
import requests # https://pypi.org/project/requests/
import random # https://docs.python.org/pt-br/3/library/random.html
import json # https://docs.python.org/3/library/json.html
import os # https://docs.python.org/3/library/os.html
import datetime # https://docs.python.org/3/library/datetime.html

# Inicializando variaveis
categorias = ['artilharia', 'assistências', 'cartões amarelos']
acertos = 0
# Embaralhando as categorias para garantir que a ordem seja aleatória
random.shuffle(categorias)
ligas = {
    "Premier League": {
        "ID": 39,
        "URL": "https://media.api-sports.io/football/leagues/39.png"
    },
    "Brasileirão": {
        "ID": 71,
        "URL": "https://media.api-sports.io/football/leagues/71.png"
    },
    "Serie A": {
        "ID": 135,
        "URL": "https://media.api-sports.io/football/leagues/135.png"
    },
    "La Liga": {
        "ID": 140,
        "URL": "https://media.api-sports.io/football/leagues/140.png"
    },
    "Ligue 1": {
        "ID": 61,
        "URL": "https://media.api-sports.io/football/leagues/61.png"
    },
    "Bundesliga": {
        "ID": 78,
        "URL": "https://media.api-sports.io/football/leagues/218.png"
    },
    "Champions League": {
        "ID": 2,
        "URL": "https://media.api-sports.io/football/leagues/2.png"
    },
    "Libertadores": {
        "ID": 13,
        "URL": "https://media.api-sports.io/football/leagues/13.png"
    }
}

def manipulacao_txt(categoria_quiz, user_choice, resultado):

    with open(caminho_arquivo, 'a', encoding='utf-8') as adicionar:
            adicionar.write(f'Nome do usuário: {nome}\n')
            adicionar.write(f'Liga escolhida: {liga}\n')
            adicionar.write(f'Ano escolhido: {ano}\n')
            adicionar.write(f'Categoria atual: {categoria_quiz}\n')
            adicionar.write(f'Opções:\n')
            adicionar.write(f'1. {random_names[0]}\n')
            adicionar.write(f'2. {random_names[1]}\n')
            adicionar.write(f'3. {random_names[2]}\n')
            adicionar.write(f'4. {random_names[3]}\n')
            adicionar.write(f'A resposta escolhida foi {user_choice}\n')
            adicionar.write(f'A resposta está {resultado}!\n')

def criar_arquivo_com_hora(nome_base):
    """
    Cria um arquivo de texto com o nome base concatenado com a hora atual,
    dentro da pasta 'log' no diretório atual.

    Args:
        nome_base (str): Nome base para o arquivo (sem extensão).
    """
    try:
        # Obtém a hora atual
        hora_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Concatena a hora ao nome base
        nome_arquivo = f"{nome_base}_{hora_atual}.txt"

        # Obtém o caminho completo do diretório atual
        diretorio_atual = os.getcwd()

        # Caminho completo para a pasta 'log'
        caminho_log = os.path.join(diretorio_atual, "assets", "log")

        # Cria a pasta 'log' se ela não existir
        if not os.path.exists(caminho_log):
            os.makedirs(caminho_log)

        # Caminho completo para o novo arquivo dentro da pasta 'log'
        global caminho_arquivo
        caminho_arquivo = os.path.join(caminho_log, nome_arquivo)

        # Cria o arquivo vazio
        with open(caminho_arquivo, 'w') as arquivo:
            print(f"Arquivo '{nome_arquivo}' criado com sucesso em {caminho_log}")
            print()

    except Exception as erro:
        print(f"Erro ao criar o arquivo: {erro}")

# Exemplo de uso da função
nome_base_do_arquivo = "Chute_Certeiro_not_interface"
criar_arquivo_com_hora(nome_base_do_arquivo)

def quiz():
    
    while True:
        global nome
        nome = input('Informe o seu nome por favor: ').title().strip()
        if nome:
            break
        else:
            print("Você não informou o seu nome!")
        

    print("Ligas disponíveis: " + ", ".join(ligas.keys()))



    while True:
        global liga
        liga = input("Qual liga você deseja para o quiz? ").title().strip()
        if liga in ligas:
            break
        print("Liga inválida. Por favor, escolha uma das ligas disponíveis.")

    while True:
        global ano
        ano = int(input("Qual ano você deseja (entre 2016 e 2023)? "))
        if 2016 <= ano <= 2023:
            break
        print("Ano inválido. Por favor, escolha um ano entre 2016 e 2023.")

    global acertos
    
    for categoria in categorias:

        liga_escolhida = ligas[liga]["ID"]
        ano_escolhido = ano

        if categoria == 'artilharia':
            busca_api = 'topscorers'
        elif categoria == 'assistências':
            busca_api = 'topassists'
        elif categoria == 'cartões amarelos':
            busca_api = 'topyellowcards'

        url = f"https://api-football-v1.p.rapidapi.com/v3/players/{busca_api}"
        querystring = {"league": str(liga_escolhida), "season": str(ano_escolhido)}
        headers = {
            "X-RapidAPI-Key": "06f0c1d958mshcd70f7d1495b050p1b4cb5jsnd9f5e358c544",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")
            return
    
        try:
            data = response.json()
            all_players = data['response']
            ...
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar os dados: {e}")
            return

        all_players = data['response']

        if categoria == 'artilharia':
            question = "Quem é o artilheiro do campeonato?"
            all_names = [(player['player']['name'], player['statistics'][0]['goals']['total']) for player in all_players]
        elif categoria == 'assistências':
            question = "Quem fez mais assistências?"
            all_names = [(player['player']['name'], player['statistics'][0]['goals'].get('assists', 0)) for player in all_players if 'goals' in player['statistics'][0] and isinstance(player['statistics'][0]['goals'].get('assists', 0), int)]
        else:
            question = "Quem tem mais cartões amarelos?"
            all_names = [(player['player']['name'], player['statistics'][0]['cards']['yellow']) for player in all_players]

        if len(all_names) < 4:
            raise ValueError("Não há jogadores suficientes para formar o quiz.")

        all_names.sort(key=lambda x: x[1], reverse=True)
        correct_name = all_names[0][0]
        global random_names
        random_names = random.sample(all_players, 4)
        random_names = [player['player']['name'] for player in random_names]

        if correct_name not in random_names:
            random_names.pop()
            random_names.append(correct_name)

        random.shuffle(random_names)

        print(f"{question}")

        for i, op in enumerate(random_names, 1):
            print(f"{i}. {op}")


        while True:
            resposta = int(input("Escolha a opção correta (1-4): "))
            if resposta not in [1, 2, 3, 4]:
                print("Resposta inválida. Por favor, escolha um número entre 1 e 4.")
            else:
                break

        if random_names[resposta-1] == correct_name:
            manipulacao_txt(categoria, resposta, "correta!")
            acertos +=1
            print("Resposta correta!")

        else:
            manipulacao_txt(categoria, resposta, f"incorreta a resposta erá {correct_name}")
            print(f"Resposta errada. A resposta correta era: {correct_name}")
    
    if acertos > 1:
        print(f"Parabéns {nome} você acertou {acertos} questões")
        with open(caminho_arquivo, 'a') as adicionar:
            adicionar.write(f'Parabéns {nome} você acertou {acertos} questões\n')
    else:
        print(f"{nome} você acertou {acertos} questões\n")
        with open(caminho_arquivo, 'a') as adicionar:
            adicionar.write(f'{nome} você acertou {acertos} questões\n')

quiz()
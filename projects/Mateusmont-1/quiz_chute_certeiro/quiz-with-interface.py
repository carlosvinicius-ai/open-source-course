"""
Este é um programa de quiz de futebol que usa a API-FOOTBALL (https://rapidapi.com/api-sports/api/api-football/details). 
Para obter dados sobre jogadores de várias ligas de futebol.
O usuário pode escolher a liga e o ano do campeonato, e o programa irá gerar perguntas sobre os jogadores dessa liga e ano.
As categorias do quiz incluem 'artilheiro', 'assistências' e 'cartões amarelos'.
"""
# Importando as bibliotecas necessárias
import flet as ft # https://flet.dev/docs/
import requests # https://pypi.org/project/requests/
import random # https://docs.python.org/pt-br/3/library/random.html
import json # https://docs.python.org/3/library/json.html
import time # https://docs.python.org/3/library/time.html
import os # https://docs.python.org/3/library/os.html
import datetime # https://docs.python.org/3/library/datetime.html
"""
Pode ser necesserio executar no terminal os comando
pip install Flet
pip install requests
"""

# Inicialização das variáveis
categorias = ['artilheiro', 'assistências', 'cartões amarelos'] # Definindo as categorias do quiz
random.shuffle(categorias) # Embaralhando as categorias para garantir que a ordem seja aleatória
categoria_atual = 0 # Definindo a categoria atual como a primeira da lista embaralhada
acertos = 0 # Inicializando a contagem de acertos

# Dicionário contendo as ligas de futebol disponíveis para o quiz
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

# Função principal que inicia o programa
def main(page: ft.Page):
    page.title = 'QUIZ - CHUTE CERTEIRO'  # Título da página
    page.bgcolor = ft.colors.BLACK  # Cor de fundo da página
    page.window_maximized = True  # Maximizar a janela
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical ao centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal ao centro
    page.scroll = ft.ScrollMode.AUTO
    
    solicitar_nome(page)  # Chamar a função para solicitar o nome do usuário

# Função para solicitar o nome do usuário
def solicitar_nome(page, *_):
    # Define a cor de fundo da página como preto
    page.bgcolor = ft.colors.BLACK

    # Função interna que é chamada quando o botão é clicado
    def btn_click(e):
        # Verifica se o campo de texto está vazio
        if not txt_name.value:
            # Se estiver vazio, exibe uma mensagem de erro
            txt_name.error_text = "Por favor insira seu nome!"
            # Atualiza a página para mostrar a mensagem de erro
            page.update()
        else:
            # Se o campo de texto não estiver vazio, declara a variável global nome_usuario
            global nome_usuario
            # Armazena o nome do usuário na variável global
            nome_usuario = txt_name.value.title().strip()
            # Chama a função mostrar_ligas
            mostrar_ligas(page)

    # Cria um campo de texto para o usuário inserir seu nome
    txt_name = ft.TextField(label="Seu nome!", text_align='center', width='300')

    # Cria um container para o menu
    menu = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor="#7586a4",
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            ft.Text(value="QUIZ - CHUTE CERTEIRO", size= 40, color="white")
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                    src="/images/logo.png",
                    width=300,
                    height=300,
                        )
                    ]
                ),
            ]
        )
    )

    # Cria um container para o campo de texto e o botão
    nome = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            txt_name
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            ft.ElevatedButton(
                                text='value',
                                content=ft.Column([
                                ft.Text(value='Confirmar', size=30, color="black"),]),
                                on_click=btn_click)
                        )
                    ],
                )
            ]
        )
    )

    # Cria o layout da página com o menu e o container do nome
    layout = ft.Container(
        width=1000,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                menu,
                nome,
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

    # Atualiza a página
    page.update


# Função para mostrar as ligas disponíveis
def mostrar_ligas(page):

    # Define a cor de fundo da página como preto
    page.clean()

    # Função interna para lidar com o clique do botão
    def on_button_click(e, liga_id):
        global liga_selecionada  # Declara a variável global liga_selecionada
        liga_selecionada = liga_id  # Armazena o ID da liga selecionada na variável global
        mostrar_anos(page)  # Chama a função mostrar_anos para atualizar a página com os anos disponíveis para a liga selecionada

    # Lista para armazenar as linhas de botões
    linhas_de_botoes = []

    # Itera sobre todas as ligas disponíveis
    for nome_liga, dados_liga in ligas.items():
        # Cria um botão personalizado com a imagem da liga e o nome da liga
        botao_liga = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Row([
                            ft.Image(src=dados_liga['URL'], width=80, height=80),
                            ft.Text(value=nome_liga,size=30, color='black')
                        ]),
                        on_click=lambda e, liga_id=dados_liga["ID"]: on_button_click(e, liga_id),
                        width=400
                    )
                )
            ]
        )
        
        linhas_de_botoes.append(botao_liga)

    def botoes_liga():
         # Adiciona todas as linhas de botões à página
        return linhas_de_botoes # Adiciona a linha de botões à página

    # Cria um container para o menu
    menu = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor="#7586a4",
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            ft.Text(value="ESCOLHA O CAMPEONATO", size= 40, color="white")
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                    src="/images/logo.png",
                    width=300,
                    height=300,
                        )
                    ]
                ),
            ]
        )
    )

    # Cria um container para o campo de texto e o botão
    escolhe_campeonato = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            *botoes_liga()
                        ]
                    )
                )
            ]
        )
    )


    # Cria o layout da página com o menu e o container do nome
    layout = ft.Container(
        width=1300,
        # height=900,
        margin=ft.margin.all(20),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            columns=15,
            spacing=0,
            run_spacing=0,
            controls=[
                menu,
                escolhe_campeonato,
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

    # Atualiza a página
    page.update

# Função para mostrar os anos
def mostrar_anos(page):
    # Limpa a página
    page.clean()

    # Função para lidar com o clique no botão
    def on_button_click(e, ano):
        global ano_selecionado
        # Define o ano selecionado
        ano_selecionado = ano
        # Inicia o quiz
        start_quiz(page, categorias[categoria_atual])

    # Lista para armazenar as linhas de botões
    linhas_de_botoes = []

    # Define os anos
    anos = list(range(2016, 2024))
    # Itera sobre os anos
    for ano in anos:
        # Cria um botão para cada ano   
        botao_ano = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    ft.ElevatedButton(
                        content=ft.Column([
                            ft.Text(value=ano,size=30, color='black',text_align='center'),
                        ]),
                        on_click=lambda e, a =ano: on_button_click(e, a),
                        width=200
                    )
                )
            ]
        )
        
        # Adiciona o botão à lista temporária
        linhas_de_botoes.append(botao_ano)

    def botoes_ano():
         # Adiciona todas as linhas de botões à página
        return linhas_de_botoes # Adiciona a linha de botões à página
    
    # Cria um container para o menu
    menu = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor="#7586a4",
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            ft.Text(value="ESCOLHA O ANO", size= 40, color="white")
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                    src="/images/logo.png",
                    width=300,
                    height=300,
                        )
                    ]
                ),
            ]
        )
    )

    # Cria um container para o campo de texto e o botão
    escolhe_ano = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            *botoes_ano()
                        ]
                    )
                )
            ]
        )
    )


    # Cria o layout da página com o menu e o container do nome
    layout = ft.Container(
        width=1300,
        # height=900,
        margin=ft.margin.all(20),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            columns=15,
            spacing=0,
            run_spacing=0,
            controls=[
                menu,
                escolhe_ano,
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

    # Atualiza a página
    page.update

# Função para iniciar o quiz na interface gráfica
def start_quiz(page, category):  

    # Definindo a categoria do quiz globalmente
    global categoria_quiz
    categoria_quiz = str(category)

    # Limpar a interface
    page.clean()

    # Chamada da função que consome a API de futebol
    api_futebol()

    # Definindo globalmente a resposta correta e os nomes aleatórios
    global correct_answer
    global random_names
    # Gerando o quiz com base na categoria
    correct_answer, random_names = generate_quiz(category)
    
    # Verificando o nome da liga escolhida pelo usuário
    verificar_liga()

    # Chamada da função que exibe a tela do quiz
    mostrar_quiz(page)
# Função para buscar dados da API de futebol
def api_futebol():
    # Verifica a categoria do quiz e define a busca na API
    if categoria_quiz == 'artilheiro':
        busca_api = 'topscorers'
    elif categoria_quiz == 'assistências':
        busca_api = 'topassists'
    else:
        busca_api = 'topyellowcards'
    
    # Define a URL da API
    url = f"https://api-football-v1.p.rapidapi.com/v3/players/{busca_api}"

    # Define os parâmetros da consulta
    querystring = {"league": str(liga_selecionada), "season": str(ano_selecionado)}

    # Define os cabeçalhos da requisição
    headers = {
	    "X-RapidAPI-Key": "06f0c1d958mshcd70f7d1495b050p1b4cb5jsnd9f5e358c544",
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    # Fazendo uma requisição GET para a URL especificada
    response = requests.get(url, headers=headers, params=querystring)

    # Verificando se a requisição foi bem sucedida
    if response.status_code != 200:
        print(f"Erro na requisição: {response.status_code}")
        return

    # Definindo a variável global 'data'
    global data

    # Convertendo a resposta da requisição para JSON
    data = response.json()

    # Verificando se a resposta contém a chave 'response'
    if 'response' not in data:
        print("Dados esperados não estão presentes na resposta da API")
        return

# Definindo a função 'generate_quiz'
def generate_quiz(category):
    # Definindo a variável global 'all_names'
    global all_names
    
    # Obtendo todos os jogadores da resposta
    all_players = data['response']

    # Verificando se os dados dos jogadores estão presentes
    for player in all_players:
        if 'player' not in player or 'name' not in player['player']:
            print("Dados do jogador estão ausentes ou incompletos")
            return
    
    # Preparando os dados para o quiz com base na categoria escolhida
    if category == 'artilheiro':
        all_names = [(player['player']['name'], player['statistics'][0]['goals']['total']) for player in all_players]
    elif category == 'assistências':
        all_names = [(player['player']['name'], player['statistics'][0]['goals']['assists']) for player in all_players]
    else:  # cartões amarelos
        all_names = [(player['player']['name'], player['statistics'][0]['cards']['yellow']) for player in all_players]

    # Ordenando os nomes e pegando o nome correto
    all_names.sort(key=lambda x: x[1], reverse=True)
    
    correct_name = all_names[0][0]
    
    # Escolhendo 4 nomes aleatórios
    global random_names
    random_names = random.sample(all_players, 4)
    random_names = [player['player']['name'] for player in random_names]
    
    # Certificando-se de que o nome correto está na lista
    if correct_name not in random_names:
        random_names.pop()
        random_names.append(correct_name)
    
    # Embaralhando a lista de nomes
    random.shuffle(random_names)
    random.shuffle(random_names)
    
    # Embaralha as respostas
    random.shuffle(data['response'])
    
    return correct_name, random_names

# Definindo a função 'verificar_liga'
def verificar_liga():
    # Declarando 'chave_correspondente' como uma variável global
    global chave_correspondente
    global url_liga

    # Iterando sobre cada item no dicionário 'ligas'
    for liga, info in ligas.items():
        # Verificando se o ID da liga atual corresponde à 'liga_selecionada'
        if info["ID"] == liga_selecionada:
            # Se corresponder, atribuímos o nome da liga à 'chave_correspondente'
            chave_correspondente = liga
            # Atribuímos a URL da liga à 'url_liga'
            url_liga = info['URL']
            # E interrompemos o loop
            break
        else:
            # Se não corresponder, definimos 'chave_correspondente' como 'Não encontrada'
            chave_correspondente = 'Não encontrada'

# Definindo a função 'check_answer'
def check_answer(page, user_choice, correct_answer):   
    # Definindo as variáveis globais
    global categoria_atual
    global acertos

    # Limpando a Interface
    page.clean()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical ao centro
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal ao centro
    
    def texto_tela(page, imagem:bool, texto: str,  *_: str):
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical ao centro
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.Page.scroll
        if imagem:
            page.add(ft.Image(src=f"/images/logo.png", height=300, width=300))
            
        layout = ft.Container(content=ft.Text(texto, color='White', size=40))
        page.add(layout)

        if _:
            for resto in _:
                page.add(ft.Container(content=ft.Text(resto, color='White', size=40)))    
        
    # Adicionando um texto na interface
    texto_tela(page, False, "Verificando sua resposta aguarde!")

    # Aguardando 2 segundos
    time.sleep(2)

    # Limpando a Interface
    page.clean()

    # Verificando se a resposta do usuário está correta
    if user_choice == correct_answer:
        # Incrementando a variável 'acertos'
        acertos += 1
        # Chamando a função 'manipulacao_txt' com a resposta correta
        manipulacao_txt(user_choice, 'correta')
        # Adicionando um texto na interface
        texto_tela(page, False,"Sua resposta está correta!")

    else:
        # Chamando a função 'manipulacao_txt' com a resposta errada
        manipulacao_txt(user_choice, f'errada a resposta correta era {correct_answer}')
        # Adicionando um texto na interface
        texto_tela(page, False,f"Sua resposta está incorreta! A resposta era {correct_answer}!")

    # Aguardando 2 segundos
    time.sleep(2)

    # Incrementando a categoria atual e iniciando o próximo quiz se houver mais categorias
    categoria_atual += 1
    if categoria_atual < len(categorias):
        # Chamando a função 'start_quiz' com a próxima categoria
        start_quiz(page, categorias[categoria_atual])
    else:
        # Limpando a interface
        page.clean()

        texto1 = "Fim do Quiz!"
        texto2 = "Você respondeu todas as categorias"
        # Verificando se o usuário acertou mais de uma questão
        if acertos >1:
            # Adicionando um texto na interface
            texto3= f"Parabéns {nome_usuario} você acertou {acertos} de {len(categorias)} questões"
            texto_tela(page, True, texto1, texto2, texto3)  
            # Adicionando o resultado do quiz no arquivo 'resposta_quiz.txt'
            with open(caminho_arquivo, 'a') as adicionar:
                adicionar.write(f'Parabéns{nome_usuario} você acertou: {acertos} de {len(categorias)} questões\n')

        else:
            # Adicionando um texto na interface
            texto3= f"{nome_usuario} você acertou {acertos} de {len(categorias)} questões"
            texto_tela(page, True, texto1, texto2, texto3)
            # Adicionando o resultado do quiz no arquivo 'resposta_quiz.txt'
            with open(caminho_arquivo, 'a') as adicionar:
                adicionar.write(f'{nome_usuario} você acertou: {acertos} de {len(categorias)} questões\n')

        # Aguardando 5 segundos
        time.sleep(5)
        # Fechando a janela
        page.window_close()
        
# Definindo a função 'mostrar_quiz'
def mostrar_quiz(page):
    # Função para lidar com o clique do botão
    def on_button_click(e, jogador):
        global jogador_selecionado
        # Atualiza o jogador selecionado
        jogador_selecionado = jogador
        # Chama a função de confirmação
        confirmacao(page)
        
    # Limpar a interface
    page.clean()
    page.scroll = ft.ScrollMode.AUTO
    # Verifica a categoria do quiz e define o texto da pergunta
    if categoria_quiz == 'artilheiro':
        texto_quiz = f'Artilheiro de {ano_selecionado}?'
        texto_quiz2 = ""
    elif categoria_quiz == 'assistências':
        texto_quiz = f'Lider de assistências'
        texto_quiz2 = f' de {ano_selecionado}?'
    else:
        texto_quiz = f'Lider de cartões '
        texto_quiz2 = f'amarelos de {ano_selecionado}?'
    
    if texto_quiz2 == "":
        mostrar_texto = ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Row([
                                ft.Text(value=texto_quiz, size= 40, color="white"),
                            ])  
                        )
                    ]
                ),
    else:
        mostrar_texto = ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Row([
                                ft.Text(value=texto_quiz, size= 40, color="white"),
                            ])  
                        )
                    ]
                ),ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Row([
                                ft.Text(value=texto_quiz2, size= 40, color="white"),
                            ])  
                        )
                    ]
                ),

    # Lista para armazenar as linhas de botões
    linhas_de_jogadores = []

    # Itera sobre todas as ligas disponíveis
    for player in data['response']:
        if player['player']['name'] in random_names:
        # Cria um botão personalizado com a imagem do jogador e o nome dele
            botao_jogador = ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        ft.ElevatedButton(
                            content=ft.Row([
                                ft.Image(src=player['player']['photo'], width=85, height=85),
                                ft.Text(player['player']['name'], size=30, color='black')
                            ]),
                            on_click=lambda e, jogador=player['player']['name']: on_button_click(e, jogador),
                            width=350,
                            height=100
                        )
                    )
                ]
            )
        
            linhas_de_jogadores.append(botao_jogador)
            
    def botoes_jogador():
        return linhas_de_jogadores # Adiciona a linha de botões à página

    # Cria um container para o menu
    menu = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor="#7586a4",
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            *mostrar_texto
                        ]
                    )
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                    src=url_liga,
                    width=300,
                    height=300,
                        )
                    ]
                ),
            ]
        )
    )

    # Cria um container para o campo de texto e o botão
    escolhe_jogador = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            *botoes_jogador()
                        ]
                    )
                )
            ]
        )
    )


    # Cria o layout da página com o menu e o container do nome
    layout = ft.Container(
        width=1300,
        # height=900,
        margin=ft.margin.all(20),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            columns=15,
            spacing=0,
            run_spacing=0,
            controls=[
                menu,
                escolhe_jogador,
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

    # Atualiza a página
    page.update
            
            

# Definindo a função 'confirmacao'
def confirmacao(page):
    
    # Definindo a função 'retorna_quiz' que chama a função 'mostrar_quiz'
    def retorna_quiz(e):
        mostrar_quiz(page)

    # Definindo a função 'confirmado' que chama a função 'check_answer'
    def confirmado(e):
        check_answer(page, jogador_selecionado, correct_answer)

    # Limpa a página
    page.clean()
    
    # Adiciona um texto à página
    mostrar_texto = ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Row([
                                ft.Text(value="Você tem certeza", size= 40, color="white"),
                            ])  
                        )
                    ]
                ),ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            content=ft.Row([
                                ft.Text(value="da sua resposta ?", size= 40, color="white"),
                            ])  
                        )
                    ]
                ),
    
    # Cria um container para o menu
    menu = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor="#7586a4",
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            *mostrar_texto
                        ]
                    )
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                    src="/images/logo.png",
                    width=300,
                    height=300,
                        )
                    ]
                ),
            ]
        )
    )

    # Cria um container para o campo de texto e o botão
    escolhe_corfimacao = ft.Container(
        col={'xs': 12, 'md': 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Row([
        # Botão 'Sim' que chama a função 'confirmado' quando clicado
                                ft.ElevatedButton(content=ft.Column([
                                    ft.Text(value='Sim', size=30, color="black"),
                                    ]),        
                                on_click=confirmado),
        # Botão 'Não' que chama a função 'retorna_quiz' quando clicado
                                ft.ElevatedButton(content=ft.Column([
                                    ft.Text(value='Não', size=30, color="black"),
                                    ]),        
                                    on_click=retorna_quiz),
                                ],alignment= ft.MainAxisAlignment.CENTER,)
                            ]
                        )
                    )
                ]
            )
        )
    

    # Cria o layout da página com o menu e o container do nome
    layout = ft.Container(
        width=1300,
        # height=900,
        margin=ft.margin.all(20),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.WHITE),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            columns=15,
            spacing=0,
            run_spacing=0,
            controls=[
                menu,
                escolhe_corfimacao,
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

    # Atualiza a página
    page.update

# Função para manipular o arquivo de texto com as respostas do quiz
def manipulacao_txt(user_choice, resultado):

    with open(caminho_arquivo , 'a', encoding='utf-8') as adicionar:
            adicionar.write(f'Nome do usuário: {nome_usuario}\n')
            adicionar.write(f'Liga escolhida: {chave_correspondente}\n')
            adicionar.write(f'Ano escolhido: {ano_selecionado}\n')
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

    except Exception as erro:
        print(f"Erro ao criar o arquivo: {erro}")

# Exemplo de uso da função
nome_base_do_arquivo = "Chute_Certeiro"
criar_arquivo_com_hora(nome_base_do_arquivo)

# Iniciando o aplicativo com a função 'main' como alvo
ft.app(target=main, assets_dir="assets",) #caso queira rodar a aplicação WEB acrescentar view=ft.WEB_BROWSER

# importando a biblioteca para chamar a api
import requests
#importando a biblioteca para usar as informações da biblioteca
import json

# importando a biblioteca datetime para armazenar o dia e a hora da cotação
from datetime import datetime

# importando a bilbioteca random para pegar aleatoriamento o valor do dicionário
import random as rd

# importando biblioteca para adicionar a cada 30 seg uma informação na planilha
from time import sleep

# criando o arquivo cotação na pasta moedas
try:
    with open('D:/Python-Projetos/Pessoal/moedas_python/moedas/cotacao.csv', 'x') as base:
        base = base.write('moeda,valor,data,hora\n')

except FileExistsError:
    pass

# criando o dicionário para poder utilizar qual moeda eu quiser
moedas = {
    'Dirham dos Emirados': ['AED-BRL', 'AEDBRL'],
    'Peso Argentino': ['ARS-BRL', 'ARSBRL'],
    'Dólar Australiano': ['AUD-BRL', 'AUDBRL'],
    'Boliviano': ['BOB-BRL', 'BOBBRL'],
    'Bitcoin': ['BTC-BRL', 'BTCBRL'],
    'Dólar Canadense': ['CAD-BRL', 'CADBRL'],
    'Franco Suíço': ['CHF-BRL', 'CHFBRL'],
    'Peso Chileno': ['CLP-BRL', 'CLPBRL'],
    'Yuan Chinês': ['CNY-BRL', 'CNYBRL'],
    'Peso Colombiano': ['COP-BRL', 'COPBRL'],
    'Coroa Dinamarquesa': ['DKK-BRL', 'DKKBRL'],
    'Dogecoin': ['DOGE-BRL', 'DOGEBRL'],
    'Ethereum': ['ETH-BRL', 'ETHBRL'],
    'Euro': ['EUR-BRL', 'EURBRL'],
    'Libra Esterlina': ['GBP-BRL', 'GBPBRL'],
    'Dólar de Hong Kong': ['HKD-BRL', 'HKDBRL'],
    'Novo Shekel Israelense': ['ILS-BRL', 'ILSBRL'],
    'Rúpia Indiana': ['INR-BRL', 'INRBRL'],
    'Iene Japonês': ['JPY-BRL', 'JPYBRL'],
    'Litecoin': ['LTC-BRL', 'LTCBRL'],
    'Peso Mexicano': ['MXN-BRL', 'MXNBRL'],
    'Coroa Norueguesa': ['NOK-BRL', 'NOKBRL'],
    'Dólar Neozelandês': ['NZD-BRL', 'NZDBRL'],
    'Sol do Peru': ['PEN-BRL', 'PENBRL'],
    'Zlóti Polonês': ['PLN-BRL', 'PLNBRL'],
    'Guarani Paraguaio': ['PYG-BRL', 'PYGBRL'],
    'Rublo Russo': ['RUB-BRL', 'RUBBRL'],
    'Riyal Saudita': ['SAR-BRL', 'SARBRL'],
    'Coroa Sueca': ['SEK-BRL', 'SEKBRL'],
    'Dólar de Cingapura': ['SGD-BRL', 'SGDBRL'],
    'Baht Tailandês': ['THB-BRL', 'THBBRL'],
    'Nova Lira Turca': ['TRY-BRL', 'TRYBRL'],
    'Dólar Taiuanês': ['TWD-BRL', 'TWDBRL'],
    'Dólar Americano': ['USD-BRL', 'USDBRL'],
    'Peso Uruguaio': ['UYU-BRL', 'UYUBRL'],
    'Bolívar Venezuelano': ['VEF-BRL', 'VEFBRL'],
    'XRP': ['XRP-BRL', 'XRPBRL'],
    'Rand Sul-Africano': ['ZAR-BRL', 'ZARBRL']
}

print(f'{' CONVERSOR DE MOEDA ':-^30}')
print('')

# mostrando as opções de moedas no nosso dicionário para o nosso usuário
for moeda in moedas.keys():
    print(f'Digite {moeda} para trazer o valor dela em Real')


# repetindo para aceitar apenas quando o usuário digitar uma moeda que está em nosso dicionário

while True:
    converter = str(input('\nEscolha uma das opções acima (Digite aleatório para caso deseje que seja aleatório): ')).strip().title()
    
    if converter ==  'Aleatório':
        # escolhendo aleatóriamente entre a lista de itens
        converter = rd.choice(list(moedas.keys()))

    elif converter not in moedas:
        continue

    break


#repetindo para adicionar a nossa planilha
vezes_adicionar = int(input('Digite o número de vezes que deseja adicionar: (intervalo de 30s) '))

for i in range(vezes_adicionar):

    converter = rd.choice(list(moedas.keys()))

    # chamando a api de acordo com a moeda escolhida
    atual = requests.get(f'https://economia.awesomeapi.com.br/last/{moedas[converter][0]}')

    # convertendo em json para poder buscar a informação que desejamos
    atual = atual.json()

    # buscando o BID da moeda escolhida
    # BID é a conversão atual da moeda
    valor_atual = atual[moedas[converter][1]]['bid']

    # pegando a data atual e formatando ela
    data_agora = datetime.now()
    data_atual = data_agora.strftime('%d/%m/%Y')
    hora_atual = data_agora.strftime('%H:%M:%S')



    # armazenando a data atual no nosso arquivo txt
    with open('D:/Python-Projetos/Pessoal/moedas_python/moedas/cotacao.csv', 'a') as adicionar:
        adicionar = adicionar.write(f'{converter},{float(valor_atual):.2f},{data_atual},{hora_atual}\n')


    # mostrando para o usuário o valor armazenado

    print(f'O valor armazenado na nossa tabela foi: \nA moeda {converter} está valendo R${float(valor_atual):.2f} no dia e hora {data_atual}')

    sleep(5)
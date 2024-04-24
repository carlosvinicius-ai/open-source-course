import sys
#interagir com linhas de comando
import os as sistema
#interação com o systema operacional, usudo para pegar o usuário logado
from selenium import webdriver
#permite controlar o navegador
from selenium.webdriver.edge.service import Service
#automação com o edge
from selenium.webdriver.support.ui import Select
#interação com elementos de select do html
from selenium.webdriver.common.by import By
#para encontrador elementos da pagina como ID, Name, Xpath
from selenium.webdriver.common.alert import Alert
#interação com as porcarias de popup
from selenium.common.exceptions import NoSuchElementException
#usada para enviar teclas
#from selenium.webdriver.common.keys import Keys
#usado para teclas especiais como TAB
from selenium.webdriver.support.ui import WebDriverWait
#condição para esperar o carregamento da pagina ou de elemento especifico
#from selenium.webdriver.support import expected_conditions as EC
#agardar o botão ou elemento estar clicavel
from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs
from time import sleep


# Corrigindo o caminho para o msedgedriver.exe
driver_path = r'C:/Projeto/GT_Pessoal/Scripts_Python/msedgedriver.exe'

# Configurando o serviço para utilizar o Edge Driver especificado
service = Service(executable_path=driver_path)
options = webdriver.EdgeOptions()
options = webdriver.EdgeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
prefs = {
    "profile.managed_default_content_settings.images": 2  # Isso desativa o carregamento de imagens
}
options.add_experimental_option("prefs", prefs)



def processa_linhas(cod, nome):
    # Atribui cada parte a variáveis e prepara as partes do texto para as variaveis
    routingId = cod
    userSftp = f'ABAST.{routingId}'
    b2bi = f'/backup/axway/EDI/1.ENVIO/4.ABASTECE/{routingId}'
    app_pickups = f'ABAST_{nome.upper()}'
    #app_pickups = f'ABAST_{nome.replace(" - ", "-").replace(" ","").upper()}'

    #Exibe os resultados
    print(f"codigo: {cod}")
    print(f"nome: {nome.upper()}")
    print(f"routingId: {routingId}")
    print(f"userSftp: {userSftp}")
    print(f"b2bi: {b2bi}")
    print(f"ABAST_: {app_pickups}")
    
    return routingId, userSftp, b2bi, app_pickups

# Checando se os argumentos foram passados corretamente
if len(sys.argv) < 3:
    print("Uso: python config_edi_B2Bi_novpn.py <usuario> <senha>")
    sys.exit(1)

# Atribuindo os argumentos às variáveis
login_ = sys.argv[1]
senha_ = sys.argv[2]

senha_user = "senha"
sftp_server = 'www.SemParar.com.br'
porta = xxxx
porta_axway = xxxx 

driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(10)  # Espera implícita de 10 segundos

#driver.get('https://localhost:6443')

#Função de logar
def logar():
    # Login
    login = driver.find_element(By.ID, "loginUserId")
    login.click()  # Assegure-se de que click() está sendo chamado com ()
    login.send_keys(login_)

    # Senha
    senha = driver.find_element(By.ID, "loginPassword")
    senha.send_keys(senha_)

    # Botão de Login
    logar = driver.find_element(By.ID, "N1006B")
    logar.click()
    driver.implicitly_wait(10)  # Espera implícita de 10 segundos

def config_properties():
#alterando nome do credenciado no propeties
    properties = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/table/tbody/tr[2]/td/div/a')
    properties.click()
    properties = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input')
    properties.click()
    properties.clear()
    properties.send_keys(nome)
    properties = driver.find_element(By.LINK_TEXT, "Save changes")
    properties.click()

#Excluindo existente e criando um novo
def config_routing_id():
    routing_id = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/table/tbody/tr[4]/td/div/a')
    routing_id.click()
    try:#apagando o abastece se existente
        routing_id = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/div[3]/table/tbody/tr[2]/td[1]/span/input')
        routing_id.click()
        # Aguarda e muda o foco para o alerta
        alert = Alert(driver)
        # Clica em "OK" no alerta/popup
        alert.accept()
        #para cancelar usar alert.dismiss()
        #selecionando para apagar
        routing_id = driver.find_element(By.LINK_TEXT, 'Delete')
        routing_id.click()
        alert.accept()

        #criando um novo routing id
        routing_id = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input')
        routing_id.clear()
        routing_id.send_keys(routingId)
        routing_id = driver.find_element(By.LINK_TEXT, "Add")
        routing_id.click()
        driver.implicitly_wait(5)  # Espera implícita de 5 segundos

    except NoSuchElementException:
        #criando um novo routing id
        routing_id = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input')
        routing_id.clear()
        routing_id.send_keys(routingId)
        routing_id = driver.find_element(By.LINK_TEXT, "Add")
        routing_id.click()
        driver.implicitly_wait(5)  # Espera implícita de 5 segundos

def new_trading_partners():
        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[3]/tbody/tr[2]/td/span/a')
        trading_partners.click()
        
        #Navegando entrejanelas
        driver.switch_to.window(driver.window_handles[1])

        sleep(2)
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[8]/td/table/tbody/tr/td[1]/input[1]')
        trading_partners.click()
        trading_partners = driver.find_element(By.LINK_TEXT, "Next »")
        trading_partners.click()
        
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr/td[1]/input')
        trading_partners.click()
        trading_partners = driver.find_element(By.LINK_TEXT, "Next »")
        trading_partners.click()
        
        #Configurando o SFTP settings site
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/input')
        trading_partners.click()
        trading_partners.send_keys(sftp_server)
        
        #Configurando o SFTP settings porta
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[2]/td[2]/input')
        trading_partners.click()
        trading_partners.clear()
        trading_partners.send_keys(porta)
        
        #Configurando o SFTP settings ditetorio
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/input')
        trading_partners.click()
        trading_partners.clear()
        trading_partners.send_keys('/' + userSftp + '/')
        
        #criando usuário e senha
        trading_partners = driver.find_element(By.ID, 'username')
        trading_partners.click()
        trading_partners.send_keys(userSftp)
        
        trading_partners = driver.find_element(By.ID, 'userPassword')
        trading_partners.click()
        trading_partners.send_keys(senha_user)
        
        trading_partners = driver.find_element(By.ID, 'passwordConfirmation')
        trading_partners.click()
        trading_partners.send_keys(senha_user)
        
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/input[5]')
        trading_partners.click()
        
        trading_partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/span/a')
        trading_partners.click()
        
        driver.switch_to.window(driver.window_handles[2])
        sleep(2)
        trading_partners = driver.find_element(By.LINK_TEXT, "Use key")
        trading_partners.click()
        
        driver.switch_to.window(driver.window_handles[1])
        
        trading_partners = driver.find_element(By.ID, 'next')
        trading_partners.click()
        
        trading_partners = driver.find_element(By.NAME, 'friendlyName')
        trading_partners.click()
        trading_partners.send_keys("ABASTECE_SFTP")
        
        trading_partners = driver.find_element(By.ID, 'finish')
        trading_partners.click()
        
        driver.switch_to.window(driver.window_handles[0])
        
        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[4]/tbody/tr[2]/td[2]/a')
        trading_partners.click()
        
        trading_partners = driver.find_element(By.LINK_TEXT, "Advanced")
        trading_partners.click()
        
        trading_partners = driver.find_element(By.NAME, "retries")
        trading_partners.click()
        trading_partners.clear()
        trading_partners.send_keys(60)
        
        
        trading_partners = driver.find_element(By.NAME, "sftpBlockSize")
        trading_partners.click()
        trading_partners.clear()
        trading_partners.send_keys(327680)
        
        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/span[2]/a')
        trading_partners.click()
        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[6]/div/a/img')
        trading_partners.click()
        
def new_trading_pickup():
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[3]/tbody/tr[2]/td/span/a')
        trading_pickup.click()
        driver.switch_to.window(driver.window_handles[1])
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[8]/td/table/tbody/tr/td[1]/input[1]')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Next »')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr/td[1]/input')
        trading_pickup.click()
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Next »')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.ID, 'senderAddressType1')
        trading_pickup.click()
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/span/a')
        trading_pickup.click()
        
        driver.switch_to.window(driver.window_handles[2])
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[3]/td[1]/span/input')
        trading_pickup.click()
        sleep(2)
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/span[1]/a')
        trading_pickup.click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        
        trading_pickup = driver.find_element(By.ID, 'next')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.ID, 'receiverAddressType1')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/span/a')
        trading_pickup.click()
        sleep(2)
        
        driver.switch_to.window(driver.window_handles[2])
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[1]/span/input')
        sleep(2)
        trading_pickup.click()
        
        sleep(2)
        trading_pickup = driver.find_element(By.LINK_TEXT, 'OK')
        trading_pickup.click()
        sleep(2)
        driver.switch_to.window(driver.window_handles[1])

        sleep(2)
        
        trading_pickup = driver.find_element(By.ID, 'next')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/input')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.ID, 'next')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td[2]/input')
        trading_pickup.click()
        trading_pickup.send_keys(sftp_server)
        
        trading_pickup = driver.find_element(By.ID, 'port')
        trading_pickup.click()
        trading_pickup.clear()
        trading_pickup.send_keys(porta)
        
        #criando usuário e senha
        trading_pickup = driver.find_element(By.ID, 'username')
        trading_pickup.click()
        trading_pickup.send_keys(userSftp)
        
        trading_pickup = driver.find_element(By.ID, 'userPassword')
        trading_pickup.click()
        trading_pickup.send_keys(senha_user)
        
        trading_pickup = driver.find_element(By.ID, 'passwordConfirmation')
        trading_pickup.click()
        trading_pickup.send_keys(senha_user)
        
        trading_pickup = driver.find_element(By.ID, 'valueCheckdebounce')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/span/a')
        trading_pickup.click()
        
        driver.switch_to.window(driver.window_handles[2])
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Use key')
        trading_pickup.click()
        
        driver.switch_to.window(driver.window_handles[1])
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Next »')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.NAME, 'friendlyName')
        trading_pickup.click()
        trading_pickup.send_keys(nome)
        
        trading_pickup = driver.find_element(By.ID, 'finish')
        trading_pickup.click()
        
        driver.switch_to.window(driver.window_handles[0])
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[4]/tbody/tr[2]/td[3]/a')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Directories')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/span[2]/table/tbody/tr/td/table/tbody/tr/td[2]/input')
        trading_pickup.click()
        trading_pickup.clear()
        trading_pickup.send_keys('/' + userSftp + '/mailbox')
        trading_pickup = driver.find_element(By.LINK_TEXT, "Advanced")
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.NAME, "sftpBlockSize")
        trading_pickup.click()
        trading_pickup.clear()
        trading_pickup.send_keys(327680)
        trading_pickup = driver.find_element(By.LINK_TEXT, "Save changes")
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[4]/tbody/tr[3]/td[3]/a')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Directories')
        trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/span[2]/table/tbody/tr/td/table/tbody/tr/td[2]/input')
        trading_pickup.click()
        trading_pickup.clear()
        trading_pickup.send_keys('mailbox')
        
        trading_pickup = driver.find_element(By.LINK_TEXT, 'Save changes')
        trading_pickup.click()

def config_trading_partners():
    #alterando TradingPartners
    trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[3]/table/tbody/tr[1]/td[13]/div/a/img')
    trading_partners.click()
    #entrar no partiner
    trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/a')
    trading_partners.click()
    #entrar no abastece
    trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/div/a/img')
    trading_partners.click()

    try:#apagando o abastece se existente
        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[4]/tbody/tr[2]/td[1]/span/input')
        trading_partners.click()
        #selecionando para apagar
        trading_partners_selecionar = driver.find_element(By.ID, 'userAction')
        select_objeto = Select(trading_partners_selecionar)
        select_objeto.select_by_value('deleteBP')

        trading_partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/span/span/a[1]')
        trading_partners.click()
        # Aguarda e muda o foco para o alerta
        alert = Alert(driver)
        # Clica em "OK" no alerta/popup
        alert.accept()
        #para cancelar usar alert.dismiss()
        new_trading_partners()

    except NoSuchElementException:
        #criando um partner
       new_trading_partners()
        
#configurar o trading pickup
def config_trading_pickup():
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[6]/div/a/img')
    trading_pickup.click()
        
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[2]/a')
    trading_pickup.click()
    
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[3]/table/tbody/tr[1]/td[9]/div/a/img')
    trading_pickup.click()
    
    try:#apagando o abastece se existente
        sleep(2)
        #trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[6]/div/a/img')
        #trading_pickup.click()
        sleep(2)
        #trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[2]/a')
        #trading_pickup.click()
        
        trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[4]/tbody/tr[1]/th[1]/a/input')
        trading_pickup.click()
        #selecionando para apagar
        trading_pickup_selecionar = driver.find_element(By.ID, 'userAction')
        select_objeto = Select(trading_pickup_selecionar)
        select_objeto.select_by_value('deleteBP')

        trading_pickup = driver.find_element(By.ID, 'selectedButton')
        trading_pickup.click()
        # Aguarda e muda o foco para o alerta
        alert = Alert(driver)
        # Clica em "OK" no alerta/popup
        alert.accept()
        #para cancelar usar alert.dismiss()
        new_trading_pickup()

    except NoSuchElementException:
        new_trading_pickup()

        #print('Tentando tab')
        #trading_partners.send_keys(Keys.TAB)
        #for _ in range(6):
            #trading_partners.send_keys(Keys.ARROW_DOWN)
        
        #trading_partners.click()
        
def fim():
    #Chamada da API
    client = ElevenLabs(
    api_key="7cca14c36c31fb428b03c649e3ae352e", # senha da api to ELEVEN_API_KEY
    )
    #envio da requisição
    audio = client.generate(
        text=f"{sistema.getlogin().replace('.', ' ')} já estou cansado de trabalhar por você, volte a trabalhar.",
        voice=Voice(
            voice_id='tS45q0QcrDHqHoaWdCDR',
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.3, use_speaker_boost=True)
        )
    )
    #reprodução da requisição
    play(audio)
    
with open('postos.txt', 'r') as arquivo:
    for linha in arquivo:
        
        driver.get(f'https://localhost:{porta_axway}')
        logar()
        # Lê o conteúdo do arquivo
        info = linha.upper().strip()
        # Divide o texto em partes vírgulas
        cod, nome = info.split(',', 1)
        #processa_linhas(cod, nome)
        routingId, userSftp, b2bi, app_pickups = processa_linhas(cod, nome)
        
        #entrar na Communities
        communities = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[6]/div/a/img')
        communities.click()
        communities = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[2]/a')
        communities.click()

        config_properties()

        config_routing_id()

        config_trading_partners()

        config_trading_pickup()
        
        porta_axway += 1
        
    fim()


# Espera explícita para o link do histórico estar visível e clicável
#link_historico = WebDriverWait(driver, 20).until(
 #   EC.element_to_be_clickable((By.XPATH, "//a/span[contains(text(),'Histórico')]"))
#)
#link_historico.click()

input("Pressione Enter para fechar o navegador...")


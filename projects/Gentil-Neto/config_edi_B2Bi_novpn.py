import sys
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep as dormir


# Checando se os argumentos foram passados corretamente
if len(sys.argv) < 3:
    print("Uso: python config_edi_B2Bi_novpn.py <usuario> <senha>")
    sys.exit(1)

# Atribuindo os argumentos às variáveis
login_ = sys.argv[1]
senha_ = sys.argv[2]

# Corrigindo o caminho para o msedgedriver.exe
driver_path = r'C:/Projeto/GT_Pessoal/Scripts_Python/msedgedriver.exe'

# Configurando o serviço para utilizar o Edge Driver especificado
service = Service(executable_path=driver_path)
options = webdriver.EdgeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
prefs = {
    "profile.managed_default_content_settings.images": 2  # Isso desativa o carregamento de imagens
}
options.add_experimental_option("prefs", prefs)


senha_user = "Senha"
sftp_server = 'www.SemParar.com.br'
porta = xxxx
contact = 'Service Support (servicesupport@semparar.net)'

driver = webdriver.Edge(service=service, options=options)
driver.implicitly_wait(10)  # Espera implícita de 10 segundos

driver.get('IP SITE')

# Login
def logar():
    login = driver.find_element(By.ID, "loginUserId")
    login.click()  # Assegure-se de que click() está sendo chamado com ()
    login.send_keys(login_)

    # Senha
    senha = driver.find_element(By.ID, "loginPassword")
    senha.send_keys(senha_)

    # Botão de Login
    logar = driver.find_element(By.ID, "N65642")
    logar.click()
    driver.implicitly_wait(3)  # Espera implícita de 3 segundos
    
def processa_linhas(cod, nome):
    # Atribui cada parte a variáveis e prepara as partes do texto para as variaveis
    routingId = cod
    userSftp = f'ABAST.{routingId}'
    b2bi = f'/backup/axway/EDI/1.ENVIO/4.ABASTECE/{routingId}'
    app_pickups = f'ABAST_{nome.upper()}'
    #app_pickups = f'ABAST_{nome.replace(" - ", "-").replace(" ","").upper()}'

    # Exibe os resultados
    print(f"codigo: {cod}")
    print(f"nome: {nome.upper()}")
    print(f"routingId: {routingId}")
    print(f"userSftp: {userSftp}")
    print(f"b2bi: {b2bi}")
    print(f"app_pickups: {app_pickups}")
    
    return routingId, userSftp, b2bi, app_pickups

def config_b2bi_summary():
    b2bi_summary = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[6]/div/a/img')
    b2bi_summary.click()
    b2bi_summary = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[2]/a')
    b2bi_summary.click()

def config_b2bi_search_app_pickups():  
    application_pickups = driver.find_element(By.NAME, 'searchByName')
    application_pickups.click()
    application_pickups.clear()
    application_pickups.send_keys('*'+cod+'*')
    application_pickups = driver.find_element(By.LINK_TEXT, 'Find')
    application_pickups.click()
    
def config_b2bi_message_handler():
    message_handler = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[8]/div/a/img')
    message_handler.click()
    message_handler = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[3]/td[1]/div/a/img')
    message_handler.click()
    message_handler = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/a[2]')
    message_handler.click()
#Função original    
# def verifica_espaco_vazio(input_id, button_id):
#     input_element = driver.find_element(By.ID, input_id)
#     if input_element.get_attribute('value') == '':
#         print(f"O campo {input_id} está vazio. Clicando no botão {button_id}.")
#         button = driver.find_element(By.ID, button_id)
#         button.click()
#     else:
#         print(f"O campo {input_id} contém valor.")

def verifica_espaco_vazio(input_id, button_id):
    input_element = driver.find_element(By.ID, input_id)
    if input_element.get_attribute('value') == '':
        print(f"O campo {input_id} está vazio. Clicando no botão {button_id}.")
        button = driver.find_element(By.ID, button_id)
        button.click()
        return True  # Ação de clicar foi realizada
    else:
        print(f"O campo {input_id} contém valor.")
        return False  # Ação de clicar não foi realizada
    
def insere_posto():
    # Define uma função para verificar se um input está vazio e clicar no botão correspondente
  
    # Verifica cada par de input e botão
    #driver.switch_to.window(driver.window_handles[1])
    #função original
    # verifica_espaco_vazio('copyToName1', 'copyTo1ChooserBtn')
    # verifica_espaco_vazio('copyToName2', 'copyTo2ChooserBtn')
    # verifica_espaco_vazio('copyToName3', 'copyTo3ChooserBtn') 
    # Função para verificar espaço vazio e tentar clicar no botão correspondente

# Tenta clicar no primeiro campo, se falhar, tenta no segundo, e assim por diante
    if verifica_espaco_vazio('copyToName1', 'copyTo1ChooserBtn'):
        pass  # O clique foi realizado com sucesso, não precisa fazer mais nada
    elif verifica_espaco_vazio('copyToName2', 'copyTo2ChooserBtn'):
        pass  # O clique foi realizado com sucesso no segundo campo, após falha no primeiro
    elif verifica_espaco_vazio('copyToName3', 'copyTo3ChooserBtn'):
        pass  # O clique foi realizado com sucesso no terceiro campo, após falhas nos anteriores
    else:
        print("Nenhum campo vazio necessitou de clique.")

def config_b2b_new_list(type,list_type, const_list):
    list_new = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[3]/tbody/tr[1]/td/a')
    list_new.click()
    driver.switch_to.window(driver.window_handles[1])
    #interagindo com select
    list_new = driver.find_element(By.ID, "ConditionAttribute1")
    #criando uma instancia da classe select
    select = Select(list_new)
    #selecionando pelo valor
    select.select_by_value("ProductionFilename")
    list_new = driver.find_element(By.ID, 'ConditionOperator1')
    select = Select(list_new)
    select.select_by_value("ends with")
    
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr[2]/td[4]/input[1]')
    list_new.click()
    list_new.clear()
    list_new.send_keys(list_type)
    #adicionando novo process message when
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[2]/td/span/a')
    list_new.click()
    list_new = driver.find_element(By.ID, "ConditionAttribute2")
    select = Select(list_new)
    select.select_by_value("ARQUIVO")
    list_new = driver.find_element(By.ID, 'ConditionOperator2')
    select = Select(list_new)
    select.select_by_value("==")
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input[1]')
    list_new.click()
    list_new.clear()
    list_new.send_keys(const_list)
    #add um novo
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td/span/a')
    list_new.click()
    list_new = driver.find_element(By.ID, "ConditionAttribute3")
    select = Select(list_new)
    #selecionando pelo valor
    select.select_by_visible_text('To')
    list_new = driver.find_element(By.ID, 'ConditionOperator1')
    select = Select(list_new)
    select.select_by_value("ends with")
    
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr[2]/td[4]/a')
    list_new.click()
    
    driver.switch_to.window(driver.window_handles[2])
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/span/value/a')
    list_new.click()
    list_new = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/div[2]/table[1]/tbody/tr[1]/td[2]/input')
    list_new.click()
    list_new.clear()
    list_new.send_keys('*BACKUP_ABAST')
    
    list_new = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/div[1]/div[2]/span/a')
    list_new.click()
    list_new = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr/td/span/a')
    list_new.click()
    driver.switch_to.window(driver.window_handles[1])
    
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr/td/span[2]/a')
    list_new.click()
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/span[1]/a')
    list_new.click()
    driver.switch_to.window(driver.window_handles[2])
    #selecionando o que estamos trabalhando
    list_new = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/table/tbody/tr/td/div[2]/content/form/table/tbody/tr[1]/td[2]/input')
    list_new.click()
    list_new.clear()
    list_new.send_keys(nome.replace('_','*'))
    list_new = driver.find_element(By.LINK_TEXT, 'Find')
    list_new.click()
    
    list_new = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[1]/span/input')
    list_new.click()
    list_new = driver.find_element(By.LINK_TEXT, 'OK')
    list_new.click()
    driver.switch_to.window(driver.window_handles[1])
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[10]/tbody/tr/td/span[3]/a')
    list_new.click()
    
    list_new = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td[2]/input')
    list_new.click()
    list_new.clear()
    list_new.send_keys(f'ABASTECE_LISTA_{type}_RPA')  
    list_new = driver.find_element(By.LINK_TEXT, 'Finish')
    list_new.click()             
    driver.switch_to.window(driver.window_handles[0])        
    input("Pressione Enter para fechar o navegador...")  

def config_b2bi_new_partiner():
    #Buscando partner
    partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[7]/div/a/img')
    partners.click()
    partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr/td/div[2]/content/form/table/tbody/tr[1]/td[2]/input')
    partners.click()
    partners.send_keys('*'+ cod +'*')
    partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr/td/div[2]/content/form/span[1]/a')
    partners.click()
    
    #adicionando um novo
    partners = driver.find_element(By.LINK_TEXT, 'Add a partner')
    partners.click()
    
    #add
    driver.switch_to.window(driver.window_handles[1])
    partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[1]/td/table/tbody/tr/td[1]/input')
    partners.click()
    partners = driver.find_element(By.ID, 'next')
    partners.click()
    partners = driver.find_element(By.NAME, 'name')
    partners.click()
    partners.send_keys(nome)
    partners = driver.find_element(By.NAME, 'contact')
    partners.click()
    partners.send_keys(contact)
    partners = driver.find_element(By.NAME, 'routingId')
    partners.click()
    partners.send_keys(routingId)
    partners = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[4]/tbody/tr[1]/td/span/input')
    partners.click()
    partners = driver.find_element(By.ID, 'finish')
    partners.click()
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[0])

def config_b2bi_new_trading_pickup():
    #sumario do b2bi
    config_b2bi_summary()
    #entrando no diretorio
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[3]/table/tbody/tr[1]/td[9]/div/a/img')
    trading_pickup.click()
    trading_pickup = driver.find_element(By.LINK_TEXT, 'ABASTECE_SFTP_NOVPN')
    trading_pickup.click()
    trading_pickup = driver.find_element(By.LINK_TEXT, 'Directories')
    trading_pickup.click()
    driver.implicitly_wait(3)
    #adicionando novo usuário sftp
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/span[2]/table/tbody/tr/td/div[7]/span/a')
    trading_pickup.click()
    
    trading_pickup = driver.find_element(By.ID, 'additionalSubdirectoryPartyName')
    trading_pickup.click()
    
    driver.switch_to.window(driver.window_handles[1])
    trading_pickup = driver.find_element(By.NAME, 'searchFilterByName')
    trading_pickup.click()
    trading_pickup.send_keys(nome.replace('_','*'))
    trading_pickup = driver.find_element(By.LINK_TEXT, 'Find')
    trading_pickup.click()
    trading_pickup = driver.find_element(By.ID, 'partyId')
    trading_pickup.click()
    trading_pickup = driver.find_element(By.LINK_TEXT, 'OK')
    trading_pickup.click()
    driver.implicitly_wait(3)

    driver.switch_to.window(driver.window_handles[0])
    trading_pickup = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table[2]/tbody/tr/td/div/table/tbody/tr[2]/td/span[2]/table/tbody/tr/td/table[3]/tbody/tr[52]/td[2]/div/a')
    trading_pickup.click()
    driver.implicitly_wait(5)
    #definindo userSftp e senha
    trading_pickup = driver.find_element(By.ID, 'additionalSubdirectorySftpUserNameNew')
    trading_pickup.click()
    trading_pickup.send_keys(userSftp)
    trading_pickup = driver.find_element(By.ID, 'additionalSubdirectorySftpUserPassword')
    trading_pickup.click()
    trading_pickup.send_keys(senha_user)
    trading_pickup = driver.find_element(By.ID, 'additionalSubdirectorySftpUserPasswordConfirm')
    trading_pickup.click()
    trading_pickup.send_keys(senha_user)
    #salvando
    trading_pickup = driver.find_element(By.LINK_TEXT, 'Save')
    trading_pickup.click()
    driver.implicitly_wait(5)
    
def config_b2bi_partner_delivery():
    #cod repetido para criar um novo
        #Buscando partner
    partner_delivery = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[7]/div/a/img')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr/td/div[2]/content/form/table/tbody/tr[1]/td[2]/input')
    partner_delivery.click()
    partner_delivery.send_keys(nome)
    partner_delivery = driver.find_element(By.LINK_TEXT, 'Find')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.XPATH, f'//*[contains(text(), "{nome}")]')
    partner_delivery.click()
    #entrando no partner delivery
    partner_delivery = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/div/a/img')
    partner_delivery.click()
    
    partner_delivery = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table[3]/tbody/tr[2]/td/span/a')
    partner_delivery.click()
    driver.switch_to.window(driver.window_handles[1])
    partner_delivery = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[19]/td/table/tbody/tr/td[1]/input[1]')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.ID, 'next')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td/table/tbody/tr/td[1]/input')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.ID, 'next')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.ID, 'next')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.ID, 'next')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.ID, 'next')
    partner_delivery.click()
    partner_delivery = driver.find_element(By.NAME, 'friendlyName')
    partner_delivery.send_keys(nome)
    partner_delivery = driver.find_element(By.ID, 'finish')
    partner_delivery.click()
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(5)

def config_b2bi_application_pickups():
    
    config_b2bi_summary()
    #buscando existente
    application_pickups = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table[1]/tbody/tr/td[3]/table/tbody/tr[2]/td[1]/div/a/img')
    application_pickups.click()
    
    config_b2bi_search_app_pickups()
    
    #add novo
    application_pickups = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/table/tbody/tr[1]/td/a')
    application_pickups.click()
    
    driver.switch_to.window(driver.window_handles[1])
    application_pickups = driver.find_element(By.ID, 'next')
    application_pickups.click()
    application_pickups = driver.find_element(By.ID, 'senderAddressType1')
    application_pickups.click()
    application_pickups = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/span/a')
    application_pickups.click()
    
    driver.switch_to.window(driver.window_handles[2])
    application_pickups = driver.find_element(By.NAME, 'searchFilterByName')
    application_pickups.click()
    application_pickups.send_keys('*ABASTECE*B2Bi*')
    application_pickups = driver.find_element(By.LINK_TEXT, 'Find')
    application_pickups.click()
    driver.implicitly_wait(5)
    application_pickups = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/table[2]/tbody/tr[2]/td[1]/span/input')
    application_pickups.click()
    application_pickups = driver.find_element(By.LINK_TEXT, 'OK')
    application_pickups.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])
    application_pickups = driver.find_element(By.ID, 'next')
    application_pickups.click()
    application_pickups = driver.find_element(By.ID, 'receiverAddressType1')
    application_pickups.click()
    driver.implicitly_wait(5)
    application_pickups = driver.find_element(By.XPATH, '/html/body/form[1]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr[3]/td[2]/span/a')
    application_pickups.click()
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[2])
    application_pickups = driver.find_element(By.NAME, 'searchFilterByName')
    application_pickups.click()
    application_pickups.send_keys(nome.replace('_','*'))
    application_pickups = driver.find_element(By.LINK_TEXT, 'Find')
    application_pickups.click()
    application_pickups = driver.find_element(By.ID, 'partyId')
    application_pickups.click()
    application_pickups = driver.find_element(By.LINK_TEXT, 'OK')
    application_pickups.click()
    driver.switch_to.window(driver.window_handles[1])
    application_pickups = driver.find_element(By.ID, 'next')
    application_pickups.click()
    application_pickups = driver.find_element(By.ID, 'url')
    application_pickups.click()
    application_pickups.clear()
    application_pickups.send_keys(b2bi)
    application_pickups = driver.find_element(By.ID, 'next')
    application_pickups.click()
    application_pickups = driver.find_element(By.NAME, 'friendlyName')
    application_pickups.click()
    application_pickups.send_keys(app_pickups)
    application_pickups = driver.find_element(By.ID, 'finish')
    application_pickups.click()
    driver.switch_to.window(driver.window_handles[0])
    
    config_b2bi_search_app_pickups()
    
    application_pickups = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[3]/table/tbody/tr/td/form/table/tbody/tr/td/div/table/tbody/tr[2]/td/span[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/a')
    application_pickups.click()
    
    #alterando Message processing
    application_pickups = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/form/table[2]/tbody/tr/td/div/table/tbody/tr[1]/td/span[8]/a')
    application_pickups.click()
    application_pickups = driver.find_element(By.NAME, 'messageProcessingMode')
    application_pickups.click()
    application_pickups = driver.find_element(By.LINK_TEXT, 'Save changes')
    application_pickups.click()
    
def config_b2bi_list_lai():
    
    config_b2bi_message_handler()
    driver.implicitly_wait(5)
    
    list_lai = driver.find_element(By.ID, 'searchFilterByName')
    list_lai.click()
    list_lai.clear()
    list_lai.send_keys('*LAI*')
    list_lai = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr/td/div[2]/content/form/span[1]/a')
    list_lai.click()
    
    driver.implicitly_wait(5)
    send_copies_clicked = False  # Flag para verificar se algum elemento foi clicado

    while not send_copies_clicked:
        list_of_page = driver.find_elements(By.XPATH, '//body//*[contains(text(), "Send copies to:")]')

        for element in list_of_page:
            text = element.text
            count_and = text.count(" AND ")

            if count_and < 2:
                try:
                    element.click()
                    print(f"Clicado: {text}")
                    send_copies_clicked = True  # Atualiza a flag
                    break  # Sai do loop for, pois um elemento foi clicado
                except Exception as e:
                    print(f"Erro ao clicar no elemento: {e}")
        
        # Se nenhum elemento satisfaz a condição e a flag ainda é False, tenta ir para a próxima página
        if not send_copies_clicked:
            try:
                # Tenta encontrar e clicar no botão "Next". Ajuste o seletor conforme necessário.
                list_lai = driver.find_element(By.XPATH, '//button[contém(@texto, "Next")] ou //a[contém(@texto, "Next")]')
                list_lai.click()
                print("Indo para a próxima página...")
                
            except Exception as e:
                print("Não foi possível ir para a próxima página ou não há mais páginas.")
                config_b2b_new_list('LAI','.lai', 'LAT_ABAST')
                break  # Sai do loop while se não puder ir para a próxima página
            
            
        
     
    # Define uma função para verificar se um input está vazio e clicar no botão correspondente
  
    # Verifica cada par de input e botão
    #driver.switch_to.window(driver.window_handles[1])
    # verifica_espaco_vazio('copyToName1', 'copyTo1ChooserBtn')
    # verifica_espaco_vazio('copyToName2', 'copyTo2ChooserBtn')
    # verifica_espaco_vazio('copyToName3', 'copyTo3ChooserBtn') 
    insere_posto()
    
    driver.switch_to.window(driver.window_handles[1])
    list_lai = driver.find_element(By.NAME, 'searchFilterByName')
    list_lai.click()
    list_lai.send_keys(nome.replace('_','*'))
    list_lai = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/table/tbody/tr/td/div[2]/content/form/span[1]/a')
    list_lai.click()
    list_lai = driver.find_element(By.ID, 'partyId')
    list_lai.click()
    list_lai = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/span[1]/a')
    list_lai.click()
    driver.switch_to.window(driver.window_handles[0])
    
    list_lai = driver.find_element(By.LINK_TEXT, 'Save changes')
    list_lai.click()
                   
def config_b2bi_list_lat():
    
    config_b2bi_message_handler()
    driver.implicitly_wait(5)
    
    list_lat = driver.find_element(By.ID, 'searchFilterByName')
    list_lat.click()
    list_lat.clear()
    list_lat.send_keys('*LAT*')
    list_lat = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td[1]/table/tbody/tr/td/div[2]/content/form/span[1]/a')
    list_lat.click()
    
    driver.implicitly_wait(5)
    send_copies_clicked = False  # Flag para verificar se algum elemento foi clicado

    while not send_copies_clicked:
        list_of_page = driver.find_elements(By.XPATH, '//body//*[contains(text(), "Send copies to:")]')

        for element in list_of_page:
            text = element.text
            count_and = text.count(" AND ")

            if count_and < 2:
                try:
                    element.click()
                    print(f"Clicado: {text}")
                    send_copies_clicked = True  # Atualiza a flag
                    break  # Sai do loop for, pois um elemento foi clicado
                except Exception as e:
                    print(f"Erro ao clicar no elemento: {e}")
        
        # Se nenhum elemento satisfaz a condição e a flag ainda é False, tenta ir para a próxima página
        if not send_copies_clicked:
            try:
                # Tenta encontrar e clicar no botão "Next". Ajuste o seletor conforme necessário.
                list_lat = driver.find_element(By.XPATH, '//button[contém(@texto, "Next")] ou //a[contém(@texto, "Next")]')
                list_lat.click()
                print("Indo para a próxima página...")
                
            except Exception as e:
                print("Não foi possível ir para a próxima página ou não há mais páginas.")
                # Sai do loop while se não puder ir para a próxima página, irá criar um novo
                
                config_b2b_new_list('LAT','.ltz', 'LAT_ABAST')
                
                
    insere_posto()
    
    driver.switch_to.window(driver.window_handles[1])
    list_lat = driver.find_element(By.NAME, 'searchFilterByName')
    list_lat.clear()
    list_lat.click()
    list_lat.send_keys(nome.replace('_','*'))
    list_lat = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/table/tbody/tr/td/div[2]/content/form/span[1]/a')
    list_lat.click()
    list_lat = driver.find_element(By.ID, 'partyId')
    list_lat.click()
    list_lat = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td[3]/table/tbody/tr/td/form/span[1]/a')
    list_lat.click()
    driver.switch_to.window(driver.window_handles[0])
    
    list_lat = driver.find_element(By.LINK_TEXT, 'Save changes')
    list_lat.click()
    input("Pressione Enter para fechar o navegador...")  

with open('B2Bi.txt', 'r') as arquivo:
    logar()
    for linha in arquivo:
        # Lê o conteúdo do arquivo
        info = linha.upper().strip()
        # Divide o texto em partes vírgulas
        cod, nome = info.split(',', 1)
        processa_linhas(cod, nome)
        routingId, userSftp, b2bi, app_pickups = processa_linhas(cod, nome)

        config_b2bi_new_partiner()
        driver.implicitly_wait(5)

        config_b2bi_new_trading_pickup()
        driver.implicitly_wait(5)

        config_b2bi_partner_delivery()
        driver.implicitly_wait(5) 

        config_b2bi_application_pickups()
        driver.implicitly_wait(5)

        config_b2bi_list_lai()
        driver.implicitly_wait(5)
        
        config_b2bi_list_lat()
        driver.implicitly_wait(5)


#funções opcs OKs
#config_b2bi_new_partiner()
#config_b2bi_new_trading_pickup()
#config_b2bi_partner_delivery() 
#config_b2bi_application_pickups()
#config_b2bi_list_lai()
#config_b2bi_list_lat()
#config_b2bi_message_handler()
#config_b2b_new_list('LAI','.lai', 'LAI_ABAST')

    
'''
def deleta_lai():
    try:
        # Utilize XPath para encontrar o elemento que contém o texto específico.
        # O método contains() pode ser usado para verificar se algum texto está presente em um elemento.
        # Altere '//*[contains(text(), "SEU_CODIGO_AQUI")]' para usar seu código ou texto específico.
        partners = driver.find_element(By.XPATH, f'//*[contains(text(), "{nome}")]')
        
        # Se o elemento foi encontrado, significa que o texto está presente na página.
        print("Texto encontrado na página.")
        #Apagando message Handler existente
        partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[8]/div/a/img')
        partners.click()
        
        partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[3]/td[1]/div/a/img')
        partners.click()
        partners = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td/a[2]')
        partners.click()
        
        #buscando LAI Friendly name
        partners = driver.find_element(By.ID, 'searchFilterByName')
        partners.click()
        partners.send_keys('*LAI*')
        
        
        #Criando busca no messege handler
        buscando = False
        
        while True: 
            try:
                #tentando encontrar o elemento na pagina atual
                partners = driver.find_element(By.XPATH, f'//*[contains(text(), "{nome}")]')
                print('Credenciado encontrado')
                #se encontrado sai do loop
                buscando = True
                break
            
            except NoSuchElementException:
                #se não foi encontrado nessa pagina deve clickar no next
                print('credendiado não encontrado')
                try:
                    botao_next = driver.find_element(By.LINK_TEXT, "Next")
                    botao_next.click()
                    print("Navegando para a próxima página...")
                    dormir(3)  # Espera para carregar a próxima página (ajuste conforme necessário)
                except NoSuchElementException:
                    # Se o botão "Next" não for encontrado, significa que está na última página
                    print("Última página alcançada.")
                    break  # Sai do loop 
            
        if buscando:
            partners.click()
            
            ids_inputs = ['copyToName1', 'copyToName2', 'copyToName3']
            ids_deletes = ['delete1', 'delete2', 'delete3']

            # Para cada par de ID de input e botão
            for id_input, id_del in zip(ids_inputs, ids_deletes):
                try:
                    # Tenta encontrar o elemento de input pelo ID
                    elemento_input = driver.find_element(By.ID, id_input)
                    # Verifica se o valor do input corresponde ao valor procurado
                    if elemento_input.get_attribute('value') == nome:
                        # Se corresponder, encontra o botão pelo ID e clica nele
                        botao = driver.find_element(By.ID, id_del)
                        botao.click()
                        print(f"Botão {id_del} clicado porque o valor foi encontrado em {id_input}.")
                        partners = driver.find_element(By.LINK_TEXT, "Save changes")
                        partners.click()
                        
                        input("Pressione Enter para fechar o navegador...")
                        break  # Sai do loop se encontrou e clicou
                except Exception as e:
                    print(f"Erro ao processar {id_input}: {e}")
            
            input("Pressione Enter para fechar o navegador...")
            
        else:
            print("Elemento não encontrado em nenhuma página.")
                    
            input("Pressione Enter para fechar o navegador...")

    except NoSuchElementException:
            # Se o elemento não foi encontrado, significa que o texto não está presente na página.
            print("Texto não encontrado na página.")

            # Aqui, você pode adicionar a lógica para o que fazer se o texto NÃO for encontrado.

def deleta_lat():
    try:      
        partners = driver.find_element(By.ID, 'searchFilterByName')
        partners.click()
        partners.send_keys('*LAT*')
         #Criando busca no messege handler
        buscando = False
        
        while True: 
            try:
                #tentando encontrar o elemento na pagina atual
                partners = driver.find_element(By.XPATH, f'//*[contains(text(), "{nome}")]')
                print('Credenciado encontrado')
                #se encontrado sai do loop
                buscando = True
                break
            
            except NoSuchElementException:
                #se não foi encontrado nessa pagina deve clickar no next
                print('credendiado não encontrado')
                try:
                    botao_next = driver.find_element(By.LINK_TEXT, "Next")
                    botao_next.click()
                    print("Navegando para a próxima página...")
                    dormir(3)  # Espera para carregar a próxima página (ajuste conforme necessário)
                except NoSuchElementException:
                    # Se o botão "Next" não for encontrado, significa que está na última página
                    print("Última página alcançada.")
                    break  # Sai do loop 
            
        if buscando:
            partners.click()
            
            ids_inputs = ['copyToName1', 'copyToName2', 'copyToName3']
            ids_deletes = ['delete1', 'delete2', 'delete3']

            # Para cada par de ID de input e botão
            for id_input, id_del in zip(ids_inputs, ids_deletes):
                try:
                    # Tenta encontrar o elemento de input pelo ID
                    elemento_input = driver.find_element(By.ID, id_input)
                    # Verifica se o valor do input corresponde ao valor procurado
                    if elemento_input.get_attribute('value') == nome:
                        # Se corresponder, encontra o botão pelo ID e clica nele
                        botao = driver.find_element(By.ID, id_del)
                        botao.click()
                        print(f"Botão {id_del} clicado porque o valor foi encontrado em {id_input}.")
                        partners = driver.find_element(By.LINK_TEXT, "Save changes")
                        partners.click()
                        
                        input("Pressione Enter para fechar o navegador...")
                        break  # Sai do loop se encontrou e clicou
                except Exception as e:
                    print(f"Erro ao processar {id_input}: {e}")
            
            input("Pressione Enter para fechar o navegador...")
            
        else:
            print("Elemento não encontrado em nenhuma página.")
                    
            input("Pressione Enter para fechar o navegador...")

    except NoSuchElementException:
            # Se o elemento não foi encontrado, significa que o texto não está presente na página.
            print("Texto não encontrado na página.")

            # Aqui, você pode adicionar a lógica para o que fazer se o texto NÃO for encontrado.
            


'''



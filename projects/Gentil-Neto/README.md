# Projeto de web scraping python para automação de configurações e Fala com ElevenLabs API

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100" height="100" alt="Python">
  <img src="https://www.selenium.dev/images/selenium_logo_square_green.png" width="100" height="100" alt="Selenium">
  <img src="https://placehold.it/100x100?text=ElevenLabs" width="100" height="100" alt="ElevenLabs">
  <img src="https://avatars.githubusercontent.com/u/166254117?v=4" width="100" height="100" alt="ElevenLabs">
  <img src="https://avatars.githubusercontent.com/u/84950231?v=4" width="100" height="100" alt="ElevenLabs">

  
</p>


## Informações gerais sobre o projeto
O projeto foi criado para automação de processo que era repetitivo (RPA) afim de proporcionar maior agilidade nas configurações necessárias para a aplicação corporativa processo que em média durava cerca de 20 minutos a 30 minutos
via RPA(Robô de processo administrativo) está em média de 2 minutos, fornecendo mais agilidade para o analista.

Foi utilizado python para o desenvolvimento da lógica e tratativa dos campos junto ao Selenium e utiliza a API da ElevenLabs para transformar texto em fala utilizando Python. A integração demonstra como gerar áudio 
a partir de textos específicos utilizando vozes customizadas disponíveis através da ElevenLabs para notificar o analista o termino do script.

## 5.2. Qual é o propósito do projeto

O propósito principal deste projeto é fornecer um exemplo prático e funcional de como usar os conceitos aprendidos em sala de aula para aplicação real, busca-se também:

- Demonstrar comandos da biblioteca selenium
- Demonstrar a configuração necessária para integrar a API da ElevenLabs em um ambiente Python.
- Abordar problemas comuns encontrados durante a implementação, como a configuração e validação de certificados SSL e o acesso a URLs que podem estar bloqueadas por políticas de segurança de rede em ambientes corporativos.

### Considerações de Segurança

O projeto inclui login e senhas que somentes os analistas tem para acesso a aplicação 

### Problemas Comuns e Soluções

- **Trocas de ID's**: ao longo do projeto as maiores dificuldades foram com relação aos elementos das paginas que trocavam de ID's, sendo necessário utilizar o xPath para certificar a manipulação do elemento correto da pagina
- **Bloqueio por Políticas de Segurança**: Estratégias para solicitar alterações nas políticas de filtragem de conteúdo ou o uso de VPNs com a aprovação do departamento de TI.

## Como Usar

O código-fonte inclui um script Python simples que demonstra a integração com a API simples para notificar o analista o termino da execução do script. 

## Tecnologias utilizadas 

- ![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)

- ![ElevenLabs](https://img.shields.io/badge/ElevenLabs-000000?style=flat-square&logo=data:image/png;base64,<BASE64>)
  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 

- ![Axway EDI](https://www.axway.com/themes/custom/axway2020/img/axway-logo-dark-gray.svg)

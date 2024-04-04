## Instruções Contribuir

Este espaço é para você compartilhar seus projetos feitos durante o curso ou até mesmo projetos feitos fora do curso, para poder ver opinião dos outros e entender a base do versionamento com Git.

1. Faça um **Fork** deste repositório (caso já tenha feito, siga para o proximo passo)

2. Clone localmente com base no arquivo do seu github: `git clone https://github.com/SEU_USERNAME/open-source-course.git`;

    2.1. O git clone pega o arquivo que foi criado originalmente online e faz ele localmente

3. Crie e referencie uma nova **branch** e der o nome como `projects/SEU_USERNAME`

    > Exemplo: `git checkout -b projects/carlosvinicius-ai`

    3.1. git checkout -b vai criar e mudar para a branch que você criou

4. Dentro da pasta projects crie uma pasta com seu nome de usuario ou com o nome de seu projeto

    > Exemplo: `carlosvinicius-ai`

5. Desenvolva o seu projeto, ele tem que ter obrigatoriamente um README, o README tem que ter as seguintes informações:

    5.1. Informações gerais sobre o projeto

    5.2. Qual é o propósito do projeto

    5.3. As pessoas que participaram do projeto, com um link para o README na pasta [community](https://github.com/carlosvinicius-ai/open-source-course/tree/main/community)

6. Adicione suas alterações para serem enviadas com o comando `git add projects/SEU_USERNAME`

    6.1. git add é para adicionar um arquivo em específico

    6.2. git add * adicionar todos os arquivos utilizados

7. Crie um commit e adicione a mensagem indicando a adição do seu perfil `git commit -m ":white_check_mark: feat: add SEU_USERNAME project"`

7.1. commit é um texto referente as atualizações feitas

8. Envie suas alterações para o repositório remoto `git push origin projects/SEU_USERNAME`

9. Crie um **Pull Request**
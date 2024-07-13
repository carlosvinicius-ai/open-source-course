package org.example;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

//Seguimos o tema pois foi visualizado um exercício simples em um canal do YT
//E resolvemos incrementar com o tratamento de dados, com espaçamento
//E diferenciando maiúsculos de minúsculos, o código poderia ter sido feito sem esse
//detalhe de maiúsculos e minúsculos, mas ficamos envolvidos com o problema.

//A maior dificuldade foi acertar o local da condição while para que o código
//repetisse na ordem que o usuário precisa, e que fosse fechado apenas na hora
//prevista pelos desenvolvedores

//Github da tropa:
//https://github.com/santosmelqui
//https://github.com/leandrolol
//https://github.com/guireinhardt
//
//
                //apresentação do usuário
                System.out.println("Olá. Qual o seu primeiro nome:");
                String nome = in.nextLine().trim();
                System.out.println("Qual o sobrenome? ");
                String sobrenome = in.nextLine().trim();

                //registrando login e senha
                System.out.printf("Bem-vindo %s %s, o seu primeiro nome será o login\n Digite a senha\n", nome, sobrenome);
                System.out.println("Escolha uma senha: ");
                String senha = in.nextLine().trim();
                //confirmando senha
                boolean correto = false;
                while (!correto) {
                    System.out.println("Confirme a senha: ");
                    String senhac = in.nextLine().trim();
                    if (!senhac.equals(senha)) {
                        System.out.println("Não é a mesma");
                    } else {
                        System.out.println("Senha confirmada. Siga para logar.");
                        correto = true;
                    }
                }

                //autenticando login
                boolean autenticado = false;
                while (!autenticado) {
                    System.out.println("Login: ");
                    String login = in.nextLine().trim();
                    System.out.println("Senha: ");
                    String pass = in.nextLine().trim();
                    if (login.equals(nome) && pass.equals(senha)) {
                        System.out.printf("usuário %s logado com sucesso", login);
                        autenticado = true;

                        //Digitou errado, deve repetir
                    } else {
                        System.out.println("Login ou senha inválido");
                    }
                }
            }
        }










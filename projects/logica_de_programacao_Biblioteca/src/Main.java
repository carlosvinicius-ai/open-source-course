import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
        public class Main {
            public static void main(String[] args) {

                Scanner scanner = new Scanner(System.in);

                System.out.println("Digite seu nome: ");
                String nome = scanner.nextLine();


                System.out.println("Bem vindo " + nome.toUpperCase() + " a Biblioteca online do Senai, aqui voçê consegue fazer uma reserva online " +
                        "de um livro. ");


                System.out.println("\nVou te mostrar o menu de  livros de Programação ");
                System.out.println(" 1-Logica de programação. ");
                System.out.println(" 2-Entendendo algoritimos.");
                System.out.println(" 3-Java com orientação a objetos.");
                System.out.println(" 4-JavaScript: O guia definitivo.");
                System.out.println(" 5-Sistena de banco de dados.");
                System.out.println(" 6-Fundamentos de HTML5 e CSS3.");
                System.out.println(" 7-Curso intensivo de PYTHON. ");
                System.out.println(" 8-Marchine learning.");
                System.out.println(" 9-Aprendendo Git e Github");
                System.out.println(" 10-Programação em C++.");

                System.out.println("\nDigite qual livro gostaria de utlizar:");
                int livro = scanner.nextInt();
                scanner.nextLine();

                String nomeLivro = "";

                switch (livro) {
                    case 1:
                        nomeLivro = "Logica de programação;";
                        break;
                    case 2:
                        nomeLivro = "Entedendo algoritimos";

                        break;
                    case 3:
                        nomeLivro = "livro Java com orientação a objetos";

                        break;
                    case 4:
                        nomeLivro = "Livro JavaScripy: O guia definitivo";

                        break;
                    case 5:
                        nomeLivro = "Livro Sistema de banco de dados";

                        break;
                    case 6:
                        nomeLivro = "Livro Fundamentos de HTML5 e CSS3";

                        break;
                    case 7:
                        nomeLivro = "Livro Curso intensivo de PYTHON";

                        break;
                    case 8:
                        nomeLivro = "Livro Marchine learning";

                        break;
                    case 9:
                        nomeLivro = "Livro Aprendendo Git e Github";

                        break;
                    case 10:
                        nomeLivro = "Livro Programação em C++";

                        break;
                    default:
                        System.out.println("Livro não encontrado. Digite uma opção válida.");
                        scanner.close(); // Fechar o scanner antes de finalizar o programa
                        return;
//


                }

                System.out.print("Qual dia voçê deseja pegar  o livro na biblioteca " + nome.toUpperCase());
                System.out.println("\n1- Segunda-feira");
                System.out.println("2- Terça-feira");
                System.out.println("3- Quarta-feira");
                System.out.println("4- Quinta-feira");
                System.out.println("5- Sexta-feira");
                int dia = scanner.nextInt();

                String nomeDia = "";

                // Verifica se a opção de dia é válida
                {
                    if (dia == 1) {
                        nomeDia = "Segunda-feira";
                    } else if (dia == 2) {
                        nomeDia = "Terça-feira ";
                    } else if (dia == 3) {
                        nomeDia = "Quarta-feira";
                    } else if (dia == 4) {
                        nomeDia = "Quinta-feira";
                    } else if (dia == 5) {
                        nomeDia = "Sexta-feira";
                    } else {
                        System.out.println("Dia não encontrado,digite um dia valido.");
                        scanner.close(); // Fechar o scanner antes de finalizar o programa
                        return;
                    }


                    scanner.close();
                    System.out.println("\nVocê escolheu o livro: " + nomeLivro.toUpperCase());
                    System.out.println("Você irá retira-lo na: " + nomeDia.toUpperCase());
                }




            }
        }
    }
}
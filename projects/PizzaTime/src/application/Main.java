package application;
import entities.*;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner (System.in);

        Clientes cliente = new Clientes("Arthur de Sousa Santana");

        Sabores sabores = new Sabores ("Portuguesa");

        Bordas bordas = new Bordas ("Chocolate");

        Pizza pizza = new Pizza ("Portuguesa");

        Bebidas bebidas = new Bebidas ("Guaraná Antartica Zero");

        Sobremesa sobremesa = new Sobremesa ("Pudim");

        Pedido pedido = new Pedido ("");

        System.out.println(cliente);
        pizzaCompleta(sabores, pizza, bordas);
        System.out.println(bebidas);
        System.out.println(sobremesa);
        System.out.println(pedido);
    }

    public static void pizzaCompleta(Juncao juncao1, Juncao juncao2, Juncao juncao3){
        System.out.printf("Seu pedido final é: %s, %s, %s\n", juncao1.texto(), juncao2.texto(), juncao3.texto() );
    }
}
package ControleDeValidade;
public class teste {
    public static void main(String[] args) {

        Produto.cadastrarProduto("12345", "Nescau", "04/07/2025");
        Produto.cadastrarProduto("12333", "Heineken", "16/11/2024");

        System.out.println();

        Produto.listarProdutos();
    }
}
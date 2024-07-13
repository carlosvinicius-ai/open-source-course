package ControleDeValidade;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
public class Produto {

    private String codigoDeBarras;
    private String nome;
    private LocalDate dataValidade;
    private static final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
    private static Produto[] produtos = new Produto[10];
    private static int count = 0;


    // Construtor
    public Produto(String codigoDeBarras, String nome, LocalDate dataValidade) {
        super();
        this.codigoDeBarras = codigoDeBarras;
        this.nome = nome;
        this.dataValidade = dataValidade;
    }


    // Getter
    public String getCodigoDeBarras() {
        return codigoDeBarras;
    }

    public String getNome() {
        return nome;
    }

    public LocalDate getDataValidade() {
        return dataValidade;
    }

    public String getDataValidadeFormatada() {
        return dataValidade.format(formatter);
    }

// Setters

    public void setCodigoDeBarras(String codigoDeBarras) {
        this.codigoDeBarras = codigoDeBarras;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setDataValidade(LocalDate dataValidade) {
        this.dataValidade = dataValidade;
    }

    public void setDataValidade(String dataValidade) throws DateTimeParseException {
        try {
            this.dataValidade = LocalDate.parse(dataValidade, formatter);
        } catch (DateTimeParseException e) {
            throw new DateTimeParseException("Data de validade no formato inválido. Use dd/MM/yyyy.",
                    dataValidade, e.getErrorIndex());
        }
    }

    public static void cadastrarProduto(String codigoDeBarras, String nome, String dataValidade) {
        if (count >= produtos.length) {
            System.err.println("Erro: capacidade máxima de produtos atingida.");
            return;
        }
        try {
            LocalDate validade = LocalDate.parse(dataValidade, formatter);
            Produto produto = new Produto(codigoDeBarras, nome, validade);
            produtos[count] = produto;
            count++;
            System.out.println("Produto cadastrado com sucesso: " + produto);
        } catch (DateTimeParseException e) {
            System.err.println("Erro ao cadastrar produto: Data de validade no formato inválido. Use dd/MM/yyyy.");
        }
    }

    public static void listarProdutos() {
        if (count == 0) {
            System.out.println("Nenhum produto cadastrado.");
            return;
        }
        System.out.println("Produtos cadastrados:");
        for (int i = 0; i < count; i++) {
            System.out.println(produtos[i]);
        }
    }

    @Override
    public String toString() {
        return "Produto{" +
                "codigoDeBarras='" + codigoDeBarras + '\'' +
                ", nome='" + nome + '\'' +
                ", dataValidade=" + getDataValidadeFormatada() +
                '}';
    }
}

package entities;

public class Clientes {

    private String nome;

    // Construtor para inicializar o nome
    public Clientes (String nome) {
        this.nome = nome;
    }

    // Getter para o nome
    public String getNome() {
        return nome;
    }

    // Setter para o nome
    public void setNome(String nome) {
        this.nome = nome;
    }
    // Método toString para exibir informações do cliente:

    @Override
    public String toString() {
        return "Cliente: " + nome;
    }



}

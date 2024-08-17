package entities;

public class Sabores implements Juncao {
    private String sabor;
    // Construtor para inicializar o nome
    public Sabores (String sabor) {
        this.sabor = sabor;
    }

    public String getSabor() {
        return sabor;
    }

    public void setSabor(String sabor) {
        this.sabor = sabor;
    }
    @Override
    public String toString() {
        return "Sabor: " + sabor;
    }

    @Override
    public String texto() {
        return this.sabor;
    }
}

package entities;

public class Bebidas {
    private String bebidas;

    public Bebidas(String bebidas) {
        this.bebidas = bebidas;
    }

    public String getBebidas() {
        return bebidas;
    }

    public void setBebidas(String bebidas) {
        this.bebidas = bebidas;
    }
    @Override
    public String toString() {
        return "Sabor: " + bebidas;
    }
}

package entities;

public class Bordas implements Juncao{
    private String bordas;

    public Bordas(String bordas) {
        this.bordas = bordas;
    }

    public String getBordas() {
        return bordas;
    }

    public void setBordas(String bordas) {
        this.bordas = bordas;
    }
    @Override
    public String toString() {
        return "Borda: " + bordas;
    }

    @Override
    public String texto() {
        return this.bordas;
    }
}


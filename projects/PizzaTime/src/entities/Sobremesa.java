package entities;

public class Sobremesa {
    private String sobremesa;

    public Sobremesa(String sobremesa) {
        this.sobremesa = sobremesa;
    }

    public String getSobremesa() {
        return sobremesa;
    }

    public void setSobremesa(String sobremesa) {
        this.sobremesa = sobremesa;
    }
    @Override
    public String toString() {
        return "Sobremesa: " + sobremesa;
    }
}

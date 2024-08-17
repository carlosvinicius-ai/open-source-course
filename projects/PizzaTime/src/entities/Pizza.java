package entities;

public class Pizza implements  Juncao{

    private String pizza;

    public Pizza (String pizza){
        this.pizza = pizza;
    }

    public String getPizza() {
        return pizza;
    }

    public void setPizza(String pizza) {
        this.pizza = pizza;
    }
    @Override
    public String toString() {
        return "Produto final: " + pizza;
    }


    @Override
    public String texto() {
         return this.pizza;
    }
}



package entities;
public class Pedido {
    private String pedido;

    public Pedido(String pedido) {
        this.pedido = pedido;
    }

    public String getPedido() {
        return pedido;
    }

    public void setPedido(String pedido) {
        this.pedido = pedido;
    }
    @Override
    public String toString() {
        return "Pedido Final: " + pedido;
    }
}

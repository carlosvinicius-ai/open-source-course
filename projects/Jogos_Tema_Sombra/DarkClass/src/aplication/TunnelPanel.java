package aplication;

import javax.swing.*;
import java.awt.*;

public class TunnelPanel extends JPanel {
    private int acertouCount = 0;

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        int width = getWidth();
        int height = getHeight();

        // Desenha um túnel simples
        for (int i = 0; i < 10; i++) {
            g.setColor(getColor(i));
            g.fillRect(width / 2 - (10 * i), height / 2 - (10 * i), 20 * i, 20 * i);
        }
    }

    public void acertou() {
        acertouCount++;
        repaint(); // Atualiza a tela
    }

    private Color getColor(int depth) {
        // Muda a cor com base no número de acertos
        if (acertouCount > depth) {
            return Color.YELLOW; // Cor que representa um acerto
        }
        return Color.GRAY; // Cor do túnel
    }
}
import javax.swing.*;
import java.awt.*;
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {

        // Generate a random letter (A-Z)
        char randomLetter = (char) ThreadLocalRandom.current().nextInt(65, 90 + 1);

        // Array of possible answers
        final String[] answers = {"alfa", "alpha", "bravo", "charlie", "delta", "echo", "eco", "foxtrot", "fox trot", "golf", "hotel", "india", "juliett", "juliet", "julliett", "julliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "quebeck", "quebek", "romeo", "sierra", "tango", "uniform", "victor", "viktor", "victer", "whiskey", "xray", "x-ray", "x ray", "yankee", "zulu"};

        // Create the main JFrame window
        JFrame window = new JFrame("Phonetic Alphabet Game");
        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(false);
        window.setSize(new Dimension(600, 500));
        window.setLocationRelativeTo(null);
        window.setLayout(null);

        try {
            // Set the look and feel of the UI to match the system
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) {
            // Handle any exceptions related to setting the look and feel
            e.printStackTrace();
        }

        // JLabel to display the random letter
        JLabel letter = new JLabel(String.valueOf(randomLetter));
        letter.setFont(new Font("Segoe UI", Font.PLAIN, 100));
        letter.setHorizontalAlignment(JLabel.CENTER);
        letter.setBounds(0, 0, window.getWidth(), 200);
        window.add(letter);

        // JTextField for user input
        JTextField input = new JTextField();
        int inputWidth = 200;
        input.setBounds(window.getWidth() / 2 - inputWidth / 2, 240, inputWidth, 60);
        input.setHorizontalAlignment(JTextField.CENTER);
        input.setFont(new Font("Segoe UI", Font.PLAIN, 25));
        window.add(input);

        // JLabel to display the number of hits
        JLabel hits = new JLabel("0");
        hits.setFont(new Font("Segoe UI", Font.PLAIN, 50));
        hits.setHorizontalAlignment(JLabel.LEFT);
        int hitsHeight = 150;
        hits.setBounds(10, window.getHeight() - hitsHeight, window.getWidth(), hitsHeight);
        window.add(hits);

        // Make the window visible
        window.setVisible(true);

        // Loop
        while (true) {
            for (int i = 0; i < answers.length; i++) {
                try {
                    // Check if the user input contains a valid answer
                    if (input.getText().toLowerCase().contains(answers[i])) {
                        // Check if the first character matches the displayed letter
                        if (input.getText().toUpperCase().charAt(0) == letter.getText().charAt(0)) {
                            // Generate a new random letter
                            randomLetter = (char) ThreadLocalRandom.current().nextInt(65, 90 + 1);
                            letter.setText(String.valueOf(randomLetter));
                            // Clear the input field
                            input.setText("");
                            // Update the hit counter
                            hits.setText(String.valueOf(Integer.parseInt(hits.getText()) + 1));
                        }
                    }
                } catch (Exception _) {}
            }
        }
    }
}

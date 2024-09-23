package aplication;

import java.util.ArrayList;
import java.util.List;

public class Ensino {
    private String nome;
    private List<Serie> series;

    public Ensino(String nome) {
        this.nome = nome;
        this.series = new ArrayList<>();
    }

    public void adicionarSerie(Serie serie) {
        series.add(serie);
    }

    public String getNome() {
        return nome;
    }

    public List<Serie> getSeries() {
        return series;
    }
}

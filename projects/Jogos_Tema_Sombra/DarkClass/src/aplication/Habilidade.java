package aplication;

import java.util.ArrayList;
import java.util.List;

public class Habilidade {
    private String codigo;
    private String descricao;
    private List<Pergunta> perguntas;

    public Habilidade(String codigo, String descricao) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.perguntas = new ArrayList<>();
    }

    public void adicionarPergunta(Pergunta pergunta) {
        perguntas.add(pergunta);
    }

    public String getCodigo() {
        return codigo;
    }

    public String getDescricao() {
        return descricao;
    }

    public List<Pergunta> getPerguntas() {
        return perguntas;
    }
}

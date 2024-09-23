package aplication;

public class Pergunta {
    private String enunciado;
    private String respostaCorreta;
    private String[] opcoes;

    public Pergunta(String enunciado, String respostaCorreta, String[] opcoes) {
        this.enunciado = enunciado;
        this.respostaCorreta = respostaCorreta;
        this.opcoes = opcoes;
    }

    public String getEnunciado() {
        return enunciado;
    }

    public String getRespostaCorreta() {
        return respostaCorreta;
    }

    public String[] getOpcoes() {
        return opcoes;
    }

    public boolean verificarResposta(String resposta) {
        return resposta.equalsIgnoreCase(respostaCorreta);
    }
}

import aplication.*;

import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Ensino> ensinos = new ArrayList<>();
        ensinos.add(new Ensino("Ensino Fundamental Anos Finais"));
        ensinos.add(new Ensino("Ensino Médio"));

        // Adicione isso no início do seu método main
        JFrame frame = new JFrame("Tunnel Effect");
        TunnelPanel tunnelPanel = new TunnelPanel();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(tunnelPanel);
        frame.setSize(400, 400);
        frame.setVisible(true);

        // Adicionando séries ao ensino
        ensinos.get(0).adicionarSerie(new Serie("6º Ano"));
        ensinos.get(0).adicionarSerie(new Serie("7º Ano"));
        ensinos.get(0).adicionarSerie(new Serie("8º Ano"));

        // Adicionando habilidades para o 6º Ano
        List<Habilidade> habilidades6Ano = new ArrayList<>();
        habilidades6Ano.add(new Habilidade("EF06CI01", "Classificar como homogênea ou heterogênea a mistura de dois ou mais materiais, a partir da observação e da comparação das características e propriedades de diferentes materiais, por meio da execução de experimentos simples como mistura de água e sal, água e areia, dentre outros. "));
        habilidades6Ano.add(new Habilidade("EF06CI02", "Observar, identificar e registrar evidências de transformações químicas decorrentes da mistura de diversos materiais, ocorridas tanto na realização de experimentos quanto em situações do cotidiano, como a mistura de ingredientes para fazer um bolo, mistura de vinagre com bicarbonato de sódio, como também pelo conhecimento, por meio de publicação eletrônica ou impressa, de situações relacionadas ao sistema de produção. "));
        habilidades6Ano.add(new Habilidade("EF06CI03", "Selecionar métodos adequados para a separação de diferentes sistemas heterogêneos a partir da investigação e identificação de processos de separação de materiais de uso cotidiano, bem como pesquisar sobre procedimentos específicos tais como a produção de sal de cozinha e a destilação do petróleo."));
        habilidades6Ano.add(new Habilidade("EF06CI04", "Associar a produção de medicamentos e outros materiais sintéticos ao desenvolvimento científico e tecnológico, reconhecendo benefícios e avaliando impactos socioambientais. "));
        habilidades6Ano.add(new Habilidade("EF06CI05", "Identificar a organização básica da célula por meio de imagens impressas e digitais, de animações computadorizadas e de instrumentos ópticos, reconhecendo-a como unidade estrutural e funcional dos seres vivos unicelulares e pluricelulares, na perspectiva da História da Ciência. "));
        habilidades6Ano.add(new Habilidade("EF06CI06", "Concluir com base na análise de ilustrações e ou modelos (físicos ou digitais), que os organismos são um complexo arranjo de sistemas com diferentes níveis de organização."));
        habilidades6Ano.add(new Habilidade("EF06CI07", "Justificar o papel do sistema nervoso na coordenação das ações motoras e sensoriais do corpo, com base na compreensão e análise de suas estruturas básicas e respectivas funções."));
        habilidades6Ano.add(new Habilidade("EF06CI08", "Explicar a importância da visão (captação e interpretação das imagens) na interação do organismo com o meio e, com base no funcionamento do olho humano, selecionar lentes adequadas para a correção de diferentes defeitos da visão."));
        habilidades6Ano.add(new Habilidade("EF06CI09", "Concluir, com base na observação de situações do cotidiano ou reproduzidas em vídeos, que a estrutura, a sustentação e a movimentação dos seres vertebrados resultam da interação entre os sistemas muscular, ósseo e nervoso."));
        habilidades6Ano.add(new Habilidade("EF06CI10", "Explicar como o funcionamento do sistema nervoso pode ser afetado por substâncias psicoativas."));
        habilidades6Ano.add(new Habilidade("EF06CI11", "Identificar e descrever as diferentes camadas que estruturam o planeta Terra, da estrutura interna à atmosfera, e suas principais características."));
        habilidades6Ano.add(new Habilidade("EF06CI12", "Categorizar as rochas de acordo com suas características e origem e associar as rochas sedimentares à formação de fósseis em diferentes períodos geológicos."));
        habilidades6Ano.add(new Habilidade("EF06CI13", "Selecionar argumentos e evidências científicas que demonstrem a esfericidade da Terra."));
        habilidades6Ano.add(new Habilidade("EF06CI14", "Reconhecer e explicar que os movimentos de rotação e translação da Terra e da inclinação de seu eixo de rotação em relação ao plano de sua órbita em torno do Sol originam eventos como as mudanças na sombra de objetos ao longo do dia, em diferentes períodos do ano. "));

// Exemplo de perguntas associadas a uma habilidade
        habilidades6Ano.get(0).adicionarPergunta(new Pergunta("O que é uma mistura homogênea?", "Uma mistura com composição uniforme", new String[]{"Uma mistura com composição uniforme", "Uma mistura que não se mistura", "Uma mistura sólida", "Uma mistura gasosa"}));
        habilidades6Ano.get(0).adicionarPergunta(new Pergunta("Qual exemplo é uma mistura heterogênea?", "Mistura de água e areia", new String[]{"Mistura de água e sal", "Mistura de água e areia", "Água pura", "Óleo"}));
        habilidades6Ano.get(0).adicionarPergunta(new Pergunta("Qual exemplo é uma mistura homogênea?", "Água e sal dissolvidos", new String[]{"Água e sal dissolvidos", "Óleo e água", "Água e areia", "Frutas picadas em uma salada"}));
        habilidades6Ano.get(0).adicionarPergunta(new Pergunta("Qual das opções a seguir é uma mistura sólida que pode ser classificada como heterogênea?", "Liga metálica", new String[]{"Liga metálica", "Mistura de areia e sal", "Açúcar em pó", "Gelo triturado"}));
        habilidades6Ano.get(1).adicionarPergunta(new Pergunta("Qual das seguintes misturas representa uma transformação química?", "Mistura de vinagre e bicarbonato de sódio", new String[]{"Mistura de água e açúcar", "Mistura de vinagre e bicarbonato de sódio", "Mistura de óleo e água", "Dissolução de sal em água"}));
        habilidades6Ano.get(1).adicionarPergunta(new Pergunta("Ao misturar ingredientes para fazer um bolo, qual das opções a seguir representa uma evidência de transformação química?", "A mudança de cor da massa", new String[]{"O aumento do volume da massa", "A mudança de cor da massa", "A dissolução do fermento", "A separação de ingredientes"}));
        habilidades6Ano.get(1).adicionarPergunta(new Pergunta("Durante a reação entre vinagre e bicarbonato de sódio, o que é um dos produtos dessa reação?", "Dióxido de carbono", new String[]{"Água", "Dióxido de carbono", "Sal", "Açúcar"}));
        habilidades6Ano.get(1).adicionarPergunta(new Pergunta("Em qual das situações abaixo é possível observar uma transformação química?", "Combustão de madeira", new String[]{"Mistura de tinta com água", "Combustão de madeira", "Adição de sal à água", "Dissolução de açúcar em água"}));
        habilidades6Ano.get(1).adicionarPergunta(new Pergunta("Qual das afirmações sobre transformações químicas é verdadeira?", "Elas sempre resultam na formação de uma nova substância.", new String[]{"Elas sempre resultam na formação de uma nova substância.", "Elas ocorrem apenas em reações que produzem calor.", "Elas podem ser revertidas facilmente.", "Elas não envolvem mudanças nas propriedades dos materiais."}));


        // Menu
        StringBuilder menuEnsino = new StringBuilder("Escolha o tipo de ensino:\n");
        for (int i = 0; i < ensinos.size(); i++) {
            menuEnsino.append((i + 1)).append(". ").append(ensinos.get(i).getNome()).append("\n");
        }
        int tipoEnsino = Integer.parseInt(JOptionPane.showInputDialog(menuEnsino.toString())) - 1;

        StringBuilder menuSerie = new StringBuilder("Escolha a série:\n");
        List<Serie> series = ensinos.get(tipoEnsino).getSeries();
        for (int i = 0; i < series.size(); i++) {
            menuSerie.append((i + 1)).append(". ").append(series.get(i).getNome()).append("\n");
        }
        int serieEscolhida = Integer.parseInt(JOptionPane.showInputDialog(menuSerie.toString())) - 1;

        // Selecionar habilidades apenas para 6º Ano
        if (series.get(serieEscolhida).getNome().equals("6º Ano")) {
            StringBuilder menuHabilidade = new StringBuilder("Escolha a habilidade:\n");
            for (int i = 0; i < habilidades6Ano.size(); i++) {
                menuHabilidade.append((i + 1)).append(". ").append(habilidades6Ano.get(i).getCodigo()).append(": ").append(habilidades6Ano.get(i).getDescricao()).append("\n");
            }
            int habilidadeEscolhida = Integer.parseInt(JOptionPane.showInputDialog(menuHabilidade.toString())) - 1;
            Habilidade habilidadeSelecionada = habilidades6Ano.get(habilidadeEscolhida);
            JOptionPane.showMessageDialog(null, "Você escolheu: " + habilidadeSelecionada.getCodigo() + " - " + habilidadeSelecionada.getDescricao());

            // Perguntas
            StringBuilder resultado = new StringBuilder("Responda as perguntas:\n");
            for (Pergunta pergunta : habilidadeSelecionada.getPerguntas()) {
                resultado.append(pergunta.getEnunciado()).append("\n");
                String[] opcoes = pergunta.getOpcoes();
                for (int i = 0; i < opcoes.length; i++) {
                    resultado.append((i + 1)).append(". ").append(opcoes[i]).append("\n");
                }
                String resposta = JOptionPane.showInputDialog(resultado.toString() + "Sua resposta:");

                // Verifica se a resposta é válida
                if (resposta != null && !resposta.trim().isEmpty()) {
                    int respostaIndex;
                    try {
                        respostaIndex = Integer.parseInt(resposta) - 1; // Converte a resposta para índice
                        if (respostaIndex >= 0 && respostaIndex < opcoes.length) {
                            String respostaEscolhida = opcoes[respostaIndex];
                            if (pergunta.verificarResposta(respostaEscolhida)) {
                                JOptionPane.showMessageDialog(null, "Resposta correta!");
                                tunnelPanel.acertou();
                            } else {
                                JOptionPane.showMessageDialog(null, "Resposta incorreta. A resposta correta é: " + pergunta.getRespostaCorreta());
                            }
                        } else {
                            JOptionPane.showMessageDialog(null, "Opção inválida. Tente novamente.");
                        }
                    } catch (NumberFormatException e) {
                        JOptionPane.showMessageDialog(null, "Por favor, insira um número válido.");
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Por favor, insira uma resposta.");
                }
                resultado.setLength(0); // Limpar resultado para a próxima pergunta
            }

        }
    }
}
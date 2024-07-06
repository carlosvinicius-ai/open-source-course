package org.example;
import javax.swing.JOptionPane;
import java.util.List;

public class Cadastro {
    public static void main(String[] args) {
        CadastroUsuario cadastroUsuario = new CadastroUsuario();
        CadastroFuncionario cadastroFuncionario = new CadastroFuncionario();

        // Adicionar usuário padrão
        cadastroUsuario.adicionarUsuario("admin", "admin123");

        // Tela de Login
        boolean autenticado = false;
        while (!autenticado) {
            String username = JOptionPane.showInputDialog(null, "Username:");
            String password = JOptionPane.showInputDialog(null, "Password:");
            if (cadastroUsuario.autenticar(username, password)) {
                autenticado = true;
                JOptionPane.showMessageDialog(null, "Login bem-sucedido!");
            } else {
                JOptionPane.showMessageDialog(null, "Credenciais inválidas. Tente novamente.");
            }
        }

        // Menu principal
        while (true) {
            String[] options = {"Adicionar Funcionário", "Listar Funcionários", "Remover Funcionário", "Sair"};
            int opcao = JOptionPane.showOptionDialog(null, "Escolha uma opção:", "Sistema de Cadastro de Funcionários",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);

            switch (opcao) {
                case 0: // Adicionar Funcionário
                    String nome = JOptionPane.showInputDialog(null, "Nome do funcionário:");
                    String cargo = JOptionPane.showInputDialog(null, "Cargo do funcionário:");
                    double salario = Double.parseDouble(JOptionPane.showInputDialog(null, "Salário do funcionário:"));
                    cadastroFuncionario.adicionarFuncionario(nome, cargo, salario);
                    JOptionPane.showMessageDialog(null, "Funcionário adicionado com sucesso!");
                    break;
                case 1: // Listar Funcionários
                    List<Funcionario> funcionarios = cadastroFuncionario.listarFuncionarios();
                    if (funcionarios.isEmpty()) {
                        JOptionPane.showMessageDialog(null, "Nenhum funcionário cadastrado.");
                    } else {
                        StringBuilder funcionariosString = new StringBuilder("Lista de Funcionários:\n");
                        for (Funcionario funcionario : funcionarios) {
                            funcionariosString.append(funcionario).append("\n");
                        }
                        JOptionPane.showMessageDialog(null, funcionariosString.toString());
                    }
                    break;
                case 2: // Remover Funcionário
                    int id = Integer.parseInt(JOptionPane.showInputDialog(null, "ID do funcionário a ser removido:"));
                    if (cadastroFuncionario.removerFuncionario(id)) {
                        JOptionPane.showMessageDialog(null, "Funcionário removido com sucesso!");
                    } else {
                        JOptionPane.showMessageDialog(null, "Funcionário não encontrado.");
                    }
                    break;
                case 3: // Sair
                    JOptionPane.showMessageDialog(null, "Saindo...");
                    System.exit(0);
                default:
                    JOptionPane.showMessageDialog(null, "Opção inválida. Tente novamente.");
            }
        }
    }
}

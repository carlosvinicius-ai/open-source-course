package org.example;
import java.util.ArrayList;
import java.util.List;

public class CadastroFuncionario {
    private List<Funcionario> funcionarios = new ArrayList<>();
    private int proximoId = 1;

    public void adicionarFuncionario(String nome, String cargo, double salario) {
        Funcionario funcionario = new Funcionario(proximoId++, nome, cargo, salario);
        funcionarios.add(funcionario);
    }

    public List<Funcionario> listarFuncionarios() {
        return new ArrayList<>(funcionarios);
    }

    public boolean removerFuncionario(int id) {
        return funcionarios.removeIf(funcionario -> funcionario.getId() == id);
    }
}


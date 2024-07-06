package org.example;
import java.util.HashMap;
import java.util.Map;

public class CadastroUsuario {
    private Map<String, String> usuarios = new HashMap<>();

    public void adicionarUsuario(String username, String password) {
        usuarios.put(username, password);
    }

    public boolean autenticar(String username, String password) {
        return usuarios.containsKey(username) && usuarios.get(username).equals(password);
    }
}

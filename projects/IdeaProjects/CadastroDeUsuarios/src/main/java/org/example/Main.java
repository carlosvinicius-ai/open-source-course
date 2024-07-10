package org.example;
import java.util.HashMap;
import java.util.Map;
//import java.util.List;
//import java.util.Scanner;
//import java.util.ArrayList;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Logar{
    public static void main(String[] args) {
        Class Usuario;
     }
    public class Usuario {
        public String username;
        public String password;

        public Usuario(String username, String password) {
            this.username = username;
            this.password = password;
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }
    }
}
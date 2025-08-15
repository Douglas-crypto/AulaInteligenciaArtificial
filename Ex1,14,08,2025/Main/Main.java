package Main;
import java.util.List;
import java.util.Scanner;

import ClassPessoa.Pessoa;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Pessoa cadastro = new Pessoa();
        
         List<Pessoa> pessoas = cadastro.cadastrarPessoas(sc);
        
        cadastro.mostrarMaioresComIMC(pessoas);
        
        sc.close();
    }
}
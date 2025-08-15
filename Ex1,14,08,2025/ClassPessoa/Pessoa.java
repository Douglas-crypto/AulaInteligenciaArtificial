package ClassPessoa;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Pessoa {
    private String nome;
    private double altura;
    private int idade;
    private double peso;

    public String getNome() {
        return nome;
    }

    public double getAltura() {
        return altura;
    }

    public int getIdade() {
        return idade;
    }

    public double getPeso() {
        return peso;
    }

    public List<Pessoa> cadastrarPessoas(Scanner sc) {  
        List<Pessoa> pessoas = new ArrayList<>();
        int nCadastro = 4;

        for(int i = 0; i < nCadastro; i++) {
            Pessoa pessoa = new Pessoa();

            System.out.println("Informe o seu nome: ");
            pessoa.nome = sc.nextLine();

            System.out.println("Informe a sua altura: ");
            pessoa.altura = sc.nextDouble();
            sc.nextLine(); 

            System.out.println("Informe a sua idade: ");
            pessoa.idade = sc.nextInt();
            sc.nextLine(); 

            System.out.println("Informe o seu peso: ");
            pessoa.peso = sc.nextDouble();
            sc.nextLine(); 

            pessoas.add(pessoa);
        }
        return pessoas;
    }

    public double calcularIMC() {
        return peso / (altura * altura);
    }

   public boolean ehMaiorIdade() {
        return idade >= 18;
    }
    
    public void mostrarMaioresComIMC(List<Pessoa> pessoas) {
        
        for(Pessoa p : pessoas) {
            if(p.ehMaiorIdade()) {
                System.out.printf("%s - IMC: %.2f", 
                                p.getNome(), 
                                p.calcularIMC());
            }
        }
    }
}
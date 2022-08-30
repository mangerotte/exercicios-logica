import java.util.Locale;
import java.util.Scanner;

public class Exercicio33 {
     /* 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
    de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
    em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
    ela não pode exceder 30% do salário ou então o empréstimo será negado.*/

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.println("Qual e o valor da casa que deseja o emprestimo? ");
        double valorCasa = sc.nextDouble();
        System.out.println("Qual e o salario do comprador?");
        double valorSalario = sc.nextDouble();
        System.out.println("Quantas parcelas sera o emprestimo?");
        int parcelas = sc.nextInt();

        double valorParcela = valorCasa / parcelas;
        double porcentagem = 0.3;

        if (valorParcela > (valorSalario * porcentagem)) {
            System.out.println("Emprestimo negado!");
        } else {
            System.out.println("Emprestimo aceito!");
        }
    }
}

import java.util.Locale;
import java.util.Scanner;

public class Exercicio03 {

    /*3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
final uma mensagem.
    Ex:
        Nome do Funcionário: Maria do Carmo
        Salário: 1850,45
        O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.*/

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Locale.setDefault(Locale.US);

        System.out.print("Nome do funcionario: ");
        String name = sc.nextLine();
        System.out.print("Salario: ");
        double salary = sc.nextDouble();
        System.out.printf("O funcionario(a) %s tem um salario de R$ %.2f em Junho", name, salary);
    }
}

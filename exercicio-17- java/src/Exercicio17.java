import java.util.Locale;
import java.util.Scanner;

public class Exercicio17 {

    /* 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida. */

    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Velocidade do carro: ");
        double velocidade = sc.nextDouble();

        if (velocidade > 80) {
            double multa = (velocidade - 80) * 5;
            System.out.printf("Voce ultrapassou a velocidade limite, sua multa e de R$ %.2f", multa);
        }
        else {
            System.out.println("Voce esta dentro da velocidade permitida!");
        }
    }
}

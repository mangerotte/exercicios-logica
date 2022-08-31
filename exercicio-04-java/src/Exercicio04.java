import model.ParImpar;

import java.util.Scanner;

public class Exercicio04 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ParImpar x = new ParImpar();


        for (int i = 0; i < 7; i++) {
            System.out.print("Digite um numero: ");
            int n = sc.nextInt();
            sc.nextLine();
            x.verificao(n);

        }
        System.out.println("Os valores pares digitados foram " + x.getPar());
        System.out.println("Os valores ímpares digitados foram " + x.getImpar());

    }
}

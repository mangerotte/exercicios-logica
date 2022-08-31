import model.Sorteio;

import java.util.Scanner;

public class Exercicio112 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Sorteio sorteio = new Sorteio();

        System.out.print("Quantos numeros voce quer que eu sorteie? ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            sorteio.sorteio();
            System.out.print("Jogo " + (i +1) + sorteio);
            System.out.println();
            sorteio = new Sorteio();
        }


    }
}

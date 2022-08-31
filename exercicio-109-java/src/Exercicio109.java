import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio109 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();
        List<Integer> par = new ArrayList<>();
        List<Integer> impar = new ArrayList<>();

        while (true) {
            System.out.print("Digite um numero: ");
            int n = sc.nextInt();
            sc.nextLine();
            list.add(n);
            System.out.print("Deseja continuar? [S] ou [N]: ");
            char sair = sc.nextLine().toUpperCase().charAt(0);
            if (sair == 'N') {
                break;
            }
            if (n % 2 == 0) {
                par.add(n);
            }
            else {
                impar.add(n);
            }
        }
        System.out.println("A lista completa e " + list);
        System.out.println("A lista de numeros pares e " + par);
        System.out.println("A lista de numeros impares e " + impar);
    }
}

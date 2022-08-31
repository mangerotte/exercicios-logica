import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Exercicio108 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();

        while (true) {
            System.out.print("Digite um numero: ");
            int n = sc.nextInt();
            sc.nextLine();
            list.add(n);
            System.out.print("Deseja continuar? [S]im [N]ao: ");
            char sair = sc.nextLine().toUpperCase().charAt(0);

            if (sair == 'N'){
                break;
            }
        }
        System.out.printf("Voce digitou %d elementos%n", list.size());
        Collections.sort(list, Collections.reverseOrder());
        System.out.println("Os valores em ordem decrescente e " + list);
        Integer numero5 = list.stream().filter(x-> x == 5).findFirst().orElse(null);
        if (numero5 == null) {
            System.out.println("O valor 5 nao foi encontrado na lista!");
        }
        else {
            System.out.println("O valor 5 foi encontrado na lista!");
        }
    }
}

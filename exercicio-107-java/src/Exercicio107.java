import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio107 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            System.out.print("Digite um numero: ");
            int n = sc.nextInt();
            if (i == 0) {
                list.add(n);
                System.out.printf("%d adicionado no final da lista.%n", n);
            } else {
                int lastidx = list.size() - 1;
                int lastElement = list.get(lastidx);
                if (n > lastElement) {
                    list.add(n);
                    System.out.printf("%d adicionado no final da lista.%n", n);
                } else if (n > list.get(0) && n < lastElement) {
                    list.add(1, n);
                    System.out.printf("%d adicionado na posicao 1%n", n);
                } else {
                    list.add(0, n);
                    System.out.printf("%d adicionado no comeco da lista%n", n);
                }
            }
        }
        for (Integer x : list){
            System.out.printf("[%d] ", x);
        }
    }
}

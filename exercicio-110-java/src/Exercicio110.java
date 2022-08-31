import model.Pessoas;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercicio110 {

    public static void main(String[] args) {

        List<Pessoas> listA = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        Pessoas humano = new Pessoas();
        double maior = 0, menor = 0;
        String nome_pesado = "", nome_leve = "";

        while (true) {
            System.out.print("Nome: ");
            String nome = sc.nextLine();
            System.out.print("Peso: ");
            double peso = sc.nextDouble();
            sc.nextLine();

            if (listA.size() == 0){
                maior = peso;
                menor = peso;
            }
            System.out.print("Deseja continuar? [S] [N]: ");
            char sair = sc.nextLine().toUpperCase().charAt(0);

            humano = new Pessoas(nome,peso);
            listA.add(humano);

            if (sair == 'N') {
                break;
            }
        }
        for (Pessoas p : listA) {
            double peso = p.getPeso();
            String pesado = p.getName();
            String levim = p.getName();
            if (peso >= maior){
                maior = peso;
                nome_pesado = pesado;
            } else if (peso <= menor) {
                menor = peso;
                nome_leve = levim;
            }
        }

        System.out.printf("Foram cadastradas %d pessoas.%n", listA.size());
        System.out.printf("A pessoa mais pesada cadastrada foi %s com o peso de %.2f%n", nome_pesado, maior);
        System.out.printf("A pessoa mais leve cadastrada foi %s com o peso de %.2f%n", nome_leve, menor);



    }
}

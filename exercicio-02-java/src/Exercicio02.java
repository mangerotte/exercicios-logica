import java.util.Scanner;

public class Exercicio02 {

    /* 2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela:
    Ex:
    Qual é o seu nome? João da Silva
    Olá João da Silva, é um prazer te conhecer!*/

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Qual é o seu nome?" );
        String name = sc.nextLine();
        System.out.printf("Olá %s, é um prazer te conhecer!", name);
    }

}

package model;

public class Pessoas {
    String name;
    Double peso;

    public Pessoas() {

    }

    public Pessoas(String name, Double peso) {
        this.name = name;
        this.peso = peso;
    }

    public String getName() {
        return name;
    }

    public Double getPeso() {
        return peso;
    }

    @Override
    public String toString() {
        return "Pessoas{" +
                "name='" + name + '\'' +
                ", peso=" + peso;

    }
}

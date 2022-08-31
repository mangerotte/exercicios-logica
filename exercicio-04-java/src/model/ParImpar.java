package model;

import java.util.ArrayList;
import java.util.List;

public class ParImpar {

    List<Integer> par = new ArrayList<>();
    List<Integer> impar = new ArrayList<>();

    public ParImpar() {
    }

    public void verificao(int n) {
        if (n % 2 == 0){
            par.add(n);
        }
        else {
            impar.add(n);
        }
    }

    public List<Integer> getPar() {
        return par;
    }

    public List<Integer> getImpar() {
        return impar;
    }
}

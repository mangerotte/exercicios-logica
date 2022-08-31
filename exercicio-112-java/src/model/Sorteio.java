package model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Sorteio {

    Random nRandom = new Random();
    List<Integer> list = new ArrayList<>();

    public Sorteio() {
    }

    public List<Integer>sorteio() {
        for (int i = 0; i < 7; i++){
            list.add(nRandom.nextInt(60)); }
        return list;
    }

    @Override
    public String toString() {
        return String.valueOf(list);
    }

    public List<Integer> getList(int i) {
        return list;
    }
}

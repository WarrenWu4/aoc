import java.util.Scanner;
import java.util.HashSet;

class Pair {
    public int x, y;
    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
    @Override
    public boolean equals(Object o) {
        if (o instanceof Pair) {
            Pair p = (Pair) o;
            return this.x == p.x && this.y == p.y;
        }
        return false;
    }
    @Override
    public int hashCode() {
        return Integer.hashCode(x) * 31 + Integer.hashCode(y);
    }
}

public class Main {
    static void partOne(String input) {
        String[] parts = input.split(", ");
        Pair dir = new Pair(0, -1);
        Pair pos = new Pair(0, 0);
        for (int i = 0; i < parts.length; i++) {
            char c = parts[i].charAt(0);
            int num = Integer.parseInt(parts[i].substring(1));
            if (c == 'L') {
                int temp = dir.x;
                dir.x = -dir.y;
                dir.y = temp;
            } else {
                int temp = dir.x;
                dir.x = dir.y;
                dir.y = -temp;
            }
            pos.x = pos.x+dir.x*num;
            pos.y = pos.y+dir.y*num;
        }
        System.out.println(Math.abs(pos.x) + Math.abs(pos.y));
    }

    static void partTwo(String input) {
        String[] parts = input.split(", ");
        Pair dir = new Pair(0, -1);
        Pair pos = new Pair(0, 0);
        HashSet<Pair> visited = new HashSet<>();
        visited.add(new Pair(0, 0));
        for (int i = 0; i < parts.length; i++) {
            char c = parts[i].charAt(0);
            int num = Integer.parseInt(parts[i].substring(1));
            if (c == 'L') {
                int temp = dir.x;
                dir.x = -dir.y;
                dir.y = temp;
            } else {
                int temp = dir.x;
                dir.x = dir.y;
                dir.y = -temp;
            }
            for (int j = 0; j < num; j++) {
                pos.x = pos.x+dir.x;
                pos.y = pos.y+dir.y;
                if (visited.contains(pos)) {
                    System.out.println(Math.abs(pos.x) + Math.abs(pos.y));
                    return;
                }
                visited.add(new Pair(pos.x, pos.y));
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        partOne(input);
        partTwo(input);
        sc.close();
    }
}

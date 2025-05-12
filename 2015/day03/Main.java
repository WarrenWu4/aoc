import java.util.*;

class Coord {
    int x, y;

    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) { return true; }
        if (!(o instanceof Coord)) { return false; }
        Coord coord = (Coord) o;
        return x == coord.x && y == coord.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}

public class Main {
    static HashMap<Character, Coord> map = new HashMap<>(
        Map.of(
            '^', new Coord(0, 1),
            'v', new Coord(0, -1),
            '<', new Coord(-1, 0),
            '>', new Coord(1, 0)
        )
    );

    static void partOne(String input) {
        Set<Coord> visited = new HashSet<>();
        int x = 0, y = 0;
        visited.add(new Coord(x, y));
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            x += map.get(c).x;
            y += map.get(c).y;
            visited.add(new Coord(x, y));
        }
        System.out.println(visited.size());
    }

    static void partTwo(String input) {
        Set<Coord> visited = new HashSet<>();
        int sX = 0, sY = 0, rX = 0, rY = 0;
        visited.add(new Coord(rX, rY));
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (i % 2 == 0) {
                sX += map.get(c).x;
                sY += map.get(c).y;
                visited.add(new Coord(sX, sY));
            } else {
                rX += map.get(c).x;
                rY += map.get(c).y;
                visited.add(new Coord(rX, rY));
            }
        }
        System.out.println(visited.size());
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        partOne(input);
        partTwo(input);
        sc.close();
    }
}

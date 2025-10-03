import java.util.*;

class Main {
    public static void partOne(String input) {
        int floor = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == ')') {
                floor--;
            } else {
                floor++;
            }
        }
        System.out.println(floor);
    }

    public static void partTwo(String input) {
        int floor = 0;
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == ')') { floor--; }
            else { floor++; }
            if (floor == -1) {
                System.out.println(i+1);
                break;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        partOne(input);
        partTwo(input);
    }
}

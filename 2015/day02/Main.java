import java.util.*;

class Rectangle {
    int l, w, h;
    int[] sides = new int[3];

    Rectangle(int l, int w, int h) {
        this.l = l;
        this.w = w;
        this.h = h;
        sides[0] = l*w;
        sides[1] = w*h;
        sides[2] = h*l;
    }

    int getWrappingSize() {
        return 2*(sides[0]+sides[1]+sides[2]) + Arrays.stream(sides).min().getAsInt();
    }

    int getRibbonSize() {
        int[] measurements = {l, w, h};
        Arrays.sort(measurements);
        return 2*(measurements[0] + measurements[1]) + l*w*h;
    }
}

public class Main {
    public static void partOne(ArrayList<Rectangle> input) {
        int wrappingSize = 0;
        for (int i = 0; i < input.size(); i++) {
            wrappingSize += input.get(i).getWrappingSize();
        }
        System.out.println(wrappingSize);
    }

    public static void partTwo(ArrayList<Rectangle> input) {
        int ribbonSize = 0;
        for (int i = 0; i < input.size(); i++) {
            ribbonSize += input.get(i).getRibbonSize();
        }
        System.out.println(ribbonSize);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Rectangle> input = new ArrayList<>();
        while (scanner.hasNext()) {
            String value = scanner.next();
            String[] dimensions = value.split("x");
            input.add(new Rectangle(
                Integer.parseInt(dimensions[0]),
                Integer.parseInt(dimensions[1]),
                Integer.parseInt(dimensions[2])
            ));
        }
        partOne(input);
        partTwo(input);
        scanner.close();
    } 
}

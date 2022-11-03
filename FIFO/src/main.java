import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Queue<String> queue = new Queue<>();
        Scanner input = new Scanner(System.in);
        while (input.hasNextLine()) {
            String s = input.nextLine();
            if (s.isEmpty()) break;
            queue.push(s);
        }
        String popped;
        do {
            popped = queue.pop();
            if (popped != null)
                System.out.println(capitalize(popped));
        } while (popped != null);
    }

    private static String capitalize(final String s) {
        String[] words = s.split(" ");
        StringBuilder builder = new StringBuilder();
        for (String word : words) {
            builder.append(word.substring(0, 1).toUpperCase()).append(word.substring(1)).append(" ");
        }
        return builder.toString();
    }
}
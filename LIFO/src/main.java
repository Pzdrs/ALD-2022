import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();
        Scanner input = new Scanner(System.in);
        while(input.hasNextLine()) {
            String s = input.nextLine();
            if (s.isEmpty()) break;
            stack.push(s);
        }
        stack.print();
    }
}
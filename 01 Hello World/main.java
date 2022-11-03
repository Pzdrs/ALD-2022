import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
        	int n = scanner.nextInt();
          	for(int i = 0; i < n; i++) System.out.println("Hello world!");
        } catch(NumberFormatException ignored) {

        }
    }
}
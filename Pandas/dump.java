import java.util.*;

class dump {
    public static void main(String[] args) {
        // System.out.println("Avanish Singh, Welcome");
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 2 * (n - 1) - (2 * i - 1); j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        scan.close();
    }
}
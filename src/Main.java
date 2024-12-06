import java.util.Scanner;

public class Calculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("выберите операцию:");
            System.out.println("1. Сложение");
            System.out.println("2. Вычитание");
            System.out.println("3. Умножение");
            System.out.println("4. Деление");
            System.out.println("5. Деление с остатком");

            int choice = scanner.nextInt();

            System.out.print("Первое число: ");
            double chislo1 = sпcanner.nextDouble();

            System.out.print("Второе число: ");
            double chislo2 = scanner.nextDouble();

            double rezultat;

            if (choice == 1) {
                rezultat = chislo1 + chislo2;
                System.out.println("результат: " + rezultat)
            } else if (choice == 2) {
                rezultat = chislo1 - chislo2;
                System.out.println("результат: " + rezultat);
            } else if (choice == 3) {
                rezultat = chislo1 * chislo2;
                System.out.println("результат: " + rezultat);
            } else if (choice == 4) {
                if (chislo2 == 0) {
                    System.out.println("на ноль делить нельзя");
                } else {
                    rezultat = chislo1 / chislo2;
                    System.out.println("результат: " + rezultat);
                }
            } else if (choice == 5) {
                if (chislo2 == 0) {
                    System.out.println("на ноль делить нельзя ");
                } else {
                    rezultat = chislo1 % chislo2;
                    System.out.println("результат: " + rezultat);
                }
            } else {
                System.out.println("такой операции нет");
            }
        }

        scanner.close();
    }
}
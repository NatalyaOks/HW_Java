// Вычислить n-ое треугольного число(сумма чисел от 1 до n), n! (произведение чисел от 1 до n)

package HW1;
import java.util.Scanner;

public class Primer {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int result = 0;
        int result2 = 0;
        
            System.out.printf("Введите число: ");
            int number = scan.nextInt();
            if (number > 0){
                result = factorial(number);
                System.out.printf("Факториал числа %d = %d .\n",number, result);
                result2 = rectangle(number);
                System.out.printf("%d-e треугольное число = %d .\n",number, result2);
                scan.close();
            }}
    

    private static int factorial(int num){
        int factor = 1;
        if (num == 1 || num == 0){
            return factor;
        }
        factor = num * factorial(num -1);
        return factor;
    }


    private static int rectangle (int num){
        int rectan = 1;
        if (num == 1 || num == 0){
            return rectan;
        }
        rectan = num + rectangle(num -1);
        return rectan;
    }
    private static boolean isNumeric(String str){
        return str.matches("\\d$");
    }
}

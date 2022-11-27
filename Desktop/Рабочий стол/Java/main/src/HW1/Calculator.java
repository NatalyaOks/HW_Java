package HW1;
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);         
        System.out.print("Введите число: ");         
        double a = scan.nextDouble();           
        System.out.print("Введите второе число: ");         
        double b = scan.nextDouble();         
        System.out.printf("Укажите какое действие нужно сделать: ");  
        char c = scan.next().charAt(0); 
        double ans;    
        switch (c) {
            case '+': ans = a + b;
            break;
            case '-': ans = a - b;
            break;
            case '*': ans = a * b;
            break;
            case '/': ans = a / b;
            break;
            default: System.out.print("Некорректно указано действие");
            return;
} 
        System.out.print(a + " " + c + " " + b + " = " + ans);
        }}


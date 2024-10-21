import java.util.Scanner;
public class IC{
    public static void main(String[] args){
        int x;
        double y;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=x*2.54;
        System.out.printf("%.2f",y);
    }
}
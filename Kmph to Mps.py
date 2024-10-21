import java.util.Scanner;
public class KM{
    public static void main(String[] args){
        int x;
        double y;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=((double)x)*5.0/18.0;
        System.out.printf("%.2f",y);
    }
}
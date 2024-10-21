import java.util.Scanner;
public class Lp{
    public static void main(String[] args){
        int x,y;
        double z;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=sc.nextInt();
        z=((double)(x-y)/x)*100.0;
        System.out.printf("%.2f",z);
    }
}
import java.util.Scanner;
public class A{
    public static void main(String[] args){
        int r;
        double z;
        Scanner sc=new Scanner(System.in);
        r=sc.nextInt();
        z=(double)(3.14)*r*r;
        System.out.printf("%.2f",z);
    }
}
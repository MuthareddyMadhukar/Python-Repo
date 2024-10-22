import java.util.Scanner;
public class Ap{
    public static void main(String[] args){
        int m,n;
        Scanner sc=new Scanner(System.in);
        m=sc.nextInt();
        n=sc.nextInt();
        System.out.printf("Sum:%d%n",m+n); 
        System.out.printf("Difference:%d%n",m-n);
        System.out.printf("Product:%d%n",m*n); 
        System.out.printf("Quotient:%d%n",m/n); 
        System.out.printf("Remainder:%d%n",m%n);
    }
}
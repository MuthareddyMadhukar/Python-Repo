import java.util.Scanner;
public class D{
    public static void main(String[] args){
        int d,n;
        Scanner sc=new Scanner(System.in);
        d=sc.nextInt();
        n=d/365;
        System.out.printf("%d%n",n);
        System.out.printf("%d%n",((d-(n*365))/7));
    }
}
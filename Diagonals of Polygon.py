import java.util.Scanner;
public class P{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n,p;
        n=sc.nextInt();
        p=n*(n-3)/2;
        System.out.printf("%d",p);
    }
}
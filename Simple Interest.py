import java.util.Scanner;
public class S{
    public static void main(String[] args){
        int p,t,r;
        int s;
        Scanner sc=new Scanner(System.in);
        p=sc.nextInt();
        t=sc.nextInt();
        r=sc.nextInt();
        s= (p*t*r)/100;
        System.out.printf("%d",s);
    }
}
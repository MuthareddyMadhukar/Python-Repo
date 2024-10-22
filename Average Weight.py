import java.util.Scanner;
public class Avg{
    public static void main(String[] args){
        int x,y,z,p;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=sc.nextInt();
        z=sc.nextInt();
        p=(3*x)-y-z;
        System.out.printf("%d",p);

    }
}
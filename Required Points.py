import java.util.Scanner;
public class Rp{
    public static void main(String[] args){
        int x,y,z;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=sc.nextInt();
        z=y/x;
        System.out.printf("%d",z);
    }
}
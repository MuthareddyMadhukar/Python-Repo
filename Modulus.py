import java.util.Scanner;
public class M{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        System.out.printf("%d",x%y);
    }
}
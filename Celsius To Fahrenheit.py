import java.util.Scanner;
public class T{
    public static void main(String[] args){
        int c;
        double f;
        Scanner sc=new Scanner(System.in);
        c=sc.nextInt();
        f=(double)(c*1.80)+32;
        System.out.printf("%.2f",f);
    }
}
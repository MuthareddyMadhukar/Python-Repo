import java.util.Scanner;
public class PP{
    public static void main(String[] args){
        int x,y;
        double z;
        Scanner sc=new Scanner(System.in);
        x=sc.nextInt();
        y=sc.nextInt();
        z=((double)(y-x)*100.0)/x;
        System.out.printf("%.2f",z);
    }
}
import java.util.Scanner;
public class C{
    public static void main(String[] args){
      Scanner sc=new Scanner(System.in);
      int x,y,z;
      x=sc.nextInt();
      y=sc.nextInt();
      z=sc.nextInt();
      System.out.printf("%d KB",x*y*z);  
    }
}
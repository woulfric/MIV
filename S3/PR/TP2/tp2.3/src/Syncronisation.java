//package Threadwithoutsyn;

class Power{
    synchronized static void printPower(int n){     
        // System.out.println("this is the Thread :"+Thread.currentThread().getName());   
            int temp = 1;
            for(int i = 1; i <= 5; i++){
                System.out.println(Thread.currentThread().getName() + ": - " + n+  "." + i + " value: " + n*temp);
                temp = n*temp;
                try {
                    Thread.sleep(500);
                } catch (Exception e) {
                    System.out.println(e);
                }
            }
    }
}

class Thread1 extends Thread{
    Power p;
    Thread1(Power p){
        this.p = p;
    }
    public void run(){
        p.printPower(2);
    }
}

class Thread2 extends Thread{
    Power p;
    Thread2(Power p){
        this.p = p;
    }
    public void run(){
        p.printPower(3);
    }
}
class Thread3 extends Thread{
    Power p;
    Thread3(Power p){
        this.p = p;
    }
    public void run(){
        p.printPower(5);
    }
}
class Thread4 extends Thread{
    Power p;
    Thread4(Power p){
        this.p = p;
    }
    public void run(){
        p.printPower(8);
    }
}

public class Syncronisation {
    public static void main(String[] args){
        Power obj = new Power();
        Power obj2 = new Power();
        Thread1 p1 = new Thread1(obj);
        Thread2 p2 = new Thread2(obj);
        Thread3 p3 = new Thread3(obj2);
        Thread4 p4 = new Thread4(obj2);

        p1.start();
        p2.start();
        p3.start();
        p4.start();
    }
}
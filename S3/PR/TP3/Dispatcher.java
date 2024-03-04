import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;


public class Dispatcher extends Thread {
    private Socket socket;
    private int clientNumber;
    private int superclient;
    private int targetNumber;

    public Dispatcher(Socket socket, int clientNumber,int targetNumber) {
        super();
        this.socket = socket;
        this.clientNumber = clientNumber;
        this.targetNumber=targetNumber;
        
        // Utilisez ScheduledExecutorService pour changer le superclient toutes les 30 secondes
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
        scheduler.scheduleAtFixedRate(this::changeSuperclient, 0, 30, TimeUnit.SECONDS);
    }

    private void changeSuperclient() {
        this.superclient = getRandomSuperclient();
        System.out.println("Superclient changed to: " + superclient);
         // Informez les clients du changement de superclient
         //broadcast("Superclient changed to: " + superclient);
    }

    private int getRandomSuperclient() {
        Random random = new Random();
        return random.nextInt(5) + 1;
    }
    public void run() {
        try {

           

            // Affichez le numéro superclient généré
            System.out.println("Superclient number: " + superclient);

            InputStream input = socket.getInputStream();
            InputStreamReader ins = new InputStreamReader(input);
            BufferedReader br = new BufferedReader(ins);
            OutputStream output = socket.getOutputStream();
            PrintWriter pw = new PrintWriter(output, true);

            pw.println("You are player number: " + clientNumber);
            System.out.println("Connection from client " + clientNumber);
            System.out.println("IP: " + socket.getRemoteSocketAddress());
            if(clientNumber==superclient)
            {
                pw.println("You are a super client ..!");
            }

            while (true) {

                pw.println("Devinez la valeur secrete");
                String request = br.readLine();
                int newRequest = Integer.parseInt(request);
                
                if(superclient==clientNumber)
                {
                    if (newRequest == targetNumber) {
                        pw.println("You found the value");
                        Thread.currentThread().interrupt();
                    } else {
                        pw.println("Try again");
                    }
                }else 
                {
                    if( newRequest %2 == 0 ){
                        newRequest = newRequest/2;
                        pw.println("value changed to:"+newRequest);
                        if (newRequest == targetNumber) {
                            pw.println("You found the value");
                            Thread.currentThread().interrupt();
                    } else {
                        pw.println("Try again");
                    }
                    
                    }else{
                        newRequest = (newRequest*3)/2;
                        pw.println("value changed to:"+newRequest);
                        if (newRequest == targetNumber) {
                            String adressWinner = socket.getRemoteSocketAddress().toString();
                            PrintWriter PG = new PrintWriter(socket.getOutputStream(),true);
                            pw.println("You found the value");
                            Thread.currentThread().interrupt();
                    } else {
                        pw.println("Try again");
                    }
                    }
                } 

                }
        } catch (IOException e) {
            System.err.println("The winner is: " + socket.getRemoteSocketAddress());
        }
    }
}


import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

public class serveur extends Thread {
  
    private int clientNumber = 0;

    public void run() {
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            Random random = new Random();
            int targetNumber=random.nextInt(100);
            System.out.println("Number to guess: " + targetNumber);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                ++clientNumber;
                new Dispatcher(clientSocket, clientNumber,targetNumber).start();
            }
        } catch (IOException e) {
            System.err.println("An error occurred");
        }
    }
    
    public static void main(String[] args) {
        new serveur().start();
        System.err.println("Server is up and running");
    }
}
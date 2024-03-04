import java.io.*;
import java.net.*;
import java.util.Scanner;

public class client {
    public static void main(String[] args) {
        try {
            Socket clientSocket = new Socket("127.0.0.1", 12345);
            InputStream input = clientSocket.getInputStream();
            OutputStream output = clientSocket.getOutputStream();
            PrintWriter pw = new PrintWriter(output, true);
            BufferedReader br = new BufferedReader(new InputStreamReader(input));
            boolean stop = false;

            Scanner scanner = new Scanner(System.in);

            while (true) {
                String serverResponse = br.readLine();
                System.out.println(serverResponse);

                if ("You found the value".equals(serverResponse)) {
                    stop = true;
                    scanner.close();
                    clientSocket.close();
                }

                if (!stop) {
                    System.out.print("Choose a number between 0 and 100: ");
                    String userInput = scanner.nextLine();
                    pw.println(userInput);
                }
            }
        } catch (IOException e) {
            System.err.println("An error occurred");
        }
    }
}

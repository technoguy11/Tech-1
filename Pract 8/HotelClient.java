// HotelClient.java
import java.rmi.Naming;
import java.util.Scanner;

public class HotelClient {
    public static void main(String[] args) {
        try {
            HotelServiceInterface hotelService = (HotelServiceInterface)
                    Naming.lookup("rmi://localhost/HotelService");

            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("\n1. Book a room");
                System.out.println("2. Cancel booking");
                System.out.println("3. Exit");
                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1:
                        System.out.print("Enter guest name: ");
                        String guestName = scanner.nextLine();
                        System.out.print("Enter room number: ");
                        int roomNumber = scanner.nextInt();
                        scanner.nextLine();
                        if (hotelService.bookRoom(guestName, roomNumber)) {
                            System.out.println("Room booked successfully!");
                        } else {
                            System.out.println("Room booking failed.");
                        }
                        break;
                    case 2:
                        System.out.print("Enter guest name for cancellation: ");
                        String cancelGuestName = scanner.nextLine();
                        if (hotelService.cancelBooking(cancelGuestName)) {
                            System.out.println("Booking canceled successfully!");
                        } else {
                            System.out.println("Booking cancellation failed.");
                        }
                        break;
                    case 3:
                        System.out.println("Exiting...");
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

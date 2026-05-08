// HotelServer.java
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {
    private final Map<Integer, String> bookedRooms;

    public HotelServer() throws RemoteException {
        bookedRooms = new HashMap<>();
    }

    @Override
    public synchronized boolean bookRoom(String guestName, int roomNumber) throws RemoteException {
        if (!bookedRooms.containsKey(roomNumber)) {
            bookedRooms.put(roomNumber, guestName);
            System.out.println("Room " + roomNumber + " booked for " + guestName);
            return true;
        }
        System.out.println("Room " + roomNumber + " is already booked.");
        return false;
    }

    @Override
    public synchronized boolean cancelBooking(String guestName) throws RemoteException {
        Integer toRemove = null;
        for (Map.Entry<Integer, String> entry : bookedRooms.entrySet()) {
            if (entry.getValue().equals(guestName)) {
                toRemove = entry.getKey();
                break;
            }
        }
        if (toRemove != null) {
            bookedRooms.remove(toRemove);
            System.out.println("Booking canceled for " + guestName);
            return true;
        }
        System.out.println("No booking found for " + guestName);
        return false;
    }

    public static void main(String[] args) {
        try {
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            HotelServer server = new HotelServer();
            Naming.rebind("HotelService", server);
            System.out.println("Hotel Server is running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

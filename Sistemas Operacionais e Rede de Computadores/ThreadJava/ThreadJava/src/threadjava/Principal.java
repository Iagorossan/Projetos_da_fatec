package threadjava;

import java.util.logging.Level;
import java.util.logging.Logger;

public class Principal {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("Ola");
        
        System.out.println("Incicializando 1°Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 1° Thread");
        
        System.out.println("Incicializando 2°Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 2° Thread");
        
        System.out.println("Incicializando 3°Thread");
        Thread.sleep(1000);
        System.out.println("Finalizando 3° Thread");
        System.out.println("============Incializando código das Threads================");
                
        new Thread(() -> {
            System.out.println("Incicializando 1° Thread");
            try {
                Thread.sleep(1000);
                
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            System.out.println("Finalizando 1° Thread");
            
        }).start();
        
        
        new Thread(() -> {
            System.out.println("Incicializando 2° Thread");
            try {
                Thread.sleep(1000);
                
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            System.out.println("Finalizando 2° Thread");
            
        }).start();
        
        
        new Thread(() -> {
            System.out.println("Incicializando 3° Thread");
            try {
                Thread.sleep(1000);
                
            } catch (InterruptedException ex) {
                Logger.getLogger(Principal.class.getName()).log(Level.SEVERE, null, ex);
            }
            
            System.out.println("Finalizando 3° Thread");
            
        }).start();
    }
    
}

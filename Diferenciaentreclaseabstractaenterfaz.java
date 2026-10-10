// Clase abstracta
abstract class Figura {
    protected String nombre;

    public Figura(String nombre) {      // las abstractas SI tienen constructor
        this.nombre = nombre;
    }

    public abstract double area();      // sin cuerpo: las hijas deben implementarlo

    public void mostrar() {             // metodo normal, ya implementado
        System.out.println(nombre + " -> area: " + area());
    }
}

// Interfaz
interface Dibujable {
    void dibujar();                     // abstracto por defecto

    default void borrar() {             // metodo con cuerpo (Java 8+)
        System.out.println("Borrando dibujo...");
    }
}

// Hereda de UNA clase (extends) e implementa las interfaces que quiera (implements)
class Circulo extends Figura implements Dibujable {
    private double radio;

    public Circulo(double radio) {
        super("Circulo");
        this.radio = radio;
    }

    @Override
    public double area() {
        return Math.PI * radio * radio;
    }

    @Override
    public void dibujar() {
        System.out.println("Dibujando un circulo de radio " + radio);
    }
}

// Clase principal (la unica public, debe llamarse igual que el archivo)
public class Main {
    public static void main(String[] args) {
        Circulo c = new Circulo(5);
        c.mostrar();
        c.dibujar();
        c.borrar();
        // Figura f = new Figura("x");   // ERROR: no se puede instanciar una clase abstracta
    }
}
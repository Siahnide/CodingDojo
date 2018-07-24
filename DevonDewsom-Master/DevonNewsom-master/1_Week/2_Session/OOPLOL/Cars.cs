namespace OOPLOL.Stuff
{
    public abstract class Vehicle
    {
        // Cubic Centimeters
        public double EngineSize;
        public int NumWheels;
    }
    public class Car : Vehicle
    {
        // Object Contruction
        public Car(double engineSize)
        {
            NumWheels = 4;
            EngineSize = engineSize;
        }
        public void HonkHorn()
        {
            System.Console.WriteLine("BEEP BEEP");
        }
    }
    public class Corvette : Car
    {
        // We can get EngineSize UP to our parent in our Corvette Constructor
        public Corvette() : base (800)
        {

        }
    }
    public class Bus : Vehicle
    {
        public Bus(int numWheels)
        {
            NumWheels = numWheels;
            EngineSize = 2000;
        }
    }
}
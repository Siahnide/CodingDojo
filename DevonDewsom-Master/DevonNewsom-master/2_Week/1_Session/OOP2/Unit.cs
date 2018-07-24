namespace OOP2.RTS
{
    interface IDamagable
    {
        // 
        int Health {get;set;}
        int TakeDamage(int amount);
    }
    public abstract class Unit : IDamagable
    {
        // Method Signature
        protected int distanceTraveled = 0;
        public int Health {get;set;}
        public abstract int TakeDamage(int amount);

        public abstract int Walk(int distance);
        public Unit()
        {
            Health = 100;
        }
    }
    public class Melee : Unit
    {
        public override int Walk(int distance)
        {
            distanceTraveled += distance;
            return distanceTraveled;
        }
        public override int TakeDamage(int amount)
        {
            Health -= amount;
            return Health;
        }
    }
    public class Swifty : Unit
    {
        private int speedMultiplier = 2;
        public override int Walk(int distance)
        {
            distanceTraveled += (distance * speedMultiplier);
            return distanceTraveled;
        }
        public override int TakeDamage(int amount)
        {
            amount = amount * 2;
            // EVADE!!!
            Health -= amount;
            return Health;
        }
    }
    public class Base : IDamagable
    {
        public int Health {get;set;}
        public int TakeDamage(int amount)    
        {
            Health -= (amount / 2);
            return Health;
        }
        public Base()
        {
            Health = 250;
        }
    }
}
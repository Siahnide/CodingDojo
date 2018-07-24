using System;
using System.Collections.Generic;
using OOP2.RTS;

namespace OOP2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            List<Unit> unitSelection = new List<Unit>()
            {
                new Melee(), new Melee(), new Swifty(), new Swifty()
            };
        }
        public static void WalkSelected(IEnumerable<Unit> units, int distance)
        {
            foreach(Unit u in units)
            {
                u.Walk(distance);
            }
        }
        public static void AOEAttack(IEnumerable<IDamagable> damagables)
        {
            foreach(IDamagable thing in damagables)
            {
                thing.TakeDamage(10);
            }
        }      
    }
}

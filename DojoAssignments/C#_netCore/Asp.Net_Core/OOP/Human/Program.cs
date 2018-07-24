using System;

namespace Human
{
    class Program
    {
        static void Main(string[] args)
        {
            Human me = new Human("Josiah");
            Human dude = new Human("enemy");
            me.Attack(dude);
        }
        public class Human
        {
            public int Health = 100;
            public int Strength = 3;
            public int Inteligence = 3;
            public int Dexterity = 3;
            public string Name;
            public Human(string name)
            {
                Name = name;
            }
            public Human(int hp, int str, int intel, int dex, string name)
            {
                Health = hp;
                Strength = str;
                Inteligence = intel;
                Dexterity = dex;
                Name = name;
            }
            public void Attack(object other)
            {
                Console.WriteLine("Attacking..");
                if (other is Human)
                {
                    Human enemy = new Human("enemy");
                    enemy.Health -= Strength * 5;
                    Console.WriteLine("{0} Dealt damage and {1} lost {2} Health!",Name,enemy.Name,100 - enemy.Health);
                };
            }
        }
    }
}

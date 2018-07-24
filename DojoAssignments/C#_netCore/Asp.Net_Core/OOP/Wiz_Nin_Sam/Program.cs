using System;

namespace Wiz_Nin_Sam
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
        public class Human
        {
            public int Health = 100;
            public int Strength = 3;
            public int Inteligence = 3;
            public int Dexterity = 3;
            public string Name;
            public Human()
            {
            Health = 100;
            Strength = 3;
            Inteligence = 3;
            Dexterity = 3;
            Name = "";
            }
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
        public class Wizard : Human
        {
            public int Health = 50;
            public int Intelligence = 25;
            public void Heal()
            {
                Health += Intelligence * 10;
                Console.WriteLine("{0} Healed for {1} HP!",Name,Intelligence * 10);
            }
            public void Fireball(Human tgt)
            {
                Random rand = new Random();
                int dmg = rand.Next(20,50);
                tgt.Health -= dmg;
                Console.WriteLine("{0} Cast Fireball at {1} and dealt {2} Damage!",Name,tgt,dmg);
                
            }
        }
        public class Ninja : Human
        {
            public int Dexterity = 175;
            public void steal(object tgt)
            {
                Attack(tgt);
                Health += 10;
            }
            public void get_away()
            {
                Health -= 15;
            }

        }
        public class Samurai : Human
        {  
            public int Health = 200;
            
            public void Death_blow(Human tgt)
            {
                if(tgt.Health < 50)
                {
                    tgt.Health = 0;
                }
            }
            public void Meditate()
            {
                Health = 200;
            }
        }
    }
}

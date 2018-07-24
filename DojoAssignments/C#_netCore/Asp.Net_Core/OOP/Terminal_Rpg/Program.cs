using System;
using System.Collections.Generic;

namespace Terminal_Rpg
{
    class Program
    {
        static void Main(string[] args)
        {
            Skeleton dummy = new Skeleton();
            Skeleton E1 = new Skeleton();
            Zombie E2 = new Zombie();
            Skeleton E3 = new Skeleton();
            Skeleton E4 = new Skeleton();
            Game G1 = new Game();
            List<Creature> Players =new List<Creature>();
            Players.Add(E1);
            Players.Add(E2);
            Players.Add(E3);
            Players.Add(E4);
            G1.Encounter(Players);

        }
        public class Entity
        {
            bool hostile = false;
        }
        public class Creature : Entity
        {
            public virtual string Name {get;set;}
            public  virtual int Health {get;set;}
            public virtual int Strength {get;set;}
            public virtual int Attack(Creature tgt)
            {
                int dmg = Strength + 1;
                tgt.Health -= dmg;
                return dmg;
            }
        }
        public class Enemy : Creature
        {
            public virtual string name {get;}

            bool hostile = true;

        }
        public class Zombie : Enemy
        {
            public override string Name { get { return "Zombie"; } }
            public override int Strength { get => _strength; set => _strength = value; }
            private int _health;
            private int _strength;

            public override int Health { get => _health; set => _health = value; }
            public Zombie()
            {
                Health = 30;
                Strength = 4;
            }

        }
        public class Skeleton : Enemy
        {
            public override string Name { get { return "Skeleton"; } }
            public override int Strength { get => _strength; set => _strength = value; }
            private int _health;
            private int _strength;

            public override int Health { get => _health; set => _health = value; }
            public Skeleton()
            {
                Health = 15;
                Strength = 9;
            }
        }
        public class Necromancer : Enemy
        {
            public new int Strength = 0;
            public override int Health {get {return 20;}}

            public override int Attack(Creature tgt)
            {
                Random rand = new Random();
                int dmg = rand.Next(10,15);
                tgt.Health -= dmg;
                Health += dmg;
                return dmg;
            }
        }
        public class Hero : Creature
        {
            private int _health;

            public override int Health { get => _health; set => _health = value; }
            public override int Strength { get { return 14; } }

            public Hero()
            {
                Health = 100;
            }
            public int Rage_Bolt(Creature tgt)
            {
                int dmg = 110 - Health;
                tgt.Health -= dmg;
                return dmg;
            }

        }
        public class Game
        {
            public int players;
            public void Encounter( List<Creature> players)
            {
                Console.WriteLine("Loading Encounter...");
                Console.WriteLine("{0} Enemies Found!",players.Count);
                int count = 0;
                
                Hero Cha = new Hero();
                Pass(players,Cha,0);
            }

            public int Pass(List<Creature> players,Hero Cha,int TurnOrder)
            {
                if(players.Count == 0)
                {
                    Console.WriteLine("Congratulations! you Defeated the monsters!");
                    return 1;
                }
                if (TurnOrder == 0 && players.Count != 0)
                {
                    Turn(Cha,Cha,players,TurnOrder);
                }
                if(TurnOrder < players.Count + 1 && players.Count != 0)
                        {
                            Turn(players[TurnOrder-1],Cha,players,TurnOrder);
                        }
                        if(TurnOrder == players.Count)
                        {
                            TurnOrder = 0;
                            Turn(Cha,Cha,players,TurnOrder);
                        }
                return TurnOrder;
            }

            public void Turn(Creature active,Hero Cha,List<Creature> players,int TurnOrder)
            {
                if(players.Count == 0)
                {
                    return;
                }
                if(active.Health <= 0)
                {
                    players.Remove(players[TurnOrder-1]);
                    
                    Pass(players,Cha, TurnOrder);
                }
                
                
                if(TurnOrder == 0)
                {
                    TurnOrder += 1;
                    HeroTurn(active,Cha,players,TurnOrder);
                }
                if(active.Health > 0 && TurnOrder != 0)
                {
                    if(players.Count == 0)
                    {
                        return;
                    }
                    EnemyTurn(players[TurnOrder-1],Cha,players,TurnOrder);
                }
            }
            public void HeroTurn(Creature active,Hero Cha,List<Creature> players,int TurnOrder)
            {
                if(players.Count == 0)
                {
                    return;
                }
                int count = 0;
                foreach(Enemy x in players)
                {
                    count += 1;
                    if(x.Health >0)
                    {
                    Console.WriteLine("{0}) {1}  ({2} HP)",count,x.Name,x.Health);
                    }
                    if(x.Health <=0)
                    {
                    Console.WriteLine("{0}) {1}  Dead*",count,x.Name);
                    }
                }
                Console.WriteLine("Your Turn!");
                Console.WriteLine("");
                Skeleton dummy = new Skeleton();
                Console.WriteLine("HP {0}",Cha.Health);
                Console.WriteLine("1) Attack:{0} dmg",active.Attack(dummy));
                Console.WriteLine("2) Rage_Bolt:{0} dmg",110 - active.Health);
                string inp = Console.ReadLine();
                int input = Int32.Parse(inp);
                if (input == 1)
                {
                    string output = "Choose Target: ";
                    int Count = 0;
                    foreach(Enemy x in players)
                    {
                        Count += 1;
                        if(x.Health >0)
                        {
                        output += " " + Count + ")" + x.Name ;
                        }
                        if(x.Health <0)
                        {
                            output += "Dead";
                        }
                    }
                    Console.WriteLine(output);
                    string which = Console.ReadLine();
                    int num = Int32.Parse(which) - 1;
                    Console.WriteLine("Dealt {0} Damage to {1}!",active.Attack(players[num]),players[num].Name);
                    Console.WriteLine("~Continue~");
                    Console.ReadLine();
                    Pass(players,Cha,TurnOrder);
                    }
                    if (input == 2)
                    {
                        string output = "Choose Target: ";
                        int Count = 0;
                        foreach(Enemy x in players)
                        {
                            Count += 1;
                            if(x.Health >0)
                            {
                            output += Count + ") " + x.Name ;
                            }
                            
                        }
                        Console.WriteLine(output);
                        string which = Console.ReadLine();
                        int num = Int32.Parse(which) - 1;
                        Console.WriteLine("Dealt {0} Damage to {1}!",Cha.Rage_Bolt(players[num]),players[num].Name);
                        Console.WriteLine("~Continue~");
                        Console.ReadLine();
                        Pass(players,Cha,TurnOrder);
                        
                    }
                    
            }
            public void EnemyTurn(Creature enm,Hero Cha,List<Creature> players,int TurnOrder)
            {
                if(players.Count == 0)
                {
                    return;
                }
                Console.WriteLine("{0} Dealt {1} Damage to The Hero!",enm.Name,enm.Attack(Cha));
                Console.WriteLine("~Continue~");
                Console.ReadLine();
                TurnOrder += 1;
                Pass(players,Cha,TurnOrder);
            }
        public bool End()
        {
            Console.WriteLine("Congratulations! you Defeated the monsters!");
            return true;
        }
            
        }
    }
}

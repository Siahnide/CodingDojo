using System;
using System.Collections.Generic;
using OOP600.Characters;

namespace OOP600
{
    class Program
    {
        static void Main(string[] args)
        {
            AOEAttack(new Enemy[]{new Bandit(), new Bandit(), new Skeleton(1000)}, 10);
        }
        public static void AOEAttack(IEnumerable<Enemy> enemies, int amount)
        {
            foreach(IAttackable e in enemies)
            {
                e.Health -= amount;
            }
        }
    }
}

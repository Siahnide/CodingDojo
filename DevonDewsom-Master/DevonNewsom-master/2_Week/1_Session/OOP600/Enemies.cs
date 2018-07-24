namespace OOP600.Characters
{
    public interface IAttackable
    {
        // Health
        int Health {get;set;}
    }
    public interface IHealable
    {
        int Health {get;set;}
	
        // Method Signature
        int GetHealed(int amt);
    }
    public abstract class Enemy : IAttackable
    {
        public abstract int DefaultHealth {get;}
        public abstract int ChallengeRating {get;set;}            

        public int Health {get;set;}

        public virtual bool Attack(int dmg, IAttackable target)
        {
            target.Health -= dmg * this.ChallengeRating;
            return true;
        }

    }
    public class Bandit : Enemy
    {
        public override int DefaultHealth
        {
            get { return 75; }
        }
        public override int ChallengeRating {get;set;}

        public override bool Attack(int dmg, IAttackable target)
        {
            target.Health -= (dmg -1);
            return true;
        }

        
        public Bandit()
        {
            ChallengeRating = 1;
        }
    }
    public class NPC : IAttackable
    {
        public int Health {get;set;}
    }
    public class Skeleton : Enemy, IHealable
    {
        public override int DefaultHealth
        {
            get { return 75; }
        }
        public int GetHealed(int amt)
        {
            Health = DefaultHealth;
            return Health;
        }
        public override int ChallengeRating {get;set;}
        public Skeleton(int howSick)
        {
            ChallengeRating = howSick;
            Health = DefaultHealth;
        }
    }
}

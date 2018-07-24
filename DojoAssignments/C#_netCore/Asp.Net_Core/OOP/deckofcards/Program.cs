using System;

namespace deckofcards
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
        public class Card
        {
            public string stringVal;
            public string suit;
            public int val;

        }
        public class Deck
        {
            public List<object> cards

            public Deck()
            {
                if (Deck.cards.Count != 52)
                {
                    //add cards
                }
            }
            public void Pull()
            {
                object card = Deck.cards[0]
                Deck.Remove(Deck.cards[0]);
            }
            public void Reset()
            {
                Deck()
            }
        }
        public class Player
        {
            public string Name;
            public List<object> hand;
            public void Draw(Deck deck)
            {
                deck.Pull()
                hand.Add(card)

            }
            public void Discard(int idx)
            {
                hand.Remove(hand[idx])
            }
        }
    }
}

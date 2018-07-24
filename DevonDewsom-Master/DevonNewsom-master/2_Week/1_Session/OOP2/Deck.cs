using System.Collections.Generic;

namespace OOP2.DeckOfCards
{
    public class Deck
    {
        public List<Card> Cards;
        public Deck()
        {
            // Initialize STUFF
            for(int cardVal = 0; cardVal < 14; cardVal++)
            {
                for(int suitVal = 0; suitVal < 4; suitVal++)
                {
                    Cards.Add(new Card(suitVal, cardVal));
                }
            }
        }
    }
}
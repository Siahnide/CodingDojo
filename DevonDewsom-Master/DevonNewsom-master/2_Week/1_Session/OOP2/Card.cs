namespace OOP2.DeckOfCards
{
    public class Card
    {
        // some way to hold numerical value
        private int _cardVal;

        // some way to hold suit value
        private static string[] _suits = new string[]
        {
            "Spades", "Diamonds", "Hearts", "Clubs"
        };

        private string _suitVal;

        public Card(int suitVal, int cardVal)
        {
            _cardVal = cardVal;
            _suitVal = _suits[suitVal];
        }
        // some way to refer to card val (human readable)

    }
}
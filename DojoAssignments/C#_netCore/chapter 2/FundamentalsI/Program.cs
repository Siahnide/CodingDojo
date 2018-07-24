using System;

namespace II
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1
            for (int i = 1; i < 255; i++)
            {
                Console.WriteLine(i);
            }
            //2
            for (int i = 1; i<100; i++)
            {
                if ( i % 3 == 0 || i % 5 == 0)
                {
                    Console.WriteLine(i);
                }
            }
            //3
            for (int i = 1; i<100; i++)
            {
                if ( i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                if ( i % 3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                if ( i % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }

            }
            //4
            for (int i = 0; i<100 ; i+=3)
            {
                Console.WriteLine(i);
            }
            for (int i = 0; i<100 ; i+=5)
            {
                Console.WriteLine(i);
            }

            Random rand = new Random();
            for(int val = 0; val < 10; val++)
            {
                //Prints the next random value between 2 and 8
                int r = rand.Next(2,8);
                if ( r % 3 == 0 && r % 5 == 0)
                {
                    Console.WriteLine("FizzBuzz");
                }
                if ( r % 3 == 0)
                {
                    Console.WriteLine("Fizz");
                }
                if ( r % 5 == 0)
                {
                    Console.WriteLine("Buzz");
                }

            }
        }
    }
}

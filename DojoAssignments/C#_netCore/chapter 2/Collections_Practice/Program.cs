using System;
using System.Collections.Generic;

namespace Collections_Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numarr = {0,1,2,3,4,5,6,7,8,9};
            string[] userarr = {"Tim","Martin","Nikki","Sara"};
            bool[] boolarr = {true,false,true,false,true,false,true,false,true,false};

            List<string> flavors = new List<string>();
            flavors.Add("chocolate");
            flavors.Add("vanilla");
            flavors.Add("strawberry");
            flavors.Add("peanut");
            flavors.Add("apple");
            flavors.Add("pear");
            flavors.Add("banana");
            Console.WriteLine(flavors.Count);
            Console.WriteLine(flavors[2]);
            flavors.Remove(flavors[2]);
            Console.WriteLine(flavors.Count);

            Dictionary<string,string> user = new Dictionary<string,string>();
            for(int i = 0; i< userarr.Length; i++)
            {
                Random rand = new Random();
                int r = rand.Next(0,flavors.Count-1);
                user.Add(userarr[i],flavors[r]);
            }
            foreach (var entry in user)
            {
                Console.WriteLine(entry.Key + " -- "+ entry.Value);

            }



        }
    }
}

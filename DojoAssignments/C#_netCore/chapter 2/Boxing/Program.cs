using System;
using System.Collections.Generic;
namespace Boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> item = new List<object>();
            item.Add(7);
            item.Add(28);
            item.Add(-1);
            item.Add(true);
            item.Add("chair");
            int sum = 0;
            for(var x =0;x<item.Count;x++)
            {
                if(item[x] is int)
                {
                int num;
                num = (int)item[x];
                sum = sum + num;
                }
                if(item[x] is string)
                {
                Console.WriteLine(item[x]);
                }
                if(item[x] is bool)
                {
                Console.WriteLine(item[x]);
                }
                
            };
            Console.WriteLine(sum);

        }
    }
}

using System;
using System.Collections.Generic;

namespace Functions
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("---------------------------------------------------------------------");
            printall();
            Console.WriteLine("---------------------------------------------------------------------");
            printodd();
            Console.WriteLine("---------------------------------------------------------------------");
            printsum();
            Console.WriteLine("---------------------------------------------------------------------");
            int[] arr = {1,2,3,4,5,6,7,8,9,10};
            iterate(arr);
            Console.WriteLine("---------------------------------------------------------------------");
            max(arr);
            Console.WriteLine("---------------------------------------------------------------------");
            avg(arr);
            Console.WriteLine("---------------------------------------------------------------------");
            oddarr();
            Console.WriteLine("---------------------------------------------------------------------");
            greater(arr,10);
            Console.WriteLine("---------------------------------------------------------------------");
            square(arr);
            Console.WriteLine("---------------------------------------------------------------------");
            minmaxavg(arr);
            Console.WriteLine("---------------------------------------------------------------------");
            shift(arr);
        }
        static void printall()
        {
            for(int x = 0;x<255;x++)
            {
                Console.WriteLine(x);
            }
        }
        static void printodd()
        {
            for(int x = 0;x<255;x++)
            {
                if(x%2 == 1)
                {
                Console.WriteLine(x);
                }
            }
        }
        static void printsum()
        {
            int sum = 0;
            for(int x=0;x<255;x++)
            {
                sum += x;
                Console.WriteLine("New Number: "+ x + " | Sum: " + sum);
            }
        }
        static void iterate(int[] arr)
        {
            for (int x=0;x<arr.Length;x++)
            {
                Console.WriteLine(arr[x]);
            }
        }
        static void max(int[] arr)
        {
            int max = arr[0];
            for (int x=0;x<arr.Length;x++)
            {
                if(arr[x] > max)
                {
                    max = arr[x];
                }
            }
            Console.WriteLine(max);
        }
        static void avg(int[] arr)
        {
            int sum = 0;
            for (int x=0;x<arr.Length;x++)
            {
                sum += x;
            }
            int ans = sum/arr.Length;
            Console.WriteLine(ans);
        }
        static void oddarr()
        {
            List<int> odd = new List<int>();
            for(int x=0;x>255;x++)
            {
                if(x%2 == 1)
                {
                    odd.Add(x);
                }
            }
            int[] arr = odd.ToArray();
            Console.WriteLine(arr);
        }
        static void greater(int[] arr, int y)
        {
            int count = 0;
            for (int x=0;x<arr.Length;x++)
            {
                if(arr[x] < y)
                {
                    count += 1;
                }
            }
            Console.WriteLine(count);
        }
        static void square(int[] arr)
        {
            List<int> lis = new List<int>();
            for(int x=0;x<arr.Length;x++)
            {
                lis.Add(arr[x] * arr[x]);
            }
            int[] newarr = lis.ToArray();
            Console.WriteLine(newarr);
        }
        static void noneg(int[] arr)
        {

            List<int> lis = new List<int>();
            for(int x=0;x<arr.Length;x++)
            {
                if(arr[x] % 2 == 0)
                {
                lis.Add(arr[x]);
                }
            }
            int[] newarr = lis.ToArray();
            Console.WriteLine(newarr);
        }
        static void minmaxavg(int[] arr)
        {
            max(arr);
            avg(arr);
            int min = arr[0];
            for (int x=0;x<arr.Length;x++)
            {
                if(arr[x] < min)
                {
                    min = arr[x];
                }
            }
            Console.WriteLine(min);
        }
        static int[] shift(int[] arr)
        {
            List<int> lis = new List<int>();
            for(int x=1;x<arr.Length;x++)
            {
                lis.Add(arr[x]);
            }
            lis.Add(0);
            int[] newarr = lis.ToArray();

            return newarr;
        }
    }
}

using System;

namespace Phone
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Galaxy s8 = new Galaxy("s8",100,"T-mobile","Doo do doo dooo");
            Nokia elevenHundred = new Nokia("1100",60,"Metro PCS","Rinnggg RinggnIRNigning");


            s8.DisplayInfo();
            Console.WriteLine(s8.Ring());
            Console.WriteLine(s8.Unlock());
            Console.WriteLine("");
            elevenHundred.DisplayInfo();
            Console.WriteLine(elevenHundred.Ring());
            Console.WriteLine(elevenHundred.Unlock());
            Console.WriteLine("");
      



        }
            public interface IRingable
            {
                string Ring();
                string Unlock();
            }
            public abstract class Phone 
            {
                public string _versionNumber;
                public int _batteryPercentage;
                public string _carrier;
                public string _ringTone;
                public Phone(string versionNumber, int batteryPercentage, string carrier, string ringTone)
                {
                    _versionNumber = versionNumber;
                    _batteryPercentage = batteryPercentage;
                    _carrier = carrier;
                    _ringTone = ringTone;
                }
                
                public abstract void DisplayInfo();
                
            }
            public class Nokia : Phone,IRingable
            {
                public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone) : base( versionNumber, batteryPercentage, carrier, ringTone) 
                {
                    _versionNumber = versionNumber;
                    _batteryPercentage = batteryPercentage;
                    _carrier = carrier;
                    _ringTone = ringTone; 
                }

                public string Ring()
                {
                    return "riiiing";
                }
                public string Unlock()
                {
                    return "Unlocked!";
                }
                public override void DisplayInfo()
                {
                    Console.WriteLine("Nokia {0}",_versionNumber);
                    Console.WriteLine("Battery percentage: {0}",_batteryPercentage);
                    Console.WriteLine("Carrier {0}",_carrier);
                    Console.WriteLine("Ring Tone: {0}",_ringTone);
                }
            }
            public class Galaxy : Phone, IRingable 
            {
                public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone) : base(versionNumber, batteryPercentage, carrier, ringTone) {}

                public string Ring() 
                {
                    return "riiiing";
                }
                
                public string Unlock() 
                {
                    return "Unlocked!";
                }
                public override void DisplayInfo()
                {
                    Console.WriteLine("Galaxy {0}",_versionNumber);
                    Console.WriteLine("Battery percentage: {0}",_batteryPercentage);
                    Console.WriteLine("Carrier {0}",_carrier);
                    Console.WriteLine("Ring Tone: {0}",_ringTone);
                }
}
        
        
    }
}

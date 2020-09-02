using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int time = Int32.Parse(System.Console.ReadLine().Trim());
        int avg_speed = Int32.Parse(System.Console.ReadLine().Trim());

        double liters = (time * avg_speed) / 12.0;

        Console.WriteLine(liters.ToString("0.000"));
    }
}
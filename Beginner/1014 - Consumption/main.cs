using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int distance = Int32.Parse(System.Console.ReadLine().Trim());
        double fuelSpent = Convert.ToDouble(System.Console.ReadLine().Trim());

        double avg_consumption = distance / fuelSpent;

        Console.WriteLine(avg_consumption.ToString("0.000") + " km/l");
    }
}
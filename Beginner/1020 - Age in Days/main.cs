using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int total_days = Int32.Parse(System.Console.ReadLine().Trim());

        int years = total_days / 365;
        total_days %= 365;
        int months = total_days / 30;
        total_days %= 30;
        Console.WriteLine(years + " ano(s)");
        Console.WriteLine(months + " mes(es)");
        Console.WriteLine(total_days + " dia(s)");
    }
}
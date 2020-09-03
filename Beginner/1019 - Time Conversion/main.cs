using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int total_seconds = Int32.Parse(System.Console.ReadLine().Trim());

        int hours = total_seconds / 3600;
        total_seconds %= 3600;
        int minutes = total_seconds / 60;
        total_seconds %= 60;
        Console.WriteLine(hours + ":" + minutes + ":" + total_seconds);
    }
}
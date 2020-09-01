using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        double[] values_1 = Array.ConvertAll(Console.ReadLine().Split(' '), double.Parse);
        double[] values_2 = Array.ConvertAll(Console.ReadLine().Split(' '), double.Parse);
        
        double distance = Math.Sqrt(Math.Pow(values_2[0] - values_1[0], 2) + Math.Pow(values_2[1] - values_1[1], 2));
            
        Console.WriteLine(distance.ToString("0.0000"));
    }
}
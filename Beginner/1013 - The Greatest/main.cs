using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int[] values = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int biggest = values.Max();
            
        Console.WriteLine(biggest + " eh o maior");
    }
}
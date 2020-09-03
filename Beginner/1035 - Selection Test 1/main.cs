using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int[] values = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        int a = values[0];
        int b = values[1];
        int c = values[2];
        int d = values[3];
            
        if ((b > c) && (d > a) && ((c + d) > (a + b)) && (c >= 0) && (d >= 0) && (a % 2 == 0))
        	Console.WriteLine("Valores aceitos");
        else
        	Console.WriteLine("Valores nao aceitos");
    }
}
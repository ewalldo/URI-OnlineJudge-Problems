using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        double[] values = Array.ConvertAll(Console.ReadLine().Split(' '), double.Parse);
        double a = values[0];
        double b = values[1];
        double c = values[2];

        double root = Math.Pow(b, 2) - (4 * a * c);

        if (a == 0.0)
        	Console.WriteLine("Impossivel calcular");
        else if (root < 0.0)
        	Console.WriteLine("Impossivel calcular");
        else
        {
        	double r1 = ((-b + Math.Sqrt(root)) / (2 * a));
        	double r2 = ((-b - Math.Sqrt(root)) / (2 * a));
        	Console.WriteLine("R1 = " + r1.ToString("0.00000"));
        	Console.WriteLine("R2 = " + r2.ToString("0.00000"));
        }
    }
}
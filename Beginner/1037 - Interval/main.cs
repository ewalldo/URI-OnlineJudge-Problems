using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        double a = Convert.ToDouble(Console.ReadLine().Trim());

        if (a < 0.0)
        	Console.WriteLine("Fora de intervalo");
        else if ((a >= 0) && (a <= 25.0))
	        Console.WriteLine("Intervalo [0,25]");
	    else if ((a > 25.0) && (a <= 50.0))
	        Console.WriteLine("Intervalo (25,50]");
		else if ((a > 50.0) && (a <= 75.0))
	        Console.WriteLine("Intervalo (50,75]");
		else if ((a > 75.0) && (a <= 100.0))
	        Console.WriteLine("Intervalo (75,100]");
		else
			Console.WriteLine("Fora de intervalo");
    }
}
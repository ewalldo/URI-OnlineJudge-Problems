using System;
using System.Linq;

class URI
{
    static void Main(string[] args)
    { 
        int value_amount = Int32.Parse(System.Console.ReadLine().Trim());

        Console.WriteLine(value_amount);
        Console.WriteLine((value_amount / 100) + " nota(s) de R$ 100,00");
        value_amount %= 100;
        Console.WriteLine((value_amount / 50) + " nota(s) de R$ 50,00");
        value_amount %= 50;
        Console.WriteLine((value_amount / 20) + " nota(s) de R$ 20,00");
        value_amount %= 20;
        Console.WriteLine((value_amount / 10) + " nota(s) de R$ 10,00");
        value_amount %= 10;
        Console.WriteLine((value_amount / 5) + " nota(s) de R$ 5,00");
        value_amount %= 5;
        Console.WriteLine((value_amount / 2) + " nota(s) de R$ 2,00");
        value_amount %= 2;
        Console.WriteLine(value_amount + " nota(s) de R$ 1,00");
    }
}
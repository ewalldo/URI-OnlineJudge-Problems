using System; 

class URI
{
    static void Main(string[] args)
    { 
        int a = Int32.Parse(System.Console.ReadLine().Trim());
        int b = Int32.Parse(System.Console.ReadLine().Trim());
        int c = Int32.Parse(System.Console.ReadLine().Trim());
        int d = Int32.Parse(System.Console.ReadLine().Trim());
            
        int x = (a * b) - (c * d);
            
        Console.Write("DIFERENCA = {0}\n", x);
    }
}
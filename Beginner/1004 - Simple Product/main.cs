using System; 

class URI
{
    static void Main(string[] args)
    { 
        int a = Int32.Parse(System.Console.ReadLine().Trim());
        int b = Int32.Parse(System.Console.ReadLine().Trim());
            
        int x = a * b;
            
        Console.Write("PROD = {0}\n", x);
    }
}
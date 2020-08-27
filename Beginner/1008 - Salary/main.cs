using System; 

class URI
{
    static void Main(string[] args)
    { 
        int a = Int32.Parse(System.Console.ReadLine().Trim());
        int b = Int32.Parse(System.Console.ReadLine().Trim());
        double c = Convert.ToDouble(System.Console.ReadLine().Trim());
            
        c *= b;
            
        Console.Write("NUMBER = {0}\n", a);
        Console.Write("SALARY = U$ " + c.ToString("0.00") + "\n");
    }
}
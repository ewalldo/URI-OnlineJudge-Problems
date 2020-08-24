using System; 

class URI
{
    static void Main(string[] args)
    { 
        double a = Convert.ToDouble(System.Console.ReadLine().Trim());
        double b = Convert.ToDouble(System.Console.ReadLine().Trim());
            
        double x = (a * 3.5 + b * 7.5) / 11.0;
            
        Console.Write("MEDIA = " + x.ToString("0.00000") + "\n");
    }
}
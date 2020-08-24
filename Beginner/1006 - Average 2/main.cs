using System; 

class URI
{
    static void Main(string[] args)
    { 
        double a = Convert.ToDouble(System.Console.ReadLine().Trim());
        double b = Convert.ToDouble(System.Console.ReadLine().Trim());
        double c = Convert.ToDouble(System.Console.ReadLine().Trim());
            
        double x = (a * 2.0 + b * 3.0 + c * 5.0) / 10.0;
            
        Console.Write("MEDIA = " + x.ToString("0.0") + "\n");
    }
}
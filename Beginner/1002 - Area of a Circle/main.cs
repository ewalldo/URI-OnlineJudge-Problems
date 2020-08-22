using System; 

class URI {

    static void Main(string[] args)
    { 
        double r = Convert.ToDouble(System.Console.ReadLine());
            
        double a = 3.14159 * (Math.Pow(r, 2));
            
        Console.Write("A=" + a.ToString("0.0000" + "\n"));
    }

}
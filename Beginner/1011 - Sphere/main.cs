using System; 

class URI
{
    static void Main(string[] args)
    { 
        double pi = 3.14159;
        double r = Convert.ToDouble(Console.ReadLine().Trim());

        double vol = (4/3.0) * (r*r*r) * pi;
            
        Console.WriteLine("VOLUME = {0:0.000}", vol);
    }
}
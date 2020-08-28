using System; 

class URI
{
    static void Main(string[] args)
    { 
        string name = Console.ReadLine();
        double salary = Convert.ToDouble(Console.ReadLine().Trim());
        double soldAmount = Convert.ToDouble(Console.ReadLine().Trim());
            
        soldAmount *= 15;
        soldAmount /= 100;

        salary += soldAmount;
            
        Console.Write("TOTAL = R$ " + salary.ToString("0.00") + "\n");
    }
}
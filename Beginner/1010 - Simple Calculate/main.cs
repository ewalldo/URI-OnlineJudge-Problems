using System; 

class URI
{
    static void Main(string[] args)
    { 
        string[] values = Console.ReadLine().Split(' ');
        int x1 = Convert.ToInt32(values[0]);
        int y1 = Convert.ToInt32(values[1]);
        double z1 = Convert.ToDouble(values[2]);
            
        double price1 = y1 * z1;
        
        values = Console.ReadLine().Split(' ');
        int x2 = Convert.ToInt32(values[0]);
        int y2 = Convert.ToInt32(values[1]);
        double z2 = Convert.ToDouble(values[2]);

        double price2 = y2 * z2;
        double total = price1 + price2;
            
        // Console.Write("VALOR A PAGAR = R$ " + total.ToString("0.00") + "\n");
        Console.WriteLine("VALOR A PAGAR: R$ {0:0.00}", total);
    }
}
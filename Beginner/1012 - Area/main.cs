using System; 

class URI
{
    static void Main(string[] args)
    { 
        double pi = 3.14159;
        string[] values = Console.ReadLine().Split(' ');
        double x = Convert.ToDouble(values[0]);
        double y = Convert.ToDouble(values[1]);
        double z = Convert.ToDouble(values[2]);

        double triangle = x * z / 2;
        double circle = z * z * pi;
        double trapezium =  (x + y) / 2 * z;
        double square = y * y;
        double rectangle = x * y;
            
        Console.WriteLine("TRIANGULO: {0:0.000}", triangle);
        Console.WriteLine("CIRCULO: {0:0.000}", circle);
        Console.WriteLine("TRAPEZIO: {0:0.000}", trapezium);
        Console.WriteLine("QUADRADO: {0:0.000}", square);
        Console.WriteLine("RETANGULO: {0:0.000}", rectangle);
    }
}
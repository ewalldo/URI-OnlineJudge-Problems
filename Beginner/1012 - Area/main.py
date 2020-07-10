x, y, z = [float(x) for x in input().split()]
pi_v = 3.14159

print("TRIANGULO: %.3f" % (x * z / 2.0))
print("CIRCULO: %.3f" % ((z**2) * pi_v))
print("TRAPEZIO: %.3f" % ((x + y) / 2 * z))
print("QUADRADO: %.3f" % (y**2))
print("RETANGULO: %.3f" % (x * y))

v1, v2 = [float(x) for x in input().split()]
v11, v22 = [float(x) for x in input().split()]

print("%.4f" % (((v11 - v1)**2 + (v22 - v2)**2)**0.5))

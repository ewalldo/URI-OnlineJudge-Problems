import math

while True:
    values = str(input()).split()
    v1 = int(values[0])
    #v1, v2, v3 = [int(x) for x in input().split()]
    if v1 == 0:
        break

    v2 = int(values[1])
    v3 = int(values[2])
    area = v1 * v2
    total = (area * 100) / v3
    print(math.trunc(math.sqrt(total)))
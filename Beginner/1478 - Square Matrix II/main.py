def generateMatrix(num):
    matrix = [[num for x in range(num)] for y in range(num)] 

    for i in range(num):
        value = 1
        for j in range(i, num):
            matrix[i][j] = value
            matrix[j][i] = value
            value += 1
        
    return matrix

matrixSizes = []
while True:
    aux = input()
    if (float(aux) == 0.00):
        break
    else:
        matrixSizes.append(int(float(aux)))

maxMatriz = generateMatrix(max(matrixSizes))


for matrixSize in matrixSizes:
    slice = [maxMatriz[i][0:matrixSize] for i in range(0,matrixSize)]
    for i in range(matrixSize):
        for j in range(matrixSize):
            if j == 0:
                print("{:>3}".format(slice[i][j]), end='')
            else:
                print("{:>4}".format(slice[i][j]), end='')
            #print("{:>3}".format(slice[i][j]), end='')
        print("")
    print("")
#print("")
#print("")
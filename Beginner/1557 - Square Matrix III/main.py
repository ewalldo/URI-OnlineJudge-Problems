def generateMatrix(num):
    matrix = [[num for x in range(num)] for y in range(num)] 

    for i in range(num):
        for j in range(num):
            matrix[i][j] = 2**(i + j)
        
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
    bigger = slice[matrixSize - 1][matrixSize - 1]
    size_big = len(str(bigger))
    #print(size_big)
    for i in range(matrixSize):
        for j in range(matrixSize):
            if j == 0:
                #print("{:>3}".format(slice[i][j]), end='')
                print(str(slice[i][j]).rjust(size_big), end='')
            else:
                #print("{:>4}".format(slice[i][j]), end='')
                print(str(slice[i][j]).rjust(size_big + 1), end='')
            #print("{:>3}".format(slice[i][j]), end='')
        print("")
    print("")
#print("")
#print("")
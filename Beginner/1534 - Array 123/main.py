while True:
    try:
        value = int(input())
        for i in range(value):
            for j in range(value):
                if (i + j) == (value - 1):
                    print(2, end='')
                elif i == j:
                    print(1, end='')
                else:
                    print(3, end='')
            print("")
    except EOFError:
        break
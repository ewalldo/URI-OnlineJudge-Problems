while True:
    try:
        aux = input()
        name = int(aux)
        if name == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break
aux = input()
size = str(aux)

line = size.strip().split('.')
print(line[0])
print(line[1])
line = line[2].strip().split('-')
print(line[0])
print(line[1])
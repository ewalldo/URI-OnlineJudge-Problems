value = str(input())

pos = value.find(',')
print(value[:pos])
print(value[pos + 1:])
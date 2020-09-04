value = str(input())
o1 = list(value)
o1[0] = value[3]
o1[1] = value[4]
o1[3] = value[0]
o1[4] = value[1]
o1 = ''.join(o1)

o2 = list(value)
o2[0] = value[6]
o2[1] = value[7]
o2[6] = value[0]
o2[7] = value[1]
o2 = ''.join(o2)

o3 = list(value)
o3[2] = '-'
o3[5] = '-'
o3 = ''.join(o3)

print(o1)
print(o2)
print(o3)
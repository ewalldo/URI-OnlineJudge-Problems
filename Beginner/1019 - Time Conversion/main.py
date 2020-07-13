value = int(input())

h = value // 3600
value %= 3600
m = value // 60
value %= 60
print("%d:%d:%d" % (h, m, value))

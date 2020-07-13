value = int(input())

a = value // 365
value %= 365
m = value // 30
value %= 30
print("%d ano(s)" % (a))
print("%d mes(es)" % (m))
print("%d dia(s)" % (value))

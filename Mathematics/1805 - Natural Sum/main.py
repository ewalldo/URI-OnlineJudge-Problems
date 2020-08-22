a, b = map(int, input().split())
sum_interval = int((a + b) * (b - a + 1) / 2.0)
print(sum_interval)
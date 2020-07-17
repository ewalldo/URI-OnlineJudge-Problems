n_segments = int(input())

answer = 1 + (((n_segments - 1) * n_segments) / 2) + (((n_segments) * (n_segments - 1) * (n_segments - 2) * (n_segments - 3)) / 24)

print(int(answer))

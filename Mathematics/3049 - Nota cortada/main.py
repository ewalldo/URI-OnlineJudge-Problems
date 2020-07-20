b = int(input())
t = int(input())

values = sorted([b, t])

triangle_area = ((values[1] - values[0]) * 70) / 2
rectangle_area = values[0] * 70

left_area = triangle_area + rectangle_area
right_area = (70 * 160) - left_area

if left_area > right_area:
	print(1)
elif right_area > left_area:
	print(2)
else:
	print(0)

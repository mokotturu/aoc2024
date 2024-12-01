def main(file):
	left, right = [], []

	lines = file.read().splitlines()
	for line in lines:
		l, r = line.split('   ')
		left.append(int(l))
		right.append(int(r))

	left.sort()
	right.sort()

	distance = 0
	for i in range(len(left)):
		distance += abs(int(left[i]) - int(right[i]))

	print(distance)

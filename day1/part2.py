from collections import defaultdict


def main(file):
	left, right = [], defaultdict(int)

	lines = file.read().splitlines()
	for line in lines:
		l, r = line.split('   ')
		left.append(int(l))
		right[int(r)] += 1

	similarity = 0
	for i in range(len(left)):
		if left[i] in right:
			similarity += left[i] * right[left[i]]

	print(similarity)

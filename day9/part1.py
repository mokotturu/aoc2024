import numpy as np


def main(file):
	lines = file.read().splitlines()
	string = [c for c in lines[0]]
	print(string)

	with_gaps = []
	id = 0

	for i, c in enumerate(string):
		if i % 2 == 0:
			for j in range(int(c)):
				with_gaps.append(id)
		else:
			for j in range(int(c)):
				with_gaps.append('.')
			id += 1


	for i, c in reversed(list(enumerate(with_gaps))):
		if c != '.':
			for j in range(i):
				if with_gaps[j] == '.':
					with_gaps[j] = with_gaps[i]
					with_gaps[i] = '.'
					break

	filtered = [int(c) for c in with_gaps if c != '.']
	sum = 0
	for i, c in enumerate(filtered):
		sum += i * c

	print(sum)

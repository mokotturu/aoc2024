from collections import defaultdict

import numpy as np


def main(file):
	arr = []
	antenna_locs = defaultdict(list)
	lines = file.read().splitlines()
	for row, line in enumerate(lines):
		arr.append([])
		for col, c in enumerate(line):
			arr[-1].append(c)
			if c != '.':
				antenna_locs[c].append((row, col))

	arr = np.array(arr)
	anti_locs = set()
	for antenna, locs in antenna_locs.items():
		for i in range(len(locs)):
			for j in range(i):
				left_coord = locs[i] if locs[i][1] < locs[j][1] else locs[j]
				right_coord = locs[j] if locs[i][1] < locs[j][1] else locs[i]
				dx, dy = left_coord[0] - right_coord[0], left_coord[1] - right_coord[1]

				if left_coord[0] + dx >= 0 and left_coord[0] + dx < arr.shape[0] and left_coord[1] + dy >= 0 and left_coord[1] + dy < arr.shape[1]:
					anti_locs.add((left_coord[0] + dx, left_coord[1] + dy))
					if arr[left_coord[0] + dx][left_coord[1] + dy] == '.':
						arr[left_coord[0] + dx][left_coord[1] + dy] = '#'
				if right_coord[0] - dx >= 0 and right_coord[0] - dx < arr.shape[0] and right_coord[1] - dy >= 0 and right_coord[1] - dy < arr.shape[1]:
					anti_locs.add((right_coord[0] - dx, right_coord[1] - dy))
					if arr[right_coord[0] - dx][right_coord[1] - dy] == '.':
						arr[right_coord[0] - dx][right_coord[1] - dy] = '#'

	print(len(anti_locs))

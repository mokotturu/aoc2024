import numpy as np
from numba import njit
from tqdm import tqdm


@njit
def isInBounds(pos, w, h):
	x, y = pos
	return x >= 0 and x < w and y >= 0 and y < h

@njit
def doesEscape(pos, grid: np.ndarray):
	dx, dy = 0, -1
	w, h = grid.shape[1], grid.shape[0]
	infront = (pos[0] + dx, pos[1] + dy)
	visited = set()

	while isInBounds(infront, w, h):
		if (pos[0], pos[1], dx, dy) in visited:
			return False
		visited.add((pos[0], pos[1], dx, dy))
		infront_x, infront_y = infront
		if grid[infront_y, infront_x] == 1:
			dx, dy = -dy, dx
		else:
			pos = infront
		infront = (pos[0] + dx, pos[1] + dy)

	return True

@njit
def getPath(pos, grid: np.ndarray):
	dx, dy = 0, -1
	w, h = grid.shape[1], grid.shape[0]
	visited = set()

	infront = (pos[0] + dx, pos[1] + dy)
	while isInBounds(infront, w, h):
		visited.add((pos[0], pos[1], dx, dy))
		infront_x, infront_y = infront
		if grid[infront_y, infront_x] == 1:
			dx, dy = -dy, dx
		else:
			pos = infront
		infront = (pos[0] + dx, pos[1] + dy)

	visited.add((pos[0], pos[1], dx, dy))

	return visited

def main(file):
	lines = file.read().splitlines()
	grid = []
	pos = None
	for line_idx, line in enumerate(lines):
		grid.append([])
		for c_idx, c in enumerate(line):
			if c == '.':
				grid[-1].append(0)
			elif c == '#':
				grid[-1].append(1)
			elif c == '^':
				grid[-1].append(2)
				pos = (c_idx, line_idx)

	npgrid = np.array(grid, np.int8)

	count = 0
	path = getPath(pos, npgrid)
	path = list(set([(x, y) for (x, y, *_) in path]))
	for (x, y) in tqdm(path):
		if npgrid[y][x] > 0:
			continue

		new_grid = npgrid.copy()
		new_grid[y, x] = 1
		if not doesEscape(pos, new_grid):
			count += 1

	print(count)

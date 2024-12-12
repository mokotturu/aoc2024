import numpy as np


def get_neighbors(x, y, grid):
	neighbors = []
	if x > 0:
		neighbors.append((x - 1, y))
	if x < len(grid[y]) - 1:
		neighbors.append((x + 1, y))
	if y > 0:
		neighbors.append((x, y - 1))
	if y < len(grid) - 1:
		neighbors.append((x, y + 1))
	return neighbors

def num_corners(x, y, grid):
	c = grid[y][x]
	corners = 0
	if grid[y - 1][x] != c and grid[y][x - 1] != c:
		corners += 1
	if grid[y - 1][x] != c and grid[y][x + 1] != c:
		corners += 1
	if grid[y + 1][x] != c and grid[y][x - 1] != c:
		corners += 1
	if grid[y + 1][x] != c and grid[y][x + 1] != c:
		corners += 1
	if grid[y - 1][x - 1] != c and grid[y - 1][x] == c and grid[y][x - 1] == c:
		corners += 1
	if grid[y - 1][x + 1] != c and grid[y - 1][x] == c and grid[y][x + 1] == c:
		corners += 1
	if grid[y + 1][x - 1] != c and grid[y + 1][x] == c and grid[y][x - 1] == c:
		corners += 1
	if grid[y + 1][x + 1] != c and grid[y + 1][x] == c and grid[y][x + 1] == c:
		corners += 1
	return corners

def main(file):
	grid = np.array([[ord(c) for c in line] for line in file.read().splitlines()])
	visited = np.zeros_like(grid)
	regions = []

	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if visited[y][x] == 0:
				region = []
				stack = [(x, y)]
				while stack:
					_x, _y = stack.pop()
					if visited[_y][_x] == 0:
						region.append((_x, _y))
						visited[_y][_x] = 1
						for nx, ny in get_neighbors(_x, _y, grid):
							if grid[ny][nx] == grid[_y][_x]:
								stack.append((nx, ny))
				regions.append(region)

	padded_grid = np.zeros((len(grid) + 2, len(grid[0]) + 2))
	padded_grid[1:-1, 1:-1] = grid

	total = 0
	for region in regions:
		corners = 0
		area = 0
		for x, y in region:
			corners += num_corners(x + 1, y + 1, padded_grid)
			area += 1
		total += area * corners

	print(total)

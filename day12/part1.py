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

	total = 0
	for region in regions:
		perimeter = 0
		area = 0
		for x, y in region:
			perimeter += 4 - sum(1 for nx, ny in get_neighbors(x, y, grid) if (nx, ny) in region)
			area += 1
		total += area * perimeter

	print(total)

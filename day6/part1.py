def isInBounds(pos, w, h):
	x, y = pos
	return x >= 0 and x < w and y >= 0 and y < h

def main(file):
	lines = file.read().splitlines()
	grid = []
	for line in lines:
		grid.append(list(line))

	dx, dy = 0, -1
	w, h = len(grid[0]), len(grid)

	pos = [(x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '^'][0]

	infront = (pos[0] + dx, pos[1] + dy)
	while isInBounds(infront, w, h):
		grid[pos[1]][pos[0]] = 'X'
		infront_x, infront_y = infront
		if grid[infront_y][infront_x] == '#':
			dx, dy = -dy, dx
			infront = (pos[0] + dx, pos[1] + dy)
		else:
			pos = infront
			infront = (pos[0] + dx, pos[1] + dy)

	grid[pos[1]][pos[0]] = 'X'

	count = 0
	for line in grid:
		count += line.count('X')

	print(count)

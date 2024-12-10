import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def get_neighbors(arr, pos):
	(x, y) = pos
	neighbors = []
	if x > 0:
		neighbors.append((x - 1, y))
	if y > 0:
		neighbors.append((x, y - 1))
	if x < arr.shape[0] - 1:
		neighbors.append((x + 1, y))
	if y < arr.shape[1] - 1:
		neighbors.append((x, y + 1))
	return neighbors

def bfs(arr, start, end):
	if start == end:
		return [start]
	visited = set()
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		if node in visited:
			continue
		visited.add(node)
		for neighbor in get_neighbors(arr, node):
			if neighbor == end:
				if arr[neighbor[0], neighbor[1]] == arr[node[0], node[1]] + 1:
					return path + [neighbor]
				else:
					continue
			if neighbor not in visited and arr[neighbor[0], neighbor[1]] == arr[node[0], node[1]] + 1:
				queue.append((neighbor, path + [neighbor]))
	return []

def main(file):
	lines = file.read().splitlines()
	arr = np.array([[int(c) for c in line] for line in lines])

	zero_locs = np.where(arr == 0)
	nine_locs = np.where(arr == 9)

	total = 0
	for (_zX, _zY) in zip(zero_locs[0], zero_locs[1]):
		score = 0
		for (_nX, _nY) in zip(nine_locs[0], nine_locs[1]):
			path = bfs(arr, (_zX, _zY), (_nX, _nY))
			if path:
				score += 1
		total += score

	print(total)

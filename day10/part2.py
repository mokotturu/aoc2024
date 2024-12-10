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

def all_possible_paths(arr, start, end):
	if start == end:
		return [[start]]
	paths = []
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		for neighbor in get_neighbors(arr, node):
			if neighbor == end:
				if arr[neighbor[0], neighbor[1]] == arr[node[0], node[1]] + 1:
					paths.append(path + [neighbor])
				else:
					continue
			if arr[neighbor[0], neighbor[1]] == arr[node[0], node[1]] + 1:
				queue.append((neighbor, path + [neighbor]))
	return paths

def main(file):
	lines = file.read().splitlines()
	arr = np.array([[int(c) for c in line] for line in lines])

	zero_locs = np.where(arr == 0)
	nine_locs = np.where(arr == 9)

	total = 0
	for (_zX, _zY) in zip(zero_locs[0], zero_locs[1]):
		score = 0
		for (_nX, _nY) in zip(nine_locs[0], nine_locs[1]):
			paths = all_possible_paths(arr, (_zX, _zY), (_nX, _nY))
			score += len(paths)
		total += score

	print(total)

def nmain(file):
	lines = file.read().splitlines()
	arr = np.array([[int(c) for c in line] for line in lines])
	G = nx.DiGraph()

	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			G.add_node((i, j), value=arr[i, j])

	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			for neighbor in get_neighbors(arr, (i, j)):
				if arr[neighbor[0], neighbor[1]] == arr[i, j] + 1:
					G.add_edge((i, j), neighbor)

	pos = {(i, j): (j, -i) for i in range(arr.shape[0]) for j in range(arr.shape[1])}
	labels = {(i, j): arr[i, j] for i in range(arr.shape[0]) for j in range(arr.shape[1])}

	zero_locs = np.where(arr == 0)
	nine_locs = np.where(arr == 9)

	for (_zX, _zY) in zip(zero_locs[0], zero_locs[1]):
		for (_nX, _nY) in zip(nine_locs[0], nine_locs[1]):
			paths = bfs(arr, (_zX, _zY), (_nX, _nY))
			edges = [(paths[i], paths[i + 1]) for i in range(len(paths) - 1)]
			edge_colors = ['#ff0000aa' if (edge[0], edge[1]) in edges or (edge[1], edge[0]) in edges else '#00000000' for edge in G.edges()]
			node_colors = ['#ff0000ff' if node == (_zX, _zY) else '#00ff00ff' if node == (_nX, _nY) else '#00000000' for node in G.nodes()]	
			nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_color=node_colors, labels=labels)

	plt.savefig('day10/graph.png')
